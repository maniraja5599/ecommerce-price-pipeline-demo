"""
E-Commerce Price Scraper & Pipeline
Extracts product titles, prices, stock status, ratings, and URLs with automatic pagination.
Target: Scrape-friendly sandbox https://books.toscrape.com
"""

import re
import time
import logging
from typing import List, Dict, Optional
import requests
from bs4 import BeautifulSoup
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("EcommerceScraper")

BASE_URL = "https://books.toscrape.com/catalogue/"
START_URL = "https://books.toscrape.com/catalogue/page-1.html"

RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

class EcommerceScraper:
    def __init__(self, delay_seconds: float = 0.5):
        self.delay = delay_seconds
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9"
        })

    def scrape_page(self, page_number: int) -> List[Dict]:
        url = f"https://books.toscrape.com/catalogue/page-{page_number}.html"
        logger.info(f"Fetching page {page_number}: {url}")
        
        try:
            resp = self.session.get(url, timeout=10)
            if resp.status_code == 404:
                logger.info(f"Page {page_number} returned 404 (end of catalogue).")
                return []
            resp.raise_for_status()
        except requests.RequestException as e:
            logger.error(f"Failed to fetch {url}: {e}")
            return []

        soup = BeautifulSoup(resp.content, "html.parser")
        products = []

        articles = soup.select("article.product_pod")
        for article in articles:
            # 1. Title
            title_tag = article.select_one("h3 a")
            title = title_tag.get("title") or title_tag.text.strip() if title_tag else "N/A"

            # 2. Price
            price_tag = article.select_one("p.price_color")
            price_str = price_tag.text.strip() if price_tag else "£0.00"
            price_match = re.search(r"[\d.]+", price_str)
            price = float(price_match.group(0)) if price_match else 0.0

            # 3. Stock Status
            stock_tag = article.select_one("p.instock.availability")
            in_stock = True if stock_tag and "In stock" in stock_tag.text else False

            # 4. Rating
            rating_p = article.select_one("p.star-rating")
            rating = 0
            if rating_p:
                for cls in rating_p.get("class", []):
                    if cls in RATING_MAP:
                        rating = RATING_MAP[cls]
                        break

            # 5. Product URL
            rel_link = title_tag.get("href") if title_tag else ""
            product_url = f"{BASE_URL}{rel_link}" if not rel_link.startswith("http") else rel_link

            products.append({
                "title": title,
                "price_gbp": price,
                "in_stock": in_stock,
                "rating_stars": rating,
                "product_url": product_url,
                "scraped_at": time.strftime("%Y-%m-%d %H:%M:%S")
            })

        time.sleep(self.delay)
        return products

    def scrape_catalogue(self, max_pages: int = 3) -> pd.DataFrame:
        all_items = []
        for p in range(1, max_pages + 1):
            items = self.scrape_page(p)
            if not items:
                break
            all_items.extend(items)

        df = pd.DataFrame(all_items)
        logger.info(f"Total items extracted: {len(df)}")
        return df

if __name__ == "__main__":
    scraper = EcommerceScraper()
    df = scraper.scrape_catalogue(max_pages=2)
    print(df.head())
