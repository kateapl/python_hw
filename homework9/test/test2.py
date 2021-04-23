import os

import pytest
from homework9.hw2 import Supressor, supressor_gen


def test_index_error():
    try:
        with Supressor(IndexError):
            raise IndexError
    except IndexError:
        res = 1
    else:
        res = 0
    assert res == 0


def test_list_index():
    somelist = [2, 3]
    try:
        with Supressor(IndexError):
            somelist[2]
    except IndexError:
        res = 1
    else:
        res = 0
    assert res == 0


def test_list():
    somelist = [2, 3]
    try:
        with Supressor(IndexError):
            somelist[1]
    except IndexError:
        res = 1
    else:
        res = 0
    assert res == 0


def test_index_error_gen():
    try:
        with supressor_gen(IndexError):
            raise IndexError
    except IndexError:
        res = 1
    else:
        res = 0
    assert res == 0


def test_list_index_gen():
    somelist = [2, 3]
    try:
        with supressor_gen(IndexError):
            somelist[2]
    except IndexError:
        res = 1
    else:
        res = 0
    assert res == 0


def test_list_gen():
    somelist = [2, 3]
    try:
        with supressor_gen(IndexError):
            somelist[1]
    except IndexError:
        res = 1
    else:
        res = 0
    assert res == 0
