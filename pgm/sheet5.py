#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 00:36:13 2016

@author: catherine
"""

class node:
    def __init__(self,name,parent,children):
        self.name = name
        self.parent = parent
        self.children = children
    
edges = {"X1X2":[0.5,0.1,0.3,0.7],
         "X1X3":[0.2,0.2,0.1,0.7],
         "X1X4":[0.3,0.3,0.3,0.3],
         "X2X5":[0.8,0.5,0.4,0.8],
         "X2X6":[1.0,0.5,0.5,0.9],
         "X3X7":[0.5,0.1,0.3,0.1],
         "X3X8":[0.1,0.1,0.4,0.1],
         "X3X9":[0.7,0.1,0.7,0.2],
         "X4X10":[0.5,0.5,0.8,0.3],
         "X5X11":[0.5,0.6,0.8,0.1],
         "X7X12":[0.9,0.9,0.9,0.4],
         "X10X13":[0.9,0.5,0.1,0.5],
         "X10X14":[0.3,0.1,0.2,0.5]}


X1 = node("X1","",["X2","X3","X4"])
X2 = node("X2","X1",["X5","X6"])
X3 = node("X3","X1",["X7","X8","X9"])
X4 = node("X4","X1",["X10"])
X5 = node("X5","X2",["X11"])
X6 = node("X6", "X2",[])
X7 = node("X7","X3",["X12"])
X8 = node("X8","X3",[])
X9 = node("X9","X3",[])
X10 = node("X10","X4",["X13","X14"])
X11 = node("X11","X5",[])
X12 = node("X12","X7",[])
X13 = node("X13","X10",[])
X14 = node("X14","X10",[])

nodes = {}
for n in [X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,X13,X14]:
    nodes[n.name] = n

leafs = ["X11","X6","X12","X8","X9","X13","X14"]
thirdlayer = ["X5","X7","X10"]
secondlayer = ["X2","X3","X4"]


messages = {}

def upwardPass():
    for n in leafs:
        vals = edges[nodes[n].parent + n]
        mT = vals[0] + vals[2]
        mF = vals[1] + vals[3]
        messages[n] = (mF,mT)
    for n in thirdlayer:
        mN = [0,0]
        for c in nodes[n].children:
            multF = messages[c][0]
            multT = messages[c][1]
            margF = edges[n+c][1]*multT + edges[n+c][3]*multF#  n = F
            margT = edges[n+c][0]*multF + edges[n+c][2]*multF # n=T
            messages[n+c] = (margF,margT)
            mN[0]+= margF
            mN[1]+= margT
        messages[n]=mN
    for n in secondlayer:
        mN = [0,0]
        for c in nodes[n].children:
            multF = messages[c][0]
            multT = messages[c][1]
            margF = edges[n+c][1]*multT + edges[n+c][3]*multF#  n = F
            margT = edges[n+c][0]*multF + edges[n+c][2]*multF # n=T
            messages[n+c] = (margF,margT)
            mN[0]+= margF
            mN[1]+= margT
        messages[n]=mN
    for n in ["X1"]:
        mN = [0,0]
        for c in nodes[n].children:
            multF = messages[c][0]
            multT = messages[c][1]
            margF = edges[n+c][1]*multT + edges[n+c][3]*multF#  n = F
            margT = edges[n+c][0]*multF + edges[n+c][2]*multF # n=T
            messages[n+c] = (margF,margT)
            mN[0]+= margF
            mN[1]+= margT
        messages[n]=mN
upwardPass()    
#print messages  
    
messagesD = {}


def downwardPass():
     for n in ["X1"]:
        vals = messages["X1"]
        messagesD[n] = vals
     for n in secondlayer:
         mN = [0,0]
         c = nodes[n].parent
         multF = messagesD[c][0]
         multT = messagesD[c][1]
         margF = edges[c+n][1]*multT + edges[c+n][3]*multF#  n = F
         margT = edges[c+n][0]*multF + edges[c+n][2]*multF # n=T
         messagesD[n+c] = (margF,margT)
         mN[0]+= margF
         mN[1]+= margT
         messagesD[n]=mN
     for n in thirdlayer:
         mN = [0,0]
         c = nodes[n].parent
         multF = messagesD[c][0]
         multT = messagesD[c][1]
         margF = edges[c+n][1]*multT + edges[c+n][3]*multF#  n = F
         margT = edges[c+n][0]*multF + edges[c+n][2]*multF # n=T
         messagesD[n+c] = (margF,margT)
         mN[0]+= margF
         mN[1]+= margT
         messagesD[n]=mN
     for n in leafs:
         mN = [0,0]
         c = nodes[n].parent
         multF = messagesD[c][0]
         multT = messagesD[c][1]
         margF = edges[c+n][1]*multT + edges[c+n][3]*multF#  n = F
         margT = edges[c+n][0]*multF + edges[c+n][2]*multF # n=T
         messagesD[n+c] = (margF,margT)
         mN[0]+= margF
         mN[1]+= margT
         messagesD[n]=mN

downwardPass()
#print messagesD
probs = {}

def calculateAllProbs():
    
    #n = "X11"
    #z = sum([(messages[n][0] + messagesD[n][0]), (messages[n][1] + messagesD[n][1])])
      
    
    z=0
    
    for e in edges.values():
        z += sum(e)#[messages[n][0] + messagesD[n][0], messages[n][1] + messagesD[n][1]])
    print z
    for n in nodes.keys():
        probs[n] = ((1./z)*(messages[n][0] + messagesD[n][0]), (1./z)*(messages[n][1] + messagesD[n][1]))
      
        
calculateAllProbs()
print probs
        
#