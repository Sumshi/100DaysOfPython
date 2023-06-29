#!/usr/bin/python3
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print("ID: %d \nName: %s" % (self.id, self.name))

e1 = Employee("Tek", 101)
e2 = Employee("Tom", 102)

e1.display()
e2.display()
