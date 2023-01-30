#!/usr/bin/python3

class Duck():
    def __init__(self, input_name):
        self.__input_name = input_name

    @property
    def name(self): # Getter
        print("Inside the getter")
        return self.__input_name

    @name.setter
    def name(self, input_name): # Setter
        print("Inside the setter")
        self.__input_name = input_name

    #name = property(get_name, set_name)


pet = Duck("Donald")
pet.name
pet.name = "Daff"
