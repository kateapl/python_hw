import io
import sys

import homework4.task3 as hw3
import pytest


def test_my_precious_logger_out(capsys):
    hw3.my_precious_logger("hello")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
    assert captured.err == ""


def test_my_precious_logger_err(capsys):
    hw3.my_precious_logger("error: file not found")
    captured = capsys.readouterr()
    assert captured.err == "error: file not found\n"
    assert captured.out == ""
