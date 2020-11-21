# Using beautifulsoup to scrape a webpage

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

url = input('Enter the url: ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrive all the anchor tags
tags = soup('a')
for tag in tags :
    print(tag.get('href', None))