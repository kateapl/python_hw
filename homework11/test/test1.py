import pytest
from homework11.hw1 import SimplifiedEnum


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")

def test_colors():
    assert ColorsEnum.RED == "RED"


def test_size():
    assert SizesEnum.XL == "XL"

def test_wrong():
    with pytest.raises(ValueError):
        class SomeEnum(metaclass=SimplifiedEnum):
            __some = ("XL", "L", "M", "S", "XS")