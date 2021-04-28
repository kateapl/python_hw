import os

import pytest
from homework8.hw1 import KeyValueStorage


def test_getitem():
    storage = KeyValueStorage(os.path.dirname(__file__) + "\\task1.txt")
    assert storage["name"] == "kek"


def test_getattr():
    storage = KeyValueStorage(os.path.dirname(__file__) + "\\task1.txt")
    assert storage.song == "shadilay"


def test_int():
    storage = KeyValueStorage(os.path.dirname(__file__) + "\\task1.txt")
    assert isinstance(storage.power, int)


def test_value_error():
    with pytest.raises(ValueError):
        storage = KeyValueStorage(os.path.dirname(__file__) + "\\error.txt")
