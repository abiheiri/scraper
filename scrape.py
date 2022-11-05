#!/usr/bin/env python

from bs4 import BeautifulSoup
import argparse, requests, sys, re


class Scraper():
    prog='scraper'
    version='1.0'
    author='Al Biheiri (al@forgottheaddress.com)'
    HTTPTimeOutValue=60

    def do_get(self, fqdn, addURL):

        page = requests.get(fqdn, timeout=self.HTTPTimeOutValue)
        
        bs = BeautifulSoup(page.content, features='lxml')
        for link in bs.findAll('a'):
            if addURL == 1:
                print (fqdn + link.get('href'))
            else:
                print (link.get('href'))



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
        group.add_argument("-g", dest="get", metavar="http://mywebsite", help="get all the links inside a website")
        
        parser.add_argument("-a", dest="add", action="store_true", help="append the url to the front of each result")



        args = parser.parse_args()

        if args.get:
            if args.add:
                self.do_get(args.get, addURL=1)
            else:
                self.do_get(args.get, addURL=0)

        else:
            print(f'Usage: {sys.argv[0]} -h', "for help.")

if __name__ == "__main__":
    Scraper().parse_args(sys.argv[1:])