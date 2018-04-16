#!/usr/bin/env python3.6

import time
import traceback


class LogIt:
    """
    Easy logging context manager. Just assign a file name and if error occured
    you'll get full info.
    'A man needs a name'
    Example:
    >>> with LogIt('log.txt'):
    ...     foo() # Function that raises exception 'EX'
    Traceback (most recent call last):
        File "SomeCode.py", line XX, in <module>
            foo()
        File "SomeCode.py", line XX, in foo
            raise EX

    File log.txt contains:
    Error occured dd.mm.yyyy at HH:MM
    Run time: number_of_seconds s
    Traceback (most recent call last):
        File "SomeCode.py", line XX, in <module>
            foo()
        File "SomeCode.py", line XX, in foo
            raise EX
    In case of no errors file 'log.txt' won't be created.
    :param logfile: Name of file to store error data.
    :type logfile: str
    """
    def __init__(self, logfile):
        self.logfile = logfile

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, e_type, e_val, e_tb):
        if e_type is not None:
            self.fd = open(self.logfile, 'w')
            self.elapsed_time = time.time() - self.start_time
            self.now = time.strftime('%d.%m.%Y at %H:%M')
            print('Error occured {}'.format(self.now), file=self.fd)
            print('Run time: {} s'.format(self.elapsed_time), file=self.fd)
            traceback.print_exception(e_type, e_val, e_tb, file=self.fd)
            self.fd.close()


def foo():
    """
    Some usless function. Can cause problems.
    """
    a = 0
    for i in range(200):
        a += (i ** i) ** i
    raise ArithmeticError('WOW')
    return a

if __name__ == '__main__':

    with LogIt('err.log'):
        foo()
