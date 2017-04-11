import numpy as np

def findAncPath(A,n,nodes):
# returns list of nodes which can reach node n 
    for i in range(A.shape[1]):
        if i not in nodes and A[i,n] != 0:
            nodes.append(i)
            nodes = findPath(A,i,nodes)
    return nodes
    
def findPath(A,n,nodes):
    # returns list of nodes which can be reached from node n 
    for i in range(A.shape[1]):
        if i not in nodes and A[n,i] != 0:
            nodes.append(i)
            nodes = findPath(A,i,nodes)
    return nodes
    
    
def conditionallyIndependent(A,x,y,z):
    pass
    
def ancestor(A,X,Y,Z):
    keep = set(np.concatenate((X,Y,Z)))
    remove = []
    rowvec = []
    for i in range(A.shape[1]):
        if i not in remove:
            if len(set(findPath(A,i,[])) & keep) != 0:
                keep = keep | set(findPath(A,i,[])) 
                rowvec.append(True)
            else:
                print "haa"
                remove= np.concatenate((remove,findPath(A,i,[]) ))
                rowvec.append(False)
    print remove
    print rowvec
    
def moralize(A,X,Y,Z):
    pass
    
def seperateMat(A):
    pass

def condIndependent(adjaMat, X,Y,Z):
    # first: remove
    ancMat = ancestor(adjaMat,X,Y,Z)
    moralMat = moralize(ancMat,X,Y,Z)
    sepMat = seperateMat(moralMat,Z)
    
    # for all pairs xi,yi,zi test if xi and yi independent given zi
    for i in range(len(X)):
        if not conditionallyIndependent(adjaMat,X[i],Y[i],Z[i]): 
            return False
    return True
    
    
t = np.zeros((11,11))
t[0][2] = 1
t[1][3] = 1
t[2][4] = 1
t[3][5] = 1
t[4][6] = 1
t[5][6] = 1
t[5][7] = 1
t[6][8] = 1
t[7][9] = 1
t[9][6] = 1
                  
t = np.matrix(t)