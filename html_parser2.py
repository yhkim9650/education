from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#하위 태그객체 접근
#: 태그객체 = 태그객체.태그객체
#태그객체 = 태그객체.select_one(CSS Selector)
#리스트 = 태그객체.select(CSS Selector)
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

table = soup.select_one('table') #select_one
print(table)
print(type(table)) #<class 'bs4.element.Tag'>

#[<table align="center" border="1">
#<tr>
#<td class="rank">순위 (rank)</td>
#<td class="rankOldAndNew">신규진입여부 (rankOldAndNew)</td>
#<td class="movieCd">영화코드 (movieCd)</td>
#<td class="movieNm">영화명 (movieNm)</td>
#<td class="salesAmt">매출액 (salesAmt)</td>
#<td class="audiCnt">관객수 (audiCnt)</td>
#</tr>
#<tr>
#<td class="rank">1</td>
#<td class="rankOldAndNew">OLD</td>
#<td class="movieCd">20170561</td>
#<td class="movieNm">블랙 팬서</td>
#<td class="salesAmt">1339822000</td>
#<td class="audiCnt">171158</td>
#</tr>
#</table>]

print(table.text)
#순위 (rank)
#신규진입여부 (rankOldAndNew)
#영화코드 (movieCd)
#영화명 (movieNm)
#매출액 (salesAmt)
#관객수 (audiCnt)
#
#
#1
#OLD
#20170561
#블랙 팬서
#1339822000
#171158

#print(table.select_one('tr'))
print(table.tr) #첫번째 tr 테그 가져옴
#<tr>
#<td class="rank">순위 (rank)</td>
#<td class="rankOldAndNew">신규진입여부 (rankOldAndNew)</td>
#<td class="movieCd">영화코드 (movieCd)</td>
#<td class="movieNm">영화명 (movieNm)</td>
#<td class="salesAmt">매출액 (salesAmt)</td>
#<td class="audiCnt">관객수 (audiCnt)</td>
#</tr>

print(table.tr.text)
#순위 (rank)
#신규진입여부 (rankOldAndNew)
#영화코드 (movieCd)
#영화명 (movieNm)
#매출액 (salesAmt)
#관객수 (audiCnt)

print(table.tr.td) #tr태그의 첫번째 td
#<td class="rank">순위 (rank)</td>

print(table.tr.td.text)
#순위 (rank)
