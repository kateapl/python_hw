import homework4.task1 as hw1
import pytest


@pytest.mark.parametrize(
    ["file", "expected_result"],
    [
        ("homework4/test/double_lines.txt", True),
        ("homework4/test/one_line.txt", True),
        ("homework4/test/sev_lines.txt", False),
    ],
)
def test_read_magic_number(file: str, expected_result: bool):

    actual_result = hw1.read_magic_number(file)

    assert actual_result == expected_result


def test_empty_file():
    try:
        hw1.read_magic_number("homework4/test/empty.txt")
    except ValueError:
        actual_result = ValueError

    assert actual_result == ValueError


def test_text_file():
    try:
        hw1.read_magic_number("homework4/test/nan.txt")
    except ValueError:
        actual_result = ValueError

    assert actual_result == ValueError


def test_not_existing_file():
    try:
        hw1.read_magic_number("homework4/test/wrong.txt")
    except ValueError:
        actual_result = ValueError

    assert actual_result == ValueError
