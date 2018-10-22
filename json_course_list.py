from bs4 import BeautifulSoup
import requests
import json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 소스 : http://rednooby.tistory.com/103?category=695414
#Ajax로 코딩되어 html이 보이지 않음
#url = "https://askdjango.github.io/lv2/"
#개발자도구의 network탭을 이용하여 json url가져옴(Preserve log 체크)
json_url = "https://askdjango.github.io/lv2/data.json"
json_string = requests.get(json_url).text
list = json.loads(json_string)
#print(list)

f = open('e:/imagedown/json_course_list.txt', 'wt', encoding='utf-8')

for i,li in enumerate(list,1):
    print(i, li['name'], li['url'])
    f.write(str(i) + ' ' + li['name'] + ' - ' + li['url'] + '\n')

f.close()
