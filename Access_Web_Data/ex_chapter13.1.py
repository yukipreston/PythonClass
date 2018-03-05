import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

result = 0
url = 'http://py4e-data.dr-chuck.net/comments_7864.xml'
xml = urllib.request.urlopen(url).read()
tree = ET.fromstring(xml)
counts = tree.findall('comments/comment')

for item in counts:
    numbers = item.find('count').text
    numbers = int(numbers)
    result = result + numbers

print('User Count:', len(counts))
print ('Count:', result)
