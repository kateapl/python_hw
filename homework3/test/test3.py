from typing import List, Tuple

import homework3.task03 as hw3
import pytest

sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]


def test_make_filter():

    actual_result = hw3.make_filter(name="polly", type="bird").apply(sample_data)
    expected_result = [
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"}
    ]

    assert actual_result == expected_result


def test_nothing():

    actual_result = hw3.make_filter(type="lizard").apply(sample_data)
    expected_result = []

    assert actual_result == expected_result


def test_even():

    positive_even = hw3.Filter(
        [lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)]
    )
    actual_result = positive_even.apply(
        range(10)
    )  # should return only even numbers from 0 to 99
    expected_result = [2, 4, 6, 8]
    assert actual_result == expected_result
