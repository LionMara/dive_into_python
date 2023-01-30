#!/usr/bin/python3

'''import random '''
import random

'''
class about coin being tossed
'''

class Coin():
    def __init__(self):
        self.sideup = "Heads"

    def toss(self):
        if(random.randint(0, 1) == 0):
            self.sideup = "Heads"
        else:
            self.sideup = "Tails"

    def get_sideup(self):
        return self.sideup


my_coin = Coin()
my_coin.toss()
print("This side up: ", my_coin.get_sideup())
