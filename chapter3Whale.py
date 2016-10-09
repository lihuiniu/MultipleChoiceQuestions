# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 10:12:24 2016

@author: Whale
"""



# Simple addition program
value1 = input('Please enter a number: ')
value1 = int(value1)
value2 = input('Please enter another number: ')
value2 = int(value2)
total = value1 + value2
print ('The sum of', value1, 'and', value2, 'is', total)


# Simple cash register
cost = input('Please enter the cost of the item: ')
cost = float(cost)
cash = input('Please enter the cash given: ')
cash = float(cash)
change = cash - cost
print ('Your item costs', cost, 'and you gave me', cash, 'dollars. Your change is', change)