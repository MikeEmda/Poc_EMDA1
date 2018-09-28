from urllib import urlopen
from bs4 import BeautifulSoup
import re
g= open("headlines.txt","a+")
source  = urlopen('http://www.standard.co.uk/news/crime/rss').read()
#print source
title = re.compile('<title>(.*)</title>')
link = re.compile('<link>(.*)</link>')
description = re.compile('<description>(.*)</description>')
pubDate = re.compile('<pubDate>(.*)</pubDate>')
find_title = re.findall(title, source)
find_link = re.findall(link, source)
find_description = re.findall(description, source)
find_pubDate = re.findall(pubDate, source)
find_title.pop(0)
find_link.pop(0)
find_description.pop(0)
for f in range(len(find_title)):
    print find_title[f]
    g.write(str(find_title[f])+"\n")
    print find_link[f]
    print find_description[f]
    print find_pubDate[f]
    print

source  = urlopen('http://www.independent.co.uk/news/uk/rss').read()
#print source
title = re.compile('<title>(.*)</title>')
link = re.compile('<link>(.*)</link>')
description = re.compile('<description>(.*)</description>')
pubDate = re.compile('<pubDate>(.*)</pubDate>')
find_title = re.findall(title, source)
find_link = re.findall(link, source)
find_description = re.findall(description, source)
find_pubDate = re.findall(pubDate, source)
find_title.pop(0)
find_link.pop(0)
find_description.pop(0)
for f in range(len(find_title)):
    print find_title[f]
    g.write(str(find_title[f])+"\n")
    print find_link[f]
    print find_description[f]
    print find_pubDate[f]
    print

source  = urlopen('http://feeds.bbci.co.uk/news/uk/rss.xml?edition=uk').read()
#print source
title = re.compile('<title>(.*)</title>')
link = re.compile('<link>(.*)</link>')
description = re.compile('<description>(.*)</description>')
pubDate = re.compile('<pubDate>(.*)</pubDate>')
find_title = re.findall(title, source)
find_link = re.findall(link, source)
find_description = re.findall(description, source)
find_pubDate = re.findall(pubDate, source)
find_title.pop(0)
find_title.pop(0)
find_link.pop(0)
find_link.pop(0)
find_description.pop(0)
for f in range(len(find_title)):
    print find_title[f]
    g.write(str(find_title[f])+"\n")
    print find_link[f]
    print find_description[f]
    print find_pubDate[f]
    print