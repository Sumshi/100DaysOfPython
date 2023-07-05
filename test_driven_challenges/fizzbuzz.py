#!/usr/bin/python3

"""this is fizzbuzz module"""


def fizzbuzz(numbers):
    """
    if a number is divisible by 3 return fizz
    if a number is divisible by 5 return buzz
    if a number is divisible by 3 and 5 return fizzbuzz
    """

    new_list = []

    for num in numbers:
        if type(num) is not int:
            raise TypeError("num must be an integer")

        if num % 3 == 0 and num % 5 == 0:
            new_list.append('fizzbuzz')
        if num % 3 == 0:
            new_list.append('fizz')
        if num % 5 == 0:
            new_list.append('buzz')
        else:
            new_list.append(num)
    return new_list
