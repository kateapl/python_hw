"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import Dict, List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    length = len(a)
    result = 0
    sumab: Dict[int, int] = {}

    for i in range(length):
        for j in range(length):
            tem = a[i] + b[j]
            if tem in sumab:
                sumab[tem] += 1
                print(sumab)
            else:
                sumab[tem] = 1

    for i in range(length):
        for j in range(length):
            tem = c[i] + d[j]
            if -tem in sumab:
                result += sumab[-tem]
    return result
