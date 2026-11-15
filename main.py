"""
E-Commerce Price Scraper & Google Sheets Pipeline
Main CLI Execution Script
"""

import argparse
import json
from scraper import EcommerceScraper
from sheets_sync import DataExporter

def main():
    parser = argparse.ArgumentParser(description="Autonomous E-Commerce Price Scraper & Pipeline")
    parser.add_argument("--pages", type=int, default=3, help="Number of pages to scrape (default: 3)")
    parser.add_argument("--delay", type=float, default=0.5, help="Polite delay between requests in seconds")
    parser.add_argument("--output", type=str, default="scraped_ecommerce_products.csv", help="Output CSV filename")
    args = parser.parse_args()

    print("=" * 65)
    print(" 🛒 E-COMMERCE PRICE MONITORING & SHEETS PIPELINE ")
    print("=" * 65)

    scraper = EcommerceScraper(delay_seconds=args.delay)
    df = scraper.scrape_catalogue(max_pages=args.pages)

    exporter = DataExporter()
    out_file = exporter.export_csv(df, filename=args.output)
    summary = exporter.export_summary(df)

    print("\n📊 PIPELINE SUMMARY REPORT:")
    print(json.dumps(summary, indent=2))
    print(f"\n📁 Saved {len(df)} records to: {out_file.resolve()}\n")

if __name__ == "__main__":
    main()
