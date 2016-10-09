# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 11:08:46 2016

@author: Whale
"""
def separateRuns():
    print ('******************')
    print #blank line
    
def getGroceries(item1): # uses one parameter variable
    print (item1) # prints the contents of the item1 variable
    print ('flour')
    print ('sugar')
    print ('squash')
    separateRuns()
    
def getGroceries4(item1, item2, item3, item4):
    print (item1)
    print (item2)
    print (item3)
    print (item4)
    separateRuns()
    
    
def addTwo(startingValue):
    endingValue = startingValue + 2
    print ('The sum of', startingValue, 'and 2 is:', endingValue)

# Call the function twice with different arguments
addTwo(5)
addTwo(10)

# Main code starts here:
getGroceries('eggs')
getGroceries('beer')
getGroceries('apples')

# Now call the function with four arguments
getGroceries4('eggs', 'soap', 'lettuce', 'cat food')
getGroceries4('beer', 'milk', 'soda', 'peas')



def calculateAverage(param1, param2, param3, param4):
    total = param1 + param2 + param3 + param4
    # Divide by a floating point value to ensure we get the proper potentially fractional answer
    average = total / 4.0
    print ('Average value is:', average)
    
calculateAverage(2, 3, 4, 5)
calculateAverage(-3, 5.2, 15, 1000.8)
calculateAverage(1.4, -2.5, 14.3, 200.5)




def calculateAverage4(param1, param2, param3, param4):
    total = param1 + param2 + param3 + param4
    average = total / 4.0
    return average # hand the answer back to the caller
average1 = calculateAverage4(2, 3, 4, 5)
average2 = calculateAverage4(-3, 5.2, 15,1000.8)
average3 = calculateAverage4(1.4, -2.5, 14.3, 200.5)
print ('The three averages are:', average1, average2, average3)



def square(number):
    answer = number * number
    return # Note: this is an error, does not return an answer
# userNumber = input('Enter a number: ')
userNumber = float(userNumber) # convert to a float
numberSquared = square(userNumber) # call the function and save the result
print ('The square of your number is', numberSquared)


def calculateAverageYard(param1, param2, param3, param4):
    total = param1 + param2 + param3 + param4
    average = total / 4.0 #floating point divide
    return average
yardsOnRun1 = 4
yardsOnRun2 = 6.5
yardsOnRun3 = 2.5
yardsOnRun4 = -2
averageYardsPerRun = calculateAverageYard(yardsOnRun1, yardsOnRun2, yardsOnRun3, yardsOnRun4)
print ('Average yards per run is:', averageYardsPerRun)


yardsOnPass1 = 0
yardsOnPass2 = 25.5
yardsOnPass3 = 0
yardsOnPass4 = 12
averageYardsPerPass = calculateAverageYard(yardsOnPass1, yardsOnPass2, yardsOnPass3,
yardsOnPass4)
print ('Average yards per pass is:', averageYardsPerPass)


def F2C(nDegreesF):
    nDegreesF = (nDegreesF - 32) * 0.5556
    return nDegreesF
def C2F(nDegreesC):
    nDegreesF = (1.8 * nDegreesC) + 32
    return nDegreesF
    
# Code to ask the user to input values for conversion:
usersTempF = input('Enter a value of degrees Fahrenheit: ')
usersTempF = float(usersTempF)
convertedTempC = F2C(usersTempF)
print (usersTempF, 'degrees Fahrenheit is:', convertedTempC, 'degrees Centigrade.')

usersTempC = input('Enter a value of degrees Celsius: ')
usersTempC = float(usersTempC)
convertedTempF = C2F(usersTempC)
print (usersTempC, 'degrees Centigrade is:', convertedTempF, 'degrees Fahrenheit.')


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