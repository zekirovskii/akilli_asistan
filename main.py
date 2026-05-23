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

# assistant.py dosyasından gemini api yanıtını alan fonks cağır
from assistant import get_gemini_response

# database.py dosyasından veritabanı islemleri icin gerekli fonsk cagır
from database import initialize_db,add_event,add_note,get_events,get_notes

# veritabanını başlat
initialize_db()

# karsılama mesajı
print("Akıllı Asistana Hoş Geldiniz.")
print("Komutlar: not ekle | etkinlik ekle | notları göster | etkinlikleri göster | çıkış")

# kullanıcıdan süreklik komut alma

while True:
    komut = input("Komut Girin: ").strip().lower() # boslukları kırp kücük harf ekle

    if komut == "not ekle":
        content = input("Not içeriği nedir? ")
        add_note(content)
        print("Not başarıyla kaydedildi")
    elif komut == "etkinlik ekle":
        event=input("Etkinlik içeriği nedir? ")
        event_date=input("Etkinlik tarihi nedir? ")
        add_event(event,event_date)
        print("Etkinlik başarıyla kaydedildi.")
    elif komut == "notları göster":
        notes=get_notes()
        if notes:
            print("Kaydedilmiş notlar: ")
            for content,created_at in notes:
                print(f"\t- [{created_at}] {content}")
        else:
            print("Henüz hiç bir not eklenmedi.")
    elif komut == "etkinlikleri göster":
        events=get_events()
        if events:
            print("Etkinlikler: ")
            for event,event_date in events:
                print(f"\t- {event_date}: {event}")
        else:
            print("Henüz hiç bir etkinlik eklenmedi.")
    elif komut == "çıkış":
        break
    else:
        print("Hatalı Komut !!")


