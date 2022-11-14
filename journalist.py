"""Price scrapping script."""
from bs4 import BeautifulSoup
import requests

def get_price(url) -> float:
    """Function that scraps price from amazon shop."""
    assert url != str, "You must provide string URL"
    html = requests.get(url, timeout=20).text
    soup = BeautifulSoup(html, "html.parser")
    price = soup.find("span", class_ = "a-price-whole")
    return price.getText()
