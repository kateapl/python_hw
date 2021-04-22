import homework10.task as hw
import pytest
from bs4 import BeautifulSoup


def test_growth():
    with open("homework10\\test\\file.txt", "r") as file:
        text = file.read()
    soup = BeautifulSoup(text, "html.parser")
    table = soup.find("tr")
    growth = hw.get_growth(table)
    assert growth == ["35.46%"]


def test_price():
    with open("homework10\\test\\file.txt", "r") as file:
        text = file.read()
    soup = BeautifulSoup(text, "html.parser")
    latest_prices = hw.get_latest_price(soup, 1)
    assert latest_prices == [198.89]
