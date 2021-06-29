import pytest

from calculator import Calculator


@pytest.fixture()
def calc() -> Calculator:
    return Calculator()


@pytest.mark.parametrize(
    'first_value, second_value, result',
    [
        (1, 1, 2),
        (-1, 3, 2),
        (3, -1, 2),
        (0, 0, 0),
    ]
)
def test_add(
        calc: Calculator,
        first_value: int,
        second_value: int,
        result: int):
    assert calc.add(first_value, second_value) == result


@pytest.mark.parametrize(
    'first_value, second_value, result',
    [
        (1, 1, 0),
        (-1, 3, -4),
        (3, -1, 4),
        (0, 0, 0)
    ]
)
def test_subtract(
        calc: Calculator,
        first_value: int,
        second_value: int,
        result: int):
    assert calc.subtract(first_value, second_value) == result


@pytest.mark.parametrize(
    'first_value, second_value, result',
    [
        (2, 2, 1),
        (10, 2, 5),
        (6, -3, -2),
        (-3, 6, -0.5),
        (2, 0, ZeroDivisionError),
        (0, 2, 0)
    ]
)
def test_divide(
        calc: Calculator,
        first_value: int,
        second_value: int,
        result: int):
    assert calc.divide(first_value, second_value) == result


@pytest.mark.parametrize(
    'first_value, second_value, result',
    [
        (1, 1, 1),
        (-1, 3, -3),
        (3, -2, -6),
        (0, 0, 0),
        (2, 0, 0)
    ]
)
def test_multiply(
        calc: Calculator,
        first_value: int,
        second_value: int,
        result: int):
    assert calc.multiply(first_value, second_value) == result


@pytest.mark.parametrize(
    'first_value, second_value, result',
    [
        (1, 1, 0),
        (-1, 3, 2),
        (3, -2, -1),
        (2, 2, 0),
        (2, 0, ZeroDivisionError),
    ]
)
def test_mod(
        calc: Calculator,
        first_value: int,
        second_value: int,
        result: int):
    assert calc.mod(first_value, second_value) == result


@pytest.mark.parametrize(
    'first_value, second_value, result',
    [
        (1, 1, 1),
        (-1, 3, -1),
        (3, 3, 27)
    ]
)
def test_power(
        calc: Calculator,
        first_value: int,
        second_value: int,
        result: int):
    assert calc.power(first_value, second_value) == result


@pytest.mark.parametrize(
    'first_value, result',
    [
        (9, 3),
        (25, 5),
    ]
)
def test_root(
        calc: Calculator,
        first_value: int,
        result: float):
    assert calc.root(first_value) == result
