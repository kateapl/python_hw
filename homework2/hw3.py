"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from itertools import chain, product
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    arglist = list(chain(args))
    print(arglist)
    result = []
    for l in arglist:
        if arglist.index(l) != len(arglist) - 1:
            result.append(list(product(l, *arglist[arglist.index(l) + 1 :])))
    print(list(chain(*result)))
    res = list(chain(*result))
    list_of_lists = [list(elem) for elem in res]

    return list_of_lists
