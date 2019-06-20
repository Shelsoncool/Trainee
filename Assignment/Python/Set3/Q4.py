import urllib.request
import urllib.parse
import re

url='https://www.w3schools.com/xml/simple.xml'

try:
    x=urllib.request.urlopen(url)
    data=x.read()
    #print(data)
    name=re.findall(r'<name>(.*?)</name>',str(data))
    price=re.findall(r'<price>(.*?)</price>',str(data))
    for i in range(0,len(name)):
        print("Name: " + str(name[i])+"\n"+"Price:" + str(price[i])+"\n")
except Exception as e:
    print(str(e))
