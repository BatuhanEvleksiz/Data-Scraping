import pandas as pd

# Örnek veri
veriler = [
    {"yazar": "Albert Einstein", "alıntı": "The world as we have created it..."},
    {"yazar": "J.K. Rowling", "alıntı": "It is our choices, Harry..."}
]

# DataFrame oluştur
df = pd.DataFrame(veriler)

# Excel dosyasına kaydet
df.to_excel("quotes.xlsx", index=False)

print("✅ quotes.xlsx dosyası oluşturuldu.")