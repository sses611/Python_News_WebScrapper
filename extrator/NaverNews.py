from requests import get
from bs4 import BeautifulSoup

# def checking_url():


def search_naver_news(PS, URL):
    # pages = get_page_count()
    # for page in range(pages):U
    response = get(URL)

    if response.status_code != 200:
        print("Can't request website")
    else:
        results = []
        soup = BeautifulSoup(response.text, "html.parser")
        news = soup.find_all("ul", ["class", "headline_list"])
        # print(news)

        for new in news:
            contents = new.find_all('li', reclusive=False)
            for content in contents:
              # image = content.find('dt', class_='photo').find('img')['src']
              image = content.select_one('dt img')['src']
              link = content.find('a')['href']
              title = content.select("dt")[1].find('a').get_text();
              press = content.find('span', class_='writing').get_text();
              date = content.find('span', class_='date').get_text();
              # print(image)
              # print(link)
              # print(title)
              # print(press)
              # print(date)
              # print("///////////////")

              # info = content.find('span', class_='etc').text
              # press = info[0:6]
              # date = info[9:25]

              news_data = {
                    'center': PS,
                    'link': "https:/"+link.replace(",", " "),
                    'title': title.replace(",", " "),
                    'image': image.replace(",", " "),
                    'press': press,
                    'regidate': date
              }
              results.append(news_data)
    return results
