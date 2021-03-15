from unittest import TestCase
from unittest.mock import Mock, patch

import homework4.task2 as hw2


class TestFunc(TestCase):
    @patch("homework4.task2.read_url", return_value="<html><line>")
    def test_count_dots_on_i(self, read_url):
        self.assertEqual(hw2.count_dots_on_i("http://www.w3schools.com"), 1)


def test_wrong():
    try:
        hw2.count_dots_on_i("homework4")
    except ValueError:
        actual_result = ValueError

    assert actual_result == ValueError


def test_empty():
    try:
        hw2.count_dots_on_i("")
    except ValueError:
        actual_result = ValueError

    assert actual_result == ValueError
