##WEB SCRAPER FOR SECURITY NEWS
import json
import requests
from bs4 import BeautifulSoup

def getNewsData():
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
    }
    response = requests.get(
        "https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNREl5ZUY4U0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen", headers=headers
    )
    soup = BeautifulSoup(response.content, "html.parser")
    news_results = []

    for el in soup.select("c-wiz.XBspb"):
        news_results.append(
            {
                "link": "https://news.google.com"+ el.find("a")["href"][1:],
                "title": el.select_one("a.JtKRv").get_text(),
                "date": el.select_one("time.hvbAAd").get_text(),
            }
        )
    news_results_json = json.dumps(news_results, indent=2)
    f = open("data.json", "a+")
    f.writelines(news_results_json)
    f.close

getNewsData()

#build a backend and print all of the data