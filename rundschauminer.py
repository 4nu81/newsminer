#!/usr/bin/python

import urllib2
from bs4 import BeautifulSoup
import time

article = 5776085

with open('out.txt', 'w') as f:
    while True:

        url = "http://www.lr-online.de/;art1051,{article}".format(article = article)
        article += 1
        try:
            response = urllib2.urlopen(url)
        except urllib2.URLError:
        #    break
            pass
        soup = BeautifulSoup(response.read(), 'html.parser')
        f.write('Author: {author} Titel: {title}\n'.format(author=soup.footer.contents[1].string, title=soup.title.string))
        time.sleep(5)
