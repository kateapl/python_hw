"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any

# Example tree:
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

count = 0


def find_occurrences(tree: dict, element: Any) -> int:
    global count
    if isinstance(tree, dict):
        for k, v in tree.items():
            if k == element:
                count += 1
            find_occurrences(v, element)
    elif hasattr(tree, "__iter__") and not isinstance(tree, str):
        for item in tree:
            find_occurrences(item, element)
    elif tree == element:
        count += 1
    return count


if __name__ == "__main__":
    print(find_occurrences(example_tree, "RED"))  # 6
