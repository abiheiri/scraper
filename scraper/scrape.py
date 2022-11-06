#!/usr/bin/env python

from bs4 import BeautifulSoup
import argparse, requests, sys, re


class Scraper:
    prog='scraper'
    version='1.0'
    author='Al Biheiri (al@forgottheaddress.com)'
    HTTPTimeOutValue=60


    def do_list(self, fqdn, addURL, maxDepth):

        page = requests.get(fqdn, timeout=self.HTTPTimeOutValue)
        
        bs = BeautifulSoup(page.content, features='lxml')
        for link in bs.findAll('a'):
            if addURL == 1:
                print (fqdn + link.get('href'))
            else:
                print (link.get('href'))
                # print("href: {}".format(link.get("href")))

    def do_listWithDepth(self, fqdn, addURL, maxDepth):
        pass

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
        group.add_argument("-l", dest="list", metavar="http://mywebsite", help="list all the links inside a website")
        
        parser.add_argument("-a", dest="add", action="store_true", help="append the url to the front of each result")
        parser.add_argument("-m", dest="maxdepth", metavar="NUMBER", help="drill down to a maxdepth of", type=int)



        args = parser.parse_args()
        addURL = 0
        maxDepth = 0

        if args.list:
            if args.add:
                addURL=1
            if args.maxdepth:
                maxDepth = args.maxdepth
                if maxDepth > 10:
                    print ("Bro your nuts. I'm not doing that large of a traverse")
                    return

            self.do_list(args.list, addURL, maxDepth)

        else:
            print(f'Usage: {sys.argv[0]} -h', "for help.")

if __name__ == "__main__":
    Scraper().parse_args(sys.argv[1:])