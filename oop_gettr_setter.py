#!/usr/bin/python3

class Duck():
    def __init__(self, input_name):
        self.__input_name = input_name

    def get_name(self):
        print("Inside the getter")
        return self.__input_name

    def set_name(self, input_name):
        print("Inside the setter")
        self.__input_name = input_name

    name = property(get_name, set_name)


pet = Duck("Donald")
pet.name
pet.name = "Daff"
