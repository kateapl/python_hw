from typing import List, Tuple

import homework3.task04 as hw4
import pytest


@pytest.mark.parametrize(
    ["number", "expected_result"],
    [
        (153, True),
        (10, False),
    ],
)
def test_is_armstrong(number: int, expected_result: bool):

    actual_result = hw4.is_armstrong(number)

    assert actual_result == expected_result
