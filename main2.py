from urllib import response
from requests import get
from bs4 import BeautifulSoup

# base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
# base_url = "https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=All&SearchWord="
# base_url = "https://finance.naver.com/search/searchList.naver?query="
base_url = "https://land.naver.com/news/field.naver"

response = get(base_url)

if response.status_code != 200:
  print("Can't request website")
else:
  soup = BeautifulSoup(response.text, "html.parser")
  news_post = soup.find_all("div", class_="section_headline")

  for news in news_post:
    contents = news.find_all('li')
  for content in contents:
      dtTags = content.find_all('dt')
      dtTag_image = dtTags[0]
      dtTag_title = dtTags[1]
      ddTag = content.find_all('dd')
      
      print(dtTag_image, "\n", dtTag_title)
      print("///////////////////\n")
      # date = news_list.find_all("span", class_='date')
    # # link = news_list['href']
    # # img = news_list['img']
    
    # # news_data = {
    # #   date : date,
    # #   link : link,
    # #   img : img
    # # }
    # print(news_list, "\n//////////////////\n")