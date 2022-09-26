from requests import get
from bs4 import BeautifulSoup

# NEWS_URL = ["", ]
URL = "https://obank.kbstar.com/quics?page=C016613"

response = get(URL)

if response.status_code != 200:
  print("Can't request website")
else:
  soup = BeautifulSoup(response.text, "html.parser")
  products = soup.find_all("ul",["class", "list-product1"] )

  for product in products:
    contents = product.select('li', reclusive=False)
    for content in contents:
      content = contents[0]
      print(content)
      print("///////////////\n")