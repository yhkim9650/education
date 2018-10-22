from newspaper import Article

#크롤링할 뉴스 주소 입력
url = "https://news.v.daum.net/v/20170604205121164"
#언어가 한국어이므로 language='ko'로 설정
news = Article(url, language='ko')
news.download()
news.parse

#기사 제목 가져오기
print(news.title)

#기사 본문 가져오기(200자)
print(news.text[:200])
#기사 내용 가져오기(전부)
#print(news.text)
