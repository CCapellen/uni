#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 16:52:19 2016

@author: catherine
"""

phi1 = {1:0.05, 0:4.95}
phi31 = {00:4.95, 11:0.25, 10:0.05, 01:4.75}
phi52 = {00:3.5, 11:3.0, 10:1.5, 01:2.0}
phi843 = {0:5.0,1:0,10:0,11:0,111:5,101:5,110:5,100:0.}
phi2 = {1:2.5,0:2.5}
phi42 = {11:0.5,01:4.5,10:0.05,00:4.95}
phi68 = {11:4.9,01:0.1,10:0.25,00:4.75}
phi758 = {111:4.5,101:3.5,110:4.0,100:0.5,11:0.5,1:1.5,10:1.0,0:4.5}

dependencies = {1:0,3:1,2:0,5:2,8:43,4:2,6:8,7:58}
nodes = {1:phi1,2:phi2,3:phi31,4:phi42,5:phi52,6:phi68,7:phi758,
         8:phi843}

         

def term(a,b,c,d,e,f,g,h):
    return phi1[a]*phi31[10*c+a]*phi52[10*e+b]*phi843[100*h+10*d+c]*phi2[b]*phi42[10*d+b]*phi68[10*f+h]*phi758[100*g+10*e+h]

def brute_force(x): 
    result0 = 0
    result1 = 0
    for a in [0,1]:
        for b in [0,1]:
            for c in [0,1]:
                for d in [0,1]:
                    for e in [0,1]: 
                        for f in [0,1]:
                            for g in [0,1]:
                                for h in [0,1]:
                                    if [a,b,c,d,e,f,g,h][x-1] == 0:
                                        result0 += term(a,b,c,d,e,f,g,h)
                                    else:
                                        result1 += term(a,b,c,d,e,f,g,h)
    return result0, result1
    
print "brute force"    
z = brute_force(1)[0] + brute_force(1)[1]
for i in range(1,9):
    result = brute_force(i)
    print i, result
    print "normalized:", result[0]/z, result[1]/z

print "z", z
    
    
    
def Z(i):
    return marginal_probability(i)[0] + marginal_probability(i)[1]
         
"""    
def marginal_probability(x):
    if dependencies[x]==0:
        return nodes[x]
    else:
        d=dependencies[x]
        if d > 10:
            a = marginal_probability(int(str(d)[0]))
            b = marginal_probability(int(str(d)[1]))
            return{1:nodes[x][111]*a[1]*b[1]+nodes[x][101]*a[0]*b[1] +
                   nodes[x][110]*a[1]*b[0] + nodes[x][100]*a[0]*b[0],
                  0:nodes[x][011]*a[1]*b[1]+nodes[x][001]*a[0]*b[1] +
                   nodes[x][010]*a[1]*b[0] + nodes[x][000]*a[0]*b[0]}
        else:
            a = marginal_probability(d)
            return {1:nodes[x][11]*a[1] + nodes[x][10]*a[0],
                    0:nodes[x][01]*a[1] + nodes[x][00]*a[0]}
#z = Z()   

for i in range(1,9):
    print i, marginal_probability(i)
    print marginal_probability(i)[0]/Z(i), marginal_probability(i)[1]/Z(i)

# shortcomings are that it needs a lot of storage and a lot of time


term = [(i,dependencies[i]) for i in range(1,9)]
"""
"""
def variable_elimination(term, order):
    for x in order:
        eliminate(term, x)
    
#def eliminate(term,x):
"""    
        

