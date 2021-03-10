import string
from typing import Any, List

import homework2.hw5 as hw5
import pytest


def test_custom_range():

    assert hw5.custom_range(string.ascii_lowercase, "g") == [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
    ]
    assert hw5.custom_range(string.ascii_lowercase, "g", "p") == [
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
    ]
    assert hw5.custom_range(string.ascii_lowercase, "p", "g", -2) == [
        "p",
        "n",
        "l",
        "j",
        "h",
    ]
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    assert hw5.custom_range(string.ascii_lowercase, "p", "g", -2) == [
        "p",
        "n",
        "l",
        "j",
        "h",
    ]
    assert hw5.custom_range(arr, 2, 9, 3) == [2, 5, 8]
