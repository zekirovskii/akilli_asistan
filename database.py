import sqlite3
import os

# veritabanı dosyası yolunu oluştur
DB_PATH=os.path.join("data","assistant.db")

# veritabanı başlatan fonksiyon
def initialize_db():
    # eğer data klasörü yoksa oluştur
    os.makedirs("data", exist_ok=True)

    # veritabanına bağlan ve dosya yoksa oluştur
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()

    # eğer tablolar yoksa oluştur
    cursor.execute(

        """
        CREATE TABLE IF NOT EXISTS notes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,               -- otomatik artan birincil anahtar
            content TEXT NOT NULL,                              -- not icerigi
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP      -- varsayilan olarak suanki zaman    
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS calendar(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event TEXT NOT NULL,                            -- etkinlik acıklamasi
            event_date TEXT NOT NULL                        -- etkinlik tarihi
        )                                                  
        """
    )

    # değisiklikleri kaydet 
    conn.commit()

    # bağlatıyı kapat
    conn.close()

# veritabanına yeni not ekleme
def add_note(content):

    # veritabanına bağlan
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()

    # content i "notes" tablosuna ekle
    cursor.execute("INSERT INTO notes (content) VALUES (?)",(content,))

    # degisiklikleri kaydet
    conn.commit()
    conn.close()


# veritabanına yeni etkinlik ekleme
def add_event(event,event_date):

    # veritabanına bağlam
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()

    # etkinlik ve tarih bilgilerini "calendar" tablosuna ekle
    cursor.execute("INSERT INTO calendar (event, event_date) VALUES (?,?)",(event,event_date))

    # degisiklikleri kaydet
    conn.commit()

    # baglantıyı kapat
    conn.close()


# tüm notları veritabanından sıralı şekilde getiren fonk

def get_notes():
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()

    # "notes" tablosundan icerik ve tarih bilgilerini zaman sırasına göre getir
    cursor.execute("SELECT content, created_at FROM notes ORDER BY created_at DESC")

    # sonucları liste olarak alalım
    notes=cursor.fetchall()

    # baglantıyı kapat
    conn.close()

    return notes

# tüm etkinlikleri veritabanından sıralı şekilde getiren fonk

def get_events():

    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()

    cursor.execute("SELECT event, event_date FROM calendar ORDER BY event_date")

    events=cursor.fetchall()

    conn.close()

    return events

if __name__ == "__main__":
    initialize_db()

    add_note("eve dönerken markete uğramayı unutma")
    add_event("konser var","12.04.2026" )

    print(f"Notes: {get_notes()}")

    print(f"Events: {get_events()}")



