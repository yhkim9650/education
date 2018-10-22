from bs4 import BeautifulSoup
import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.naver.com/"
html = requests.get(url).text
#print(html)
soup = BeautifulSoup(html, "html.parser")
realTimeSrcList = soup.select("div.ah_roll_area .ah_k")
#print(realTimeSrcList)

f = open('e:/imagedown/실시간검색어.txt', 'wt', encoding='utf-8')
for i,list in enumerate(realTimeSrcList,1):
    print(i,list.text)
    f.write(str(i) + '위 ' + list.text + '\n')

f.close()
