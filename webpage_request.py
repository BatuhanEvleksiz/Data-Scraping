import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

#Tüm alıntıları bul
quotes = soup.find_all("span",class_="text")
authors = soup.find_all("small",class_="author")

for q, a in zip(quotes, authors):
    print("Alıntı:", q.text)
    print("Yazar:", a.text)
    print("---")