#!/usr/bin/python3.6
import sys


def strtoint(string: str) -> int:
    """
    Converts string to integer that is a concatenation of its characters numbers
    >>> strtoint('abcd')
    979899100
    In case of wrong type of input data returns None
    :param string: string to be converted
    :type string: str
    :return: int
    """
    if type(string) == str:
        if string:
            power = 0
            while ord(string[-1]) // pow(10, power):
                power += 1
            return pow(10, power) * strtoint(string[:-1]) + ord(string[-1])
        else:
            return 0
    else:
        print('Wrong input data -> strtoint({})'.format( string))
        return None

if len(sys.argv) > 1:
    print(strtoint(sys.argv[1]))
else:
    print('Please enter something! Exit...')
#print(strtoint('abcd'))
#print(strtoint(12))

