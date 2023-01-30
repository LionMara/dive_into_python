#!/usr/bin/python3

'''
A dive into class methods and why
'''

class Supermkt():
    produce = "Milk"

    def __init__(self,product, best_before):
        self.best_before = best_before
        self.product = product

    @classmethod
    def get_product(cls):
        print("produce= " + cls.produce)


Supermkt.get_product()
obj = Supermkt('Bread', "2023-01-30")
obj.get_product()
