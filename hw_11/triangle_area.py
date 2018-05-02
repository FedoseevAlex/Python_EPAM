#!/usr/bin/env/ python3.6
# HW #L11.2 Triangle area

"""
Triangle area module.
"""

import math
from itertools import combinations as cb

class Triangle:
    """
    Represents triangle, defined by three points.
    """
    def __init__(self, *args):
        if self.__points_checker(*args):
            self.points = args

    def __points_checker(self, *args):
        """
        Check that points is really form a triangle.

        :param args: points in form of tuples e.g. (1, 2), (4, 8), (12, 23)
        :return: boolean True -- if points can define a triangle, False otherwise.
        """

        # Check that exactly three points given
        # And each point have two coordinates
        # Also that coordinates is int or float
        # Then check that given points is not the same
        # Whether points belong to one line
        if len(args) != 3:
            raise AttributeError('Wrong number of points. Must be 3, given {}'.format(len(args)))
        elif not all(isinstance(component, (int, float)) for point in args for component in point):
            raise AttributeError('Wrong point components. Point must be defined with int or float numbers.')
        elif any(len(arg) != 2 for arg in args):
            raise AttributeError('Wrong number of coordinates in point. Must be exactly two coordinates in each point.')
        elif len(set(args)) != 3:
            raise AttributeError('It seems that some points are the same. Coincident points can not define triangle.')
        elif self.__on_one_line(*args):
            raise AttributeError('Given points are belong to one line. Such points can not define triangle.')
        else:
            return True

    @staticmethod
    def __on_one_line(*args):
        """
        Function to check if three points belong to one line.

        :param args: Points to check.
        :type args: Three tuples of two integers in each. E.g. args = (1, 2), (3, 4), (5, 6)
        :return: True if given points belong to one line. False otherwise.
        """
        p1, p2, p3 = args
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) == (p1[1] - p3[1]) * (p2[0] - p3[0])

    def area(self):
        a, b, c = [math.hypot(*map(lambda elem: elem[1] - elem[0], zip(*pair))) for pair in cb(self.points, 2)]
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

if __name__ == '__main__':
    t = Triangle((1, 3), (3, 2), (1, 8))
    print(t.area())
    t._Triangle__on_one_line(*((1, 3), (1, 2), (1, 8)))