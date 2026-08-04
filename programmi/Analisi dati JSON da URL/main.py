import urllib.request
import json, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

s = 0

url = input('Enter location: ')

if len(url) < 1 : url = 'http://py4e-data.dr-chuck.net/comments_2275393.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()

print('Retrieved', len(data), 'characters')

try:
    info = json.loads(data)
except:
    info = None

for item in info['comments']:

    s += item['count']

print('Sum: ',s)
