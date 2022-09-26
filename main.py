from requests import get
from bs4 import BeautifulSoup
from datetime import datetime
from extrator.moneytoday import search_news

TODAY = datetime.now().date()

MT = 'https://news.mt.co.kr/newsList.html?pDepth1=estate&pDepth2=Etotal'
MK = 'https://www.mk.co.kr/news/realestate/'

MoneyToday = search_news('머니투데이', MT)
# MeailK = search_new(MeailK, MK)

file = open(f"{TODAY}.csv", 'w')
file.write("center, image, title, link ,press, regidate\n")

for news in MoneyToday:
  file.write(f"{news['center']}, {news['image']}, {news['title']}, {news['link']}, {news['press']}, {news['regidate']}\n")
file.close()




