#!/usr/bin/python3

"""passes a variable number of keyword arguments to a function."""


def print_info(**kwargs):
    """kwargs parameter is treated as a dictionary inside the function
    containing all the keyword arguments passed to it.
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="John", age=30, city="London")
