import requests
from bs4 import BeautifulSoup
synonyms=input("> ")
_string_decode='68 74 74 70 3a 2f 2f 77 77 77 2e 74 68 65 73 61 75 72 75 73 2e 63 6f 6d 2f 62 72 6f 77 73 65 2f ' + synonyms.lower().encode('utf-8').hex()


url=requests.get(bytearray.fromhex(_string_decode).decode())

final_list=[]

soup=BeautifulSoup(url.text,'html.parser')
first=soup.find_all("div",{"class":"relevancy-list"})
for m in first:
    new=m.find_all('ul')
    for mm in new:
        again=mm.find_all('li')
        for i in again:
            final_list.append(i.find('span', {'class': "text"}).text )

print(final_list)
