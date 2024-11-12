# Türkçe Yapay Zeka Alanında Yapılan Çalışmalar ve Katkılar

## 📚 Akademik Yayınlar ve Araştırmalar

### Hakemli Makaleler

#### Healthcare-Focused Turkish LLM
- **Başlık**: "Healthcare-Focused Turkish LLM: Training on Real Patient-Doctor Question-Answer Data for Enhanced Medical Insight"
- **Önemli Katkılar**:
  - 167,000+ gerçek hasta-doktor soru-cevap verisi kullanımı
  - LLAMA 3 (8b) modeli üzerinde özelleştirilmiş fine-tuning
  - LoRA ve slerp merge teknikleri ile optimizasyon
  - Catastrophic forgetting problemine yönelik çözümler
  - GPT-3.5 ve uzman değerlendirmeleri ile performans analizi
- Link: https://docs.google.com/document/d/1I54QIwYtr3rQV0Oy-9zyJGmpcDrYGMaoZ0UdeVj2jMo/edit?usp=sharing

#### Turkish MMLU Benchmark
- **Başlık**: "Setting Standards in Turkish NLP: TurkishMMLU for Large Language Model Evaluation"
- **Önemli Katkılar**:
  - 6,200 çoktan seçmeli soru
  - 62 farklı bölüm, her bölümde 100 soru
  - 280,000 soruluk havuzdan seçilmiş
  - 67 disiplin ve 800+ konu
  - Türkçe NLP için standart değerlendirme kriterleri
- Link: https://docs.google.com/document/d/1b28ZQmAjh0EWE2_4aSpkvtHC_GIrvfdQu2YHmoP8Cw0/edit?usp=sharing

### Konferans Bildirisi

#### Adaptive Learning Rate Study
- **Başlık**: "Data Quality-Based Adaptive Learning Rate: A Case Study on Medical Text Classification"
- **Önemli Katkılar**:
  - Veri kalitesine dayalı adaptif öğrenme oranı
  - Tıbbi metin sınıflandırma için özelleştirilmiş yaklaşım
  - Uzman seviyesine dayalı dinamik öğrenme optimizasyonu
  - 167,000 örneklem üzerinde uygulama
  - Performans ve yakınsama iyileştirmeleri
- Link: https://docs.google.com/document/d/13zBC-LaQyjo8wdJl158NpIPs2LRrToZn/edit?usp=sharing&ouid=100950721933293531716&rtpof=true&sd=true

### Sağlık Odaklı Modeller ve Merge İşlemleri

  Modeller hem huggingface.com/alibayram hem de ollama.com/alibayram üzerinden paylaşılmıştır.

#### Doktor-Llama Serisi
- **Doktor-Llama-3-8b-slerp-cosmos**
  - Tıbbi terminoloji ve kavramlarda uzmanlaşmış
  - Çoklu model merge işlemi ile güçlendirilmiş
  - SLerp tekniği ile optimize edilmiş performans
  - Hasta-doktor diyalogları için özelleştirilmiş

- **Doktor-Llama-3-8b-slerp**
  - Llama 3 base model üzerine inşa edilmiş
  - Türkçe tıbbi literatür ile fine-tune edilmiş
  - SLerp merge teknikleri ile performans optimizasyonu

#### DoktorGemma Serisi
- **DoktorGemma2-9b**
  - Gemma modelinin tıbbi versiyonu
  - Çoklu fine-tuning aşamaları:
    1. Genel tıbbi bilgi adaptasyonu
    2. Türkçe sağlık terminolojisi optimizasyonu
    3. Hasta-doktor etkileşimi fine-tuning

- **DoktorGemma2-9b-adapter**
  - LoRA adaptörleri ile özelleştirilmiş
  - Modüler yapı sayesinde kolay güncellenebilir
  - Farklı tıbbi alt alanlara adapte edilebilir

- **Doktor-Gemma2-9b-it**
  - Özel kullanım senaryoları için optimize edilmiş
  - İteratif fine-tuning yaklaşımı
  - Performans metrikleri ile sürekli iyileştirme

### Model Merge ve Optimizasyon Teknikleri
- **SLerp (Spherical Linear Interpolation)**
  - Farklı checkpoint'lerin optimal birleşimi
  - Modeller arası bilgi transferi
  - Performans/boyut dengesinin optimizasyonu

- **LoRA Adaptörleri**
  - Düşük rank adaptasyon teknikleri
  - Verimli fine-tuning stratejileri
  - Modüler model geliştirme yaklaşımı

# 📊 Veri Setleri ve Değerlendirmeler

## Akademik Değerlendirme Veri Setleri

### Turkish MMLU (Multi-task Massive Language Understanding)
- **Kapsam**: Türk eğitim sistemine özel kapsamlı değerlendirme seti
- **İçerik**:
  - 280,000+ soru havuzundan seçilmiş
  - 67 farklı disiplin
  - 800+ farklı konu
- **Kullanım Alanları**:
  - Model performans değerlendirmesi
  - Akademik yeterlilik ölçümü
  - Türkçe dil modellerinin karşılaştırmalı analizi

### MMLU Değerlendirme Setleri
1. **yapay_zeka_turkce_mmlu_model_cevaplari**
   - Farklı AI modellerinin yanıtları
   - Karşılaştırmalı performans analizi
   - Model davranış örnekleri

2. **yapay_zeka_turkce_mmlu_liderlik_tablosu**
   - Model performans sıralamaları
   - Karşılaştırmalı metrikler
   - Zaman içindeki gelişim analizi

3. **yapay_zeka_turkce_mmlu_bolum_sonuclari**
   - Bölüm bazlı detaylı analizler
   - Konu bazlı performans değerlendirmeleri
   - Spesifik alan başarı oranları

## Profesyonel Alan Veri Setleri

### Tıbbi Veri Seti (doktorsitesi)
- **Kapsam**: 167,000+ gerçek hasta-doktor etkileşimi
- **Özellikler**:
  - Uzman doktor yanıtları
  - Çeşitli tıbbi uzmanlık alanları
  - Hasta soruları ve şikayetleri
  - Teşhis ve tedavi önerileri
- **Kullanım Alanları**:
  - Tıbbi dil modeli eğitimi
  - Sağlık danışmanlığı sistemleri
  - Medikal terminoloji analizi

### Hukuk Veri Seti (hukuk_soru_cevap)
- **İçerik**:
  - Türk hukuku soru-cevap verileri
  - Yasal terminoloji ve kavramlar
  - Hukuki analiz örnekleri
- **Kullanım Alanları**:
  - Hukuki metin analizi
  - Yasal danışmanlık sistemleri
  - Hukuk dili modelleme

## Kullanıcı Geri Bildirim Veri Setleri

### E-ticaret Yorumları
1. **hepsiburada_yorumlar**
   - Ürün değerlendirmeleri
   - Müşteri memnuniyet analizi
   - Satın alma deneyimleri

### Medya ve Eğlence Yorumları
1. **beyazperde_yorumlar**
   - Film ve dizi değerlendirmeleri
   - İzleyici yorumları
   - Medya içerik analizi

2. **kitapyurdu_yorumlar**
   - Kitap incelemeleri
   - Okuyucu değerlendirmeleri
   - Edebi içerik analizi

### Haber ve İçerik
1. **onedio_haberler**
   - Haber metinleri ve başlıkları
   - İçerik kategorileri
   - Güncel olaylar

## 💻 Açık Kaynak Katkıları

### GitHub Projeleri Contribütions
- **mlx-examples**
  - Apple Silicon optimize ML örnekleri
  - Performans iyileştirmeleri
  - Türkçe dokümantasyon

- **unsloth**
  - LLM optimizasyon araçları
  - Eğitim süreçlerinde hız kazanımı
  - Bellek optimizasyonu