"""
This module reverses a string
"""


def reverse_string(string):
    """
    This function return the reverse of a string

    >>> reverse_string("Hello")
    'olleH'
    >>> reverse_string("")
    ''
    >>> reverse_string(98)
    Traceback (most recent call last):
    ...
    TypeError: Input must be a string
    >>> reverse_string(None)
    Traceback (most recent call last):
    ...
    TypeError: Input must be a string
    >>> reverse_string(["Hello"])
    Traceback (most recent call last):
    ...
    TypeError: Input must be a string
    >>> reverse_string("H")
    'H'
    >>> reverse_string("98")
    '89'

    """
    if not isinstance(string, str):
        raise TypeError('Input must be a string')
    return string[::-1]
