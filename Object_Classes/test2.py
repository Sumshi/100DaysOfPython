#!/usr/bin/python3

class Person:
    count = 0  # global class variable

    def __init__(self, name, age):
        self.name = name
        self.age = age

        Person.count += 1  # increments the count
p1 = Person("Ayan", 23)
p2 = Person("john", 56)

print(Person.count)
