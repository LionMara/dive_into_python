#!/usr/bin/python3

'''
A primer to static methods

'''
class Supermkt():
    product = "Milk"

    def __init__(self, product, best_before):
        self.best_before = best_before
        self.product = product

    @staticmethod
    def normalize_product_name(product):
        product = product.capitalize().strip()
        return product

norm_product = Supermkt.normalize_product_name("milk ")
print(norm_product)
obj = Supermkt("Bread", "2022-05-18")
print(obj.normalize_product_name("milch "))
