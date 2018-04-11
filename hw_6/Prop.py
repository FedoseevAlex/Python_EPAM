#!/usr/bin/env/ python3.6
# HW #L6.2 Descriptor prop aka Property


class prop:
    def __init__(self, getter=None, setter=None, deleter=None):
        self.getter = getter
        self.setter = setter
        self.deleter = deleter

    def __get__(self, instance, owner):
        print('Prop getter')
        return self.getter(instance)

    def __set__(self, instance, value):
        print('Prop setter')
        return self.setter(instance, value)

    def __delete__(self, instance):
        print('Prop deleter')
        return self.deleter(instance)

    def get_func(self, getter):
        return self.__class__(getter, self.setter, self.deleter)

    def set_func(self, setter):
        return self.__class__(self.getter, setter, self.deleter)

    def del_func(self, deleter):
        return self.__class__(self.getter, self.setter, deleter)


class Something:
    def __init__(self, x):
        self.x = x
    @prop
    def attr(self):
        return self.x ** 2

    @attr.set_func
    def attr(self, value):
        self.x = value

    @attr.del_func
    def attr(self):
        del self.x

s = Something(10)
s.attr = 45
print(s.attr)