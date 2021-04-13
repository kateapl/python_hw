import os

import pytest
from homework9.hw1 import merge_sorted_files


def test_merge_sorted_files():
    args = [
        os.path.dirname(__file__) + "\\file1.txt",
        os.path.dirname(__file__) + "\\file2.txt",
    ]
    assert list(merge_sorted_files(args)) == [1, 2, 3, 4, 5, 6]


def test_empty():
    args = [os.path.dirname(__file__) + "\\empty.txt"]
    assert list(merge_sorted_files(args)) == []


def test_one():
    args = [os.path.dirname(__file__) + "\\one.txt"]
    assert list(merge_sorted_files(args)) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
