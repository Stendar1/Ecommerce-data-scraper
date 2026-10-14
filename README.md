# 📚 E-Commerce & Web Data Extraction Suite

A lightweight, automated Python data scraper designed to extract catalog, pricing, availability, and rating metrics from multi-page web architectures. Built for reliable batch processing and structured data export (CSV).

## 🚀 Features
- **Multi-Page Pagination:** Automatically iterates through 50 catalog pages.
- **Robust Field Extraction:** Extracts product title, price (£), real-time stock availability, and star ratings.
- **Clean Export:** Exports clean, formatted UTF-8 CSV data (`tum_kitaplar.csv`) ready for data analysis and Excel.
- **Server-Friendly:** Implements rate-limiting delays to prevent request throttling.

## 🛠️ Tech Stack
- **Python 3**
- **Requests:** Fast and reliable HTTP request handling.
- **BeautifulSoup4:** HTML tree traversal and DOM parsing.
- **CSV Module:** Native data pipeline export.

## 📦 Quick Start
1. Clone the repository:
   ```bash
   git clone [https://github.com/](https://github.com/)<kullanici-adin>/ecommerce-book-scraper.git
   cd ecommerce-book-scraper