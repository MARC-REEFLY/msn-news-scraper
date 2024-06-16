import time
import requests
import bs4
import json


def get_msn_news_data_from_url(url):
    start = time.time()
    url_parts = url.split("-")
    # Get the last part of the URL
    article_id = url_parts[-1]
    # Remove the "ar-" prefix if it exists
    url = f"https://assets.msn.com/content/view/v2/Detail/en-us/{article_id}"
    response = requests.request("GET", url, headers={}, data={})
    response_json = json.loads(response.text)
    body_html = response_json["body"]
    soup = bs4.BeautifulSoup(body_html, "html.parser")
    # Extract the human-readable text without HTML tags
    human_readable_text = soup.get_text()
    end = time.time()
    print(f"MSN News data time spent on 1 msn article: {end - start}")
    return human_readable_text
