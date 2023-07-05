#!/usr/bin/python3

"""function that reverses a string"""

def reverse_string(string):
    if type(string) is not str:
        raise TypeError("only strings are used")
    else:
        return string[::-1] 
