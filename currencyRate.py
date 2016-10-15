# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 00:53:53 2016

@author: Whale
"""

# Get conversion factors from one currency to another
# API documentation from: fixer.io
import urllib.request
import sys
currencyList = ["AUD","BGN","BRL","CAD","CHF","CNY","CZK","DKK","EUR","GBP","HKD","HRK",\
"HUF","IDR","ILS","INR","JPY","KRW","MXN","MYR","NOK","NZD","PHP","PLN",\
"RON","RUB","SEK","SGD","THB","TRY","USD","ZAR"]
DIGITS_AND_DECIMAL_POINT = '0123456789.'
###### Approach: view returned data as a string ######
def getInfo(currencyFrom, currencyTo):
    URL = 'http://api.fixer.io/latest?base=' + currencyFrom
    # Make the request and save the response as a string.
    req = urllib.request.Request(URL)
    response = urllib.request.urlopen(req)
    # print "Response from server is:", response
    # Do some simple math to figure out the start index of the substringToFind:
    substringPos = response.index(currencyTo)
    start = substringPos + 5 # 3 for the abbrev, 1 for the quote, 1 for the colon
    # Value ends at first non-digit or decimal point - find that index
    nChars = len(response)
    for charIndex in range(start, nChars):
        if response[charIndex] not in DIGITS_AND_DECIMAL_POINT:
            end = charIndex
            break
        
    # Use slice to get the value
    conversionFactor = response[start : end]
    conversionFactor = float(conversionFactor)
    return conversionFactor
    
print ('Welcome to my currency conversion factor program.')
print ("It will show today's conversion factor between any of the following currencies:")
print ()
abbrevString = ' '.join(currencyList) # use join to make one string from all our abbreviations
print (abbrevString)
while True:
    print ()
    while True:
        currencyFrom = input('Convert currency from? ')
        currencyFrom = currencyFrom.upper() # Force to upper case
        if currencyFrom == '':
            sys.exit()
        if currencyFrom in currencyList:
            break
        else:
            print ('Sorry', currencyFrom, 'is not in the list of currencies.')
    print ()
    while True:
        currencyTo = input('Convert currency to? ')
        currencyTo = currencyTo.upper() # Force to upper case
        if currencyTo == '':
            sys.exit()
        if currencyTo in currencyList:
            break
        else:
            print ('Sorry', currencyTo, 'is not in the list of currencies.')
    conversion = getInfo(currencyFrom, currencyTo)
    print ()
    print ('Conversion factor from:', currencyFrom, 'to:', currencyTo, 'is:', conversion)
    print ()
print ('Bye')