#compare two stocks and tabulate it
from tabulate import tabulate
from bs4 import BeautifulSoup
#import re
import requests
final=[]
headers=['Parameter']
for i in range(2):
    sname = input(f"Enter {i+1} Stock Symbol:")
    if len(sname)==0:
        continue
    headers.append(sname)
    surl = f'https://www.screener.in/company/{sname}/consolidated/'
    source = requests.get(surl).text
    soup = BeautifulSoup(source,'html.parser')
    data={}
    for info in soup.find_all('li',class_='flex flex-space-between'):
        data[info.find('span',class_='name').text.strip()] = info.find('span',class_='number').text
    final.append(data)
if len(final)==1:
    print(tabulate(final[0].items(), headers = headers))
else:
    keys = final[0].keys()
    values = zip(final[0].values(),final[1].values())
    dictionary = dict(zip(keys,values))
    print(tabulate([(k,) + v for k,v in dictionary.items()], headers = headers))


