#!/usr/bin/python3
class Student:
    def __init__(self, name, id, age):
        self.name = name
        self.age = age
        self.id = id

# creates the object of the class Student
s1 = Student("John", 101, 23)

# prints the attribute name of the object s1, use getattr
print(getattr(s1, 'name'))

# reset the value of attribute age to 40
setattr(s1, "age", 23)

# prints the modified value of age
print(getattr(s1, 'age'))

# It returns true if the object contains the attribute

print(hasattr(s1, 'id'))
# deletes the attribute age
delattr(s1, 'age')

print(s1.age)  # must give error since age has been deleted
