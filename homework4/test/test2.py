from unittest import TestCase
from unittest.mock import Mock, patch

import homework4.task2 as hw2
import pytest


class TestFunc(TestCase):
    @patch("homework4.task2.read_url", return_value="<html><line>")
    def test_count_dots_on_i(self, read_url):
        self.assertEqual(hw2.count_dots_on_i("http://www.w3schools.com"), 1)


def test_wrong():
    with pytest.raises(ValueError):
        hw2.count_dots_on_i("homework4")


def test_empty():
    with pytest.raises(ValueError):
        hw2.count_dots_on_i("")
