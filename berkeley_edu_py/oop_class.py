#!/usr/bin/python3

'''
A class was defined as a blueprint.
It is a definiton of the structure that we want.
The syntax of a class is as below:

=============================================
class ClassName(superclass):
    def __init__(self, args):
        #define or assign object attributes

    def other_methods(self, args):
        #body of the method
=============================================
__init__ method is a special method in python.
The two underscores both at end and beginning
show the importance of the method.
It is used to assign initial values to the object

'''

'''
Example:
 Define a class named Student,
with the attributes sid (student id), name, gender,
type in the init method
and a method called say_name to print out the student’s name.
All the attributes will be passed in except type,
which will have a value as ‘learning’.

'''
class Student():
    '''A class that creates object and prints name'''

    def __init__(self, sid, name, gender):
        self.sid = sid
        self.name = name
        self.gender = gender
        self.type = 'learning'

    def say_name(self):
        ''' prints name of student'''
        print("My name is " + self.name)

    def report(self, score):
        self.say_name()
        print("My id is: " + self.sid)
        print("My score is :" +str(score))


student_1 = Student('A1', 'Mary', 'Female')
student_1.report(70)
