"""
Problem:
    - Gemini ile Akıllı Asistan Projesi: notlar, etkinlikler için akıllı asistan
    - Gemini API kullanılacak
    - Kural tabanlı notlar ve etkinlikler oluşturalım
    - Doğal dilde notlar ve etkinlikler ile konuşabilme
    - Kısaca asistan notlara ve etkinliklere erişim sağlayarak özetleme, bilgi çıkarmaı takvim oluşturma

    
Örnek Senaryo:
    - notlar: akşam eve girerken markete uğra, kargoyu al
    - etkinlik: konser var, haftaya önemli toplantı var
    - chatbot: ya haftaya ne vardı?, akşam eve gelirken yapmam gereken bir şey var mıydı

Model Tanıtımı:
    - google gemini-2.5-flash 

Plan:
    - asistant.py : gemini ile chatbot oluşturma
    - database.py : notlar ve etkinlikleri sqlite içinde depolama
    - main.py : bileşenleri bir araya getir

Kütüphaneler:
    - pip install requests python-dotenv
"""