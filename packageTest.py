# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 00:47:13 2016

@author: Whale
"""

from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()
print (digits.data)
print (type(digits.data))

import networkx as nx
G=nx.Graph()
G.add_node(1)
print (type(G))


import nltk
nltk.download()