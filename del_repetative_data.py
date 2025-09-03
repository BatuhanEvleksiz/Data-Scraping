import pandas as pd

# Örnek tekrar eden veri
veriler = [
    {"isim": "Sabun", "fiyat": 19.9},
    {"isim": "Sabun", "fiyat": 19.9},
    {"isim": "Şampuan", "fiyat": 45.5}
]

df= pd.DataFrame(veriler)

# Tekrar eden satırları kaldır
df = df.drop_duplicates()

df = df.dropna()  # NaN (boş) değerleri siler


print(df)