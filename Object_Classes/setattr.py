#!/usr/bin/python3

"""setattr() is used to set the value of an attribute of an object"""


class Person:
    """defines a class person"""
    pass

p1 = Person()
setattr(p1, 'name', 'maya')
print(p1.name)
