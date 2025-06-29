import google.generativeai as genai
from typing import Dict, List
import yaml
import sys
import os

# Intent classifier'ı import et
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.intent_classifier import IntentClassifier

class HealthChatbot:
    def __init__(self):
        # Config dosyasını oku
        with open('config/config.yaml', 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
            
        # Gemini API'yi yapılandır
        self.setup_gemini(config['gemini']['api_key'])
        self.conversation_history = []
        
        # Intent classifier'ı başlat
        self.intent_classifier = IntentClassifier()
        
    def setup_gemini(self, api_key: str):
        """Gemini API yapılandırması"""
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
    
    def get_response(self, user_input: str) -> str:
        """Kullanıcı mesajına yanıt al"""
        try:
            # Intent classification yap
            intent_result = self.intent_classifier.get_structured_response(user_input)
            intent = intent_result['intent']
            confidence = intent_result['confidence']
            
            print(f"Intent: {intent}, Confidence: {confidence:.2f}")  # Debug için
            
            # Yüksek güvenlik gerektiren intent'ler için özel yanıtlar
            if intent == "emergency":
                return self._handle_emergency()
            elif intent == "greeting":
                return self._handle_greeting()
            elif intent == "goodbye":
                return self._handle_goodbye()
            elif intent == "rejection":
                return self._handle_rejection(user_input)
            elif confidence > 0.6:  # Yüksek güven skorlu intent'ler için template yanıt
                return self._handle_high_confidence_intent(intent_result)
            else:
                # Düşük güven skorlu veya bilinmeyen intent'ler için Gemini'ye sor
                return self._handle_with_gemini(user_input, intent)
                
        except Exception as e:
            return f"Üzgünüm, bir hata oluştu: {str(e)}"
    
    def _handle_emergency(self) -> str:
        """Acil durum yanıtı"""
        return ("🚨 **ACİL DURUM ALGANDI** 🚨\n\n"
                "Lütfen DERHAL aşağıdaki adımları izleyin:\n"
                "📞 **112'yi hemen arayın**\n"
                "🏥 **En yakın acil servise gidin**\n"
                "⏰ **Zaman kaybetmeyin**\n\n"
                "Bu chatbot tıbbi acil durumlarda yetersizdir. "
                "Profesyonel tıbbi yardım alın!")
    
    def _handle_greeting(self) -> str:
        """Selamlama yanıtı"""
        return ("Merhaba! 👋 Ben sağlık danışmanı chatbot'unuzum.\n\n"
                "Size şu konularda yardımcı olabilirim:\n"
                "• Genel sağlık tavsiyeleri\n"
                "• Semptom değerlendirmesi\n"
                "• Doktor yönlendirmesi\n"
                "• Sağlıklı yaşam önerileri\n"
                "• Acil durum yönlendirmesi\n\n"
                "Nasıl yardımcı olabilirim?")
    
    def _handle_goodbye(self) -> str:
        """Vedalaşma yanıtı"""
        return ("Hoşçakalın! 👋\n\n"
                "Sağlıklı günler dilerim. 🌟\n"
                "Tekrar yardıma ihtiyacınız olursa buradayım.\n\n"
                "**Hatırlatma:** Ciddi sağlık sorunlarınız için mutlaka doktora başvurun!")
    
    def _handle_rejection(self, user_input: str) -> str:
        """Reddedilmesi gereken talepler için yanıt"""
        return ("⚠️ **Önemli Uyarı**\n\n"
                "Üzgünüm, bu konuda size yardımcı olamam çünkü:\n"
                "• Tıbbi teşhis koyamam\n"
                "• İlaç reçetesi yazamam\n"
                "• Kesin tedavi öneremem\n\n"
                "🏥 **Lütfen bir sağlık kuruluşuna başvurun**\n"
                "👨‍⚕️ Sadece qualified doktorlar bu konularda yardımcı olabilir.")
    
    def _handle_high_confidence_intent(self, intent_result: Dict) -> str:
        """Yüksek güvenlik skorlu intent'ler için template yanıt"""
        intent = intent_result['intent']
        template = intent_result['template_response']
        structured = intent_result['structured_response']
        
        if template:
            return f"{structured}\n\n{template}"
        else:
            return structured
    
    def _handle_with_gemini(self, user_input: str, detected_intent: str) -> str:
        """Gemini ile yanıt al (intent bilgisi ile zenginleştirilmiş)"""
        # Intent bilgisini prompt'a ekle
        system_prompt = f"""
        Sen bir sağlık danışmanı chatbot'usun. 
        
        Kullanıcının mesajı "{detected_intent}" intent'i olarak algılandı.
        
        Görevlerin:
        1. Kullanıcılara nazik ve profesyonel yanıtlar ver
        2. Acil durumlarda 112'ye yönlendir
        3. Asla tıbbi teşhis koyma
        4. Genel sağlık tavsiyeleri ver
        5. Şüpheli durumlarda doktora başvurmalarını öner
        6. Türkçe yanıt ver
        7. Sağlık konuları dışında yardım etme
        
        Yanıtın profesyonel ama sıcak olsun.
        """
        
        # Tam promptu oluştur
        full_prompt = f"{system_prompt}\n\nKullanıcı: {user_input}"
        
        # Yanıt al
        response = self.model.generate_content(full_prompt)
        
        # Yanıtı kaydet ve döndür
        bot_response = response.text
        self.conversation_history.append({
            "user": user_input,
            "bot": bot_response,
            "intent": detected_intent
        })
        
        return bot_response
    
    def get_conversation_stats(self) -> Dict:
        """Konuşma istatistiklerini döndür"""
        if not self.conversation_history:
            return {"total_messages": 0, "intents": {}}
        
        intents = {}
        for conv in self.conversation_history:
            intent = conv.get('intent', 'unknown')
            intents[intent] = intents.get(intent, 0) + 1
        
        return {
            "total_messages": len(self.conversation_history),
            "intents": intents
        }
