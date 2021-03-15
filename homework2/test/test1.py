from typing import Dict, List

import homework2.hw1 as hw1
import pytest


@pytest.mark.parametrize(
    ["file", "expected_result"],
    [
        (
            "homework2/test/1.txt",
            [
                "Betrachtung",
                "vorgebahnte",
                "ausführen",
                "bedenkli",
                "verbirgt",
                "vielmehr",
                "Waldgang",
                "Ausflug",
                "sondern",
                "gefaßt",
            ],
        ),
        ("homework2/test/empty.txt", []),
    ],
)
def test_get_longest_diverse_words(file: str, expected_result: List[str]):

    actual_result = hw1.get_longest_diverse_words(file)

    assert actual_result == expected_result


def test_get_rarest_char():

    actual_result = hw1.get_rarest_char("homework2/test/1.txt")

    assert actual_result == "W"


def test_count_punctuation_chars():

    actual_result = hw1.count_punctuation_chars("homework2/test/1.txt")

    assert actual_result == 8


def test_count_non_ascii_chars():

    actual_result = hw1.count_non_ascii_chars("homework2/test/1.txt")

    assert actual_result == 6


def test_get_most_common_non_ascii_char():

    actual_result = hw1.get_most_common_non_ascii_char("homework2/test/1.txt")

    assert actual_result == "ü"
