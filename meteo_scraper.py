import requests
# import datetime
# from datetime import date
from bs4 import BeautifulSoup
import pandas as pd

url = "https://pomiary.gdanskiewody.pl/home/rain"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# dfs = pd.read_html(response.text)
print(soup)

table = soup.find_all('td')
print(table)
# tds = table.tr.find_all('td')
# print(tds)
# x = 0
# while x != 41:
#     for n, td in enumerate(tds):
#         print(f"index {n}: {td.text.strip()}")
#     x = x + 1

# tables = pd.read_html(url)
# t = tables[0]
# print(t.columns)
# print(type(list(t.columns)[0]))
# print(tables[1])

