"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.

from enum import Enum


class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"


class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"


Should become:

class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""

class SimplifiedEnum(type):
    def __new__(cls, name, bases, dct):
        print(dct)
        for key in dct.keys():
            if key.endswith("__keys"):
                newkey = "__keys"
                dct[newkey] = set(dct[key])
                del dct[key]
                cls_instance = super().__new__(cls, name, bases, dct)
                return cls_instance
        raise ValueError("need __keys attr")

    # to access attributes and methods through . notation
    def __getattr__(self, attrname):
        if attrname in self.__dict__['__keys']:
            return attrname


    # for access collection _items_ through ['key'] notation
    def __getitem__(self, key: str):
        if key in self.__dict__['__keys']:
            return key