from urllib.request import urlopen
from bs4 import BeautifulSoup
url= "http://example.webscraping.com/places/default/index"
Data = urlopen(url)
soup = BeautifulSoup(Data, 'lxml')

for i in soup.findAll('td'):
    print('\n Country name    :')
    print(i.div.a.text)
    print('\n img url     :')
    print((i.div.img)['src'])

