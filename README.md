# 🛒 E-Commerce Competitor Price Monitor & Pipeline

A production-grade Python data extraction pipeline designed for e-commerce intelligence, market price monitoring, and automated spreadsheet reporting.

---

## ⚡ Key Architecture & Features

- **Robust Web Scraping**: Built with `requests` and `BeautifulSoup4` with custom user-agent rotation and rate limiting.
- **Data Normalization**: Cleans currency strings, normalizes boolean stock availability, and transforms ratings into numeric scales.
- **Multi-Format Export**: Generates clean UTF-8 CSVs ready for immediate Google Sheets / Excel import or SQL ingestion.
- **Automated Summary Analytics**: Automatically outputs total product count, in-stock percentages, and average price metrics upon pipeline completion.
- **Unit Tested**: Fully tested data parsing integrity.

---

## 🚀 Quickstart

### 1. Install Dependencies
```bash
pip install requests beautifulsoup4 pandas
```

### 2. Run Pipeline
```bash
# Scrape 3 pages (60 products) with 0.5s polite delay
python main.py --pages 3 --delay 0.5 --output output/products.csv
```

### 3. Pipeline Output Sample
```json
{
  "total_products": 60,
  "in_stock_count": 60,
  "out_of_stock_count": 0,
  "stock_rate_pct": 100.0,
  "average_price_gbp": 35.07,
  "average_rating_stars": 3.3
}
```

---

## 💼 Commercial & Freelance Retainer Ready
Engineered by **Mani Raja** (FiFTO Automation).  
Available for custom client scrapers, daily price tracking pipelines, and CRM/Google Sheets sync integrations.
