import homework7.hw2 as hw2
import pytest


def test_one_backspace():
    assert hw2.backspace_compare("ab#c", "ad#c") is True


def test_two_backspace():
    assert hw2.backspace_compare("a##c", "#a#c") is True


def test_false():
    assert hw2.backspace_compare("a#c", "b") is False


def test_empty():
    assert hw2.backspace_compare("", "") is True


def test_equal():
    assert hw2.backspace_compare("dancing queen", "dancing queens#") is True
