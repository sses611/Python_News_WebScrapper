from requests import get
from bs4 import BeautifulSoup

Naver_url = "https://land.naver.com/news/field.naver"
Daum_url = ""
 
response = get(Naver_url) 

if response.status_code != 200:
  print("Can't request website")
else:
  soup = BeautifulSoup(response.text, "html.parser")
  news = soup.find("div", class_="section_headline")
  news_post = news.find_all("li", reclusive=False)


  def info_search():
    article_info = article.find("dd")
    text = article_info.text
    press = article_info.find("span", class_="writing").text
    date = article_info.find("span", class_="date").text
    print(text, "\n", press, "\n", date)
  
   

  for article in news_post: 
    # photos =  article.select("img")
    # photo_alt = photos['src']
    # print(photo_alt)
    info_search() 
    # else:
    #   photo = "No thumnail"
    #   print(photo)
    #   info_search()


  # for photo in photos:
  #   photo_link = photo.find_all('a')
  #     # company, kind, region = anchor.find_all('span', class_="company")
  #     # title = anchor.find('span', class_= 'title')
  #   print(photo_link)
  #   print("//////////////////","\n")
  # #    texts = title[1]

  #     subTitle = acricle.find_all('dd')
  #     press = subTitle[0]
  #     date  = subTitle[1]      
  #     print(photos, "\n")
  #     print("///////////////////\n")
  #     # date = news_list.find_all("span", class_='date')
    # # link = news_list['href']
    # # img = news_list['img']
    
    # # news_data = {
    # #   date : date,
    # #   link : link,
    # #   img : img
    # # }
    # print(news_list, "\n//////////////////\n")



from requests import get
from bs4 import BeautifulSoup, requests

Naver_url = "https://land.naver.com/news/field.naver"
Daum_url = ""
 
response = get(Naver_url) 

if response.status_code != 200:
  print("Can't request website")
else:
  soup = BeautifulSoup(response.text, "html.parser")
  news = soup.find("div", class_="section_headline")
  news_post = news.find_all("li", reclusive=False)


  def info_search():
    article_info = article.find("dd")
    text = article_info.text
    press = article_info.find("span", class_="writing").text
    date = article_info.find("span", class_="date").text
    print(text, "\n", press, "\n", date)
  
   

  for article in news_post: 
    # photos =  article.select("img")
    # photo_alt = photos['src']
    # print(photo_alt)
    info_search() 
    # else:
    #   photo = "No thumnail"
    #   print(photo)
    #   info_search()





  # for photo in photos:
  #   photo_link = photo.find_all('a')
  #     # company, kind, region = anchor.find_all('span', class_="company")
  #     # title = anchor.find('span', class_= 'title')
  #   print(photo_link)
  #   print("//////////////////","\n")
  # #    texts = title[1]

  #     subTitle = acricle.find_all('dd')
  #     press = subTitle[0]
  #     date  = subTitle[1]      
  #     print(photos, "\n")
  #     print("///////////////////\n")
  #     # date = news_list.find_all("span", class_='date')
    # # link = news_list['href']
    # # img = news_list['img']
    
    # # news_data = {
    # #   date : date,
    # #   link : link,
    # #   img : img
    # # }
    # print(news_list, "\n//////////////////\n")