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


class KeyValueStorage:
    def __init__(self, path: str):
        with open(path, "r") as fi:
            nums = fi.read().splitlines()
            self.storage = {num.split("=")[0]: num.split("=")[1] for num in nums}
            for key in self.storage.keys():
                try:
                    int(key)
                except ValueError:
                    pass
                else:
                    raise ValueError

    # to access attributes and methods through . notation
    def __getattr__(self, attrname) -> Union[int, str]:
        if attrname in self.storage and attrname not in self.__dict__:
            try:
                int(self.storage[attrname])
            except ValueError:
                return self.storage[attrname]
            else:
                return int(self.storage[attrname])

    # for access collection _items_ through ['key'] notation
    def __getitem__(self, key) -> Union[int, str]:
        if key in self.storage and key not in self.__dict__:
            try:
                int(self.storage[key])
            except ValueError:
                return self.storage[key]
            else:
                return int(self.storage[key])
