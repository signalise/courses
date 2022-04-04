# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 13:45:53 2022

@author: andy
"""

class Stock:
    def __init__(self, code, price, quantity):
        self.code = code
        self._price = price
        self._quantity = quantity
        
    def __str__(self):
        return self.code + "," + str(self._price) + "," + str(self._quantity)
        
    def value(self):
        return self._price * self._quantity
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        self._price = value
    

stock = Stock("ANZ", 4.34, 100)

print(stock.price)

stock.price = 100

print(stock.value())

print(stock)