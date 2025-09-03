import time
import random

for i in range(5):
    print(f"İşlem {i+1} başladı")
    sleep_time = random.uniform(1, 3)  # 1 ile 3 saniye arasında rastgele bekleme süresi
    time.sleep(sleep_time)
    print(f"İşlem {i+1} tamamlandı, {sleep_time:.2f} saniye bekledi")