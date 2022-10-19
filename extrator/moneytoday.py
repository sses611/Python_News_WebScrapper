from requests import get
from bs4 import BeautifulSoup

# def checking_url():


def search_mk_news(PS, URL):
    # pages = get_page_count()
    # for page in range(pages):U
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
                    'center': PS,
                    'link': link.replace(",", " "),
                    'title': title.replace(",", " "),
                    'image': image.replace(",", " "),
                    'press': press,
                    'regidate': date
                }
                results.append(news_data)
    return results
