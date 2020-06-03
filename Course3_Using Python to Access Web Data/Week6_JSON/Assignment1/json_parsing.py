# json parsing assignment
#code is written by krishna
#part of course 3 of python for everybody specialization
import json
import urllib.request
url=input("Enter location: ")
data=urllib.request.urlopen(url).read().decode('utf-8')
print("Retrieving",url)
print("Retrieved",len(data),"characters")
info=json.loads(data)
su=0
count=0;
for item in info["comments"]:
    su+=int(item["count"])
    count+=1
print("Count:",count)
print("Sum:",su)    
