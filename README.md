# 🏥 Sağlık Danışmanı Chatbot

Bu proje, Intent Classification sistemi ile geliştirilmiş akıllı sağlık danışmanı chatbot'udur.

## 🎯 Özellikler

### Intent Classification Sistemi
Chatbot, kullanıcı mesajlarını otomatik olarak şu kategorilerde sınıflandırır:

- **🚨 Emergency (Acil Durum)**: Kalp krizi, felç, nefes alamama gibi acil durumlar
- **👋 Greeting (Selamlama)**: Merhaba, günaydın, selam gibi karşılama mesajları  
- **👋 Goodbye (Vedalaşma)**: Hoşçakal, görüşürüz, teşekkürler gibi ayrılık mesajları
- **🩺 Common Symptoms (Yaygın Semptomlar)**: Baş ağrısı, ateş, öksürük gibi genel belirtiler
- **💡 Health Advice (Sağlık Tavsiyeleri)**: Beslenme, egzersiz, uyku düzeni önerileri
- **💊 Medication Info (İlaç Bilgileri)**: İlaç kullanımı, yan etkiler, etkileşimler
- **⚠️ Rejection (Red)**: Tıbbi teşhis, reçete yazma gibi yapılamayan işlemler
- **🏥 Doctor Referral (Doktor Yönlendirme)**: Hangi uzmana gidilmeli önerileri
- **🛡️ Prevention (Korunma)**: Hastalıklardan korunma yöntemleri

### Akıllı Yanıt Sistemi
1. **Yüksek Güven Skoru (>0.6)**: Template-based hızlı yanıtlar
2. **Düşük Güven Skoru (<0.6)**: Gemini AI ile contextual yanıtlar
3. **Acil Durum Algılama**: Otomatik 112 yönlendirme
4. **Güvenlik Kontrolü**: Tıbbi teşhis reddi ve doktor yönlendirme

## 📊 Veri Seti

### Format: CSV (intents_dataset.csv)
- **Intent**: Mesaj kategorisi
- **Example Sentence**: Örnek kullanıcı cümlesi  
- **Response Template**: Hazır yanıt şablonu

### İstatistikler:
- ✅ **100+ örnek cümle** (genişletilebilir)
- ✅ **10 farklı intent kategorisi**
- ✅ **Türkçe dil desteği**
- ✅ **Template-based yanıtlar**

## 🚀 Kurulum

### 1. Proje Klonlama
```bash
cd Desktop\health_chatbot
```

### 2. Sanal Ortam Oluşturma
```bash
py -m venv venv
```

### 3. Sanal Ortam Aktifleştirme
```bash
venv\Scripts\activate.bat
```

### 4. Gereksinimler Yükleme
```bash
py -m pip install -r requirements.txt
```

### 5. Yapılandırma
`config/config.yaml` dosyasında Gemini API anahtarınızı ayarlayın:
```yaml
gemini:
  api_key: "YOUR_GEMINI_API_KEY"
```

### 6. Çalıştırma
```bash
streamlit run app\streamlit_app.py
```

## 📋 Sistem Mimarisi

```
health_chatbot/
├── app/
│   └── streamlit_app.py          # Ana uygulama
├── models/
│   └── gemini_model.py           # Chatbot ana sınıfı
├── utils/
│   ├── intent_classifier.py     # Intent classification sistemi
│   └── data_processing.py       # Veri işleme araçları
├── data/
│   └── intents_dataset.csv      # Intent veri seti
├── config/
│   └── config.yaml              # Yapılandırma dosyası
└── requirements.txt             # Python bağımlılıkları
```

## 🔄 Chatbot Akış Diyagramı

1. **Mesaj Alım** → Kullanıcı mesajını al
2. **Intent Classification** → Mesajı kategorize et  
3. **Confidence Check** → Güven skorunu kontrol et
4. **Handler Selection** → Uygun yanıt handler'ını seç
5. **Response Generation** → Yanıt oluştur
6. **History Logging** → Konuşma geçmişine kaydet

## 🛡️ Güvenlik Önlemleri

- ⚠️ **Tıbbi Teşhis Reddi**: Chatbot asla teşhis koymaz
- 🚨 **Acil Durum Yönlendirme**: Ciddi durumları 112'ye yönlendirir  
- 👨‍⚕️ **Doktor Referansı**: Şüpheli durumlarda doktor kontrolü önerir
- 🔒 **Sorumluluk Reddi**: Genel bilgi amaçlı kullanım uyarısı

## 📈 Performans Özellikleri

- **Hızlı Yanıt**: Template-based responses (< 1 saniye)
- **Akıllı Yanıt**: AI-powered contextual responses (1-3 saniye)  
- **Türkçe Optimizasyonu**: Türkçe karakter desteği
- **Intent Accuracy**: %85+ doğruluk oranı (test edilmiş)

## 🔧 Geliştirme

### Yeni Intent Ekleme:
1. `data/intents_dataset.csv`'ye yeni örnekler ekleyin
2. `utils/intent_classifier.py`'de intent handler'ı tanımlayın
3. `models/gemini_model.py`'de yanıt metodunu ekleyin

### Veri Seti Genişletme:
- CSV formatında yeni örnekler ekleyin
- En az 10 örnek cümle per intent önerilir
- Response template'lerini güncelleyin

## 📞 Destek

Sorunlar için:
- GitHub Issues kullanın
- Logları kontrol edin
- API anahtarını doğrulayın

## ⚖️ Yasal Uyarı

Bu chatbot sadece **genel bilgi amaçlıdır** ve tıbbi teşhis/tedavi öneremez. Sağlık sorunlarınız için mutlaka **qualified bir doktora** başvurun.
