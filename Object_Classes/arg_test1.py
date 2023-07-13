#!/usr/bin/python3

"""using both args and kwargs"""


def process_data(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

process_data(1, 2, 3, name="John", age=30)

