from scraper import Scraper
import pytest

def test_scrape_help():
    """testing the -h flag"""
    scrape = Scraper()

    with pytest.raises(SystemExit) as e:
        scrape.parse_args(["-h"])

    assert e.type == SystemExit
    # This assert checks for a clean exit, but you might want to remove or modify it
    # depending on how your Scraper class is supposed to handle `-h`
    assert e.value.code == 0  
