import pytest
import requests_mock
from scraper import Scraper
from io import StringIO
import sys

# Test for -h flag
def test_help_flag():
    scraper = Scraper()
    with pytest.raises(SystemExit) as e:
        scraper.parse_args(['-h'])
    assert e.value.code == 0

# Test for --version flag
def test_version_flag():
    scraper = Scraper()
    with pytest.raises(SystemExit) as e:
        with pytest.capsys.disabled():
            scraper.parse_args(['--version'])
    assert e.value.code == 0

# Mock test for scraping a URL with depth 1
@requests_mock.Mocker()
def test_scrape_with_mock_depth_1(m):
    test_html_main = '<html><body><a href="page1.html">Page 1</a></body></html>'
    test_html_subpage = '<html><body><a href="subpage1.html">Subpage 1</a></body></html>'
    m.get('http://www.abiheiri.com', text=test_html_main)
    m.get('http://www.abiheiri.com/page1.html', text=test_html_subpage)

    scraper = Scraper()

    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output

    scraper.run('http://www.abiheiri.com', 1)

    # Restore stdout
    sys.stdout = sys.__stdout__

    assert 'http://www.abiheiri.com/page1.html' in captured_output.getvalue()
    assert 'http://www.abiheiri.com/subpage1.html' not in captured_output.getvalue()

# Mock test for scraping a URL with depth 2
@requests_mock.Mocker()
def test_scrape_with_mock_depth_2(m):
    test_html_main = '<html><body><a href="page1.html">Page 1</a></body></html>'
    test_html_subpage = '<html><body><a href="subpage1.html">Subpage 1</a></body></html>'
    m.get('http://www.abiheiri.com', text=test_html_main)
    m.get('http://www.abiheiri.com/page1.html', text=test_html_subpage)

    scraper = Scraper()

    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output

    scraper.run('http://www.abiheiri.com', 2)

    # Restore stdout
    sys.stdout = sys.__stdout__

    assert 'http://www.abiheiri.com/page1.html' in captured_output.getvalue()
    assert 'http://www.abiheiri.com/subpage1.html' in captured_output.getvalue()

# Mock test for scraping a URL with .mp3 filter
@requests_mock.Mocker()
def test_scrape_with_mp3_filter(m):
    test_html = ('<html><body>'
                 '<a href="song1.mp3">Song 1</a>'
                 '<a href="song2.mp3">Song 2</a>'
                 '<a href="document.pdf">Document</a>'
                 '</body></html>')
    m.get('http://www.abiheiri.com', text=test_html)

    scraper = Scraper()

    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output

    scraper.filter_ext = '.mp3'
    scraper.run('http://www.abiheiri.com', 1)

    # Restore stdout
    sys.stdout = sys.__stdout__

    output = captured_output.getvalue()
    assert 'http://www.abiheiri.com/song1.mp3' in output
    assert 'http://www.abiheiri.com/song2.mp3' in output
    assert 'http://www.abiheiri.com/document.pdf' not in output

