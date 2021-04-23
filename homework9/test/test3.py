import os
from pathlib import Path

import pytest
from homework9.hw3 import universal_file_counter


def test_merge_file_counter_without_tokenizer():
    p = Path("homework9\\test")
    res = universal_file_counter(p, "txt")
    assert res == 18


def test_merge_file_counter_with_tokenizer():
    p = Path("homework9\\test")
    res = universal_file_counter(p, "txt", str.split)
    assert res == 18
