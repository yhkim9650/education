from bs4 import BeautifulSoup
import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://rss.blog.naver.com/vecomm.xml"

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
}

res = requests.get(url, headers= headers).text
bsObj = BeautifulSoup(res, "html.parser")

for item in bsObj.select("item"):
    print('=' * 30)
#    for li in item.children:
#        print(li.string)

    print('author : ', item.author.text)
    print('Category : ', item.category.text)
    print('Title : ', item.title.text)
    #print('Link : ', item.link.text.lstrip())
    print('Link : ', item.guid.text)
    print('Description : ', item.description.text)
    print('PubDate : ', item.pubdate.text)
    print('Activity:verb : ', item.find('activity:verb').text)
    print('Activity:object-type : ', item.find('activity:object-type').text)
