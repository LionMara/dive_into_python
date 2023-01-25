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

'''
The concept of class attributes is introduced.
Class attributes are made to be used by all
class methods or instances created from the class.
And as such, they are instantiated outside all
class methods
'''
class Student():
    '''A class that creates object and prints name'''
    n_instances = 0

    def __init__(self, sid, name, gender):
        self.sid = sid
        self.name = name
        self.gender = gender
        self.type = 'learning'
        Student.n_instances += 1 # anytime a student object is created, this will increment

    def say_name(self):
        ''' prints name of student'''
        print("My name is " + self.name)

    def report(self, score):
        ''' gives the score of a student'''
        self.say_name()
        print("My id is: " + self.sid)
        print("My score is :" +str(score))

    def num_instances(self):
        print(f'We have {Student.n_instances} instance in total')


student_1 = Student('A1', 'Mary', 'Female')
student_1.num_instances()
student_1.report(70)

student_2 = Student('A2', 'James', 'Male')
student_2.num_instances()
student_2.report(76)
student_1.num_instances()
