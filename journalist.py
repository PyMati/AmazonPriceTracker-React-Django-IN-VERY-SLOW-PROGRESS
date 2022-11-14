"""Price scrapping script."""
from bs4 import BeautifulSoup
import requests


def get_price(url) -> str:
    """Function that scraps price from amazon shop."""
    assert url != str, "You must provide string URL"
    html = requests.get(url, timeout=20).text
    soup = BeautifulSoup(html, "html.parser")
    price = soup.find("span", class_ = "a-price-whole")
    print(price)
    # return price.getText()

get_price("https://www.amazon.pl/dp/B09V4GB53L")