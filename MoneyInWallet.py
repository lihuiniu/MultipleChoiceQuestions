# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 01:47:27 2016

@author: Whale
"""

numberOfOneDollarBills = 3
numberOFiveDollarBills = 2
total = numberOfOneDollarBills + (numberOFiveDollarBills * 5)
print ('Total amount is:', total)

rate = 10.00
totalHours = 45
regularHours = 40
overTimeHours = totalHours - regularHours
pay = (rate * regularHours) + ((rate * 1.5) * overTimeHours)
print ('For working', totalHours, 'hours, I should be paid', pay)


side1 = 3
side2 = 4
hypot = ((side1 ** 2) + (side2 ** 2)) ** 0.5
print ('Side 1 is', side1, ' Side 2 is', side2, ' Hypotenuse is:', hypot)


nOneDollarBills = 3
nFiveDollarBills = 2
total = nOneDollarBills + (nFiveDollarBills * 5)
print ('Total amount is', total)


nTwentyDollarBills = 5
nTenDollarBills = 4
nFiveDollarBills = 8
nOneDollarBills = 2
total = (nTwentyDollarBills * 20) + (nTenDollarBills * 10) + \
(nFiveDollarBills * 5) + nOneDollarBills
print ('Total amount is', total)