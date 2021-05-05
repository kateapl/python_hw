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
    def __new__(cls, name, bases, dct) -> "SimplifiedEnum":
        dct["__keys"] = set(dct[f"_{name}__keys"])
        del dct[f"_{name}__keys"]
        cls_instance = super().__new__(cls, name, bases, dct)
        return cls_instance

    # to access attributes and methods through . notation
    def __getattr__(self, attrname) -> str:
        if attrname in self.__dict__["__keys"]:
            return attrname

    # for access collection _items_ through ['key'] notation
    def __getitem__(self, key: str) -> str:
        if key in self.__dict__["__keys"]:
            return key
