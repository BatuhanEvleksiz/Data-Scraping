import requests
import json
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

#Data için boş liste

data =[]

for q, a in zip(quotes, authors):
    data.append({
        "yazar": a.text, "alıntı":q.text
    })

#JSON olarak kaydet
with open("dictionary1.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

#JSON dosyasını oku
with open("dictionary1.json", "r", encoding="utf-8") as f:
    yuklenen = json.load(f)

print(yuklenen)