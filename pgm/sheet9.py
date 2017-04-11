#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 17:13:39 2017

@author: catherine
"""
import numpy as np
import itertools as iter

names = {'0':'Fuse', '1':'Drum', 
         '2':'Toner','3':'Paper',
         '4':'Roller', '5':'Burning',
         '6':'Quality','7':'Wrinkled',
         '8':'Mult. Pages', '9':'Paper Jams'}


dep = {'5':'0','6':'123',
                '7':'03','8':'34', '9':'04', '0':'957'}

table = np.array([[0,0,0,1,0,0,0,0,0,0,0,0,1,0,1],
                 [0,0,0,0,1,0,0,1,0,0,1,1,0,0,0],
                 [1,1,0,0,0,1,0,1,0,0,0,1,0,0,0],
                 [1,0,1,0,1,0,1,0,1,1,0,1,1,0,0],
                 [0,0,0,0,0,0,1,0,0,0,0,0,0,1,1],
                 [0,0,0,1,0,0,0,0,0,0,0,0,1,0,0],
                 [1,1,1,0,1,1,0,1,0,0,1,1,0,0,0],
                 [0,0,1,0,0,0,0,0,1,0,0,0,1,1,1],
                 [0,0,1,0,0,0,1,0,1,0,0,0,0,0,1],
                 [0,0,1,1,0,0,1,1,1,1,0,0,0,1,0]])

data = table.transpose()
num_ex = data.shape[0]

# fill prob with histograms
prob = {}

for var in names.keys():

    dic = {}
    
    nodes = var
    if var in dep.keys():
        nodes = var + dep[var]
    # get data table for sub graph
    cols_table = [table[int(n)] for n in nodes]
    rows_data = np.array(cols_table).transpose()
    
    # initialize all possible combinations to zero:
    for state in iter.product(['0','1'],repeat=len(nodes)): 
        dic[''.join(list(state))] = 0
    
    for d in rows_data:
        key = ''
        for i in d:
            key += str(i)
        if dic.has_key(key):
            dic[key] += 1./num_ex # normalize values in prob

        else: dic[key] = 1./num_ex # should not happen
    prob[var] = dic



# print tables
for var in prob.keys():
    wrt = 'P('+names[var] + '|'
    if var in dep.keys():
        wrt += ', '.join([names[de] for de in dep[var]])
    print(wrt + ')')
    for i in prob[var].keys():
        print str(i) + ' : ' + str(prob[var][i])
    print


