"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.

That how first steps for the instruction may look like:
 - Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository "python_hw"
 - Checkout branch hw4
 - Open terminal
 - Enter 'python3 -m pytest -v --doctest-modules homework4\task4.py'
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']

    >>> fizzbuzz(15)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']
    """
    fb = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            fb.append("fizzbuzz")
        elif i % 3 == 0:
            fb.append("fizz")
        elif i % 5 == 0:
            fb.append("buzz")
        else:
            fb.append(f"{i}")
    return fb


if __name__ == "__main__":
    import doctest

    doctest.testmod()

