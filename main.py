import imp
from typing import ItemsView
from wsgiref import headers
import requests
import re
import csv
from bs4 import BeautifulSoup

url = "https://www.cultizm.com/kor/sale/?p=1"
# headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")


items = soup.find("div", attrs={"class":re.compile("^listing--container") }) 

infos = items.find("a", attrs={"class":re.compile("^listing--supplier-link cultizm-supplier-name") })  

# print(infos)

def save_to_file():
    file =open("list.csv", mode="w")
    print(file)
    return

save_to_file()
    
# for item in items:
#     name = listing--supplier-link cultizm-supplier-name
# (item.find("div", attrs={"class" : "gridItemRoot"}).get_text())