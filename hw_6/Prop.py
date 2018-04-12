#!/usr/bin/env/ python3.6
# HW #L6.2 Descriptor prop aka Property


class Prop:
    """
    Property
    """
    def __init__(self, getter=None, setter=None, deleter=None):
        self.getter = getter
        self.setter = setter
        self.deleter = deleter

    def __get__(self, instance, owner):
        if instance == None:
            return self
        print('Prop getter')
        return self.getter(instance)

    def __set__(self, instance, value):
        print('Prop setter')
        return self.setter(instance, value)

    def __delete__(self, instance):
        print('Prop deleter')
        return self.deleter(instance)

    def get_func(self, getter):
        """
        Method to assign getter function.
        :param getter: function that gets attribute value.
        :type getter: function
        :return: result of getter function work
        """
        return self.__class__(getter, self.setter, self.deleter)

    def set_func(self, setter):
        """
        Method to assign setter function.
        :param setter: function that sets attribute value.
        :type setter: function
        :return: result of setter function work
        """
        return self.__class__(self.getter, setter, self.deleter)

    def del_func(self, deleter):
        """
        Method to assign deleter function.
        :param deleter: function that deletes attribute value.
        :type deleter: function
        :return: result of deleter function work
        """
        return self.__class__(self.getter, self.setter, deleter)


class Something:
    """
    Test class for prop
    """
    def __init__(self, x):
        self.x = x
    @Prop
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