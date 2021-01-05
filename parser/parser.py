from bs4 import BeautifulSoup
import requests as req

resp = req.get("https://python-scripts.com/beautifulsoup-html-parsing#BeautifulSoup-examples")

soup = BeautifulSoup(resp.text, 'lxml')
spisok = []
items = soup.find_all("td")
for i in range(len(items)):
    spisok.append({i+1: items[i]})
print(spisok)


