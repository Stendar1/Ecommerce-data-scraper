import csv
import time
import requests
from bs4 import BeautifulSoup

# Sayfa şablonu (1'den 50'ye kadar gideceğiz)
base_url = "https://books.toscrape.com/catalogue/page-{}.html"

with open("tum_kitaplar.csv", "w", encoding="utf-8-sig", newline="") as file:
  writer = csv.writer(file)
  writer.writerow(["Kitap Adı", "Fiyat", "Stok Durumu", "Puan"])

  toplam_kitap = 0

  for sayfa in range(1, 51):
    url = base_url.format(sayfa)
    print(f"Sayfa {sayfa}/50 taranıyor...")

    response = requests.get(url)
    if response.status_code != 200:
      print(f"Sayfa {sayfa} bulunamadı, durduruluyor.")
      break

    soup = BeautifulSoup(response.text, "html.parser")
    kitaplar = soup.find_all("article", class_="product_pod")

    for kitap in kitaplar:
      # 1. Başlık
      baslik = kitap.find("h3").find("a")["title"]

      # 2. Fiyat
      fiyat = kitap.find("p", class_="price_color").text

      # 3. Stok
      stok = kitap.find("p", class_="instock availability").text.strip()

      # 4. Yıldız Puanı (One, Two, Three, Four, Five şeklinde class içinde tutulur)
      puan_kutusu = kitap.find("p", class_="star-rating")
      puan = puan_kutusu["class"][1] if puan_kutusu else "Bilinmiyor"

      writer.writerow([baslik, fiyat, stok, puan])
      toplam_kitap += 1

    # Sunucuyu boğmamak için insani bir bekleme (profesyonel kural)
    time.sleep(0.1)

print(
    f"\nBitti! Toplam {toplam_kitap} kitap tertemiz çekildi ve 'tum_kitaplar.csv' hazırlandı."
)