"""Price scrapping script."""
from bs4 import BeautifulSoup
import requests


def get_price(url):
    """Function that scraps price from amazon shop."""
    assert url != str, "You must provide string URL"
    html = requests.get(url, timeout=20).text
    soup = BeautifulSoup(html, "html.parser")
    price = soup.find_all("span", class_ = "a-price-whole")
    value = price[0].getText()
    return value
