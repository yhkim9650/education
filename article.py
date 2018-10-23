from bs4 import BeautifulSoup
import requests
import sys
import io
from collections import OrderedDict
from itertools import count
import pprint

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://www.segye.com/newsView/20181023002443"
article = requests.get(url).text
soup = BeautifulSoup(article, "html.parser")

news = soup.select('.news_text2018')

text = ''
for p in news:
    text = text + p.text

print(text).replace("<p>","")
