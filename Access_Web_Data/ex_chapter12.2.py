import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter: ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

total = 0
tags = soup('span')

for tag in tags:
    number = int(tag.contents[0])
    total = total + number

print (total)
