#!/usr/bin/python3
def add(x, y):
    """Adds function"""
    return (x + y)

def subtract(x, y):
    """subtracts function"""
    return (x - y)

def multiply(x, y):
    """multiplies two numbers"""
    return (x * y)

def divide(x, y):
    """divides two numbers"""
    if y == 0:
        raise ValueError("cannot divide by 0")
    return (x / y)
