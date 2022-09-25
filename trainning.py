"""
from requests import get

websites =  (
  "google.com",
  "https://airbnb.com",
  "twitter.com",
  "facebook.com"
)

results =  {
  
}

for website in websites:
  if not website.startswith("https://"):
    # print(website, "have to fix")
    website = f"https://{website}"
  response = get(website)
  if response.status_code == 200:
    results[website] = "OK"
  else:
    results[website] = "NOT OK"

print(results)
"""

list_of_numbers= [1, 2, 3]
first, second, thrid = list_of_numbers

print(first, second, thrid)