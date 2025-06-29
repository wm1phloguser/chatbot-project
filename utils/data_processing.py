import pandas as pd
import random
from typing import Dict, List

def create_health_dataset() -> pd.DataFrame:
    """Sağlık chatbotu için örnek veri seti oluştur"""
    data = {
        'intent': [],
        'user_input': [],
        'bot_response': []
    }
    
    # Örnek veriler
    examples = {
        'greeting': {
            'inputs': [
                "Merhaba", "Günaydın", "İyi günler",
                "Selam", "Sağlık botuna hoş geldim"
            ],
            'responses': [
                "Merhaba! Size nasıl yardımcı olabilirim?",
                "Hoş geldiniz! Sağlığınızla ilgili nasıl yardımcı olabilirim?"
            ]
        },
        'symptom': {
            'inputs': [
                "Başım ağrıyor", "Ateşim var", "Öksürüyorum",
                "Midem bulanıyor", "Grip belirtilerim var"
            ],
            'responses': [
                "Belirtilerinizi ne zamandır yaşıyorsunuz?",
                "Semptomlarınızı daha detaylı anlatabilir misiniz?"
            ]
        }
    }
    
    # Veri setini oluştur
    for intent, content in examples.items():
        for _ in range(50):  # Her intent için 50 örnek
            data['intent'].append(intent)
            data['user_input'].append(random.choice(content['inputs']))
            data['bot_response'].append(random.choice(content['responses']))
    
    return pd.DataFrame(data)

def save_dataset(df: pd.DataFrame, filepath: str) -> None:
    """Veri setini CSV olarak kaydet"""
    df.to_csv(filepath, index=False, encoding='utf-8')

if __name__ == "__main__":
    # Veri seti oluştur ve kaydet
    df = create_health_dataset()
    save_dataset(df, '../data/health_chatbot_dataset.csv')
