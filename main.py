# -*- coding: utf-8 -*-

import urllib2
from collections import OrderedDict

# Get the page content
urlics_str = '''https://sports.yahoo.com/ www.icc-cricket.com www.fifa.com www.rolandgarros.com www.yahoo.com www.lancasterarchery.com https://twitter.com/fih_hockey http://hoopshype.com/'''

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


def which_sport_on_page(url):

    sport_names_dict = {}

    sport_names_dict = dict.fromkeys(['football', 'cricket', 'tennis', 'archery', 'hockey', 'basketball'])

    req = urllib2.Request(url, headers=hdr)
    try:
        response = urllib2.urlopen(req)
        html_content = response.read().lower()
    except urllib2.HTTPError, e:
        print e.fp.read()
        return

    for name in sport_names_dict.keys():
        sport_names_dict[name] = html_content.count("{}".format(name))

    res = OrderedDict(sorted(sport_names_dict.items(), key=lambda v: v[1]))
    print res.values()
    return res.keys()[-1] if res[res.keys()[-1]] else "NA"

for urlic in urlics_str.split():

    if urlic.startswith("www"):
        urlic = "http://" + urlic

    print str(urlic)
    print which_sport_on_page(urlic)
