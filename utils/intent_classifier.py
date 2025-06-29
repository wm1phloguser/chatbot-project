import pandas as pd
import re
from typing import Dict, List, Tuple
from difflib import SequenceMatcher
import os

class IntentClassifier:
    def __init__(self):
        self.intents_data = None
        self.load_intents()
        
    def load_intents(self):
        """Intent verilerini CSV dosyasından yükle"""
        try:
            csv_path = os.path.join('data', 'intents_dataset.csv')
            self.intents_data = pd.read_csv(csv_path, encoding='utf-8')
            print(f"Intent verisi yüklendi: {len(self.intents_data)} satır")
        except Exception as e:
            print(f"Intent verisi yüklenirken hata: {e}")
            self.intents_data = None
    
    def similarity(self, a: str, b: str) -> float:
        """İki metin arasındaki benzerlik skorunu hesapla"""
        return SequenceMatcher(None, a.lower(), b.lower()).ratio()
    
    def classify_intent(self, user_input: str) -> Tuple[str, float, str]:
        """Kullanıcı girdisini intent olarak sınıflandır"""
        if self.intents_data is None:
            return "unknown", 0.0, "Intent verisi yüklenemedi."
        
        user_input_clean = self.clean_text(user_input)
        best_match = None
        best_score = 0.0
        best_response = ""
        
        # Her intent örneği ile karşılaştır
        for index, row in self.intents_data.iterrows():
            example_clean = self.clean_text(row['example_sentence'])
            score = self.similarity(user_input_clean, example_clean)
            
            # Anahtar kelime kontrolü ekle
            keyword_score = self.keyword_match(user_input_clean, example_clean)
            final_score = (score * 0.7) + (keyword_score * 0.3)
            
            if final_score > best_score:
                best_score = final_score
                best_match = row['intent']
                best_response = row['response_template']
        
        # Güven eşiği kontrolü
        confidence_threshold = 0.3
        if best_score < confidence_threshold:
            return "unknown", best_score, ""
            
        return best_match, best_score, best_response
    
    def clean_text(self, text: str) -> str:
        """Metni temizle ve normalize et"""
        if pd.isna(text):
            return ""
        # Türkçe karakterleri koru, sadece gereksiz işaretleri kaldır
        text = re.sub(r'[^\w\sçğıöşüÇĞIİÖŞÜ]', '', str(text))
        return text.lower().strip()
    
    def keyword_match(self, user_input: str, example: str) -> float:
        """Anahtar kelime eşleşme skorunu hesapla"""
        user_words = set(user_input.split())
        example_words = set(example.split())
        
        if not user_words or not example_words:
            return 0.0
            
        intersection = user_words.intersection(example_words)
        union = user_words.union(example_words)
        
        return len(intersection) / len(union) if union else 0.0
    
    def get_intent_response(self, intent: str, confidence: float) -> str:
        """Intent'e göre özelleştirilmiş yanıt döndür"""
        
        intent_responses = {
            "greeting": [
                "Merhaba! Size nasıl yardımcı olabilirim?",
                "Selam! Sağlık konularında size yardımcı olmak için buradayım.",
                "İyi günler! Size nasıl yardımcı olabilirim?"
            ],
            "goodbye": [
                "Hoşçakalın! Sağlıklı günler dilerim.",
                "Güle güle! Geçmiş olsun ve sağlıklı kalın.",
                "Görüşmek üzere! Sağlıklı günler dilerim."
            ],
            "emergency": [
                "🚨 ACİL DURUM: Lütfen derhal 112'yi arayın veya en yakın acil servise gidin!",
                "🚨 ACİL DURUM: Hemen 112'yi arayın! Bu çok ciddi bir durum.",
                "🚨 ACİL DURUM: Derhal tıbbi yardım alın! 112'yi arayın!"
            ],
            "common_symptoms": [
                "Belirtileriniz için genel öneriler verebilirim, ancak kesin tanı için doktor kontrolü önemlidir.",
                "Bu semptomlar için bazı önerilerim var, ama uzun sürerse mutlaka doktora başvurun.",
                "Genel tavsiyeler verebilirim, ancak ciddi durumlarda doktor kontrolü şarttır."
            ],
            "health_advice": [
                "Sağlıklı yaşam için önerilerim var:",
                "Sağlığınız için faydalı bilgiler:",
                "Sağlıklı kalmanız için öneriler:"
            ],
            "medication_info": [
                "İlaç konusunda genel bilgi verebilirim, ancak mutlaka doktor/eczacı kontrolü yapın.",
                "İlaçlar konusunda dikkatli olunmalıdır. Uzman görüşü alın.",
                "Medikal konularda doktor tavsiyesi en güvenilir yoldur."
            ],
            "rejection": [
                "Üzgünüm, bu konuda kesin bir yanıt veremem. Doktor kontrolü öneriyorum.",
                "Bu tür tıbbi kararları ancak qualified bir doktor verebilir.",
                "Güvenliğiniz için bu konuda doktora başvurmanızı öneriyorum."
            ],
            "doctor_referral": [
                "Size uygun sağlık kuruluşu veya doktor önerisinde bulunabilirim:",
                "Durumunuza göre hangi uzmana gitmeniz gerektiğini söyleyebilirim:",
                "Sağlık sistemi konusunda yönlendirme yapabilirim:"
            ],
            "prevention": [
                "Hastalıklardan korunma yöntemleri hakkında bilgi verebilirim:",
                "Sağlığınızı korumak için önemli öneriler:",
                "Önleyici sağlık tedbirleri konusunda bilgiler:"
            ]
        }
        
        import random
        if intent in intent_responses:
            return random.choice(intent_responses[intent])
        else:
            return "Size nasıl yardımcı olabilirim?"
    
    def get_structured_response(self, user_input: str) -> Dict:
        """Kullanıcı girdisi için yapılandırılmış yanıt döndür"""
        intent, confidence, template_response = self.classify_intent(user_input)
        
        response_data = {
            "intent": intent,
            "confidence": confidence,
            "template_response": template_response,
            "structured_response": self.get_intent_response(intent, confidence),
            "user_input": user_input
        }
        
        return response_data 