import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
url = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0'
res = requests.get(url, headers=headers)
text = res.text
#print(text)

soup = BeautifulSoup(text, 'html.parser')
#print(soup)

for li in soup.select('#elThumbnailResultArea > li'): #반복되는 태그
    #print(li)
    print(li.dl.dt.a.text, li.dl.dt.a['href'])
    print(li.dl.dt.a.text)
