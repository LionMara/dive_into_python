#!/usr/bin/python3

'''
A class called people
it creates an object, it
also has a method to greet the person
'''

class People():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Greetings, "  + self.name)



person1 = People('Ironman', 35)
person1.greet()

person2 = People('Batman', 30)
person2.greet()
