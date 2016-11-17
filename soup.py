# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

import urllib2


urlics_str = '''https://sports.yahoo.com/ www.icc-cricket.com www.fifa.com www.rolandgarros.com www.yahoo.com www.lancasterarchery.com https://twitter.com/fih_hockey http://hoopshype.com/'''
hdr = {'User-Agent':
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
for urlic in urlics_str.split():

    if urlic.startswith("www"):
        urlic = "http://" + urlic
    req = urllib2.Request(urlic, headers=hdr)
    response = urllib2.urlopen(req)
    html_content = response.read().lower()

    soup = BeautifulSoup(html_content, 'lxml')

    l = ['football', 'cricket', 'tennis', 'archery', 'hockey', 'basketball']
    content_str = ("".join(str(soup.find_all('meta')).split())).lower()

    for word in l:
        if word in content_str:
            print urlic, word
