import homework7.hw2 as hw2
import pytest


def test_one_backspace():
    assert hw2.backspace_compare("ab#c", "ad#c")


def test_two_backspace():
    assert hw2.backspace_compare("a##c", "#a#c")


def test_false():
    assert not hw2.backspace_compare("a#c", "b")


def test_empty():
    assert hw2.backspace_compare("", "")


def test_equal():
    assert hw2.backspace_compare("dancing queen", "dancing queens#")
