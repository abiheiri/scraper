import pytest
from scraper import Scraper

def test_scrape_help():
    scrape = Scraper()

    scrape.parse_args ("-h")

    