import requests
from bs4 import BeautifulSoup
import csv
import re

url = "https://ja.wikipedia.org/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

today = soup.find("div", attrs={"id": "on_this_day"})

entries = today.find_all("li")
today_list = []

for i, entry in enumerate(entries, 1):
  today_text = entry.get_text().replace("（", "(").replace("）", ")")
  match = re.search("\((.*?)年\)", today_text)
  if match:
    today_list.append([i, entry.get_text(), match.group(1)])
  else:
    today_list.append([i, entry.get_text()])

with open("output.csv", "w", encoding="Shift_JIS") as file:
  writer = csv.writer(file, lineterminator="\n")
  writer.writerows(today_list)