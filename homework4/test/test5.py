import homework4.task4 as hw4
import pytest


def test_fizzbuzz():

    actual_result = list(hw4.fizzbuzz(5))

    assert actual_result == ["1", "2", "fizz", "4", "buzz"]


def test_fizzbuzz15():

    actual_result = list(hw4.fizzbuzz(15))

    assert actual_result == [
        "1",
        "2",
        "fizz",
        "4",
        "buzz",
        "fizz",
        "7",
        "8",
        "fizz",
        "buzz",
        "11",
        "fizz",
        "13",
        "14",
        "fizzbuzz",
    ]
