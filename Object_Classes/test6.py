#!/usr/bin/python3

class Student:
    """initializes class attributes"""
    def __init__(self, name, id, age):
        self.name = name
        self.age = age
        self.id = id

    def display_details(self):
        print("Name:%s, ID:%d, age:%d"%(self.name,self.id))

s = Student("John", 101, 33)
print(s.__doc__)
print(s.__dict__)
print(s.__module__)
