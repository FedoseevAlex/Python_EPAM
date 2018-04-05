#!/usr/bin/python3.6

from time import time
import functools

def time_deco(func):
    """
    This decorator can measure work time of func(*args, **kwargs)
    :param func: function to decorate
    :type: func: function
    :return: decorated function
    """
    # To make inner look like func
    @functools.wraps(func)
    def inner(*args, **kwargs):
        # Get time before call func(*args, **kwargs)
        time_before_launch = time()
        res = func(*args, **kwargs)
        print('Elapsed time for "{}({}, {})" -- {} sec'.format(func.__name__, args, kwargs, time() - time_before_launch))
        return res
    return inner

@time_deco
def factorial(num: int) -> int:
    """
    I can calculate factorial.
    >>> factorial(5)
    120
    >>> factorial(not_int_argument)
    None
    :param num: number to calculate num!
    :type num: int
    :return: int
    """
    if type(num) == int and num >= 0:
        # a - accumulator to store num! value
        return functools.reduce(lambda a, x: a * x if x > 1 else 1, range(1, num + 1), 1)
    else:
        return None


print(factorial(1000))
