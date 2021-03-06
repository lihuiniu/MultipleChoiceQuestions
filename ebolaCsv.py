# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 01:28:08 2016

@author: Whale
"""

import matplotlib.pyplot as plt
import csv
import operator
import datetime as dt
with open('/Users/kvenkatr/python/ebola.csv', 'rt') as f:
    filtereddata = [row for row in csv.reader(f) if row[3] != "0.0" and
    row[3] != "0" and "deaths" in row[0]]
sorteddata = sorted(filtereddata, key=operator.itemgetter(1))
guineadata = [row for row in sorteddata if row[1] == "Guinea" and
              row[0] == "Cumulative number of confirmed Ebola deaths"]
sierradata = [row for row in sorteddata if row[1] == "Sierra Leone"
and
    row[0] == "Cumulative number of confirmed Ebola deaths"]
liberiadata = [row for row in sorteddata if row[1] == "Liberia" and
               row[0] == "Cumulative number of confirmed Ebola deaths"]
g_x = [dt.datetime.strptime(row[2], '%Y-%m-%d').date() for
       row in guineadata]
g_y = [row[3] for row in guineadata]

s_x = [dt.datetime.strptime(row[2], '%Y-%m-%d').date() for
       row in sierradata]
s_y = [row[3] for row in sierradata]
l_x = [dt.datetime.strptime(row[2], '%Y-%m-%d').date() for
       row in liberiadata]
l_y = [row[3] for row in liberiadata]
plt.figure(figsize=(10,10))
plt.plot(g_x,g_y, color='red', linewidth=2, label="Guinea")
plt.plot(s_x,s_y, color='orange', linewidth=2, label="Sierra Leone")
plt.plot(l_x,l_y, color='blue', linewidth=2, label="Liberia")
plt.xlabel('Date', fontsize=18)
plt.ylabel('Number of Ebola Deaths', fontsize=18)
plt.title("Confirmed Ebola Deaths", fontsize=20)
plt.legend(loc=2)
plt.show()