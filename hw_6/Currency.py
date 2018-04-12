#!/usr/bin/env/ python3.6
# HW #L6.1 Currency

import abc
import decimal


class PositiveDecimal:
    """
    Only positive values to store money values.
    """
    def __init__(self):
        self.label = '<Course at {}>'.format(id(self))

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.label]

    def __set__(self, instance, value):
        try:
            to_set = decimal.Decimal(str(value))
        except decimal.InvalidOperation:
            raise ValueError('Wrong attribute value')
        if to_set < 0:
            raise ValueError('Negative values not allowed.')
        else:
            instance.__dict__[self.label] = to_set


class Currency(abc.ABC):
    """
    This abstract class representing currencies.
    >>> Dollar(Currency):
    ... pass
    """
    course = None
    symbol = '¤'

    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return '{} {}'.format(self.amount, self.symbol)

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value) -> None:
        try:
            to_set = decimal.Decimal(str(value))
        except decimal.InvalidOperation:
            raise ValueError('Wrong attribute value.')
        if to_set < 0:
            raise ValueError('Negative values not allowed.')
        else:
            self._amount = to_set

    def __eq__(self, other):
        return self.amount / self.course == other.amount / other.course

    def __lt__(self, other):
        return self.amount / self.course < other.amount / other.course

    def __le__(self, other):
        return self.amount / self.course <= other.amount / other.course

    def __gt__(self, other):
        return self.amount / self.course > other.amount / other.course

    def __ge__(self, other):
        return self.amount / self.course >= other.amount / other.course

    def __ne__(self, other):
        return self.amount / self.course != other.amount / other.course

    def __mul__(self, other):
        if isinstance(other, (int, float, decimal.Decimal)):
            return self.amount * decimal.Decimal(str(other))
        else:
            raise ArithmeticError('Only {} and int, float or decimal.Decimal multiplication is allowed.')

    def __rmul__(self, other):
        if isinstance(other, (int, float, decimal.Decimal)):
            return self.amount * decimal.Decimal(str(other))
        else:
            raise ArithmeticError('Only {} and int, float or decimal.Decimal multiplication is allowed.')

    def __truediv__(self, other):
        if isinstance(other, (int, float, decimal.Decimal)):
            return self.amount / decimal.Decimal(str(other))
        else:
            raise ArithmeticError('Only {} and int, float or decimal.Decimal division is allowed.')

    def __rtruediv__(self, other):
        if isinstance(other, (int, float, decimal.Decimal)):
            return  decimal.Decimal(str(other)) / self.amount
        else:
            raise ArithmeticError('Only {} and int, float or decimal.Decimal division is allowed.')

    def to(self, other):
        """
        Currency conversion method.
        :param other: currency class you want to convert to
        :type other: currency class
        :return: value in converted currency
        """
        return '{} {}'.format(self.amount * other.course / self.course, other.symbol)



class Dollar(Currency):
    """
    Dollar class. 99% freedom
    """
    course = decimal.Decimal(str(1))
    symbol = '$'
    pass


class Euro(Currency):
    """
    Euro class.
    """
    course = decimal.Decimal(str(0.81))
    symbol = '€'
    pass


class Ruble(Currency):
    """
    Ruble class, comrade!
    """
    course = decimal.Decimal(str(60))
    symbol = 'R'
    pass


d = Dollar(10)
r = Ruble(240)
e = Euro(10)
"""
print(d)
print(d.amount)
print(d.course)
"""
d.course = 1
r.course = 60
e.course = 0.81

print(d.to(Ruble))