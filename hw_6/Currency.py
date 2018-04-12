#!/usr/bin/env/ python3.6
# HW #L6.1 Currency

import abc
import decimal


class PositiveDecimal:
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
        return '{} {}'.format(self.amount * other.course / self.course, other.symbol)



class Dollar(Currency):
    course = PositiveDecimal()
    symbol = '$'
    pass


class Euro(Currency):
    course = PositiveDecimal()
    symbol = '€'
    pass


class Ruble(Currency):
    course = PositiveDecimal()
    symbol = 'R'
    pass


d = Dollar(234)
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

