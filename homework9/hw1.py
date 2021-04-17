"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from itertools import cycle, islice
from pathlib import Path
from typing import Iterator, List, Union


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    iter_list = []
    for file in file_list:
        with open(file, "r") as f:
            iter_list.append(f.readlines())
    length = len(iter_list[0])
    i = []
    j = 0
    count = 0
    for elem in islice(cycle(iter_list), length * len(file_list)):
        if len(file_list) == count:
            j += 1
            count = 0
        i.append(int(elem[j]))
        count += 1
    return iter(i)
