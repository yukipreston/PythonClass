import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'
address = 'Wayne State'

url = serviceurl + urllib.parse.urlencode(
    {'address': address})
print ('Retrieving:', url)
data = urllib.request.urlopen(url).read().decode()
print ('Retrieved:', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

print (js['results'][0]['place_id'])
