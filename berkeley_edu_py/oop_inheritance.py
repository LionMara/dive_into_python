#!/usr/bin/python3

'''importing numpy'''
import numpy as np


'''
Inheritance allows us to define a class that inherits
all the methods and attributes from another class.

A child class inherits from a parent class or superclass

syntax: ClassName(superclass):

ClassNmae can access all attributes and methods
from superclass.

In this sense, a superclass is seen as general
a child class is seen to be specific.


'''

'''
EXAMPLE
=============

Define a class named SensoR
attributes: name, location, and record_date,
an attribute data as an empty dictionary to store data.
method add_data with t and data as input parameters to take in timestamp and data arrays. 
Within this method, assign t and data to the data attribute with ‘time’ and ‘data’ as the keys. 
Clear_data method to delete the data.
'''

class Sensor():
    '''Class that creates sensor'''

    def __init__(self, name, location, record_date):
        self.name = name
        self.location =location
        self.record_date = record_date
        self.data = {}

    def add_data(self, t, data):
        '''Adds data to dictionary created'''
        self.data['time'] = t
        self.data['data'] = data
        print(f'We have {len(data)} points saved')

    def clear_data(self):
        ''' Clears all data '''
        self.data = {}
        print('Data cleared')



''' Class Accelerometer that inherits from class Sensor '''

class Accelerometer(Sensor):
    def show_type(self):
        print("I'm an accelerometer")

#end class Accelerometer

''' Class UCBAcc created at berkeley '''

class UCBAcc(Accelerometer):
    '''Creates a sensor created by  berkeley'''

    def show_type(self):
        print(f'I am {self.name}, created at UC Berkeley')

# end class UCBAcc

''' Class NewSensor that inherits from Sensor '''

'''
class NewSensor(Sensor):
    def __init__(self, name, location, record_date, brand):
        self.name = name
        self.location = location
        self.record_date = record_date
        self.brand = brand
        self.data = {}
new_sensor = NewSensor('OK', 'SF', '2019-03-01', 'XYX')
print(new_sensor.brand)

** The above can also be written using the super keyword
'''
class NewSensor(Sensor):
    def __init__(self, name, location, record_date, brand):
        super().__init__(name, location, record_date)
        self.brand = brand

new_sensor = NewSensor('OK', 'SF', '2019-03-01', 'XYX')
print(new_sensor.brand)

''' creating a sensor object '''
'''
sensor1 = Sensor('sensor1', 'Berkeley', '2019-01-01')
data = np.random.randint(-10, 10, 10)
sensor1.add_data(np.arange(10), data)
print(sensor1.data)
'''


''' Creating object of class Accelerometer'''
'''
acc = Accelerometer('acc1', 'Oakland', '2019-02-01')
acc.show_type()
data = np.random.randint(-10, 10, 10)
acc.add_data(np.arange(10), data)
print(acc.data)
'''

''' Creating an object for UCBAcc '''
'''
acc_ucb = UCBAcc('UCBAcc', 'Berkeley', '2019-03-01')
acc_ucb.show_type()
'''
