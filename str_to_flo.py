urunler = [
    {"isim": "Sabun", "fiyat": "19,90 TL"},
    {"isim": "Şampuan", "fiyat": "45,50 TL"},
    {"isim": "Diş Macunu", "fiyat": "25 TL"}
]

temiz_urunler = []

for u in urunler:
    # "TL" yazısını kaldır, virgülü noktaya çevir
    fiyat_str = u["fiyat"].replace("TL", "").replace(",", ".").strip()
    fiyat_float = float(fiyat_str)
    
    temiz_urunler.append({
        "isim": u["isim"],
        "fiyat": fiyat_float
    })

print(temiz_urunler)
