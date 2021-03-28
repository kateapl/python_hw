"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from collections import Counter
from typing import List, Optional


def check_rows(board: List[List]) -> Optional[str]:
    for row in board:
        if all(a == "x" for a in row):
            return "x"
        elif all(a == "o" for a in row):
            return "o"


def check_columns(board: List[List]) -> Optional[str]:
    for col in zip(*board):
        if all(a == "x" for a in col):
            return "x"
        elif all(a == "o" for a in col):
            return "o"


def check_diagonals(board: List[List]) -> Optional[str]:
    count_x, count_anti_x = 0, 0
    count_o, count_anti_o = 0, 0

    for i in range(3):
        count_x += int(board[i][i] == "x")
        count_o += int(board[i][i] == "o")
        count_anti_x += int(board[i][3 - i - 1] == "x")
        count_anti_o += int(board[i][3 - i - 1] == "o")

    if count_x == 3 or count_anti_x == 3:
        return "x"

    if count_o == 3 or count_anti_o == 3:
        return "o"


def tic_tac_toe_checker(board: List[List]) -> str:
    possibilities = [check_rows(board), check_columns(board), check_diagonals(board)]
    count = Counter(possibilities)
    print(count["x"])
    print(count["o"])
    b = 0
    for row in board:
        b += row.count("-")
    if not count["x"] and not count["o"] and b:
        return "unfinished!"
    elif count["x"] > count["o"]:
        return "x wins!"
    elif count["x"] < count["o"]:
        return "o wins!"
    else:
        return "draw!"
