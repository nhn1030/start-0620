import imp
import requests

from bs4 import BeautifulSoup
amazon_result = requests.get("https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/ref=zg_bs_pg_50?_encoding=UTF8&pg=2")

amazon_soup = BeautifulSoup(amazon_result.text, "html.parser")

print(amazon_soup)