import pytest
from homework8.hw2 import TableData


def test_len():
    presidents = TableData(
        database_name="homework8\example.sqlite", table_name="presidents"
    )
    assert len(presidents) == 3


def test_getitem():
    presidents = TableData(
        database_name="homework8\example.sqlite", table_name="presidents"
    )
    assert presidents["Yeltsin"] == ["Yeltsin", 999, "Russia"]


def test_exist():
    presidents = TableData(
        database_name="homework8\example.sqlite", table_name="presidents"
    )
    assert "Yeltsin" in presidents


def test_loop():
    presidents = TableData(
        database_name="homework8\example.sqlite", table_name="presidents"
    )
    preslist = []
    for president in presidents:
        preslist.append(president)
    print(preslist)
    assert preslist == [
        ("Yeltsin", 999, "Russia"),
        ("Trump", 1337, "US"),
        ("Big Man Tyrone", 101, "Kekistan"),
    ]


def test_change():
    presidents = TableData(
        database_name="homework8\example.sqlite", table_name="presidents"
    )
    presidents.cursor.execute("INSERT INTO presidents VALUES('Stalin', 345, 'USSR')")
    presidents.connection.commit()
    assert len(presidents) == 4
    presidents.cursor.execute("DELETE from presidents where name = 'Stalin'")
    presidents.connection.commit()
