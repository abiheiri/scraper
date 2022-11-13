"importing scraper"
from scraper import Scraper

def test_scrape_help():
    """testing the -h flag"""
    scrape = Scraper()

    scrape.parse_args ("-h")
