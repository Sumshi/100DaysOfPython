#!/usr/bin/python3

"""getattr() is used to get the value of an attribute of an object"""

class Person:
    name = 'john'

p1 = Person()
name = getattr(p1, 'name')
print(name)
