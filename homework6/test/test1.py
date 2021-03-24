import pytest
from homework6.counter import instances_counter


@instances_counter
class Empty:
    pass


def test_not_created_object():
    assert Empty.get_created_instances() == 0


def test_get_created_instances():
    user, _, _ = Empty(), Empty(), Empty()
    assert user.get_created_instances() == 3


def test_reset_instances_counter():
    Empty.reset_instances_counter()
    user, _, _ = Empty(), Empty(), Empty()
    assert user.reset_instances_counter() == 3
    assert user.get_created_instances() == 0
