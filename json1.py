import json

data = {
    "isim":"Batu",
    "yas":23,
    "uni":"MSKU"
}

#JSON olarak kaydet
with open("ornek.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

#JSON dosyasını oku
with open("ornek.json", "r", encoding="utf-8") as f:
    yuklenen = json.load(f)

print(yuklenen)