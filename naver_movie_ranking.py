from bs4 import BeautifulSoup
import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
html = requests.get(url).text
#print(html)
soup = BeautifulSoup(html, "html.parser")

ranking = soup.select(".tit3")

f = open('e:/imagedown/naver_movie_rank.txt', 'wt', encoding='utf-8')

for i,rank in enumerate(ranking,1):
    print(i, rank.text.strip(), rank.find('a')['href'])
    f.write(str(i) + '위 ' + rank.text.strip() + ' ' + 'https://movie.naver.com' + rank.find('a')['href'] + '\n')

f.close()
