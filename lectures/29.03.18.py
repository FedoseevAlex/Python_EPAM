# Task 1 из лекции
# перевод строки в число рекурсивно
"""
def strtoint(string):
    if type(string) == str:
        if string:
            power = 1
            while ord(string[-1]) // 10**power:
                power += 1
            return 10**power * strtoint(string[:-1]) + ord(string[-1])
        else:
            return 0
    else:
        print('Wrong input! Exit ...')
"""

# Tests
"""
print(strtoint('abcd'))
print(strtoint('asdasdas acsdcascadca '))
print(strtoint(12313))
"""
# Task 2 из лекции
# написать декоратор для времени
# >>> import time
# >>> time.time()
# 12334254.234563
#import time


#def deco(func):
#    def inner(*args, **kwargs):
#        tim1 = time.time()
#        res = func(*args, **kwargs)
#        print (res)
#        print('Elapsed time: {}'.format(time.time() - tim1))
#        return res
#    return inner
#
#@deco
#def test(a):
#    res = 2
#    for i in range(a):
#        res += res ** i
#    return res
#test(10)


#import time
#import functools
#
#
#def deco(func):
#    @functools.wraps(func)
#    def inner(*args, **kwargs):
#        tim1 = time.time()
#        res = func(*args, **kwargs)
#        print (res)
#        print('Elapsed time: {}'.format(time.time() - tim1))
#        return res
#    return inner
#
#@deco
#def test(a):
#    res = 2
#    for i in range(a):
#        res += res ** i
#    return res
#test(2)

# Task 3 из лекции
# написать декоратор validate

#import functools
#
#def validate(func, low_bound = 0, upper_bound = 256):
#
#    @functools.wraps(func)
#    def inner(*args):
#        for i in args:
#            if low_bound <= i < upper_bound:
#                continue
#            else:
#                break
#        else:
#            return func(*args)
#    return inner
#@validate
#def echo(*args):
#    print(args)
#
#
#echo(1)
#echo(1000)

