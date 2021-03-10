from typing import List, Tuple

import homework2.hw2 as hw2
import pytest


@pytest.mark.parametrize(
    ["inp", "expected_result"],
    [
        ([3, 2, 3], (3, 2)),
        ([2, 2, 1, 1, 1, 2, 2], (2, 1)),
    ],
)
def test_major_and_minor_elem(inp: List, expected_result: Tuple[int, int]):

    actual_result = hw2.major_and_minor_elem(inp)

    assert actual_result == expected_result
