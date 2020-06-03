# json parsing using google geo api assignment 
#code is written by krishna
#part of course 3 of python for everybody specialization
import urllib.request
from urllib.parse import urlencode
import urllib.error
import json
import ssl

api_key=False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:

    address = input("Enter location: ")
    
    
    if len(address) < 1:
        break
    
    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    

    print('Retrieving', url)

    uh = urllib.request.urlopen(url,context=ctx)
    data=uh.read().decode()
    
    print('Retrived', len(data), 'characters')

    try:
        info = json.loads(data)
    except:
        info = None
    if not info or 'status' not in info or info['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    placeid = info["results"][0]['place_id']
    print("Place id", placeid)

#     thank u so much 
