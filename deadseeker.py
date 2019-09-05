'''
deadseeker.py
Seeking out your 404s in around 50 lines of vanilla Python.
'''

import sys
import urllib
from urllib import request
from urllib.parse import urlparse, urljoin
from urllib.request import Request
from html.parser import HTMLParser
from collections import deque

search_attrs = set(['href', 'src'])
agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'


class LinkParser(HTMLParser):
    def __init__(self, home, verbose):
        ''':home:    a homepage, e.g. 'https://healeycodes.com/'
           :verbose: boolean for for verbose mode'''
        super().__init__()
        self.home = home
        self.verbose = verbose
        self.checked_links = set()
        self.pages_to_check = deque()
        self.page = home
        self.pages_to_check.appendleft(home)
        self.scanner()

    def scanner(self):
        '''Loop through remaining pages, looking for HTML responses'''
        while self.pages_to_check:
            page = self.pages_to_check.pop()
            req = Request(page, headers={'User-Agent': agent})
            res = request.urlopen(req)
            if 'html' in res.headers['content-type']:
                with res as f:
                    body = f.read().decode('utf-8', errors='ignore')
                    self.page = page
                    self.feed(body)

    def handle_starttag(self, tag, attrs):
        '''Override parent method and check tag for our attributes'''
        for attr in attrs:
            # ('href', 'http://google.com')
            if attr[0] in search_attrs and attr[1] not in self.checked_links:
                self.checked_links.add(attr[1])
                self.handle_link(attr[1])

    def handle_link(self, link):
        '''Send a HEAD request to the link, catch any pesky errors'''
        if not bool(urlparse(link).netloc):  # relative link?
            link = urljoin(self.home, link)
        try:
            req = Request(link, headers={'User-Agent': agent}, method='HEAD')
            status = request.urlopen(req).getcode()
        except urllib.error.HTTPError as e:
            print(f'HTTPError: {e.code} - {link} - {self.page}')  # (e.g. 404, 501, etc)
        except urllib.error.URLError as e:
            print(
                f'URLError: {e.reason} - {link} - {self.page}'
            )  # (e.g. conn. refused)
        except ValueError as e:
            print(
                f'ValueError {e} - {link} - {self.page}'
            )  # (e.g. missing protocol http)
            print(f'ValueError {e} - {link}')  # (e.g. missing protocol http)
        else:
            if self.verbose:
                print(f'{status} - {link} - {self.page}')
        if self.home in link:
            self.pages_to_check.appendleft(link)


# check for verbose tag
verbose = len(sys.argv) > 2 and sys.argv[2] == 'v'
# enable this as a script, e.g., 'https://healeycodes.com/ v'
LinkParser(sys.argv[1], verbose)
