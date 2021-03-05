from typing import Tuple

import pytest

from homework1.task03 import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("homework1/test/03.txt", (1, 67)),
        ("homework1/test/t03.txt", (-5, -1)),
    ],
)
def test_min_max(value: str, expected_result: Tuple[int, int]):

    actual_result = find_maximum_and_minimum(value)

    assert actual_result == expected_result
