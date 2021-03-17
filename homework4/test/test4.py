import homework4.task4 as hw4
import pytest


def test_fizzbuzz():
    actual_result = hw4.fizzbuzz(5)
    assert actual_result == ["1", "2", "fizz", "4", "buzz"]
