#!/usr/bin/python3
class Student:
    count = 0  # global class variable
    def __init__(self):
        Student.count += 1
s1=Student()
s2=Student()    
s3=Student()    
print("The number of students:",Student.count)
