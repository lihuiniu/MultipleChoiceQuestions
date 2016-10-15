# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 01:41:22 2016

@author: Whale
"""

import csv
import matplotlib.pyplot as plt
# csv has Name, Year, Age, Cmp, Att, Yds, TD, Teams

#ways to call DictReader
# if fieldnames are Name, Year, Age, Cmp, Att, Yds, TD, Teams
# fieldNames = ['Name', 'Year', 'Age', 'Cmp', 'Att', 'Yds', 'TD','Teams']
# reader = csv.DictReader('qb_data.csv', fieldNames)
# If csv file has first row as Name, Year, Cmp, Att, Yds, TD, Teams
# we don't need to define fieldnames, the reader automatically recognizes
# them.

# num(s) and getcolors() functions
def num(s):
    try:
        return int(s)
    except ValueError:
        return 0
        
def getcolors():
    colors = [(31, 119, 180), (255,0,0), (0,255,0), (148, 103, 189),\
(140, 86, 75), (218, 73, 174), (127, 127, 127), (140,140,26), (23,\
190, 207), (65,200,100), (200, 65,100), (125,255,32), (32,32,198),\
(255,191,201), (172,191,201), (0,128,0), (244,130,150), (255,\
127, 14), (128,128,0), (10,10,10), (44, 160, 44), (214, 39, 40),\
(206,206,216)]
    for i in range(len(colors)):
        r, g, b = colors[i]
        colors[i] = (r / 255. , g / 255. , b / 255.)
    return colors
    
def getQbNames():
    qbnames = ['Peyton Manning']
    name=''
    i=0
    with open('qb_data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if ( row['Name'] != name and qbnames[i] != row['Name']):
                qbnames.append(row['Name'])
                i = i+1
    return qbnames
    
def readQbdata():
    resultdata = []
    with open('qb_data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        resultdata = [row for row in reader]

    return resultdata

fdata=[]
prevysum=0
# -- functions End --
qbnames = getQbNames()
fdata = readQbdata()
i=0
rank=0
prevysum=0
lastyr=0
highrank=244
colorsdata = getcolors()
fig = plt.figure(figsize=(15,13))
ax=fig.add_subplot(111,axisbg='white')
# limits for TD
plt.ylim(10, 744)
plt.xlim(1940, 2021)
colindex=0
lastage=20

for qbn in qbnames:
    x=[]
    y=[]
    prevysum=0
    for row in fdata:
        if ( row['Name'] == qbn and row['Year'] != 'Career'):
            yrval = num(row['Year'])
            lastage = num(row['Age'])
            prevysum += num(row['TD'])
            lastyr = yrval
            x += [yrval]
            y += [prevysum]
    if ( rank > highrank):
        plt.plot(x,y, color=colorsdata[colindex], label=qbn,linewidth=2.5)
        plt.legend(loc=0, prop={'size':10})

        colindex = (colindex+1)%22
        plt.text(lastyr-1, prevysum+2, qbn+"("+str(prevysum)+"):"+str(lastage), fontsize=9)
    else:
        plt.plot(x,y, color=colorsdata[22], linewidth=1.5)
        rank = rank +1
        
plt.xlabel('Year', fontsize=18)
plt.ylabel('Cumulative Touch Downs', fontsize=18)
plt.title("Cumulative Touch Downs by Quarter Backs", fontsize=20)
plt.show()