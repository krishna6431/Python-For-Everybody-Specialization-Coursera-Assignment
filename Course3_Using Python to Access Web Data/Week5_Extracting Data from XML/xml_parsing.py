#this code is written by krishna kant verma
import xml.etree.ElementTree as ET
import urllib.request
url=input("Enter location: ")
data=urllib.request.urlopen(url).read()
print("Retrieving",url)
print("Retrieved",len(data),"characters")
tree=ET.fromstring(data)
count_list=tree.findall('comments/comment/count')
total=0
counter=0
for count in count_list:
    counter+=1
    total+=int(count.text)
print("Count:",counter)    
print("Sum:",total)