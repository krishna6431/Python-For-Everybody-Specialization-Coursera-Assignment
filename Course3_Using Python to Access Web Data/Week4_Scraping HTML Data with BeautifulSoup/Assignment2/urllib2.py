import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
url=input('Enter-')
count=input('Enter Count: ')
pos=input('Enter Position: ')
print('Retrieving:',url)
while count:
    html=urllib.request.urlopen('url').read()
    soup=BeautifulSoup(html,'html.parser')
    tags=soup('a')
    list1=list()
    for tag in tags:
        list1.append(tag.get('href',None))
    print(list1[pos-1])
    url=list1[pos-1]
    list1.clear()
    count-=1
a=input()    
