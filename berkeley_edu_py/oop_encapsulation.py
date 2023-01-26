#!/usr/bin/python3

'''
Encapsulation describes the idea of restricting
access to methods and attributes in a class.

In python this is achieved by using private methods
 or attributes using  single and double underscores

'''

#example
''' Class Sensor '''

class Sensor():
    def __init__(self, name, location):
        self.name = name
        self._location = location
        self.__version = '1.0'

    #a getter version
    def get_version(self):
        print(f'The sensor version is {self.__version}')

    #a setter function
    def set_version(self, version):
        self.__version = version


'''
ceating a sensor object
to show workings of private functions
'''

sensor1 = Sensor('Acc', 'Berkeley')
print(sensor1.name)
print(sensor1._location)

#sensor1.get_version()
sensor1.set_version('1.1')
sensor1.get_version()
