import pandas as pd
import csv
import random

def generate_expanded_dataset():
    """1000+ satırlık genişletilmiş veri seti oluştur"""
    
    # Genişletilmiş veri seti
    expanded_data = []
    
    # 1. GREETING (Selamlama) - 120 örnek
    greeting_examples = [
        ("Merhaba", "Merhaba! Size nasıl yardımcı olabilirim?"),
        ("Selam", "Selam! Sağlık konularında size yardımcı olmak için buradayım."),
        ("İyi günler", "İyi günler! Size nasıl yardımcı olabilirim?"),
        ("Günaydın", "Günaydın! Bugün size nasıl yardımcı olabilirim?"),
        ("İyi akşamlar", "İyi akşamlar! Size nasıl yardımcı olabilirim?"),
        ("Hoş geldiniz", "Hoş bulduk! Sağlık konularında size yardımcı olmak için buradayım."),
        ("Merhaba doktor", "Merhaba! Ben bir sağlık danışmanı chatbot'uyum. Size nasıl yardımcı olabilirim?"),
        ("Hey", "Merhaba! Size nasıl yardımcı olabilirim?"),
        ("Selamün aleyküm", "Aleykümselam! Size nasıl yardımcı olabilirim?"),
        ("Hi", "Merhaba! Size nasıl yardımcı olabilirim?"),
        ("Hello", "Merhaba! Size nasıl yardımcı olabilirim?"),
        ("Merhabalar", "Merhaba! Size nasıl yardımcı olabilirim?"),
        ("Selamlar", "Selam! Sağlık konularında yardımcı olmak için buradayım."),
        ("İyi sabahlar", "İyi sabahlar! Size nasıl yardımcı olabilirim?"),
        ("Merhaba hemşire", "Merhaba! Ben sağlık danışmanı chatbot'uyum. Yardımcı olabilirim."),
        ("Selam doktor", "Selam! Sağlık konularında size yardımcı olmak için buradayım."),
        ("Merhaba bot", "Merhaba! Sağlık danışmanı olarak size yardımcı olabilirim."),
        ("Bana yardım et", "Tabii ki! Size nasıl yardımcı olabilirim?"),
        ("Yardım lazım", "Elbette! Size nasıl yardımcı olabilirim?"),
        ("Merhaba size bir sorum var", "Merhaba! Sorularınızı cevaplamak için buradayım."),
        # Devam eden örnekler...
    ]
    
    # Greeting için daha fazla örnek üret
    greeting_variations = [
        "Merhaba", "Selam", "İyi günler", "Günaydın", "İyi akşamlar", "İyi sabahlar",
        "Hey", "Hello", "Hi", "Merhabalar", "Selamlar", "Hoşgeldiniz", "Selamün aleyküm",
        "Merhaba doktor", "Selam hemşire", "Merhaba bot", "İyi geceler", "Hoş bulduk",
        "Nasılsın", "Nasılsınız", "Sağlık olsun", "Hayırlı günler", "Hayırlı akşamlar"
    ]
    
    greeting_starters = [
        "Merhaba", "Selam", "İyi günler", "Size bir sorum var", "Yardım lazım",
        "Bana yardım edebilir misiniz", "Sağlık konusunda yardım", "Danışmanlık lazım",
        "Merhaba size bir şey soracağım", "Selam doktor", "İyi akşamlar hemşire",
        "Hayırlı günler", "Allah'tan razı olayım", "Size sormak istediğim var"
    ]
    
    # 120 greeting örneği oluştur
    for i in range(120):
        if i < len(greeting_examples):
            expanded_data.append(['greeting'] + list(greeting_examples[i]))
        else:
            # Rastgele kombinasyon
            greeting = random.choice(greeting_variations + greeting_starters)
            response = random.choice([
                "Merhaba! Size nasıl yardımcı olabilirim?",
                "Selam! Sağlık konularında size yardımcı olmak için buradayım.",
                "İyi günler! Size nasıl yardımcı olabilirim?",
                "Hoş geldiniz! Sağlık konularında yardımcı olabilirim."
            ])
            expanded_data.append(['greeting', greeting, response])
    
    # 2. GOODBYE (Vedalaşma) - 120 örnek
    goodbye_examples = [
        ("Hoşçakal", "Hoşçakalın! Sağlıklı günler dilerim."),
        ("Güle güle", "Güle güle! Geçmiş olsun ve sağlıklı kalın."),
        ("İyi günler", "İyi günler! Sağlıklı kalın."),
        ("Görüşürüz", "Görüşmek üzere! Sağlıklı günler dilerim."),
        ("Bay bay", "Hoşçakalın! Sağlıklı kalın."),
        ("Teşekkürler", "Rica ederim! Sağlıklı günler dilerim."),
        ("Sağ ol", "Rica ederim! Her zaman yardıma hazırım."),
        ("Çok teşekkürler", "Bu kadar naziksiniz! Sağlıklı kalın."),
        ("Yardım için teşekkürler", "Rica ederim! Size yardımcı olabildiysem ne mutlu bana."),
        ("Elveda", "Hoşçakalın! Sağlıklı günler dilerim."),
    ]
    
    goodbye_variations = [
        "Hoşçakal", "Güle güle", "İyi günler", "Görüşürüz", "Bay bay", "Bye",
        "Teşekkürler", "Sağ ol", "Çok teşekkürler", "Elveda", "Hoşça kal",
        "Allah'a ısmarladık", "İyi akşamlar", "İyi geceler", "Kendine iyi bak",
        "Sağlıklı kal", "Geçmiş olsun", "Şifalar dilerim", "Sağlığın yerinde olsun"
    ]
    
    # 120 goodbye örneği
    for i in range(120):
        if i < len(goodbye_examples):
            expanded_data.append(['goodbye'] + list(goodbye_examples[i]))
        else:
            goodbye = random.choice(goodbye_variations)
            response = random.choice([
                "Hoşçakalın! Sağlıklı günler dilerim.",
                "Güle güle! Geçmiş olsun ve sağlıklı kalın.",
                "Rica ederim! Sağlıklı günler dilerim.",
                "Görüşmek üzere! Sağlıklı kalın."
            ])
            expanded_data.append(['goodbye', goodbye, response])
    
    # 3. EMERGENCY (Acil Durum) - 120 örnek
    emergency_keywords = [
        "Acil yardım", "112", "Ambulans", "Acil servis", "Kalp krizi", "Felç",
        "Nefes alamıyorum", "Bayılacak gibiyim", "Çok kötüyüm", "Ölüyorum",
        "Kan kusuyorum", "Göğsüm çok ağrıyor", "Sol kolum uyuştu", "Konuşamıyorum",
        "Yürüyemiyorum", "Gözüm görmüyor", "Çok şiddetli ağrı", "Bilinçsizlik",
        "Epilepsi nöbeti", "Astım krizi", "Şiddetli alerjik reaksiyon", "Kaza geçirdim",
        "Düştüm kafam çarptı", "Çok fazla kan kaybı", "Zehirlendim", "İlaç zehirlenmesi",
        "Çok yüksek ateş", "Şiddetli kusma", "Karnım çok ağrıyor", "Apandisit"
    ]
    
    emergency_sentences = [
        "Acil yardım lazım", "Hemen 112 aramam gerekiyor mu", "Ambulans çağırmalı mıyım",
        "Acil servise gitmeli miyim", "Kalp krizi geçiriyorum", "Felç belirtileri var",
        "Nefes alamıyorum yardım", "Bayılacak gibiyim çok kötüyüm", "Ölüyorum galiba",
        "Kan kusuyorum ne yapmalıyım", "Göğsüm çok ağrıyor kötü hissediyorum",
        "Sol kolum uyuştu tehlikeli mi", "Konuşamıyorum yardım edin",
        "Yürüyemiyorum ne yapmalıyım", "Gözüm görmüyor çok korkuyorum",
        "Çok şiddetli ağrı var", "Bilinç kaybı yaşıyorum", "Epilepsi nöbeti geçiriyorum"
    ]
    
    # 120 emergency örneği
    for i in range(120):
        if i < len(emergency_keywords):
            keyword = emergency_keywords[i]
        else:
            keyword = random.choice(emergency_keywords + emergency_sentences)
        
        response = "ACİL DURUM: Lütfen derhal 112'yi arayın veya en yakın acil servise gidin!"
        expanded_data.append(['emergency', keyword, response])
    
    # 4. COMMON_SYMPTOMS (Yaygın Semptomlar) - 120 örnek
    symptoms_data = [
        ("Baş ağrısı", "Baş ağrınız için bolca su için dinlenin. Eğer şiddetli ve sürekli ise doktora başvurun."),
        ("Ateş", "Ateşiniz varsa dinlenin bol sıvı tüketin. 38.5°C üzerinde ise doktor kontrolü önerilir."),
        ("Öksürük", "Öksürük için ıhlamur çayı içebilir dinlenebilirsiniz. 2 haftadan fazla sürerse doktora gidin."),
        ("Boğaz ağrısı", "Boğaz ağrısı için ılık tuzlu su ile gargara yapabilirsiniz. Şiddetli ise doktor kontrolü gerekli."),
        ("Mide ağrısı", "Mide ağrısı için hafif yiyecekler tüketin. Şiddetli ve sürekli ise doktora başvurun."),
        ("Baş dönmesi", "Baş dönmesi yaşıyorsanız oturun veya uzanın. Sık tekrarlanıyorsa doktor kontrolü gerekli."),
        ("Halsizlik", "Halsizlik için dinlenin ve beslenmenize dikkat edin. Uzun sürerse doktora başvurun."),
        ("Uykusuzluk", "Uykusuzluk için düzenli uyku saatleri oluşturun. Kronik ise uzman yardımı alın."),
        ("Stres", "Stres için nefes egzersizleri yapın meditasyon deneyin. Uzun sürerse psikolog desteği alın."),
        ("Sinirlilik", "Sinirlilik hissi için derin nefes alın ve sakinleşmeye çalışın. Sürekli ise uzman yardımı alın."),
    ]
    
    # Semptom varyasyonları
    symptom_variations = [
        "Baş ağrısı var", "Başım ağrıyor", "Kafam ağrıyor", "Migrenimvar",
        "Ateşim var", "Ateşim çıktı", "Humma var", "Vücut sıcaklığım yüksek",
        "Öksürük var", "Öksürüyorum", "Kuru öksürük", "Balgamlı öksürük",
        "Boğazım ağrıyor", "Boğazım şişti", "Yutkunamıyorum", "Boğazım kurdu",
        "Midem ağrıyor", "Karın ağrısı", "Midmede yanma", "Hazımsızlık",
        "Başım dönüyor", "Sersemlik", "Denge kaybı", "Ayağa kalkamıyorum",
        "Yorgunum", "Bitkinim", "Enerjim yok", "Halsizlik hissediyorum",
        "Uyuyamıyorum", "Uykum kaçtı", "Gecenin köründe uyanıyorum", "İnsomnia",
        "Stresim var", "Gerginlik", "Endişe", "Kaygı hissi", "Panik",
        "Sinirlerim bozuk", "Öfkeliyim", "Sabırsızlık", "Tahammülsüzlük"
    ]
    
    # 120 common symptoms örneği
    for i in range(120):
        if i < len(symptoms_data):
            expanded_data.append(['common_symptoms'] + list(symptoms_data[i]))
        else:
            symptom = random.choice(symptom_variations)
            response = "Semptomlarınız için genel öneriler verebilirim, ancak uzun sürerse doktor kontrolü önerilir."
            expanded_data.append(['common_symptoms', symptom, response])
    
    # 5. HEALTH_ADVICE (Sağlık Tavsiyeleri) - 120 örnek
    health_topics = [
        "Sağlıklı beslenme", "Egzersiz", "Su içme", "Uyku düzeni", "Sigara",
        "Alkol", "Vitamin", "Diyet", "Kilo verme", "Bağışıklık", "Spor",
        "Meditasyon", "Stres yönetimi", "Kalp sağlığı", "Beyin sağlığı",
        "Kemik sağlığı", "Diş sağlığı", "Göz sağlığı", "Kadın sağlığı",
        "Erkek sağlığı", "Çocuk sağlığı", "Yaşlı sağlığı", "Hamilelik",
        "Emzirme", "Adölesan sağlığı", "Mental sağlık", "Hijyen"
    ]
    
    # 120 health advice örneği
    for i in range(120):
        topic = random.choice(health_topics)
        response = f"Sağlıklı yaşam için {topic} konusunda önerilerim var."
        expanded_data.append(['health_advice', topic, response])
    
    # 6. MEDICATION_INFO (İlaç Bilgileri) - 120 örnek
    medication_topics = [
        "İlaç kullanımı", "Ağrı kesici", "Antibiyotik", "Yan etki", "Doz aşımı",
        "İlaç etkileşimi", "Hamilelikte ilaç", "Çocuklarda ilaç", "Bitkisel ilaç",
        "Reçetesiz ilaç", "Aspirin", "Parol", "Nurofen", "İbuprofen", "Vitamin hapı",
        "Probiyotik", "Mineral takviyesi", "Homopatik ilaç", "Merhem", "Damla",
        "Şurup", "Tablet", "Kapsül", "İgne", "Serum", "Aşı", "İlaç saklama"
    ]
    
    # 120 medication info örneği
    for i in range(120):
        topic = random.choice(medication_topics)
        response = "İlaç kullanımı konusunda mutlaka doktor veya eczacı tavsiyesi alın."
        expanded_data.append(['medication_info', topic, response])
    
    # 7. REJECTION (Red) - 120 örnek
    rejection_requests = [
        "Teşhis koy", "Ameliyat öner", "Kesin çözüm", "İlaç reçetesi yaz",
        "Tıbbi işlem", "Hastalık teşhisi", "Tedavi planı", "Ameliyat gerekli mi",
        "Ciddi mi", "Ne yapmalıyım", "Hangi hastalık", "Tanı koy",
        "Reçete ver", "İlaç öner", "Doktor yerine geç", "Muayene et",
        "Sağlık raporu", "Test sonucu", "Röntgen yorumla", "Tahlil sonucu",
        "Kan testi", "İdrar testi", "Biyopsi", "Tomografi", "MR sonucu"
    ]
    
    # 120 rejection örneği
    for i in range(120):
        request = random.choice(rejection_requests)
        response = "Üzgünüm, bu konuda kesin yanıt veremem. Doktor kontrolü öneriyorum."
        expanded_data.append(['rejection', request, response])
    
    # 8. DOCTOR_REFERRAL (Doktor Yönlendirme) - 120 örnek
    referral_questions = [
        "Hangi doktora gideyim", "Uzman doktor", "Hastane önerisi", "Randevu",
        "Acil mi normal mi", "Pratisyen hekim", "Uzman branş", "Sağlık ocağı",
        "Özel hastane", "Muayene", "Kardiyolog", "Nöroloji", "Psikiyatrist",
        "Jinekolog", "Üroloji", "Ortopedi", "Kulak burun boğaz", "Göz doktoru",
        "Dış doktoru", "Diyetisyen", "Fizyoterapist", "Psikolog", "Ebe",
        "Hemşire", "Eczacı", "Laborant", "Teknisyen", "Ambulans"
    ]
    
    # 120 doctor referral örneği
    for i in range(120):
        question = random.choice(referral_questions)
        response = "Şikayetinize göre uygun doktor önerisinde bulunabilirim."
        expanded_data.append(['doctor_referral', question, response])
    
    # 9. PREVENTION (Korunma) - 120 örnek
    prevention_topics = [
        "Nasıl korunurum", "Önleyici tedbirler", "Hijyen", "Maske", "El yıkama",
        "Temizlik", "Mesafe", "Aşı", "Beslenme ile korunma", "Spor ile korunma",
        "Grip korunma", "Soğuk algınlığı", "Korona korunma", "Hepatit korunma",
        "Kanser korunma", "Kalp krizi korunma", "Şeker hastalığı korunma",
        "Tansiyon korunma", "Kolesterol korunma", "Obezite korunma", "Sigara bırakma",
        "Alkol bırakma", "Kilo kontrolü", "Stres yönetimi", "Uyku düzeni",
        "Güneş korunma", "Radyasyon korunma", "Kimyasal korunma", "Enfeksiyon korunma"
    ]
    
    # 120 prevention örneği
    for i in range(120):
        topic = random.choice(prevention_topics)
        response = "Hastalıklardan korunma yöntemleri hakkında bilgi verebilirim."
        expanded_data.append(['prevention', topic, response])
    
    return expanded_data

def save_expanded_dataset():
    """Genişletilmiş veri setini kaydet"""
    data = generate_expanded_dataset()
    
    # CSV dosyasına kaydet
    with open('data/intents_dataset_expanded.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['intent', 'example_sentence', 'response_template'])
        writer.writerows(data)
    
    print(f"Genişletilmiş veri seti oluşturuldu: {len(data)} satır")
    
    # İstatistikleri göster
    df = pd.DataFrame(data, columns=['intent', 'example_sentence', 'response_template'])
    print("\nIntent dağılımı:")
    print(df['intent'].value_counts())

if __name__ == "__main__":
    save_expanded_dataset() 