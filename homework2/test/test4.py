from typing import Any, List

import homework2.hw4 as hw4
import pytest


def func(a, b):
    return (a ** b) ** 2


def test_cache():
    cache_func = hw4.cache(func)

    some = 100, 200

    val_1 = cache_func(*some)
    val_2 = cache_func(*some)

    assert val_1 == val_2
