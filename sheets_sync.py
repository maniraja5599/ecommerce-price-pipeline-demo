"""
Google Sheets & CSV Exporter Pipeline
Handles export of scraped e-commerce data to CSV, Excel, and Google Sheets.
"""

import os
import logging
from pathlib import Path
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("SheetsSync")

class DataExporter:
    def __init__(self, output_dir: str = "output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def export_csv(self, df: pd.DataFrame, filename: str = "ecommerce_prices.csv") -> Path:
        out_path = self.output_dir / filename
        df.to_csv(out_path, index=False, encoding="utf-8")
        logger.info(f"✅ Data exported successfully to CSV: {out_path.resolve()}")
        return out_path

    def export_summary(self, df: pd.DataFrame) -> dict:
        total_products = len(df)
        in_stock_count = df["in_stock"].sum() if "in_stock" in df else 0
        avg_price = df["price_gbp"].mean() if "price_gbp" in df else 0.0
        avg_rating = df["rating_stars"].mean() if "rating_stars" in df else 0.0

        summary = {
            "total_products": int(total_products),
            "in_stock_count": int(in_stock_count),
            "out_of_stock_count": int(total_products - in_stock_count),
            "stock_rate_pct": round((in_stock_count / total_products * 100), 1) if total_products > 0 else 0,
            "average_price_gbp": round(float(avg_price), 2),
            "average_rating_stars": round(float(avg_rating), 1)
        }
        return summary
