#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import argparse
import sys
from urllib.parse import urljoin, urlparse

class Scraper:
    def __init__(self):
        self.prog = 'scraper'
        self.version = '1.0'
        self.author = 'Al Biheiri (al@forgottheaddress.com)'
        self.http_timeout = 10
        self.visited_urls = set()

    def fetch_links(self, url):
        """ Fetch links from a given URL and return full URLs. """
        try:
            response = requests.get(url, timeout=self.http_timeout)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, features='lxml')

            links = []
            for link in soup.findAll('a'):
                href = link.get('href')
                if href:
                    full_url = urljoin(url, href)
                    # Check if the URL is an HTTP URL
                    if urlparse(full_url).scheme in ['http', 'https']:
                        links.append(full_url)

            return links
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return []

    def scrape_links(self, url, depth, link_limit=10):
        """ Recursively scrape links to a specified depth, printing as they are found. """
        if depth <= 0 or url in self.visited_urls:
            return

        self.visited_urls.add(url)
        links = self.fetch_links(url)[:link_limit]

        for link in links:
            print(link)
            self.scrape_links(link, depth - 1)

    def run(self, url, max_depth):
        """ Run the scraper with the given arguments. """
        if max_depth > 10:
            print("Depth too large. Limiting to 10 for performance reasons.")
            max_depth = 10

        self.scrape_links(url, max_depth)

    def parse_args(self, args):
        """ Parse command line arguments. """
        parser = argparse.ArgumentParser(description="Web Scraper")
        parser.add_argument('--version', action='version', version=f'{self.prog} {self.version}')
        parser.add_argument("-l", dest="url", help="URL to scrape")
        parser.add_argument("-m", dest="max_depth", type=int, help="Maximum depth to scrape", default=1)
        return parser.parse_args(args)

if __name__ == "__main__":
    args = Scraper().parse_args(sys.argv[1:])
    Scraper().run(args.url, args.max_depth)
