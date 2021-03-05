from typing import Dict, List

import pytest

from homework1.task04 import check_sum_of_four


@pytest.mark.parametrize(
    ["a", "b", "c", "d", "expected_result"],
    [
        ([1, 2], [3, 4], [5, 6], [7, 8], 0),
        ([1, 2, 21], [3, 4, -2], [-2, 6, 4], [-2, 8, -4], 3),
    ],
)
def test_min_max(
    a: List[int], b: List[int], c: List[int], d: List[int], expected_result: int
):

    actual_result = check_sum_of_four(a, b, c, d)

    assert actual_result == expected_result
