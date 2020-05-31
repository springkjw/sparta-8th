# 1. 지니 뮤직에 있는 노래 1~50위 곡 크롤링
# https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1
import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

# MongoDB에 연결하기
client = MongoClient('localhost', 27017)
# MongoDB의 Database에 접속
db = client.dbsparta

# requests 로 HTML 파일을 불러오기
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

