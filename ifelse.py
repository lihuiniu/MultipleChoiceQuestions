# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 12:32:31 2016

@author: Whale
"""

usersAnswer = input('What is 6 + 3? ') # Get the user's answer
usersAnswer = int(usersAnswer) # convert to an integer
if usersAnswer == 9:
    print ('Yessiree Bob')
    print ('You are a genius')
else:
    print ('Sorry, that is not correct')
    print ('The correct answer was 9')
    
    
COST_PER_WIDGET = 7.49 # Constant price of one widget
nWidgets = input('How many widgets do you want to buy? ')
nWidgets = int(nWidgets) # convert to an integer
if nWidgets == 1:
    print ('One widget will cost you $', COST_PER_WIDGET)
else:
    cost = nWidgets * COST_PER_WIDGET
    print (nWidgets, 'widgets will cost you $', cost)
    
def createHeader(fullName, gender):
    if gender == 'm':
        title = 'Mr.'
    else:
        title = 'Ms.'
    header = 'Dear ' + title + ' ' + fullName + ',' # use concatenation
    return header
# A few test calls to the function
print (createHeader('Joe Smith', 'm'))
print (createHeader('Susan Jones', 'f'))
print (createHeader('Henry Jones', 'm'))


def createHeader(fullName, gender):
    if gender == 'm':
        title = 'Mr.'
    elif gender == 'f':
        title = 'Ms.'
    else: #not sure, could be male or female
        title = 'Mr. or Ms.'
    header = 'Dear ' + title + ' ' + fullName + ',' # use concatenation
    return header
print (createHeader('Joe Smith', 'm'))
print (createHeader('Susan Jones', 'f'))
print (createHeader('Henry Jones', 'm'))
print (createHeader('Chris Smith', '?')) # Not sure if this is male or female


#Convert a number score to a letter grade:
def letterGrade(score):
    if score >= 90:
        letter = 'A'
    elif score >= 80:
        letter = 'B'
    elif score >= 70:
        letter = 'C'
    elif score >= 60:
        letter = 'D'
    else:
        letter = 'F' #fall through or default case
    return letter
grade1 = letterGrade(75)
print (grade1)
grade2 = letterGrade(82)
print (grade2)
print (letterGrade(95)) #call and print in one statement




def isSquare(length, width):
    if length == width:
        itsASquare = True
    else:
        itsASquare = False
    return itsASquare
# Intermediate function that checks for a square and prints the result
def printSquare(aLength, aWidth):
    theResult = isSquare(aLength, aWidth)
    if theResult:
        print (aLength, 'and', aWidth, 'represent a square')
    else:
        print (aLength, 'and', aWidth, 'do not represent a square')
#Test cases
printSquare(5, 5)
printSquare(7.5, 8.5)
# Get user inputconvert to floats and call the function.
userLength = input('Enter a length: ')
userLength = float(userLength)
userWidth = input('Enter a width: ')
userWidth = float(userWidth)
printSquare(userLength, userWidth)