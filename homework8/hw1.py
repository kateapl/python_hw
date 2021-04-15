# We have a file that works as key-value storage,
# each like is represented as key and value separated by = symbol, example:
#
# name=kek
# last_name=top
# song_name=shadilay
# power=9001
#
# Values can be strings or integer numbers.
# If a value can be treated both as a number and a string, it is treated as number.
#
# Write a wrapper class for this key value storage that works like this:
#
# storage = KeyValueStorage('path_to_file.txt')
# that has its keys and values accessible as collection items and as attributes.
# Example:
# storage['name']  # will be string 'kek'
# storage.song_name  # will be 'shadilay'
# storage.power  # will be integer 9001
#
# In case of attribute clash existing built-in attributes take precedence.
# In case when value cannot be assigned to
# an attribute (for example when there's a line `1=something`) ValueError should be raised.
# File size is expected to be small, you are permitted to read it entirely into memory.
from typing import Union


class KeyValueStorage:
    storage = {}

    def __init__(self, path: str):
        with open(path, "r") as fi:
            for line in fi:
                kv = line.split("=")
                print(kv)
                try:
                    int(kv[0])
                except ValueError:
                    try:
                        self.storage[kv[0]] = int(kv[1])
                    except ValueError:
                        self.storage[kv[0]] = kv[1].strip("\n")
                else:
                    raise ValueError()

    # to access attributes and methods through . notation
    def __getattr__(self, attrname) -> Union[int, str]:
        value = self.storage.get(attrname, None)
        if value is not None:
            return value

    # for access collection _items_ through ['key'] notation
    def __getitem__(self, key: str) -> Union[int, str]:
        value = self.storage.get(key, None)
        if value is not None:
            return value
