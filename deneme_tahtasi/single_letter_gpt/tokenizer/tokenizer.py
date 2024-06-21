# this library is used to tokenize the text data

""" 
data_filename = os.path.join("../../video_ve_ozet_havuzu/reproduce_gpt2/tinyshakespeare/", "tiny_shakespeare.txt")
text = open(data_filename, 'r').read()

letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'ı', 'ğ', 'ü', 'ş', 'ö', 'ç',
               '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
               ' ', ',', '.', '!', '?', ';', ':', '-', '(', ')', '"', "'", '+', '*', '/', '=', '@', '<', '>', '\\', '_',
               '\n',
                ]

def letter_encoder(letter):
  letter = letter.lower()
  if letter in letter_list:
    return letter_list.index(letter)
  else:
    return 0

def letter_decoder(index):
  return letter_list[index]

def text_encoder(text):
  return [letter_encoder(letter) for letter in text]
 """

import os


class Tokenizer:
    def __init__(self):
        self.letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                           'ı', 'ğ', 'ü', 'ş', 'ö', 'ç',
                           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
                           ' ', ',', '.', '!', '?', ';', ':', '-', '(', ')', '"', "'", '+', '*', '/', '=', '@', '<', '>', '\\', '_',
                           '\n',
                            ]
        self.eot_token = len(self.letter_list) - 1

    def letter_encoder(self, letter):
        letter = letter.lower()
        if letter in self.letter_list:
            return self.letter_list.index(letter)
        else:
            return 0

    def letter_decoder(self, index):
        return self.letter_list[index]

    def text_encoder(self, text):
        return [self.letter_encoder(letter) for letter in text]

    def text_decoder(self, text):
        return ''.join([self.letter_decoder(index) for index in text])
    

