#!/usr/bin/python3

'''Trouble'''

class Square():
    def __init__(self):
        self.__height = 2
        self.__width = 2

    def set_side(self, new_side):
        self.__height = new_side
        self.__width = new_side

    def get_height(self):
        return self.__height

    def set_height(self, h):
        if h >= 0:
            self.__height = h
        else:
            raise Exception("Value needs to be 0 or larger")

square = Square()
square.__height = 3
