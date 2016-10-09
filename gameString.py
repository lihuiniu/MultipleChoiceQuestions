# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 20:39:00 2016

@author: Whale
"""

# Saving lots of data
import random
from FileReadWrite import * # means import everything as though it were typed here

DATA_FILE_PATH = 'AddingGameData.txt'
# Main program starts here
if not fileExists(DATA_FILE_PATH):
    userName = input('You must be new here, please enter your name: ')
    score = 0
    nProblems = 0
    nCorrect = 0
    print ('To quit the game, press RETURN/ENTER and your info will be saved')
    print ('OK', userName, "let's get started ...")
    print ()
else:
    savedDataString = readFile(DATA_FILE_PATH) #read the whole file into a variable
    savedDataList = savedDataString.split(',') # turn that into a list
    userName = savedDataList[0]
    score = savedDataList[1]
    score = int(score)
    nProblems = savedDataList[2]
    nProblems = int(nProblems)
    nCorrect = int(savedDataList[3]) # can do both in a combined step

    print ('Welcome back', userName, 'nice to see you again! ')
    print ('Your current score is: ', score)
    print ()
    
# Main loop
while True:
    firstNumber = random.randrange(0, 11)
    secondNumber = random.randrange(0, 11)
    correctAnswer = firstNumber + secondNumber
    question = 'What is: ' + str(firstNumber) + ' + ' + str(secondNumber) + '? '
    userAnswer = input(question)
    if userAnswer == '':
        break
    userAnswer = int(userAnswer)
    nProblems = nProblems + 1
    if userAnswer == correctAnswer:
        print ('Yes, you got it!')
        score = score + 2
        nCorrect = nCorrect + 1
    else:
        print ('No, sorry, the correct answer was: ', correctAnswer)
        score = score - 1
    print ('Your current score is: ', score)
    print ()
print ('Thanks for playing')
print ()
print ('You have tried', nProblems, 'problems and you have correctly answered', nCorrect)

# Make a list of the useruserName, userScore, nProblems, nCorrect then
# create a string from that using join
dataList = [userName, str(score), str(nProblems), str(nCorrect)]
outputText = ','.join(dataList)
writeFile(DATA_FILE_PATH, outputText)




# Write multiple lines of text to a file

DATA_FILE_PATH2 = 'MultiLineData.txt'
myFileHandle2 = openFileForWriting(DATA_FILE_PATH2)
data1 = 'Here is some data as a string'
writeALine(myFileHandle2, data1)
data2 = 'Here is a second line of string data'
writeALine(myFileHandle2, data2)
# Could have some code join several pieces of data into a single string
data3 = '123,Joe Schmoe,123.45,0'
writeALine(myFileHandle2, data3)
closeFile(myFileHandle2)


myFileHandle3 = openFileForWriting(DATA_FILE_PATH2)
data11 = readALine(myFileHandle3)
print (data11)
data21 = readALine(myFileHandle3)
print (data21)
data31 = readALine(myFileHandle3)
print (data31)
# Could add code to split data3 into several different pieces of data
closeFile(myFileHandle3)