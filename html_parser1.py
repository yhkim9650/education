from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

text = '''
<html>
<body>
<h1 align="center" id="boxofficeTypeId" class="boxofficeType">일별 박스오피스</h1>
<center>
<h1 id="showRangeId" class="showRange">20180220~20180220</h1>
</center>
<table border="1" align="center">
<tr>
<td class="rank">순위 (rank)</td>
<td class="rankOldAndNew">신규진입여부 (rankOldAndNew)</td>
<td class="movieCd">영화코드 (movieCd)</td>
<td class="movieNm">영화명 (movieNm)</td>
<td class="salesAmt">매출액 (salesAmt)</td>
<td class="audiCnt">관객수 (audiCnt)</td>
</tr>
<tr>
<td class="rank">1</td>
<td class="rankOldAndNew">OLD</td>
<td class="movieCd">20170561</td>
<td class="movieNm">블랙 팬서</td>
<td class="salesAmt">1339822000</td>
<td class="audiCnt">171158</td>
</tr>
</table>
</body>
</html>
'''
soup = BeautifulSoup(text, "html.parser")
###############################33
h1 = soup.select_one('h1')
print(h1) #첫번째 h1 태그 값
print(h1.text)
print(type(h1))
print(h1['align'], str(h1['class'][0]), h1['id'])

#태그[속성="속성값"] #속성값에 공백이 없으면 속성값 사이에 " 않써도 됨 #CSS Selector
print('=' * 30)
h1 = soup.select_one('h1[align=center]')
print(h1)
print(h1.text)
print(h1['id'])

# *= 부분 문자열 포함
print('=' * 30)
h1 = soup.select_one('h1[align*=ent]')
print(h1)

#속성이 id 일 경우 태그#속성값 사용 가능
print('=' * 30)
h1 = soup.select_one('h1#showRangeId')
print(h1)
print(h1.text)

print('=' * 30)
h1 = soup.select_one('h1[id=showRangeId]')
print(h1)
print(h1.text)

#속성이 class 일 경우 태그.속성값 사용 가능
print('=' * 30)
h1 = soup.select_one('h1.boxofficeType')
print(h1)
h1 = soup.select_one('h1[class=boxofficeType]')
print(h1)

#바로 상위에 body, center 태그가 있음
print('=' * 30)
h1 = soup.select_one('body > h1')  #바로 상위에 body가 있음
print(h1)
h1 = soup.select_one('center > h1') # 바로 상위에 center가 있음
print(h1)

# 상위 어딘가에 center 태그가 있음
print('=' * 30)
h1 = soup.select_one('center h1')
print(h1)
h1 = soup.select_one('body h1') # 상위 어딘가에 body가 있음
print(h1)

td = soup.select_one('tr .rankOldAndNew')
print(td)
print(td.text)
