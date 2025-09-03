from bs4 import BeautifulSoup

html = """
<html>
  <head><title>Deneme Sayfa</title></head>
  <body>
    <h1>Bu bir başlıktır</h1>
    <p>Bu bir paragraftır.</p>
    <p>Python öğrenmek çok keyifli!</p>
  </body>
</html>
"""
#BeautifulSoup ile parse et
soup = BeautifulSoup(html, "html.parser")

#h1 etiketini bul
baslik = soup.find("h1").text

#tüm paragrafları bul
paragraflar = [p.text for p in soup.find_all("p")]

print("Başlık:", baslik)
print("Paragraflar:", paragraflar)