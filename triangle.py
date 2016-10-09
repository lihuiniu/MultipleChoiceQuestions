# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 11:52:45 2016

@author: Whale
"""

# Assumes that values passed in could be values representing strings
def calculateHypotenuse(side1, side2):
    side1= float(side1)
    side2 = float(side2)
    hypot = ((side1 ** 2) + (side2 ** 2)) ** 0.5
    return hypot
firstTriangleSide1 = input('Enter side 1: ')
firstTriangleSide2 = input('Enter side 2: ')
hypot1 = calculateHypotenuse(firstTriangleSide1, firstTriangleSide2) # call function to do calc
secondTriangeSide1 = input('Enter the first side: ')
secondTriangeSide2 = input('Enter second side: ')
hypot2 = calculateHypotenuse(secondTriangeSide1, secondTriangeSide2) # call function to do calc
print ('The hypotenuse of the first triangle is: ', hypot1)
print ('The hypotenuse of the second triangle is: ', hypot2)




TAX_RATE = .09 # 9 percent tax
COST_PER_SMALL_WIDGET = 5.00
COST_PER_LARGE_WIDGET = 8.00
def calculateCost(nSmallWidgets, nLargeWidgets):
    subTotal = (nSmallWidgets * COST_PER_SMALL_WIDGET) + (nLargeWidgets * COST_PER_LARGE_WIDGET)
    taxAmount = subTotal * TAX_RATE
    totalCost = subTotal + taxAmount
    return totalCost
total1 = calculateCost(4, 8) # 4 small and 8 large widgets
print ('Total for the first order is', total1)
total2 = calculateCost(12, 15)
print ('Total for the second order is', total2)


def myFunction():
    global someVariable # tell Python that you are using a global variable
    someVariable = someVariable + 1
someVariable = 20
myFunction()
print (someVariable)



def myFunction(aVariable):
    aVariable = aVariable + 1 # change a local (parameter) variable
    return aVariable # and return it
someVariable2 = 20
someVariable2 = myFunction(someVariable2) # pass in global, and re-assign the answer
print (someVariable2)