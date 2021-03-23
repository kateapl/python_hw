import pytest
from homework5.task2 import custom_sum


def test_decorator_doc_parameter():
    assert (
        custom_sum.__doc__
        == """This function can sum any objects which have __add___"""
    )


def test_decorator_name_parameter():
    assert custom_sum.__name__ == "custom_sum"


def test_decorator_orig_parameter():
    res = custom_sum.__original_func
    assert res(1, 2, 3, 4) == 10
