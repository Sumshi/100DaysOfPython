#!/usr/bin/python3

""" is used to check if an object has a particular attribute."""


class Person:
    name = 'john'

p1 = Person()
has_name_attr = hasattr(p1, 'name')
has_age_attr = hasattr(p1, 'age')
print(has_name_attr)  # Output: True
print(has_age_attr)  # Output: False
