from bs4 import BeautifulSoup
import requests
import json
import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#소스 : http://rednooby.tistory.com/104?category=695414
url = "https://askdjango.github.io/lv3/"
html = requests.get(url).text
#print(html)
#자바스크립트 마지막엔 항상 세미콜론(;)이 있으므로 정규표현식을 사용하여 세미콜론 별로 잘라냄

#정규표현식에서 일부만 매칭되길 원하면 search
#정규표현식에서 전부를 매칭되길 원하면 match를 사용
#re.search(r'var courses = ();') # 끝에 있는 ()부분을 뽑아내겠다는 뜻
# .: 모든 *:문자열 즉 .* :모든문자열
# ' ? '을 사용하여 최소 매칭을 해줍니다.
matched = re.search(r'var courses = (.*?);', html, re.S) # re.S를 사용하여 개행을 포함하여 인식한다)
#print(matched)
#group으로 모두 출력하는데 1번째줄부터 출력합니다.
#만약 (0)을 주면 첫째줄인 var courses = [도 출력될것입니다.
#print(matched.group(1))
#json string으로 변경
json_string = matched.group(1)
list = json.loads(json_string)
#print(list)
f= open('e:/imagedown/javascript_list.txt', 'wt', encoding='utf-8')
for i,li in enumerate(list,1):
    print(i,li['name'],li['url'])
    f.write(str(i) + ' ' + li['name'] + ' - ' + li['url'] + '\n')

f.close()
