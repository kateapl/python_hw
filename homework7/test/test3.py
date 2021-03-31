from typing import List

import homework7.hw3 as hw3
import pytest


@pytest.mark.parametrize(
    ["board", "expected_result"],
    [
        ([["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]], "unfinished!"),
        ([["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]], "x wins!"),
        ([["x", "o", "x"], ["x", "o", "o"], ["o", "x", "x"]], "draw!"),
        ([["x", "o", "o"], ["x", "o", "o"], ["o", "x", "x"]], "o wins!"),
    ],
)
def test_tic_tac_toe_checker(board: List[List], expected_result: str):
    actual_result = hw3.tic_tac_toe_checker(board)

    assert actual_result == expected_result
