import requests
from bs4 import BeautifulSoup

YOUTUBE_TRENDING_URL ="https://www.youtube.com/feed/trending"

#does not execute javascript

response = requests.get(YOUTUBE_TRENDING_URL)


print("status code",response.status_code)

with open("trending.html", "w") as f:
  f.write(response.text)

doc = BeautifulSoup(response.text,"html.parser")

print("page title :",doc.title.text)


#find all the videos div
videos_div = doc.find_all('div',class_= 'ytd-video-renderer')