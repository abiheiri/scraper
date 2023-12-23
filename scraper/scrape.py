#!/usr/bin/env python

import signal
import sys
from bs4 import BeautifulSoup
import requests
import argparse
from urllib.parse import urljoin

class Scraper:
    def __init__(self):
        self.prog = 'scraper'
        self.version = '1.4'
        self.author = 'Al Biheiri (al@forgottheaddress.com)'
        self.http_timeout = 10
        self.visited_urls = set()
        self.filter_ext = None

    def is_directory_link(self, url):
        # Simple heuristic: if the URL doesn't have a period in the last segment, it's likely a directory
        return '/' in url.rstrip('/') and '.' not in url.rstrip('/').split('/')[-1]

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
                    if full_url.startswith(('http://', 'https://')):
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
            if self.filter_ext and link.lower().endswith(self.filter_ext):
                print(link)
            if self.is_directory_link(link) or (self.filter_ext and link.lower().endswith(self.filter_ext)):
                self.scrape_links(link, depth - 1)

    def run(self, url, max_depth):
        """ Run the scraper with the given arguments. """
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url

        if max_depth > 10:
            print("Depth too large. Limiting to 10 for performance reasons.")
            max_depth = 10

        print(f"Filter set to: {self.filter_ext}")
        self.scrape_links(url, max_depth)

    def parse_args(self, args):
        """ Parse command line arguments. """
        parser = argparse.ArgumentParser(description="Web Scraper")
        parser.add_argument('url', help="URL to scrape")
        parser.add_argument('-m', '--max_depth', type=int, help="Maximum depth to scrape", default=1)
        parser.add_argument('-f', '--filter', type=str, help="Filter results by file extension, e.g., 'mkv' (without the dot)")
        parser.add_argument('--version', action='version', version=f'{self.prog} {self.version}')

        args = parser.parse_args(args)
        if args.filter:
            self.filter_ext = '.' + args.filter.lower()  # Ensure dot is included
        return args

def signal_handler(sig, frame):
    print("Quitting...")
    sys.exit(0)

if __name__ == "__main__":
    # Register the signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    scraper = Scraper()
    args = scraper.parse_args(sys.argv[1:])
    scraper.run(args.url, args.max_depth)
