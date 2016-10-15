# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 00:45:40 2016

@author: Whale
"""
from numpy.random import randn
import matplotlib as mpl
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_palette("hls")
mpl.rc("figure", figsize=(10,6))
data = randn(250)
plt.title("KDE Demonstration using Seaborn and Matplotlib",
fontsize=20)
sns.distplot(data, color='#ff8000')