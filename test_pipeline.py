import pytest
from scraper import EcommerceScraper
from sheets_sync import DataExporter

def test_scraper_single_page():
    scraper = EcommerceScraper(delay_seconds=0.1)
    items = scraper.scrape_page(1)
    assert len(items) == 20
    first = items[0]
    assert "title" in first
    assert "price_gbp" in first
    assert isinstance(first["price_gbp"], float)
    assert first["price_gbp"] > 0
    assert "in_stock" in first
    assert "rating_stars" in first

def test_exporter_summary():
    scraper = EcommerceScraper(delay_seconds=0.1)
    df = scraper.scrape_catalogue(max_pages=1)
    exporter = DataExporter()
    summary = exporter.export_summary(df)
    assert summary["total_products"] == 20
    assert summary["average_price_gbp"] > 0
