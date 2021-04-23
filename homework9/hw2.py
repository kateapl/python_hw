"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

>>> with supressor(IndexError):
...    [][2]

"""


from contextlib import contextmanager


class Supressor:
    def __init__(self, exception) -> None:
        self.exception = exception

    def __enter__(self) -> None:
        pass

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        return isinstance(exc_value, self.exception)


@contextmanager
def supressor_gen(exception):
    try:
        yield
    except exception:
        pass
