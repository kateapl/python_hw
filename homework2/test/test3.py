from typing import Any, List

import homework2.hw3 as hw3
import pytest


@pytest.mark.parametrize(
    ["args", "expected_result"],
    [
        ([[1, 2], [3, 4]], [[1, 3], [1, 4], [2, 3], [2, 4]]),
        ([[50], [23]], [[50, 23]]),
    ],
)
def test_combinations(args: List[Any], expected_result: List[List]):

    actual_result = hw3.combinations(*args)

    assert actual_result == expected_result
