from requests import get
from bs4 import BeautifulSoup
from datetime import datetime
from extrator.moneytoday import search_mk_news
from extrator.NaverNews import search_naver_news
# from extrator.MKnews 

TODAY = datetime.now().date()

MT = 'https://news.mt.co.kr/newsList.html?pDepth1=estate&pDepth2=Etotal' # 머니투데이
NV = 'https://land.naver.com/news/field.naver?bss_ymd=20221019&news_type_cd=10' #네이버

MoneyToday = search_mk_news('머니투데이', MT)
Naver = search_naver_news('네이버부동산', NV)

# MeailK = search_new(MeailK, MK)

file = open(f"{TODAY}.csv", 'w', encoding='utf-8-sig')
file.write("center, image, title, link ,press, regidate\n")

for news in MoneyToday:
  file.write(f"{news['center']}, {news['image']}, {news['title']}, {news['link']}, {news['press']}, {news['regidate']}\n")


for news in Naver:
  file.write(f"{news['center']}, {news['image']}, {news['title']}, {news['link']}, {news['press']}, {news['regidate']}\n")
file.close()

