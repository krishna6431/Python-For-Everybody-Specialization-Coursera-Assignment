# Code is Written By Krishna

import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
url=input('Enter-')
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')
tags=soup('span')
arr=list()
for tag in tags:
    arr.append(*(tag.contents))

su=0    
for i in range(0,len(arr)):
    su+=int(arr[i])
print("Count",len(arr))
print("Sum",su)


# Thank U so mUCH
