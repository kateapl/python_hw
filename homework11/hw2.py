"""
You are given the following code:

class Order:
    morning_discount = 0.25

    def __init__(self, price):
        self.price = price

    def final_price(self):
        return self.price - self.price * self.morning_discount

Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy

Example of the result call:

def morning_discount(order):
    ...

def elder_discount(order):
    ...

order_1 = Order(100, morning_discount)
assert order_1.final_price() == 50

order_2 = Order(100, elder_discount)
assert order_1.final_price() == 10
"""
from typing import Union


class Order:
    def __init__(self, price, discount=None) -> None:
        self.price = price
        self._discount = discount

    @property
    def discount(self) -> Union[int, float]:
        if self._discount:
            return self._discount()
        return 0

    def final_price(self) -> Union[int, float]:
        return self.price - self.price * self.discount


def morning_discount() -> Union[int, float]:
    return 0.5


def elder_discount() -> Union[int, float]:
    return 0.9
