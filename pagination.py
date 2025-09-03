import requests
from bs4 import BeautifulSoup
import json

base_url = "https://quotes.toscrape.com/page/{}/"

all_data = []

for page in range(1,6):
    url = base_url.format(page)
    response = requests.get(url)

    #Eğer sayfa bulunamazsa 404 hatasından kurtul:
    if response.status_code == 404:
        break

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    for q, a in zip(quotes,authors):
        all_data.append({
            "yazar":a.text,
            "alıntı":q.text
        })

#JSON olarak kaydet.
with open("quotes_all.json", "w", encoding="utf-8") as f:
    json.dump(all_data, f, ensure_ascii=False, indent=4)

print(f"✅ Toplam {len(all_data)} alıntı kaydedildi")