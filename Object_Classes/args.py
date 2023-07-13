#!/usr/bin/python3

"""args - accepts any number of arguments"""


def sum_numbers(*args):
    """calculates sum of arguments passed
    allows passing a variable number of non-keyword arguments to a function
    """
    total = 0
    for num in args:
        total += num
    return total

result = sum_numbers(10, 20, 30, -10)
print(result)
