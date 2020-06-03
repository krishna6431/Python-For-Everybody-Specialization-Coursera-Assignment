import re
hand=open('actual.txt')
num_list=[]
for line in hand:
    line=line.rstrip()
    num=re.findall('[0-9]+',line)
    for i in num:
        num_list.append(int(i))
print(sum(num_list))
a=int(input())
       
# for i in num_list:
#     su+=int(i)
# print(su)    
