""" Home task calculator module """
from math import sqrt


def is_int(x, y=1):
    """ Check if value is integer """
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Values must be an integer!")


class Calculator:
    """ Calculator implementation """

    def add(self, x: int, y: int) -> int:
        """ Add to attributes to each other """
        is_int(x, y)
        return x + y

    def subtract(self, x: int, y: int) -> int:
        """ Subtract one attribute from another """
        is_int(x, y)
        return x - y

    def divide(self, x: int, y: int) -> float:
        """ Divide x attribute on y """
        is_int(x, y)
        return x / y if y != 0 else ZeroDivisionError

    def multiply(self, x: int, y: int) -> int:
        """ Multiply x attribute on y """
        is_int(x, y)
        return x * y

    def mod(self, x: int, y: int) -> int:
        """ Take mod of one attribute from another """
        is_int(x, y)
        return x % y if y != 0 else ZeroDivisionError

    def power(self, x: int, y: int) -> int:
        """ Raise attributes x to a power y """
        is_int(x, y)
        return x ** y

    def root(self, x: int) -> float:
        """ Take a root from attributes """
        is_int(x)
        return sqrt(x)
