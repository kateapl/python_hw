from typing import List

import pytest

from homework1.task05 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["nums", "k", "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([2, 4], 1, 4),
        ([-1, -3, -1, -3, 5, 3, -6, -7], 4, 8),
    ],
)
def test_subarray_sum(nums: List[int], k: int, expected_result: int):
    actual_result = find_maximal_subarray_sum(nums, k)

    assert actual_result == expected_result
