#!/usr/bin/python3

"""module that counts vowels in a string"""


def count_vowels(string):
    """count vowel function"""
    if type(string) is not str:
        raise TypeError("a string must be passed")
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']

    for char in string:
        if char.lower() in vowels:
            count += 1
    return count
