import pytest

from calculator import Calculator


@pytest.fixture()
def calc() -> Calculator:
    return Calculator()


def test_add(calc: Calculator):
    assert calc.add(1, 1) == 1 + 1
