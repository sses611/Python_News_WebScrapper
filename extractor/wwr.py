from requests import get
from bs4 import BeautifulSoup

#추가작업 진행예정

# def extract_wwr_jobs(keyword):
#   base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
  
#   response = get(f"{base_url}{keyword}")
#   if response.status_code != 200:
#     print("Can't request website")
#   else:
#     soup = BeautifulSoup(response.text, "html.parser")
#     jobs = 4soup.find_all('section', class_="jobs") #class_로 해야 찾을 수 있다.
#     results = []
#   `
#       for post in job_post:
#         anchors = post.find_all('a')
#         anchor = anchors[1]
#         link = anchor['href']
#         company, kind, region = anchor.find_all('span', class_="company")
#         title = anchor.find('span', class_= 'title')
      
#         job_data = {
#           "company" : company.string,
#           "kind" : kind.string,
#           "region" : region.string,
#           "position" : title.string,
#           "link" : f"https://weworkremotely.com/{link}"
#         }
#         results.append(job_data)
#   return results
