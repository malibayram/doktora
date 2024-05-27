https://github.com/kexinhuang12345/clinicalBERT/tree/master

#### Tez Izleme Komitesi

1. 28 Mayıs 2024 TIK 1
2. 28 Kasım 2024 TIK 2
3. 28 Mayıs 2025 TIK 3
4. 28 Kasım 2025 TIK 4

#### Tezini tamamlayan öğrenci aşağıdaki şartların her üçünü de sağlamalıdır:

- Tez danışmanıyla beraber tez çalışmasından üretilmiş;

  1. \*Ulusal / uluslararası hakemli etkinliklerde sözlü sunum yapmış ve bildiri kitapçığında basılmış olması,
  2. YTÜ-AYDEK tarafından ilgili alanda belirlenen indeksler kapsamındaki dergilerde yayınlanmış veya yayına kabul edilmiş en az bir makalesinin olması,
  3. Tamamlanmış veya devam eden, yükseköğretim kurumları dışında ulusal/uluslararası bir AR-GE projesinde bursiyer/araştırmacı/yürütücü olarak görev almış olmak veya proje önerisi sunmuş ve biçimsel olarak ret almamış olması.

  \*İlgili tüm yayınların bilimsel hakem sürecinden geçmesi gerekmektedir.

### Tezdeki Yan Anlatılar

- Yeni bir tokenizasyon yöntemi geliştirme böylece daha küçük ve daha hızlı tokenizasyonla daha iyi performans elde etme
- Alana özgü embedding modeli veya yöntemi geliştirme veya büyük embedding modellerini alana uyarlamak için yöntemler geliştirme
- Model adaptasyonu olarak modeli alana özgü küçültme ve performansı artırma, gereksiz weightleri atma, yüksek parametre sayısı eşit midir yüksek başarım?
- Learning rate parametresini verinin özelliklerine göre ayarlamak için yöntemler geliştirme
  - İlk aklıma gelen yöntem verideki her bir örneğin kaynağına göre learning rate ayarlamak. Yani veri ne kadar sağlam bir kaynak tarafından oluşturulmuşsa o kadar yüksek learning rate vermek. Bu sayede veri ne kadar güvenilir ve doğruysa o kadar hızlı öğrenme yapılabilir. Örneğin herhangi bir hastanın sorduğu soruya pratisyen doktor, uzman doktor ve profesör doktorun verdiği cevaplar varsa bu veriye göre learning rate ayarlanabilir. Pratisyen doktorun verdiği cevaplara daha düşük learning rate verilir. Profesör doktorun verdiği cevaplara daha yüksek learning rate verilir.
  - [Mastering Optimization: Dynamic Learning Rates Unveiled](https://statusneo.com/mastering-optimization-dynamic-learning-rates-unveiled/)
  - [Maximize Your Model's Performance: A Guide to Setting the Optimal Learning Rate](https://www.linkedin.com/pulse/maximize-your-models-performance-guide-setting-rate-solis-castro/)
  - [Fine-tuning Models: Hyperparameter Optimization](https://encord.com/blog/fine-tuning-models-hyperparameter-optimization/)

### Github Repoları

- [AI-Researcher](https://github.com/Tech-Watt/AI-Researcher)
- [ChatDoctor](https://github.com/Kent0n-Li/ChatDoctor)
  - [Youtube Videosu](https://youtu.be/3uXy2ZS0aJg)
- [awesome-multi-agent-papers](https://github.com/kyegomez/awesome-multi-agent-papers)

### Youtube Videoları

| Sıra | Video Başlığı                                                                                                                                         | İzlendi | Özet Hazırlandı |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | --------------- |
| 1    | [All Learning Algorithms Explained in 14 Minutes](https://youtu.be/BT6Aw6Q75Yg)                                                                       |         |                 |
| 2    | [Fabric: Opensource AI Framework That Can Automate Your Life!](https://youtu.be/nTQIYWgn-lQ)                                                          |         |                 |
| 3    | [OpenAI Embeddings and Vector Databases Crash Course](https://youtu.be/ySus5ZS0b94)                                                                   |         |                 |
| 4    | [Word2Vec Part 2 Implement word2vec in gensim Deep Learning Tutorial 42 with Python](https://youtu.be/Q2NtCcqmIww)                                    |         |                 |
| 5    | [But what is a GPT? Visual intro to transformers Chapter 5, Deep Learning](https://youtu.be/wjZofJX0v4M)                                              | - [x] t |                 |
| 6    | [Building RAG at 5 different levels](https://youtu.be/oxepyi_hLuA)                                                                                    |         |                 |
| 7    | ["I want Llama3 to perform 10x with my private knowledge" - Local Agentic RAG w/ llama3](https://youtu.be/u5Vcrwpzoz8)                                |         |                 |
| 8    | [Hugging Face + Langchain in 5 mins Access 200k+ FREE AI models for your AI apps](https://youtu.be/_j7JEDWuqLE)                                       | -[x]    |                 |
| 9    | [How Does Rag Work? - Vector Database and LLMs](https://www.youtube.com/shorts/xS55duPS-Pw)                                                           | [x]     |                 |
| 10   | [QLoRA—How to Fine-tune an LLM on a Single GPU (w/ Python Code)](https://youtu.be/XpoKB3usmKc)                                                        |         |                 |
| 11   | [Automate AI Research with Crew.ai and Mozilla Llamafile](https://youtu.be/OUgb3hKSn9U)                                                               | [x]     |                 |
| 12   | [Top 7 AI Examples In Healthcare - The Medical Futurist](https://youtu.be/mkiDXTS6-mU)                                                                |         |                 |
| 13   | [A first evaluation of the new Llama 2 model on medical tasks. Direct comparison with GPT-3.5 and GPT-4.](https://www.youtube.com/shorts/RXDdqKGnrkI) | [x]     |                 |
| 14   | [AI in Medicine: Me LLaMA - Large Language Models for Medical Applications](https://youtu.be/Z41qeL9Dzq4)                                             |         |                 |
| 15   | [STUNNING Medical AI Agents OUTPERFORM Doctors 🤯trained in the simulation, continuous improvement.](https://youtu.be/jQwwLEZ2Hz8)                    |         |                 |
| 16   | [DoctorGPT: Offline & Passes Medical Exams!](https://youtu.be/J9nJh33GM-w)                                                                            |         |                 |

<!--
DoctorGPT: Offline & Passes Medical Exams! to kebab case => doctorgpt-offline-passes-medical-exams
 -->
