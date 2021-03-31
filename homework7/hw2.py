"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""


def backspace_compare(first: str, second: str):
    s1 = [
        "" if char == "#" or i == first.find("#", i) - 1 else char
        for i, char in enumerate(first)
    ]
    s2 = [
        "" if char == "#" or i == second.find("#", i) - 1 else char
        for i, char in enumerate(second)
    ]
    s1 = "".join(s1)
    s2 = "".join(s2)
    return s1 == s2
