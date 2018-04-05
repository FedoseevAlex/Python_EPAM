import functools

# factory accepts lambda as argument
def factory(l_func):
    """
    Decorator factory. Receives function that will be called with a result of decorated decorator as argument.
    :param l_func: function
    :return: function - decorated decorator
    """
    # Then it gets a decorator to decorate
    def decorated(decorator):
        # Make new decorator look like accepted one
        @functools.wraps(decorator)
        # Decorate it with wrapper and accept an decorator arguments
        def wrapper(*dargs, **dkwargs):
            # If there's a callable argument in dargs or in dkwargs, then
            if any(callable(item) for item in dargs) or any(callable(dkwargs[item]) for item in dkwargs):
                # Define a function that pass arguments to decorated function
                def inner(*args, **kwargs):
                    # Decorate it
                    decorated_func = decorator(*dargs, **dkwargs)
                    # call decorated function with it's *args and **kwargs
                    res = decorated_func(*args, **kwargs)
                    print('ret - {}, lambda - {}'.format(res, l_func(res)))
                    return l_func(res)
                return inner
            # if there were no callable arguments
            else:
                # then get decorated function
                def inner(func):
                    @functools.wraps(func)
                    # also get it's parameters
                    def limb(*args, **kwargs):
                        # Manually decorate function with *dargs and **dkwargs
                        decorated_func = decorator(*dargs, **dkwargs)(func)
                        # Call decorated func with it's *args and **kwargs
                        res = decorated_func(*args, **kwargs)
                        # Apply lambda to result
                        print('ret - {}, lambda - {}'.format(res, l_func(res)))
                        return l_func(res)
                    return limb
                return inner
        return wrapper
    return decorated


@factory(lambda x: x ** 2)
def repeat(times: int):
    """
    Repeat decorator. Decorated funtion will be called 'times' times
    :param times: how much rounds will decorated function do
    :type times: int
    :return: decorated function
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            for time in range(1, times):
                res += func(*args, **kwargs)
            return res
        return wrapper
    return decorator


@repeat(5)
def test(*args, **kwargs):
    """
    Just test function. Does nothing at all.
    :param args: some args just to pass something
    :param kwargs: some kwargs just to pass something
    :return: int
    """
    print("it's alive")
    return 4

test()

@factory(lambda x: x ** 2)
def trace(func):
    """
    Decorator that adds input information. Cen be used for logging, but it is not exactly.
    :param func: function to be wrapped
    :return:wrapped function with trace of input
    """
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        res = func(*args, **kwargs)
        return res
    return inner


@trace
def strtoint2(string):
    """
    Converts string to integer that is a concatenation of its characters
    >>> strtoint2('abcd')
    979899100
    In case of wrong type of input data returns None
    :param string: string to be converted
    :type string: str
    :return: int
    """
    if type(string) == str:
        res = 0
        power = 0
        for i in string:
            while(ord(i) // 10**power):
                power += 1
            res *= 10**power
            res += ord(i)
        return res
    else:
        return None

strtoint2('abcd')
