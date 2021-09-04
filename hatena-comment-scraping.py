import requests
from bs4 import BeautifulSoup

url = "https://b.hatena.ne.jp"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

top_entry = soup.find("section", attrs={"class":"entrylist-unit"})

entries = top_entry.find_all("div", attrs={"class":"entrylist-contents"})

for entry in entries:
  title_tag = entry.find("h3", attrs={"class":"entrylist-contents-title"})
  title = title_tag.find("a").get("title")
  print(title)

  bookmark_tag = entry.find("span", attrs={"class":"entrylist-contents-users"})

  bookmark_link = bookmark_tag.find("a").get("href")

  bookmark_url = url + bookmark_link

  response = requests.get(bookmark_url)

  soup = BeautifulSoup(response.content,"html.parser")
  
  comments = soup.find_all("span",attrs={"class":"entry-comment-text"})
  for comment in comments:
    print(comment.get_text())