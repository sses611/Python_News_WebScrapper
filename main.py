from requests import get
from bs4 import BeautifulSoup

# def get_page_count():
#   URL = "https://news.mt.co.kr/newsList.html?pDepth1=estate&pDepth2=Etotal"
#   response = get(URL)

#   if response.status_code != 200:
#     print("Can't request website")
#   else:
#     soup = BeautifulSoup(response.text, "html.parser")
#     pagination = soup.find("div", id="paging_t17")
#     pages = pagination.select("span a", reclusive=False)

#     if pages == None:
#         return 1

#     count = len(pages)

#     if count >= 10:
#       return 10
#     else:
#       return count


def search_news():
    # pages = get_page_count()
    URL = "https://news.mt.co.kr/newsList.html?pDepth1=estate&pDepth2=Etotal"
    response = get(URL)


    if response.status_code != 200:
        print("Can't request website")
    else:
      results = []
      soup = BeautifulSoup(response.text, "html.parser")
      news = soup.find_all("ul", ["class", "conlist_p1 mgt30"])

      for new in news:
        contents = new.find_all('li', reclusive=False)
        for content in contents:
          link = content.find('a')['href']
          title = content.find('img')['alt']
          image = content.find('img')['src']

          info = content.find('span', class_='etc').text
          press = info[0:6]
          date = info[9:25]
        
          news_data = {
            'linlk' : link,
            'title' : title,
            'image' : image,
            'press' : press,
            'date' : date 
          }
          results.append(news_data)
      
        for result in results:
          print(result)
          print("////////////////\n")

search_news()