#!/usr/bin/python3

''' Class square '''

'''
The notion of encapsulation is dealt here
Encapsulation protects data from unwanted access.
In python this is accomplished by adding
access modifiers.
Access modifiers
-----------------------
One leading underscore(_protected)
Two leading underscores(__private)

private access modifier offers more encapsulation
'''

class Square():
    '''A class that creates a square'''
    def __init__(self):
        self.__height = 2
        self.__width = 2

    def set_side(self, new_side):
        self.__height = new_side
        self.__width= new_side

    def print_side(self):
        if (self.__height == self.__width):
            print("I'm a square")
        else:
            print('Not a square')


square = Square()
square._Square__height = 3
square.print_side()
