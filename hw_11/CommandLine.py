#!/usr/bin/env/ python3.6
# HW #L11.2 Triangle area

"""
Command line module implements user text interface.

"""

from Triangle import Point, Triangle
import re


def make_action():
    """
    Gets command from user input and call corresponding handler function.
    :return None
    """
    triangle = None
    print('Triangle area!')
    print('Type "h" for help.')
    while True:
        command = input('> ')
        if command == 'new':
            triangle = get_triangle()

        elif command in ['help', '?', 'h']:
            get_help()

        elif command in ['quit', 'exit', 'q']:
            print('Exit...')
            break

        elif triangle is None and command in ['area', 'isosceles', 'equilateral']:
            print('No triangle was defined. Type "new" to define a triangle first.')
            continue

        elif command == 'area':
            print('Triangle area is: {}'.format(triangle.area()))

        elif command == 'isosceles':
            print(triangle.is_isosceles)

        elif command == 'equilateral':
            print(triangle.is_equilateral)

        elif command is None:
            print('No command was entered. Type "help" to get list of possible commands.')

        else:
            print('Wrong command. Type "help" to get list of possible commands.')


def get_triangle() -> Triangle:
    """
    This function creates triangle from given points.
    In case of wrong points it will print a warning and triangle is not created.

    :return: Triangle -- object that created with user input
    """
    a = get_point()
    b = get_point()
    c = get_point()

    try:
        res = Triangle(a, b, c)
    except ValueError as raised:
        print('Error in triangle definition. {}'.format(raised.args[0]))
        return None

    print('Triangle created {}'.format(str(res)))
    return res


def get_point() -> Point:
    """
    Ask user to type point coordinates and creates Point object.

    :return: Point -- point defined with provided coordinates x and y
    """
    while True:
        point_pattern = re.compile('\d*[.]?\d*\s\d*[.]?\d*')
        coordinates = input("Enter coordinates as follows: 'x y'\n> ").strip()
        if point_pattern.fullmatch(coordinates):
            x, y = coordinates.split(' ')
            return Point(float(x), float(y))
        else:
            print('Wrong point coordinates. Try again.')


def get_help():
    """
    Prints help message for user.
    :return None
    """
    help_string = {'new': 'Command to define triangle from three points.',
                   'help': "Show help message. Possible alternatives are: '?', 'h'.",
                   'quit': "Quit and close program. Possible alternatives are: 'q', 'exit'.",
                   'area': "Calculate and print area of triangle.",
                   'isosceles': "Print True if given triangle is isosceles, or False otherwise.",
                   'equilateral': "Print True if given triangle is equilateral, or False if not."}
    print('Help:')
    for key, val in help_string.items():
        print('    {} -- {}'.format(key, val))


if __name__ == '__main__':
    get_help()
    import doctest
    doctest.testmod()
