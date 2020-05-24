# 웹 스크래밍 = 웹 크롤링
# 웹 사이트 정도를 긁어오는 기술
# requests => API 또는 HTML 페이지 요청
# bs4(beautiful soup 4 ) => 받아온 HTML 파일을 읽기 쉽게 파싱(parsing)
import requests
from bs4 import BeautifulSoup

# 크롤링: 데이터를 훔치는 작업
# 크로링 > 창vs방패
# 요청을 날리는걸 웹 브라우저가 날리는 것처럼 속이는 작업
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
data = requests.get(
    'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',
    headers=headers
)
soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('#old_content > table > tbody > tr')

for movie in movies:
    a_tag = movie.select_one('td.title > div > a')
    # <a 태그 결과값>
    # a_tag = movie.select('td.title > div > a')
    # [<a 태그 결과값>]
    
    if a_tag is not None:
        print(a_tag.text)

# select : 결과값이 항상 리스트
# select_one : 결과값이 항상 HTML 태그
