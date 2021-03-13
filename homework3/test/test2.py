import homework3.task2 as hw2
import pytest


def test_slow_calculate():

    actual_result = hw2.main()
    print(hw2.main())

    assert actual_result < 60
