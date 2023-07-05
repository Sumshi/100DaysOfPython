#!/usr/bin/python3

"""this is fizzbuzz module"""


def fizzbuzz(numbers):
    """
    if a number is divisible by 3 return fizz
    if a number is divisible by 5 return buzz
    if a number is divisible by 3 and 5 return fizzbuzz
    """

    result = []

    for num in numbers:
        if type(num) is not int:
            raise TypeError("num must be an integer")

        if num % 3 == 0 and num % 5 == 0:
            result.append('fizzbuzz')
        elif num % 3 == 0:
            result.append('fizz')
        elif num % 5 == 0:
            result.append('buzz')
        else:
            result.append(str(num))
    return new_list
