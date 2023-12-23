from scraper import Scraper
import pytest

def test_scrape_help():
    """testing the -h flag"""
    scrape = Scraper()

    with pytest.raises(SystemExit) as e:
        scrape.parse_args("-h")
    
    assert e.type == SystemExit
    assert e.value.code == 0  # Ensure that the exit code is 0, which typically indicates a clean exit
