import requests
from bs4 import BeautifulSoup

BBC_BASE_URL = "https://www.bbc.com"
ALL_BBC_BASE_URL = set(
    ["https://www.bbc.com", "http://www.bbc.com", "https://www.bbc.co.uk", "http://www.bbc.co.uk"]
    )
chapter_class_1 = ["news", "sport", "weather"]
chapter_class_2 = ["travel", "culture", "capital", "future"]
chapter_class_3 = ["food"]
chapter_class_4 = ["arts"]
chapter_class_5 = ["bitesize"]

def get_items(chapter="news", n_items=10):
    """
    This function takes in a name of chapter (like "news" or "sports")
    and number of items required from that chapter and returns a list
    of tuples having title and url
    """
    n_items = int(n_items)
    request_url = BBC_BASE_URL + "/" + chapter
    exception_message = None
    title_and_url = []

    try:
        with requests.Session() as s:
            data = s.get(request_url)
    except requests.exceptions.RequestException as e:
        exception_message = "An fatal exception happened while getting news : {}, try again".format(e)
    if exception_message is not None:
        return exception_message

    soup = BeautifulSoup(data.content, "html.parser")
    all_headings = []

    if chapter in chapter_class_1:
        all_headings = soup.find_all('a', class_="gs-c-promo-heading")
    elif chapter in chapter_class_2:
        all_headings = soup.find_all('div', class_ = "promo-unit-header")
    elif chapter in chapter_class_3:
        all_headings = soup.find_all('h3', class_ = "promo__title")
    elif chapter in chapter_class_4:
        all_headings = soup.find_all('div', class_ = "k-promo-title")
    elif chapter in chapter_class_5:
        all_headings = soup.find_all('h2', class_ = "promo-title")

    for heading in all_headings[:n_items]:
        try:
            if chapter in chapter_class_1:
                title_and_url.append((heading.h3.text, make_url(heading['href'])))
            elif chapter in chapter_class_2:
                title_and_url.append((heading.h3.text, make_url(heading.select('a')[1]['href'])))
            elif chapter in set(chapter_class_3 + chapter_class_4 + chapter_class_5):
                title_and_url.append((heading.text, make_url(heading.find_parent('a')['href'])))
        except Exception:
            continue
    
    return title_and_url

def make_url(url):
    """
    utility function to make full url from relative url
    """
    if "http" in url:
        return url
    return BBC_BASE_URL + url