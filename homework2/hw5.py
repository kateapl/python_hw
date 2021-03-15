"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
from typing import Any, List


def custom_range(iterable, start, stop=None, step: int = 1) -> List[Any]:
    if stop is None:
        start, stop = iterable[0], iterable[iterable.index(start)]
    result = []
    for i in range(iterable.index(start), iterable.index(stop), step):
        result.append(iterable[i])
    return result
