#!/usr/bin/env/ python3.6
# HW #L11.2 Triangle area

"""
This module contains Point class and Triangle class.
Point defined by two in or float values.
Triangle is defined by three Point objects.
"""

import math
from functools import partial


class Point:
    """
    This class represents a point in 2D. Thus point accepts exactly two arguments 'x' and 'y'.
    If no arguments were given during an instantiation the (0, 0) point will be created.
    Note: Point is immutable! After creating of instance it is not possible to change point coordinates.
    Example:

    >>> a = Point(0, 1)
    >>> a
    (0.0, 1.0)
    >>> b = Point(0, 4)
    >>> a.distance(b)
    3.0
    >>> b.distance()
    4.0
    """

    def __init__(self, x=0, y=0):
        """
        Initialise new Point object with provided coordinates.
        :param x: Coordinate on X axis
        :type x: int or float. Any given value will be cast to float. If no value given x = 0.
        :param y: Coordinate on X axis
        :type y: int or float. Any given value will be cast to float. If no value given y = 0.

        Example:
        >>> a = Point(x=123)
        >>> a
        (123.0, 0.0)
        >>> a = Point(y=392.3)
        >>> a
        (0.0, 392.3)
        >>> b = Point(12, '34')
        Traceback (most recent call last):
        ...
        ValueError: Wrong value to define point. Both x and y must be int or float.
        >>> c = Point()
        >>> c
        (0.0, 0.0)
        """
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            self.__x = float(x)
            self.__y = float(y)
        else:
            raise ValueError('Wrong value to define point. Both x and y must be int or float.')

    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    @property
    def x(self) -> float:
        """
        Property that returns x coordinate of point.
        Note: Setter and deleter not defined for x. So it can not be changed or deleted.
        Examples:
        >>> a = Point(42.134, 1.01)
        >>> a.x
        42.134
        >>> a.x = 0
        Traceback (most recent call last):
        ...
        AttributeError: can't set attribute
        >>> del a.x
        Traceback (most recent call last):
        ...
        AttributeError: can't delete attribute

        :return: coordinate of type float
        """
        return self.__x

    @property
    def y(self) -> float:
        """
        Property that returns x coordinate of point.
        Note: Setter and deleter not defined for y. So it can not be changed or deleted.
        Examples:
        >>> a = Point(42.134, 1.01)
        >>> a.y
        1.01
        >>> a.y = 45
        Traceback (most recent call last):
        ...
        AttributeError: can't set attribute
        >>> del a.y
        Traceback (most recent call last):
        ...
        AttributeError: can't delete attribute

        :return: coordinate of type float
        """
        return self.__y

    def distance(self, other=None) -> float:
        """
        Calculate distance between two points.
        Note: If no point provided, function will return distance from (0, 0) point.
        >>> a = Point(1, 0)
        >>> b = Point(6, 0)
        >>> a.distance(b)
        5.0
        >>> a.distance()
        1.0
        >>> a.distance('foo')
        Traceback (most recent call last):
        ...
        ValueError: Wrong type of argument. Distance is calculated between two Point objects.

       :param other: Point to calculate distance to.
       :type other: Point instance.
       :return: float value of distance
       """
        if isinstance(other, Point):
            return math.hypot(self.x - other.x, self.y - other.y)
        elif other is None:
            return math.hypot(self.x, self.y)
        else:
            raise ValueError('Wrong type of argument. Distance is calculated between two Point objects.')

    @staticmethod
    def on_one_line(*args) -> bool:
        """
        This method checks belonging of all given points to one line.
        Note: If 1 or 2 points are given function will always return True because every single point belongs to some
        line as well as every two points.
        Examples:
        >>> a = Point(1, 0)
        >>> b = Point(34, 0)
        >>> c = Point(42, 0)
        >>> Point.on_one_line(a, b, c)
        True
        >>> a = Point(1, 2)
        >>> b = Point(34, 43)
        >>> c = Point(42, 54)
        >>> Point.on_one_line(a, b, c)
        False
        >>> Point.on_one_line(a)
        True
        >>> Point.on_one_line(Point(1, 3), Point(32, 34))
        True
        >>> Point.on_one_line('foo', a , b, c)
        Traceback (most recent call last):
        ...
        ValueError: Some of given arguments is not points.

        :param args: Any number of points.
        :type args: Point instances.
        :return: True if all given points lie on one straight line. False otherwise.
        """
        if not all(isinstance(arg, Point) for arg in args):
            raise ValueError('Some of given arguments is not points.')
        elif len(args) <= 1:
            # One point as well as two points always belong to one line, thus:
            return True
        else:
            check_three_points = partial(lambda a, b, c: (a.x - b.x) * (a.y - c.y) == (a.x - c.x) * (a.y - b.y),
                                         args[0], args[1])
            return all(map(check_three_points, args[2:]))


class Triangle:
    """
    Represents triangle, defined by three points a, b and c.
                         a
                        /\
                       /  \
                    c /____\ b
    Example:
    >>> t = Triangle(Point(0, 0), Point(8, 0), Point(4, 5))
    >>> t
    ((0.0, 0.0), (8.0, 0.0), (4.0, 5.0))
    >>> t.area()
    20.0
    >>> t.is_equilateral
    False
    >>> t.is_isosceles
    True
    """

    def __init__(self, a=None, b=None, c=None):
        """
        This method takes three points to initialise a triangle.
        Given points define triangle vertex.

        Example:
        >>> Triangle(Point(0, 0), Point(0, 3), Point(4, 4))
        ((0.0, 0.0), (0.0, 3.0), (4.0, 4.0))
        >>> Triangle(Point(1, 1), Point(1, 3), Point(1, 5))
        Traceback (most recent call last):
        ...
        ValueError: Given points belong to one line and can not define triangle.

        :param a:
        :type a:
        :param b:
        :type b:
        :param c:
        :type c:
        """
        if None not in (a, b, c) and not Point.on_one_line(a, b, c):
            self._a = a
            self._b = b
            self._c = c
        else:
            raise ValueError('Given points belong to one line and can not define triangle.')

    def __repr__(self):
        return '({}, {}, {})'.format(self._a, self._b, self._c)

    def area(self, mantissa=3):
        """
        Method to calculate area of triangle. Calculated value is rounded according to mantissa parameter.
        Mantisssa define how much digits after decimal point to be left.
        By default mantissa=3. If more accurate value is necessary increase mantissa.
        If mantissa less than zero than function return 0.0
        Example:
        >>> t = Triangle(Point(0, 3.1415), Point(2.7, 3), Point(3 ** 0.5, 6.023))
        >>> t.area(1)
        4.0
        >>> t.area()
        4.013
        >>> t.area(6)
        4.012568
        >>> t.area(-1)
        Traceback (most recent call last):
        ...
        ValueError: Negative number for mantissa is not allowed.

        :param mantissa: Amount of numbers after decimal point.
        :type mantissa: int
        :return:
        """
        if mantissa < 0:
            raise ValueError('Negative number for mantissa is not allowed.')
        a_edge = self._a.distance(self._b)
        b_edge = self._b.distance(self._c)
        c_edge = self._c.distance(self._a)
        p = (a_edge + b_edge + c_edge) / 2
        return round(math.sqrt(p * (p - a_edge) * (p - b_edge) * (p - c_edge)), mantissa)

    @property
    def is_isosceles(self):
        """
        Checks whether triangle is isosceles.
        Example:
        >>> a = Point(-2, 0)
        >>> b = Point(2, 0)
        >>> c = Point(0, 4)
        >>> t = Triangle(a, b, c)
        >>> t.is_isosceles
        True

        :return: True if triangle have at least two equal edges. False otherwise.
        """
        a_edge = self._a.distance(self._b)
        b_edge = self._b.distance(self._c)
        c_edge = self._c.distance(self._a)
        return any([a_edge == b_edge, b_edge == c_edge, c_edge == a_edge])

    @property
    def is_equilateral(self) -> bool:
        """
        Checks if triangle is equilateral.
        >>> a = Point(-9, 10)
        >>> b = Point(-1, 4)
        >>> c = Point(3 * 3 ** 0.5 - 5, 4 * 3 ** 0.5 + 7)
        >>> t = Triangle(a, b, c)
        >>> t.is_equilateral
        True

        :return: True if edges of triangle are equal. False otherwise.
        """
        a_edge = self._a.distance(self._b)
        b_edge = self._b.distance(self._c)
        c_edge = self._c.distance(self._a)
        return all([a_edge == b_edge, b_edge == c_edge, c_edge == a_edge])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
