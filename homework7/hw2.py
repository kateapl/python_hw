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
        ""
        if first.index(char) == first.find("#", first.index(char))
        or first.index(char) == first.find("#", first.index(char)) - 1
        else char
        for char in first
    ]
    s2 = [
        ""
        if second.index(char) == second.find("#", second.index(char))
        or second.index(char) == second.find("#", second.index(char)) - 1
        else char
        for char in second
    ]
    s1 = "".join(map(str, s1))
    s2 = "".join(map(str, s2))
    print(s1)
    print(s2)
    return s1 == s2
