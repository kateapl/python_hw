"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:

    if(len(data) == 0):
        return False
    if (len(data) == 1):
        if data[0] == 1:
            return True
    if (len(data) == 2):
        if data == [1, 1]:
            return True

    fib = [1, 1]
    prew = cur = 1

    for i in range(len(data) - 2):
        tmp = prew + cur
        fib.append(tmp)
        prew = cur
        cur = tmp
        print(tmp)

    if fib == data:
        return True
    return False
