#!/usr/bin/env python

from bs4 import BeautifulSoup
import argparse, requests, sys, re


class Scraper():
    prog='scraper'
    version='1.0'
    author='Al Biheiri (al@forgottheaddress.com)'
    HTTPTimeOutValue=60

    def do_get(self, fqdn):

        page = requests.get(fqdn, timeout=self.HTTPTimeOutValue)
        
        bs = BeautifulSoup(page.content, features='lxml')
        for link in bs.findAll('a'):
            print (fqdn + link.get('href'))



    def parse_args(self, args):
        from argparse import RawTextHelpFormatter
        parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter, 
        epilog=\
        '''

        ----------------------------------------------------------------
        This is designed to scrape
        
        ''',
        )


        parser.add_argument('--version', action='version', version='{} {}'.format(self.prog, self.version))


        group = parser.add_mutually_exclusive_group()
        group.add_argument("-g", dest="get", metavar="GET", help="type the web address")
        


        args = parser.parse_args()

        if args.get:
            self.do_get(args.get)

        else:
            print(f'Usage: {sys.argv[0]} -h', "for help.")

if __name__ == "__main__":
    Scraper().parse_args(sys.argv[1:])