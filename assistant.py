import os
import requests # http istekleri
from dotenv import load_dotenv

# .env dosyasından ortam değişkenlerini yükleyelim

load_dotenv()

# API keyi alma
api_key=os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini Api Key .env dosyasında tanımlı değil.")

# gemini 2.5 flash modeline ait url
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

# api çağrısı için gerekli http başlıkları

headers={
    "Content-Type":"application/json", # json formatında veri göndereceğimizi belirtiyoruz
    "X-Goog-Api-Key": api_key # yetkilendirme için api anahtarı
}

# gemini apisine prompt gönderip yanıt alan bir fonksiyon

def get_gemini_response(prompt:str) -> str:
    # apiye göndeirelcek olan json yapısı
    payload={
        "contents":[
            {
                "parts": [
                    {"text":prompt} # kullanıcıdan gelen mesajı içeren bölüm
                ]  
            }
        ]
    }

    # gemini apiye post
    response=requests.post(url, headers=headers, json=payload)

    # istek başarılıysa http 200
    if response.status_code==200:
        try: 
            result=response.json() # json formatındaki yanıtı sözlüğe çevir
            return result["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            return f"yanıt hatası: {e}"
    else:
        return f"api hatası {response.status_code}: {response.text}"
    
def detect_intent():
    pass

if __name__ == "__main__":
    user_input=input("Kullanıcı Sorusu: ")
    yanit=get_gemini_response(user_input)
    print(f"Akıllı Asistan Yanıtı: {yanit}")
