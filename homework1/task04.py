"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List
from itertools import product


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    com = list(product(a, b, c, d))
    result = 0
    for cell in com:
        if cell[0] + cell[1] + cell[2] + cell[3] == 0:
            result += 1
    return result
