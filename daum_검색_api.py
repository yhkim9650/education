import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
from html.parser import HTMLParser
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://dapi.kakao.com/v2/search/web"
MYAPP_KEY = '73b6bdd831a01d706e87951bc2b82aca'
headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}
params = {
    'query':'류현진',
    'output':'json',
    'size': 50
}
res = requests.get(url, params=params, headers = headers)
print(res.text)
#print(res.content)
data = json.loads(res.text)

for key in data:
    print(data[key])
