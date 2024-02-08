import requests
# import datetime
# from datetime import date
from bs4 import BeautifulSoup
import pandas as pd

url = "https://pomiary.gdanskiewody.pl/home/rain"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

tables = pd.read_html(url)
t = tables[0]
print(t.columns)
print(type(list(t.columns)[0]))
