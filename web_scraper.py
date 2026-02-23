import requests, certifi
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com"
res = requests.get(url, verify=certifi.where())

soup = BeautifulSoup(res.text, "html.parser")

titles = [t.text for t in soup.find_all("span", class_="text")]

print("Scraped:", len(titles), "quotes")

with open("data.csv","w",newline="",encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Quote"])
    for t in titles:
        writer.writerow([t])
