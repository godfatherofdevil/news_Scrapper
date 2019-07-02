import requests
from bs4 import BeautifulSoup

BBC_BASE_URL = "https://www.bbc.com"

def get_items(chapter="news", n_items=10):
    """
    This function takes in a name of chapter (like "news" or "sports")
    and number of items required from that chapter and returns it
    """
    n_items = int(n_items)
    request_url = BBC_BASE_URL + "/" + chapter
    exception_message = None
    try:
        data = requests.get(request_url)
    except requests.exceptions.RequestException as e:
        exception_message = "An fatal exception happened while getting news : {}, try again".format(e)
    if exception_message is not None:
        return exception_message

    title_and_url = []

    soup = BeautifulSoup(data.content, "html.parser")

    all_headings = soup.find_all('a', class_="gs-c-promo-heading")

    for heading in all_headings[:n_items]:
        try:
            title_and_url.append((heading.h3.text, BBC_BASE_URL + heading['href']))
        except Exception:
            continue
    
    return title_and_url