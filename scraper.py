import csv
import requests
from bs4 import BeautifulSoup

base_url = "https://quotes.toscrape.com"
current_path = "/"

# Yeni bir CSV dosyası açıyoruz
with open("tum_sozler.csv", "w", encoding="utf-8-sig", newline="") as file:
  writer = csv.writer(file)
  writer.writerow(["Sayfa", "Yazar", "Söz"])

  sayfa_no = 1

  # Sayfa linki var olduğu sürece durma
  while current_path:
    print(f"Sayfa {sayfa_no} kazınıyor...")
    response = requests.get(base_url + current_path)
    soup = BeautifulSoup(response.text, "html.parser")

    # Sayfadaki sözleri topla ve yazdır
    quotes = soup.find_all("div", class_="quote")
    for q in quotes:
      text = q.find("span", class_="text").text
      author = q.find("small", class_="author").text
      writer.writerow([sayfa_no, author, text])

    # Sırada 'Next' butonu var mı kontrol et
    next_button = soup.find("li", class_="next")
    if next_button:
      current_path = next_button.find("a")["href"]
      sayfa_no += 1
    else:
      # Next butonu yoksa döngüden çık
      current_path = None

print("\nBitti! Bütün sayfalar tarandı ve 'tum_sozler.csv' hazırlandı.")