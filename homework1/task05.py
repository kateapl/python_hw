"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    result = nums[0]

    while k >= 1:
        for i in range(len(nums) - k + 1):
            tem = 0
            for j in range(k):
                tem = tem + nums[i + j]
            if result < tem:
                result = tem
        k = k - 1
    return result
