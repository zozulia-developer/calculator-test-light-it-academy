import pytest

from calculator import Calculator


def test_add(calculator: Calculator):
    assert calculator.add(1 + 1) == 1 + 1
