from requests import get
from bs4 import BeautifulSoup

def search_news():
  URL = "https://news.mt.co.kr/newsList.html?pDepth1=estate&pDepth2=Etotal"
  response = get(URL)
  
  if response.status_code != 200:
    print("Can't request website")
  else:
    soup = BeautifulSoup(response.text, "html.parser")
    news = soup.find_all("ul", ["class", "conlist_p1 mgt30"])
  
    for new in news:
      contents = new.find_all("li")
      for content in contents:
        anchors = content.find('a')
        link = anchors['href']
        image = anchors.find('img')['src']
      
        info = content.find("div", class_="con")
        title = info.find("strong").text
        press = info.find('span').text
         
        print("link->", link, "\n",
              "image->", image, "\n",
              "title->", title, "\n",
              "press->", press)
        print("//////////////////\n")