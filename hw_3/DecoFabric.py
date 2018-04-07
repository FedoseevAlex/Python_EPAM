import functools

# factory accepts lambda as argument
def factory(l_func):
    # Then it gets a decorator to decorate
    def decorated(decorator):
        # Make new decorator look like accepted one
        @functools.wraps(decorator)
        # Decorate it with wrapper and accept an decorator arguments
        def wrapper(*dargs, **dkwargs):
            # Then decorated decorator with arguments receive a function to decorate
            def inner(func):
                if any(callable(item) for item in dargs):
                    func = decorator(*dargs, **dkwargs)
                else:
                    func = decorator(*dargs, **dkwargs)(func)

                # Manually decorate it with received decorator arguments
"""
                # Update magic parameters
                #@functools.wraps(func)
                # Get arguments to pass them to func
                def limb(*args, **kwargs):
                    # Call decorated function
                    res = func(*args, **kwargs)
                    print('ret - {}, lambda - {}'.format(res, l_func(res)))
                    # Apply lambda to result of decorated function and return it
                    return l_func(res)
                return limb"""
                return res
            return inner
        return wrapper
    return decorated

"""
@factory(lambda x: x * 2)
def repeat(times: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = 0
            for time in range(times):
                res += func(*args, **kwargs)
            return res
        return wrapper
    return decorator


@repeat(5)
def test(*args, **kwargs):
    Test function that does nothing
    print("it's alive")
    return 3

test()
"""
@factory(lambda x: x * 2)
def trace(func):

    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        res = func(*args, **kwargs)
        return res
    return inner


@trace
def strtoint2(string):
    res = 0
    power = 0
    for i in string:
        while(ord(i) // 10**power):
            power += 1
        res *= 10**power
        res += ord(i)
    return res


strtoint2('abcd')
