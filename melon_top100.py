import requests
from bs4 import BeautifulSoup
import time

html = requests.get('https://www.reddit.com/').text
soup = BeautifulSoup(html, 'html.parser')
print(html)
tag_list = soup.select('div.rpBJOHq2PR60pnwJlUyP0')

for idx, tag in enumerate(tag_list, 1):
    print(idx, tag.text)
