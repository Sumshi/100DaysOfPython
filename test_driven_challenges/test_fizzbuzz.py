#!/usr/bin/python3
import unittest

fizzbuzz = __import__('fizzbuzz').fizzbuzz

def test_fizzbuzz():
    # Test case 1
    assert fizzbuzz(15) == [
        "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
        "11", "Fizz", "13", "14", "FizzBuzz"
    ]

    # Test case 2
    assert fizzbuzz(7) == [
        "1", "2", "Fizz", "4", "Buzz", "Fizz", "7"
    ]

    # Test case 3
    assert fizzbuzz(5) == [
        "1", "2", "Fizz", "4", "Buzz"
    ]

    # Test case 4
    assert fizzbuzz(1) == [
        "1"
    ]

    # Test case 5
    assert fizzbuzz(0) == []

    # Test case 6
    assert fizzbuzz(30) == [
        "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
        "11", "Fizz", "13", "14", "FizzBuzz", "16", "17", "Fizz", "19", "Buzz",
        "Fizz", "22", "23", "Fizz", "Buzz", "26", "Fizz", "28", "29", "FizzBuzz"
    ]
