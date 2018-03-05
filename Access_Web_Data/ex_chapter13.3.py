import urllib.request, urllib.parse, urllib.error
import json

url = 'http://py4e-data.dr-chuck.net/comments_7865.json'
data = urllib.request.urlopen(url).read().decode()
total = 0

js = json.loads(data)
info = js["comments"]

for item in info:
    test = item["count"]
    total = total + test

print ('Count:', len(info))
print ('Sum:', total)
