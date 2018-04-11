#!/usr/bin/env/ python3.6
# Task #L6.1 Class Book, descriptor price
class Price:
    """
    Price descriptor
    """
    def __init__(self):
        self.label = id(self)
        
    def __get__(self, instance, owner):
        return instance.__dict__[self.label]
    
    def __set__(self, instance, value):
        if 0 <= value <= 100:
            instance.__dict__[self.label] = value
        else:
            raise ValueError("Price must be between 0 and 100")
        
    def __delete__(self, instance):
        instance.__dict__.pop(self.label, 0)
        
        
class Book:
    """
    Book class
    """
    price = Price()
    
    def __init__(self, author, title, bookprice):
        self.price = bookprice
        self.author = author
        self.title = title


# Test
"""
b = Book('William Faulkner', 'The Sound and the Fury', 12)
print('b.price right after init: ')
print(b.price)
b.price = 66
print('b.price after assigning new value: ')
print(b.price)

c = Book('Willi Famkneraul', 'The Sound ', 45)
print('c.price right after init: ')
print(c.price)
c.price = 23
print('c.price after assigning new value: ')
print(c.price)
print('b.price is still the same: ')
print(b.price)

print('If you try to assign wrong value to b.price: ')
b.price = 55
print(b.price)

try:
    b.price = 101
except ValueError as e:
    print('NO WAY Error - {}'.format(e))
"""
