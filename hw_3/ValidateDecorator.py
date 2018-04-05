#!/usr/bin/python3.6

import functools


def validate(lower_bound: int=0, upper_bound: int=255):
    """
    Returns decorator that checks if input args is between lower_bound and upper_bound
    :param lower_bound:
    :param upper_bound:
    :return: function (decorator with validate option)
    """
    def wrapper_validate(func):
        # To make inner look like func in help
        @functools.wraps(func)
        def inner(*args):
            for arg in args:
                # If arg contain 3 values and all of them of int type and between limits
                if len(arg) == 3 and all(lower_bound <= x <= upper_bound if type(x) == int else False for x in arg):
                    continue
                else:
                    print('Function call is not valid')
                    break
            else:
                func(*args)
        return inner
    return wrapper_validate


@validate(lower_bound=0, upper_bound=255)
def set_pixel(*pixel_values):
    """
    Test function to check arguments validation
    :param pixel_values: checked arguments
    :type pixel_values: collection of lists or tuples with 3 int values inside
    :return: None
    """
    print('Pixel created!')

# Test

"""
set_pixel((0, 127, 300))  # Too high value is invalid

set_pixel((25, 59, -1))  # Negative int is invalid

set_pixel((25, 59, 65))  # Valid input

set_pixel((93, 0, 78), (43, 200, 11))  # Valid input

set_pixel((93, 0, 78), [43, 200, 11])  # Valid input

set_pixel((25, 59, 65), (43, 200, 1111))  # Invalid input

set_pixel([25, 59, -1])  # Negative int is invalid

set_pixel([25, 59, 125])  # Valid input

set_pixel(('a', 1.25, []))  # Wrong type is invalid

set_pixel((), [], {})  # No input is invalid

set_pixel({'r': 3, 'g': 34, 'b': 123 })  # Input is invalid
"""
