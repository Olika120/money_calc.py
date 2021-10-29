import requests
from bs4 import BeautifulSoup
import re
import signal, os

headers = {'User-Agent': 'Mozilla/5.0'}
econ_url = 'https://www.mnb.hu/arfolyamok'
html_text = requests.get(econ_url, headers=headers).text
soup = BeautifulSoup(html_text, 'html.parser')

for tb in soup.find_all("table"):
    trs = tb.findAll("tr")
    for tr in trs:
        tds = tr.findAll("td")
        tdcnt = 0
        deviza = "NULL"
        value = "0"
        for td in tds:
            if tdcnt == 0: deviza = td.text
            if tdcnt == 3: value = td.text
            tdcnt+=1
        if deviza != "NULL":
            print(deviza+" = "+value+" HUF")
