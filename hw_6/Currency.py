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
            try:
                return instance.__dict__[self.label]
            except KeyError:
                return self

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
    course = PositiveDecimal()
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

    def to(self, other):
        return '{} {}'.format(self.amount * other.course / self.course, other.symbol)



class Dollar(Currency):
    symbol = '$'
    pass

class Euro(Currency):
    symbol = '€'
    pass

class Ruble(Currency):
    symbol = 'R'
    pass

d = Dollar(234)
r = Ruble(240)
print(d)
print(d.amount)
print(d.course)
Dollar.course = 1
Ruble.course = -60
Euro.course = -9
r.to(Dollar)
print(r.to(Euro))