import homework11.hw2 as hw2
import pytest


def test_morning():
    order_1 = hw2.Order(100, hw2.morning_discount)
    assert order_1.final_price() == 50


def test_old():
    order_2 = hw2.Order(100, hw2.elder_discount)
    assert order_2.final_price() == 10


def test_none():
    order_2 = hw2.Order(100)
    assert order_2.final_price() == 100
