#!/usr/bin/python

import urllib2
from bs4 import BeautifulSoup
import datetime

today = datetime.datetime.today()
days = []

for i in xrange(3):
    date = today - datetime.timedelta(days = i)
    days.append(date.strftime('%Y%m%d'))

url = 'http://www.golem.de/ticker/'
try:
    response = urllib2.urlopen(url)
except urllib2.URLError:
    pass
else:
    soup = BeautifulSoup(response.read(), 'html.parser')
    for date in days:
        print date
        for li in soup.find(id='list-{date}'.format(date=date)).find_all('li'):
            link = li.a.get('href')
            time = li.p.text
            print time, link

    #f.write('Author: {author} Titel: {title} Link: {link}\n'.format(author=soup.footer.contents[1].string, title=soup.title.string, link=link))
    #time.sleep(5)
