import streamlit as st
import sys
import os

# Ana dizini Python path'ine ekle
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.gemini_model import HealthChatbot

def initialize_session_state():
    """Session state değişkenlerini başlat"""
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = HealthChatbot()

def main():
    st.set_page_config(
        page_title="Sağlık Danışmanı Chatbot",
        page_icon="🏥",
        layout="wide"
    )
    
    # Ana başlık
    st.title("🏥 Sağlık Danışmanı Chatbot")
    
    # Session state'i başlat
    initialize_session_state()
    
    # Sidebar - Debug ve İstatistikler
    with st.sidebar:
        st.header("📊 Sistem Bilgileri")
        
        # Intent Classification açıklaması
        with st.expander("🎯 Intent Classification"):
            st.write("""
            **Desteklenen Intent'ler:**
            - 🚨 Emergency (Acil Durum)
            - 👋 Greeting (Selamlama)  
            - 👋 Goodbye (Vedalaşma)
            - 🩺 Common Symptoms (Semptomlar)
            - 💡 Health Advice (Sağlık Tavsiyesi)
            - 💊 Medication Info (İlaç Bilgisi)
            - ⚠️ Rejection (Red)
            - 🏥 Doctor Referral (Doktor Yönlendirme)
            - 🛡️ Prevention (Korunma)
            """)
        
        # Konuşma istatistikleri
        if st.session_state.messages:
            stats = st.session_state.chatbot.get_conversation_stats()
            st.subheader("📈 Konuşma İstatistikleri")
            st.metric("Toplam Mesaj", stats['total_messages'])
            
            if stats['intents']:
                st.write("**Intent Dağılımı:**")
                for intent, count in stats['intents'].items():
                    st.write(f"• {intent}: {count}")
        
        # Debug modu
        debug_mode = st.checkbox("🔧 Debug Modu", help="Intent classification detaylarını göster")
        
        if st.button("🗑️ Konuşmayı Temizle"):
            st.session_state.messages = []
            st.session_state.chatbot = HealthChatbot()
            st.rerun()
    
    # Ana içerik alanı
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Yasal uyarı
        with st.expander("⚠️ Önemli Uyarı"):
            st.warning(
                "Bu chatbot sadece genel bilgi amaçlıdır ve tıbbi teşhis/tedavi öneremez. "
                "Acil durumlarda 112'yi arayın veya bir sağlık kuruluşuna başvurun."
            )
        
        # Mesaj geçmişini göster
        for i, message in enumerate(st.session_state.messages):
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                
                # Debug bilgilerini göster
                if debug_mode and message["role"] == "assistant" and i > 0:
                    # Son kullanıcı mesajının intent bilgisini al
                    try:
                        history = st.session_state.chatbot.conversation_history
                        if history and len(history) > i//2:
                            intent_info = history[i//2].get('intent', 'unknown')
                            st.caption(f"🎯 Algılanan Intent: `{intent_info}`")
                    except:
                        pass
        
        # Kullanıcı girişi
        if prompt := st.chat_input("Nasıl yardımcı olabilirim?"):
            # Kullanıcı mesajını göster
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Bot yanıtını göster
            with st.chat_message("assistant"):
                with st.spinner("Düşünüyorum..."):
                    response = st.session_state.chatbot.get_response(prompt)
                    st.markdown(response)
                    
                    # Debug modunda intent bilgilerini göster
                    if debug_mode:
                        try:
                            intent_result = st.session_state.chatbot.intent_classifier.get_structured_response(prompt)
                            st.caption(f"🎯 Intent: `{intent_result['intent']}` | 📊 Confidence: `{intent_result['confidence']:.2f}`")
                        except:
                            st.caption("Debug bilgisi alınamadı")
                            
            st.session_state.messages.append({"role": "assistant", "content": response})
    
    with col2:
        # Hızlı sorular
        st.subheader("⚡ Hızlı Sorular")
        
        quick_questions = [
            "Merhaba",
            "Baş ağrım var",
            "Ateşim çıktı", 
            "Sağlıklı beslenme önerileri",
            "Hangi doktora gideyim",
            "Nefes alamıyorum",
            "Teşhis koy",
            "Hoşçakal"
        ]
        
        for question in quick_questions:
            if st.button(question, key=f"quick_{question}", use_container_width=True):
                # Butona basıldığında soruyu chat input'a ekle
                st.session_state.temp_input = question
                st.rerun()
        
        # Temp input varsa işle
        if hasattr(st.session_state, 'temp_input'):
            prompt = st.session_state.temp_input
            delattr(st.session_state, 'temp_input')
            
            # Kullanıcı mesajını ekle
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Bot yanıtını al ve ekle
            response = st.session_state.chatbot.get_response(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response})
            
            st.rerun()

if __name__ == "__main__":
    main()
