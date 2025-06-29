import pandas as pd
import csv

def create_updated_responses():
    """Daha belirgin ve faydalı yanıtlar ile veri setini güncelle"""
    
    updated_data = []
    
    # 1. GREETING (Selamlama) - 120 örnek
    greeting_examples = [
        ("Merhaba", "Merhaba! Ben sağlık danışmanı chatbot'unuzum. Size semptomlarınız, ilaç kullanımı, doktor seçimi ve sağlıklı yaşam konularında yardımcı olabilirim. Hangi konuda bilgi almak istiyorsunuz?"),
        ("Selam", "Selam! Sağlık konularında size praktik öneriler verebilirim. Semptomlarınızı değerlendirebilir, hangi doktora gitmeniz gerektiğini söyleyebilir, genel sağlık tavsiyeleri verebilirim."),
        ("İyi günler", "İyi günler! Size şu konularda yardımcı olabilirim: 🩺 Semptom değerlendirmesi, 💊 İlaç bilgileri, 👨‍⚕️ Doktor yönlendirme, 💡 Sağlık tavsiyeleri. Ne ile ilgili yardıma ihtiyacınız var?"),
        ("Günaydın", "Günaydın! Bugün sağlığınızla ilgili hangi konuda size yardımcı olabilirim? Semptomlarınızı sorabilir, sağlık tavsiyeleri alabilir veya hangi doktora gitmeniz gerektiğini öğrenebilirsiniz."),
        ("Merhaba doktor", "Merhaba! Ben bir sağlık danışmanı AI'yım. Size genel sağlık konularında bilgi verebilirim ama tıbbi teşhis koyamam. Semptomlarınızı dinler, genel öneriler verebilir ve uygun doktora yönlendirebilirim."),
    ]
    
    # Greeting variations için template
    greeting_responses = [
        "Merhaba! Size semptom değerlendirmesi, doktor önerisi ve sağlık tavsiyeleri konularında yardımcı olabilirim. Ne ile ilgili bilgi almak istiyorsunuz?",
        "Selam! Sağlığınızla ilgili sorularınızı yanıtlayabilirim. Semptomlar, ilaçlar, doktor seçimi - hangi konuda yardıma ihtiyacınız var?",
        "İyi günler! Size pratik sağlık önerileri verebilirim. Şikayetlerinizi dinler ve size en uygun çözüm yollarını önerebilirim.",
        "Hoş geldiniz! Sağlık danışmanı olarak size yardımcı olmak için buradayım. Hangi konuda bilgi almak istiyorsunız?"
    ]
    
    # 120 greeting örneği
    base_greetings = ["Merhaba", "Selam", "İyi günler", "Günaydın", "İyi akşamlar", "Hey", "Hi", "Hoşgeldiniz"]
    for i in range(120):
        if i < len(greeting_examples):
            updated_data.append(['greeting'] + list(greeting_examples[i]))
        else:
            greeting = base_greetings[i % len(base_greetings)]
            response = greeting_responses[i % len(greeting_responses)]
            updated_data.append(['greeting', greeting, response])
    
    # 2. COMMON_SYMPTOMS (Yaygın Semptomlar) - 130 örnek
    symptom_examples = [
        ("Baş ağrısı", "Baş ağrısı için: 💊 Parol (500mg) veya İbuprofen (400mg) alabilirsiniz. 💧 Günde 2-3 litre su için. 😴 Karanlık odada dinlenin. 🍃 Nane yağı şakaklarınıza sürün. Ağrı 2 günden fazla sürerse nöroloji uzmanına başvurun."),
        ("Ateş", "Ateş için: 🌡️ 38.5°C altında normal, üstünde ilaç alın. 💊 Parol (500mg 6 saatte bir) veya Aspirin kullanın. 🧊 Soğuk kompres uygulayın. 💧 Bol sıvı tüketin. Ateş 3 günden fazla sürerse doktora gidin."),
        ("Öksürük", "Öksürük için: 🍯 Bal + limon + ılık su karışımı için. 🌿 Ihlamur veya adaçayı demleyin. 💨 Buhar banyosu yapın. 💊 Kuru öksürükte öksürük şurubu kullanın. 2 haftadan fazla sürerse göğüs hastalıkları uzmanına gidin."),
        ("Boğaz ağrısı", "Boğaz ağrısı için: 🧂 Tuzlu su ile gargara yapın (günde 3-4 kez). 🍯 Bal yalayın. 🫖 Sıcak çay için. 💊 Boğaz pastili emin. Yutkunamıyacak kadar ağırsa KBB uzmanına başvurun."),
        ("Mide ağrısı", "Mide ağrısı için: 🥄 Probiyotik yoğurt tüketin. 🌿 Papatya çayı için. 🍚 Pilav, haşlanmış patates gibi yumuşak yiyecekler tercih edin. ❌ Baharatlı, yağlı yemeklerden kaçının. Şiddetli ağrıda gastroenteroloji uzmanına gidin."),
        ("Baş dönmesi", "Baş dönmesi için: 🪑 Hemen oturun veya uzanın. 💧 Su için (dehidrasyon olabilir). 🍯 Kan şekeri düşükse bal yiyin. 🧘‍♀️ Derin nefes alın. Sık tekrarlanıyorsa nöroloji veya iç hastalıkları uzmanına başvurun."),
        ("Halsizlik", "Halsizlik için: 😴 Günde 7-8 saat uyuyun. 🥗 B vitamini açısından zengin gıdalar tüketin. 🚶‍♀️ Hafif egzersiz yapın. ☀️ Güneş ışığından yararlanın. 1 haftadan fazla sürerse kan tahlili yaptırın."),
        ("Uykusuzluk", "Uykusuzluk için: 📱 Yatmadan 1 saat önce ekranlardan uzak durun. 🫖 Papatya çayı için. 🛁 Ilık duş alın. 🕘 Düzenli uyku saatleri oluşturun. 🧘‍♀️ Meditasyon yapın. Kronikse psikiyatrist desteği alın."),
        ("Stres", "Stres için: 🫁 4-7-8 nefes tekniği yapın (4 say içeri, 7 say tutun, 8 say dışarı). 🏃‍♀️ Günlük 30 dk yürüyüş. 🎵 Sakinleştirici müzik dinleyin. 🧘‍♀️ Yoga deneyin. Aşırı stres varsa psikolog desteği alın."),
        ("Sinirlilik", "Sinirlilik için: 🥶 Soğuk su içın. 🚶‍♀️ Kısa yürüyüş yapın. 💭 10'a kadar sayın. 🎯 Dikkatinizi başka yöne çevirin. 🫖 Melisa çayı için. Sürekli öfke problemi varsa psikolog görün."),
    ]
    
    # Daha fazla semptom örneği
    additional_symptoms = [
        ("Midem bulanıyor", "Bulantı için: 🫖 Zencefil çayı için. 🍋 Limon kokusunu soluyun. 🍚 Az ve sık öğün tüketin. 💊 Metoklopramid (Primperan) kullanabilirsiniz. Hamilelik şüphesi varsa jinekolog kontrolü."),
        ("Kusuyorum", "Kusma için: 💧 Sık sık az su için. ⚡ Elektrolit içeceği alın. 🍌 Muz, elma gibi yumuşak meyveler. 💊 Anti-emetik ilaç. 24 saatten fazla sürerse acil servise başvurun."),
        ("Karın ağrısı", "Karın ağrısı için: 🔥 Sıcak su torbası uygulayın. 🌿 Rezene çayı için. 🚫 Katı gıda tüketmeyin. 💊 Spazmolitik (Buscopan) alabilirsiniz. Sağ alt karında ağrı varsa acil servise gidin."),
        ("İshal", "İshal için: 💧 Bol sıvı alın (su kaybını önlemek için). 🧂 Tuzlu kraker yiyin. 🍌 Muz tüketin. 💊 Probiyotik kullanın. 3 günden fazla sürerse doktora başvurun."),
        ("Kabızlık", "Kabızlık için: 🥗 Lifli gıdalar tüketin. 💧 Günde 2-3 litre su için. 🚶‍♀️ Düzenli yürüyüş yapın. 🫒 Sabah aç karnına zeytinyağı için. 1 haftadan fazla sürerse gastroenteroloji uzmanına gidin."),
    ]
    
    # 130 semptom örneği oluştur
    all_symptoms = symptom_examples + additional_symptoms
    symptom_variations = [
        "Başım ağrıyor", "Kafam ağrıyor", "Migrenım var", "Ateşim var", "Ateşim çıktı", 
        "Öksürüyorum", "Boğazım ağrıyor", "Midem ağrıyor", "Başım dönüyor", "Yorgunum"
    ]
    
    for i in range(130):
        if i < len(all_symptoms):
            updated_data.append(['common_symptoms'] + list(all_symptoms[i]))
        else:
            symptom = symptom_variations[i % len(symptom_variations)]
            response = "Bu semptom için genel önerilerim var. Daha detaylı bilgi için lütfen semptomunuzu daha açık söyleyin."
            updated_data.append(['common_symptoms', symptom, response])
    
    # 3. HEALTH_ADVICE (Sağlık Tavsiyeleri) - 120 örnek
    health_advice_examples = [
        ("Sağlıklı beslenme", "Sağlıklı beslenme için: 🥗 Günde 5 porsiyon sebze-meyve. 🐟 Haftada 2-3 kez balık. 🌾 Tam tahıl ürünleri tercih edin. 🚫 İşlenmiş gıdalardan kaçının. 💧 Günde 8-10 bardak su içın. 🥜 Kuruyemiş ve tohum tüketin."),
        ("Egzersiz", "Egzersiz için: 🏃‍♀️ Haftada en az 150 dk orta tempo kardiyo. 💪 Haftada 2-3 gün kuvvet antrenmanı. 🚶‍♀️ Günde 10.000 adım hedefleyin. 🧘‍♀️ Esneklik egzersizleri ekleyin. ⏰ Düzenli program oluşturun."),
        ("Uyku düzeni", "Kaliteli uyku için: ⏰ Her gün aynı saatte yatıp kalkın. 🌙 Yatak odası serin ve karanlık olsun. 📱 Yatmadan 1 saat önce ekran kullanmayın. ☕ Akşam kafein almayın. 🛁 Gevşetici rutinler oluşturun."),
        ("Kilo verme", "Sağlıklı kilo verme: 🍽️ Porsiyon kontrolü yapın. 🥗 Sebze ağırlıklı beslenin. 🚶‍♀️ Günlük aktivite artırın. 💧 Yemek öncesi su için. ⏰ Düzenli öğün saatleri. 📊 Haftalık 0.5-1 kg hedefleyin."),
        ("Stres yönetimi", "Stres yönetimi için: 🧘‍♀️ Günde 10 dk meditasyon. 🫁 Derin nefes egzersizleri. 🎵 Müzik dinleyin. 📖 Hobi edinin. 👥 Sosyal destek alın. 🏃‍♀️ Düzenli egzersiz yapın."),
    ]
    
    # 120 sağlık tavsiyesi örneği
    for i in range(120):
        if i < len(health_advice_examples):
            updated_data.append(['health_advice'] + list(health_advice_examples[i]))
        else:
            topics = ["Beslenme", "Spor", "Uyku", "Stres", "Kilo", "Vitamin", "Hijyen"]
            topic = topics[i % len(topics)]
            response = f"{topic} konusunda size detaylı ve pratik öneriler verebilirim. Hangi alanda özellikle bilgi almak istiyorsunuz?"
            updated_data.append(['health_advice', topic, response])
    
    # 4. MEDICATION_INFO (İlaç Bilgileri) - 120 örnek
    medication_examples = [
        ("Ağrı kesici", "Ağrı kesici için: 💊 Parol (500mg 6 saatte bir, günde max 4 tablet). 💊 İbuprofen (400mg 8 saatte bir). 💊 Aspirin (500mg). ⚠️ Mide koruyucu ile alın. 🚫 Alkol ile kullanmayın. Max 3 gün kullanın."),
        ("Antibiyotik", "Antibiyotik kullanımı: ⏰ Düzenli saatlerde alın. 💊 Kuru tamam bitin (yarıda bırakmayın). 🥛 Probiyotik ekleyin. 🚫 Alkol ile kullanmayın. 💊 Mide koruyucu kullanın. Yan etki görürseniz doktora danışın."),
        ("Vitamin", "Vitamin kullanımı: ☀️ D vitamini (günde 1000 IU). 🍊 C vitamini (günde 1000mg). 💊 B kompleks. 🐟 Omega-3. 🍽️ Yemek ile alın. 🩸 Yılda 1 kez vitamin seviyenizi kontrol ettirin."),
        ("Aspirin", "Aspirin kullanımı: 💊 Ağrı için 500mg (max günde 3 kez). 💓 Kalp koruma için 100mg (günde 1). 🥛 Mide koruyucu ile alın. 🚫 18 yaş altı kullanmasın. Kanama riski varsa doktora danışın."),
        ("Parol", "Parol kullanımı: 💊 500mg tablet günde max 4 kez (6 saat ara ile). 👶 Çocuklarda doz vücut ağırlığına göre. 🍽️ Yemek ile veya sonrasında alın. ⚠️ Alkol ile kullanmayın. Karaciğer hastalığı varsa dikkat."),
    ]
    
    # 120 ilaç bilgisi örneği
    for i in range(120):
        if i < len(medication_examples):
            updated_data.append(['medication_info'] + list(medication_examples[i]))
        else:
            medications = ["Ağrı kesici", "Vitamin", "Soğuk algınlığı ilacı", "Mide ilacı", "Antibiyotik"]
            med = medications[i % len(medications)]
            response = f"{med} hakkında size kullanım şekli, dozaj ve dikkat edilmesi gerekenler konusunda bilgi verebilirim. Mutlaka doktor veya eczacı kontrolünde kullanın."
            updated_data.append(['medication_info', med, response])
    
    # Diğer intent'ler için mevcut yanıtları koru ama geliştir
    
    # 5. GOODBYE (120 örnek)
    for i in range(120):
        goodbyes = ["Hoşçakal", "Teşekkürler", "Güle güle", "Görüşürüz"]
        goodbye = goodbyes[i % len(goodbyes)]
        response = "Rica ederim! Sağlığınızla ilgili herhangi bir sorunuz olduğunda tekrar yazabilirsiniz. Sağlıklı kalın! 🌟"
        updated_data.append(['goodbye', goodbye, response])
    
    # 6. EMERGENCY (120 örnek)
    for i in range(120):
        emergencies = ["Nefes alamıyorum", "Göğsüm ağrıyor", "Kalp krizi", "Felç"]
        emergency = emergencies[i % len(emergencies)]
        response = "🚨 ACİL DURUM! Derhal 112'yi arayın! Zaman kaybetmeyin - en yakın hastaneye gidin! Bu chatbot acil durumlar için yeterli değildir."
        updated_data.append(['emergency', emergency, response])
    
    # 7. REJECTION (120 örnek)
    for i in range(120):
        rejections = ["Teşhis koy", "Reçete yaz", "Ameliyat gerekli mi"]
        rejection = rejections[i % len(rejections)]
        response = "⚠️ Bu konuda kesin yanıt veremem çünkü tıbbi teşhis/reçete yazma yetkim yok. Size genel bilgiler verebilirim ama kesin kararlar için mutlaka doktora başvurun."
        updated_data.append(['rejection', rejection, response])
    
    # 8. DOCTOR_REFERRAL (120 örnek)
    referral_examples = [
        ("Hangi doktora gideyim", "Şikayetinize göre: 🧠 Baş ağrısı → Nöroloji, 💓 Kalp → Kardiyoloji, 🦴 Eklem ağrısı → Ortopedi, 👁️ Göz → Göz hastalıkları, 👂 Kulak → KBB, 🤰 Kadın sağlığı → Jinekoloji. Genel kontrol için pratisyen hekim yeterli."),
        ("Kardiyolog", "Kardiyoloji uzmanına şu durumlarda gidin: 💓 Göğüs ağrısı, 🫀 Çarpıntı, 🩸 Yüksek tansiyon, 🧬 Aile kalp hastalığı öyküsü. 📋 Yanınızda EKG, kan tahlili götürün."),
        ("Nöroloji", "Nöroloji uzmanına şu durumlarda: 🧠 Şiddetli baş ağrısı, 😵‍💫 Baş dönmesi, 🤲 Titreme, 😴 Uyku bozukluğu, 🧠 Hafıza sorunları. 📋 MR/BT varsa götürün."),
    ]
    
    for i in range(120):
        if i < len(referral_examples):
            updated_data.append(['doctor_referral'] + list(referral_examples[i]))
        else:
            departments = ["Kardiyoloji", "Nöroloji", "Ortopedi", "KBB", "Göz doktoru"]
            dept = departments[i % len(departments)]
            response = f"{dept} uzmanına hangi durumlarda gidilmesi gerektiği ve randevu süreçleri hakkında bilgi verebilirim."
            updated_data.append(['doctor_referral', dept, response])
    
    # 9. PREVENTION (120 örnek)
    prevention_examples = [
        ("Grip korunma", "Gripten korunma: 🧼 Sık el yıkayın, 😷 Kalabalıkta maske takın, 💉 Yıllık grip aşısı, 💪 Bağışıklığı güçlendirin, 🏃‍♀️ Düzenli egzersiz, 😴 Yeterli uyku, 🍊 C vitamini alın."),
        ("Kalp krizi korunma", "Kalp krizi korunma: 🚭 Sigara bırakın, 🏃‍♀️ Düzenli egzersiz, 🥗 Az tuzlu beslenin, ⚖️ Kilo kontrolü, 😌 Stresi azaltın, 🩺 Düzenli kontrol."),
        ("Kanser korunma", "Kanser korunma: 🚭 Sigara bırakın, ☀️ Güneşten korunun, 🥗 Sebze-meyve tüketin, 🚫 İşlenmiş et sınırlayın, 🏃‍♀️ Aktif olun, 🍷 Alkol sınırlayın."),
    ]
    
    for i in range(120):
        if i < len(prevention_examples):
            updated_data.append(['prevention'] + list(prevention_examples[i]))
        else:
            topics = ["Grip", "Kanser", "Kalp hastalığı", "Diyabet", "Enfeksiyon"]
            topic = topics[i % len(topics)]
            response = f"{topic} korunma yöntemleri hakkında detaylı bilgiler verebilirim. Hangi alanda özellikle bilgi almak istiyorsunuz?"
            updated_data.append(['prevention', topic, response])
    
    return updated_data

def save_updated_dataset():
    """Güncellenmiş veri setini kaydet"""
    data = create_updated_responses()
    
    # CSV dosyasına kaydet
    with open('data/intents_dataset.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['intent', 'example_sentence', 'response_template'])
        writer.writerows(data)
    
    print(f"✅ Güncellenmiş veri seti kaydedildi: {len(data)} satır")
    
    # İstatistikleri göster
    df = pd.DataFrame(data, columns=['intent', 'example_sentence', 'response_template'])
    print("\n📊 Yeni intent dağılımı:")
    print(df['intent'].value_counts())

if __name__ == "__main__":
    save_updated_dataset() 