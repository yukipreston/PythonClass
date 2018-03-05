import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Reno.html"
position = 18
numOfTimes = 7
names = list()

while numOfTimes > 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    tag = tags[position-1]
    url = tag.get('href', None)
    names.append(tag.contents[0])

    numOfTimes = numOfTimes - 1

print(names)
