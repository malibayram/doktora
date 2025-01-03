import math
from dataclasses import dataclass

import torch
import torch.nn as nn
from torch.nn import functional as F


class CausalSelfAttention(nn.Module):
  def __init__(self, config):
    super().__init__()
    assert config.n_embd % config.n_head == 0
    # key, query, value projections for all heads, but in a batch
    self.c_attn = nn.Linear(config.n_embd, config.n_embd * 3)
    # output projection
    self.c_proj = nn.Linear(config.n_embd, config.n_embd)
    # regularization
    self.n_head = config.n_head
    self.n_embd = config.n_embd
    # not really a 'bias', more of a mask, but following the OpenAI/HF naming though
    self.register_buffer("bias", torch.tril(torch.ones(config.block_size, config.block_size))
                         .view(1, 1, config.block_size, config.block_size))
    
  def forward(self, x):
    B, T, C = x.size() # batch, sequence length, embedding dimensionality (n_embd)
    # calculate query, key, values for all heads in batch and move head forward to be the batch dim
    # nh is "number of heads" hs is "head size" and C is (number of channels) = nh * hs
    # e.g. in GPT-2 (124M), n_head=12, hs=64, so nh * hs=C=768 Channels in the transformer
    qkv = self.c_attn(x)
    q, k, v = qkv.split(self.n_embd, dim=2)
    k = k.view(B, T, self.n_head, C // self.n_head).transpose(1, 2) # (B, nh, T, hs)
    q = q.view(B, T, self.n_head, C // self.n_head).transpose(1, 2) # (B, nh, T, hs)
    v = v.view(B, T, self.n_head, C // self.n_head).transpose(1, 2) # (B, nh, T, hs)
    # attention (materializes the large (T, T) matrix for all of the queries and keys)
    att = (q @ k.transpose(-2, -1)) * (1.0 / math.sqrt(k.size(-1)))
    att = att.masked_fill(self.bias[:, :, :T, :T] == 0, float('-inf'))
    att = F.softmax(att, dim=-1)
    y = att @ v # (B, nh, T, T) x (B, nh, T, hs) -> (B, nh, T, hs)
    y = y.transpose(1, 2).contiguous().view(B, T, C) # re-assemble all head outputs side by side
    # output projection
    y = self.c_proj(y)
    return y


class MLP(nn.Module):
  def __init__(self, config):
    super().__init__()
    self.c_fc = nn.Linear(config.n_embd, config.n_embd * 4) # c_fc: fully connected layer 
    # first c in c_fc is for "context" and the second c is for "context" in the context of the output
    self.gelu = nn.GELU(approximate='tanh') # gelu: activation function
    # gelu is a non-linear activation function that is a smoothed version of the ReLU function
    self.c_proj = nn.Linear(config.n_embd * 4, config.n_embd) # c_proj: projection layer
    # c in c_proj is for "context" in the context of the output

  def forward(self, x):
    x = self.c_fc(x)
    x = self.gelu(x)
    x = self.c_proj(x)    
    return x


class Block(nn.Module):
  def __init__(self, config):
    super().__init__()
    self.ln_1 = nn.LayerNorm(config.n_embd) # layer normalization for the first sub-block
    self.attn = CausalSelfAttention(config) # self-attention mechanism
    self.ln_2 = nn.LayerNorm(config.n_embd) # layer normalization for the second sub-block
    self.mlp = MLP(config) # multi-layer perceptron

  def forward(self, x):
    x = x + self.attn(self.ln_1(x))
    x = x + self.mlp(self.ln_2(x))
    return x

@dataclass 
class GPTConfig:
  block_size: int = 1024 # max sequence length
  vocab_size: int = 50257 # number of tokens: 50.000 BPE merges + 256 bytes tokens + 1  token
  # BPE means Byte Pair Encoding, which is a data compression technique that builds a dictionary of common
  # byte pairings in a dataset. It is used in text compression and is a form of lossless data compression.
  n_layer: int = 12 # number of layers
  n_head: int = 12 # number of heads
  n_embd: int = 768 # embedding dimension

class GPT(nn.Module):
  def __init__(self, config) :
    super().__init__()
    self.config = config

    self.transormer = nn.ModuleDict(dict(
      wte = nn.Embedding(config.vocab_size, config.n_embd), # wte: word to embedding
      wpe = nn.Embedding(config.block_size, config.n_embd), # wpe: position to embedding
      h = nn.ModuleList([Block(config) for _ in range(config.n_layer)]), # h: block of hidden layers
      ln_f = nn.LayerNorm(config.n_embd) # ln_f: layer normalization for the final output
    ))
    self.lm_head = nn.Linear(config.n_embd, config.vocab_size, bias=False) # lm_head: linear mapping for the final output

  def forward(self, idx):
    # idx is of shape (batch_size, sequence_length) (B, T)
    B, T = idx.size()
    assert T <= self.config.block_size, "Cannot forward sequence length {} > block size {}".format(T, self.config.block_size)
    # forward the token and position embeddings
    pos = torch.arange(T, dtype=torch.long, device=idx.device) # shape (T)
    pos_emb = self.transformer.wpe(pos) # position embeddings of shape (T, n_embd)
    tok_emb = self.transformer.wte(idx) # token embeddings of shape (B, T, n_embd)
    x = tok_emb + pos_emb # combine the embeddings
    # forward the block of transformers
    for block in self.transformer.h:
      x = block(x)
    # forward the final layer normalization and the classifier head
    x = self.transformer.ln_f(x)
    logits = self.lm_head(x) # logits of shape (B, T, vocab_size)
    return logits



  @classmethod
  def from_pretrained(cls, model_type):
    """Load a pre-trained GPT-2 model weights from huggingface"""
    assert model_type in {'gpt2', 'gpt2-medium', 'gpt2-large', 'gpt2-xl'}
    from transformers import GPT2LMHeadModel
    print("Loading weights from pretrained gpt: %s" % model_type)
    # n_layer, n_head and n_embd are determined from the model_type
    config_args = {
      'gpt2':         dict(n_layer=12, n_head=12, n_embd=768),  # 124M params
      'gpt2-medium':  dict(n_layer=24, n_head=16, n_embd=1024), # 345M params
      'gpt2-large':   dict(n_layer=36, n_head=20, n_embd=1280), # 774M params
      'gpt2-xl':      dict(n_layer=48, n_head=25, n_embd=1600)  # 1558M params
    }[model_type]

    config_args['vocab_size'] = 50257 # always 50257 for GPT model checkpoints
    config_args['block_size'] = 1024 # always 1024 for GPT model checkpoints
    # create from scratch initialized minGPT model
    config = GPTConfig(**config_args)
    model = GPT(config)
    sd = model.state_dict()
    sd_keys = sd.keys()
    sd_keys = [k for k in sd_keys if not k.endswith('.attn.bias')] # discard this mask that is not used in GPT-2

    # init a huggingface transformer model, which will download the weights for us
    model_hf = GPT2LMHeadModel.from_pretrained(model_type)
    sd_hf = model_hf.state_dict()

    # copy while ensuring all of the parameters are aligned and match in names and shapes
    sd_keys_hf = sd_hf.keys()
    sd_keys_hf = [k for k in sd_keys_hf if not k.endswith('attn.bias')] # same just the mask
    transposed = ['attn.c_attn.weight', 'attn.c_proj.weight', 'mlp.c_fc.weight', 'mlp.c_proj.weight']
    # basically the openai checkpoints use a "Conv1D" module but we want to use a vanilla linear layer
    # this means we need to transpose the weight matrices then we import them
    assert len(sd_keys) == len(sd_keys_hf), f"missmatched keys: {sd_keys} != {sd_keys_hf}"

    for k in sd_keys_hf:
      if any(k.endswith(w) for w in transposed):
        # special case for the conv1d -> linear layer transposition
        assert sd_hf[k].shape[::-1] == sd[k].shape, f"transposing {k} -> {k.replace('conv1d', 'linear')}"
        with torch.no_grad():
          sd[k].copy_(sd_hf[k].t())
      else:
        # vanilla copy for all other weights
        assert sd[k].shape == sd_hf[k].shape, f"shape mismatch for {k}"
        with torch.no_grad():
          sd[k].copy_(sd_hf[k])

    return model

device = 'cpu'
if torch.cuda.is_available():
  device = 'cuda'
elif hasattr(torch.backends, 'mps'):
  device = 'mps'
print("using device: %s" % device)

num_return_sequences = 5
max_length = 30

model = GPT.from_pretrained('gpt2')
model.eval()
model.to('cuda')

# prefix tokens
import tiktoken

enc = tiktoken.get_encoding('gpt2')
tokens = enc.encode("Hello, I'm a language model,")
tokens = torch.tensor(tokens, dtype=torch.long) # convert to tensor (8,)
tokens = tokens.unsqueeze(0).repeat(num_return_sequences, 1) # (5, 8)
x = tokens.to('cuda')

# generate! right now x is (B, T) where B is the number of examples to generate and T is the length of the input sequence
# B is 5 and T is 8 in this case
# set the seed to 42 so we get the same results
torch.manual_seed(42)
torch.cuda.manual_seed(42)

while x.size(1) < max_length:
  # forward the model to get the logits
  with torch.no_grad():
    logits = model(x) # logits is of shape (B, T, vocab_size)
    # take the logits at the last position
    logits = logits[:, -1, :] # logits is now of shape (B, vocab_size)
    # get the probabilities
    probs = F.softmax(logits, dim=-1)
    # sample from the distribution or take the most likely
    # do top-k sampling 50 default huggingface pipeline
    # topk_probs here becomes (5, 50) and topk_indices becomes (5, 50)
    topk_probs, topk_indices = torch.topk(probs, 50, dim=-1)
    # select a token from the top-k options
    ix = torch.multinomial(topk_probs, 1) # ix is of shape (B, 1)
    # gather the corresponding indices
    xcol = topk_indices.gather(-1, ix) # xcol is of shape (B, 1)
    # append to the sequence
    x = torch.cat((x, xcol), dim=1) # x is of shape (B, T+1)

# print the generated sequences
for i in range(num_return_sequences):
  tokens = x[i, :max_length].tolist()
  decoded = enc.decode(tokens)
  print("> ", decoded)