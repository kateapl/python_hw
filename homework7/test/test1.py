import homework7.hw1 as hw1
import pytest

example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}

empty = {}


def test_empty():
    assert hw1.find_occurrences(empty, "something") == 0


def test_not_exist():
    assert hw1.find_occurrences(example_tree, "something") == 0


def test_find_occurrences():
    assert hw1.find_occurrences(example_tree, "RED") == 6
