import requests

url = "https://quotes.toscrape.com/"
response = requests.get(url)

print("Durum kodu:", response.status_code)  # 200 başarılı demek
print("İlk 500 karakter:", response.text[:500])  # HTML'nin bir kısmını yazdır
