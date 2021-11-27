#compare two stocks and tabulate it
from tabulate import tabulate
from bs4 import BeautifulSoup
import requests
final=[]
headers=['Parameter']
for i in range(2):
    sname = input(f"Enter {i+1} Stock Symbol:")
    headers.append(sname)
    surl = f'https://www.screener.in/company/{sname}/consolidated/'
    source = requests.get(surl).text
    soup = BeautifulSoup(source,'html.parser')
    data={}
    profile = soup.find('div',class_='sub commentary always-show-more-box').text
    for info in soup.find_all('li',class_='flex flex-space-between'):
        data[info.find('span',class_='name').text.strip()] = info.find('span',class_='number').text
    final.append(data)
keys = final[0].keys()
values = zip(final[0].values(),final[1].values())
dictionary = dict(zip(keys,values))
print(tabulate([(k,) + v for k,v in dictionary.items()], headers = headers))
