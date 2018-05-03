#import time
#
#class TimeCode:
#    def __enter__(self):
#        self.init_time = time.time()
#        return self
#
#    def __exit__(self,  e_type, e_val, e_tb):
#        print('Elapsed time - {} s'.format(time.time() - self.init_time))
#        return True
#
#with TimeCode() as t:
#    acc = 0
#    for i in range(5000):
#        acc += i ** i


#import time
#import contextlib
#
#class TimeCode(contextlib.ContextDecorator):
#    def __enter__(self):
#        self.init_time = time.time()
#        return self
#
#    def __exit__(self,  e_type, e_val, e_tb):
#        print('Elapsed time - {} s'.format(time.time() - self.init_time))
#        return True
#
#@TimeCode()
#def foo():
#    acc = 0
#    for i in range(5000):
#        acc += i ** i
#
#
#foo()
#
#
#with TimeCode():
#    foo()

class desc:
    def __init__(self):
            self.label = id(self)

    def __get__(self, instance, owner):
        print('desc __get__')
        if instance is None:
                return owner.__dict__[self.label]
        else:
                return instance.__dict__[self.label]

    def __set__(self, instance, value):
        print('desc __set__')
        instance.__dict__[self.label] = value


class A:
    a = desc()

    def __init__(self, value):

        self.a = value


#A.a = 89
foo = A(13) # Дескриптор работает как задумано

#print('A.a = {}'.format(A.a))
print('foo.a = {}'.format(foo.a))
foo.a = 10
#print('A.a = {}'.format(A.a))
print('foo.a = {}'.format(foo.a))
A.a = 45343  # Здесь дескриптор пропадает и просто присваивается значение
print('A.a = {}'.format(A.a))
print('foo.a = {}'.format(foo.a)) # Тут __get__ уже не вызывается

