#!/usr/bin/env/ python3.6
# HW #L6.1 Currency

import abc
import decimal

class PositiveDecimal:

    def __init__(self):
        self.label = 'Course <{}>'.format(id(self))

    def __get__(self, instance, owner):
        try:
            return instance.__dict__[self.label]
        except KeyError:
            return self

    def __set__(self, instance, value):
        if isinstance(value, (int, float)):
            if value < 0:
                raise ValueError('Must be positive.')
            instance.__dict__[self.label] = decimal.Decimal(str(value))
        else:
            raise ValueError('Wrong value for money.')

class Currency(abc.ABC):
    _amount = PositiveDecimal()
    course = PositiveDecimal()
    symbol = None

    def __init__(self, amount):
        self._amount = amount

    def to(self, other):
         return self._amount * (1 / self.course) * other._amount


class Dollar(Currency):
    #course = 2
    symbol = '$'

class Rubble(Currency):
    course = PositiveDecimal()
    symbol = 'R'

class Euro(Currency):
    course = PositiveDecimal()
    symbol = '€'

a = Dollar(3)
print(a.course)

b = Rubble(192)


c = Euro(1)

# print(b.to(Dollar))
# print(b.to(Rubble))
# print(b.to(Euro))