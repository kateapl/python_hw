from unittest.mock import Mock

from homework3.task1 import cache


@cache(times=2)
def f(inp):
    return inp


def test_cache():
    mock = Mock()
    mock.patch(
        # api_call is from slow.py but imported to main.py
        "homework3.task1.cache",
        return_value=5,
    )

    expected = 5
    actual = f(5)
    assert expected == actual


def test_cache_is_called():
    mock = Mock()
    mock.patch(
        # api_call is from slow.py but imported to main.py
        "homework3.task1.cache",
    )
    f(13)
    mock.patch.assert_called_once()
