from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#여러 태그객체 접근
#: 리스트 = soup.select(CSS Selector)

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

for tr in soup.select('tr'):
    #print(tr.td.text)
    #print(tr.select_one('td'))
    print(tr.select_one('td[class=rank]').text,
        tr.select_one('td[class=rankOldAndNew]').text,
        tr.select_one('td[class=movieCd]').text,
        tr.select_one('td[class=movieNm]').text,
        tr.select_one('td[class=salesAmt]').text,
        tr.select_one('td[class=audiCnt]').text
        )
