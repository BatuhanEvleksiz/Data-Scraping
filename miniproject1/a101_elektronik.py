import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import time
import random

def get_a101_products():
    all_data = []
    
    # Headers ekle - bot gibi görünmemek için
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'tr-TR,tr;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    for page in range(1, 4):  # 3 sayfa
        print(f"🔄 Sayfa {page} işleniyor...")
        
        # A101'in gerçek URL yapısı
        url = f"https://www.a101.com.tr/elektronik?page={page}"
        
        try:
            # Session kullan - daha stabil
            session = requests.Session()
            session.headers.update(headers)
            
            response = session.get(url, timeout=10)
            print(f"Status Code: {response.status_code}")
            
            if response.status_code != 200:
                print(f"❌ Sayfa {page} yüklenemedi")
                continue
                
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Sayfanın gerçekte yüklenip yüklenmediğini kontrol et
            if len(response.text) < 1000:
                print(f"❌ Sayfa {page} içeriği boş görünüyor")
                continue
            
            # A101'in güncel HTML yapısına göre selector'ları güncelle
            # Çeşitli olasılıkları dene
            product_containers = soup.find_all("div", class_=lambda x: x and ("product" in x.lower() or "item" in x.lower()))
            
            if not product_containers:
                # Alternatif selectors
                product_containers = soup.find_all("article")
                if not product_containers:
                    product_containers = soup.find_all("div", attrs={"data-testid": lambda x: x and "product" in x})
            
            print(f"📦 {len(product_containers)} ürün container'ı bulundu")
            
            if not product_containers:
                print("⚠️  HTML yapısı değişmiş olabilir. Sayfayı manuel kontrol edin.")
                # Debug için HTML'in bir kısmını yazdır
                print("Sayfa başlığı:", soup.title.text if soup.title else "Bulunamadı")
                continue
            
            page_products = 0
            for container in product_containers:
                try:
                    # Ürün ismini bul - çeşitli selectors dene
                    name_elem = (
                        container.find("h3") or 
                        container.find("h4") or 
                        container.find(class_=lambda x: x and ("title" in x or "name" in x)) or
                        container.find("a", title=True)
                    )
                    
                    # Fiyatı bul
                    price_elem = (
                        container.find(class_=lambda x: x and ("price" in x or "fiyat" in x)) or
                        container.find("span", string=lambda x: x and ("₺" in x or "TL" in x)) or
                        container.find(text=lambda x: x and ("₺" in x or "TL" in x))
                    )
                    
                    if name_elem and price_elem:
                        name = name_elem.get_text(strip=True) if hasattr(name_elem, 'get_text') else str(name_elem).strip()
                        price = price_elem.get_text(strip=True) if hasattr(price_elem, 'get_text') else str(price_elem).strip()
                        
                        # Link bul
                        link_elem = container.find("a", href=True)
                        link = ""
                        if link_elem:
                            href = link_elem['href']
                            if href.startswith('/'):
                                link = "https://www.a101.com.tr" + href
                            else:
                                link = href
                        
                        all_data.append({
                            "isim": name,
                            "fiyat": price,
                            "link": link,
                            "sayfa": page
                        })
                        page_products += 1
                        
                except Exception as e:
                    continue
            
            print(f"✅ Sayfa {page}'dan {page_products} ürün eklendi")
            
            # Sayfalar arası bekleme
            time.sleep(random.uniform(2, 4))
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Sayfa {page} için bağlantı hatası: {e}")
            continue
        except Exception as e:
            print(f"❌ Sayfa {page} için genel hata: {e}")
            continue
    
    return all_data

def save_data(data):
    if not data:
        print("❌ Kaydedilecek veri yok!")
        return
    
    # JSON kaydı
    try:
        with open("a101_elektronik.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"💾 JSON dosyası kaydedildi ({len(data)} ürün)")
    except Exception as e:
        print(f"❌ JSON kayıt hatası: {e}")
    
    # Excel kaydı
    try:
        df = pd.DataFrame(data)
        df.to_excel("a101_elektronik.xlsx", index=False)
        print(f"📊 Excel dosyası kaydedildi ({len(data)} ürün)")
    except Exception as e:
        print(f"❌ Excel kayıt hatası: {e}")

if __name__ == "__main__":
    print("🚀 A101 Elektronik ürünleri çekiliyor...")
    products = get_a101_products()
    
    if products:
        save_data(products)
        print(f"🎉 Toplam {len(products)} ürün başarıyla kaydedildi!")
        
        # İlk 3 ürünü önizleme olarak göster
        print("\n📋 İlk 3 ürün:")
        for i, product in enumerate(products[:3], 1):
            print(f"{i}. {product['isim']} - {product['fiyat']}")