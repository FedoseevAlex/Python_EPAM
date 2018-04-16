#!/usr/bin/env python3.6

import time
import traceback

class LogIt:
    def __init__(self, logfile):
        self.logfile = logfile

    def __enter__(self):
        self.fd = open(self.logfile, 'w')
        self.start_time = time.time()
        return self.fd

    def __exit__(self, e_type, e_val, e_tb):
        if e_type is not None:
            self.elapsed_time = time.time() - self.start_time
            self.now = time.strftime('%d.%m.%Y at %H:%M')
            print('Error occured {}:'.format(self.now), file=self.fd)
            print('Run time: {} s'.format(self.elapsed_time), file=self.fd)
            traceback.print_exception(e_type, e_val, e_tb, file=self.fd)
        self.fd.close()

def foo():
    a = 0
    for i in range(200):
        a += (i ** i) ** i
    print(a)
    return a

if __name__ == '__main__':

    with LogIt('err.log'):
        foo()
