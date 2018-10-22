import requests
from bs4 import BeautifulSoup
import sys
import io
import os.path
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

saveName = 'e:/python_section4/rss_chosun.xml'
url = "http://myhome.chosun.com/rss/www_section_rss.xml"

if os.path.exists(saveName):
    os.remove(saveName)
    req.urlretrieve(url, saveName)

items = open(saveName, 'r', encoding='utf-8').read()
soup = BeautifulSoup(items, "html.parser")
#print(soup)
fileName = 'e:/python_section4/rss_chosun_news.txt'
f = open(fileName, 'wt', encoding='utf-8')

newsList = soup.find_all("item")
for li in newsList:
    print('=' * 50)
    f.write('=' * 50)
    for list in li.children:
        if list.string != None:
            print((list.string).replace("<p>","").replace("</p>","").replace("strong","").replace("/strong","").replace("<br","").replace(">>",""), end='')
            f.write(str(list.string).replace("<p>","").replace("</p>","").replace("strong","").replace("/strong","").replace("<br","").replace(">>",""))
#    print('Title : ', li.title.text)
#    print('Link : ', li.link.text)
#    print('Description : ', li.description.text)
#    print('Dc:date : ', li.find('dc:date').text)
#    print('Author : ', li.author.text)
#    print('Pubdate : ', li.pubdate.text)
f.close()
