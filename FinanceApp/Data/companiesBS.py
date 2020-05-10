import requests
from bs4 import BeautifulSoup

data = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
soup = BeautifulSoup(data.content,"lxml")


names = soup.select("table[id=constituents] >tbody > tr > td:nth-child(1) > a")
inds = soup.select("table[id=constituents] >tbody > tr > td:nth-child(2) > a")

for i in range(500):
    with open("comapniesBS.csv", "a") as f:
        f.write(names[i].text + "/" + inds[i].text + "\n")
