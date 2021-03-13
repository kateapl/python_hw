# In previous homework task 4, you wrote a cache function that remembers other function output value.
# Modify it to be a parametrized decorator, so that the following code::
#
#     @cache(times=3)
#     def some_function():
#         pass
#
#
# Would give out cached value up to `times` number only.
# Example::
#
#     @cache(times=2)
#     def f():
#         return input('? ')   # careful with input() in python2, use raw_input() instead
#
#     >>> f()
#     ? 1
#     '1'
#     >>> f()     # will remember previous value
#     '1'
#     >>> f()     # but use it up to two times only
#     '1'
#     >>> f()
#     ? 2
#     '2'


import pickle
from collections import Callable


def cache(times: int):
    def wrapper(func: Callable):
        cachedict = dict()
        times_called = 0

        def cachefunc(*args):
            hash = pickle.dumps(args)
            if hash not in cachedict:
                cachedict[hash] = func(*args)
            nonlocal times_called
            times_called += 1
            if times_called == times:
                del cachedict[hash]
                times_called = 0
            else:
                return cachedict[hash]

        return cachefunc

    return wrapper
