
# By Hosam Alqaderi and Catherine Capellen


def TgivenRS(t,r,s):
    if t==1:
        if r==1:
            return 1 
        else:
            return 0.9 if s==1 else 0
    else:
        return 1 - TgivenRS(1,r,s)
    
def JgivenR(j,r):
    if r+j==2: 
        return 1 
    if (j==1 and r == 0):
        return 0.2
    if (j+r==0) :
        return 0.8
    else:
        return 0
        
        
def R(r):
    return 0.2 if r else 0.8

def S(s):
    return 0.1 if s else 0.9
    
def ST(s,t):
    return sum([TgivenRS(t,r,s)*JgivenR(j,r)*R(r)*S(s) for r in [0,1] for j in [0,1]])
     
    
def probTableST():
    s1t1 =  ST(1,1)
    s0t1 = ST(0,1)
    s1t0 = ST(1,0)
    s0t0 = ST(0,0)
    
    print "p(S=0,T=0)=",s0t0 , "p(S=0,T=1)=",s0t1, "\np(S=1,T=0)=",s1t0, "p(S=1,T=1)=",s1t1
   
def T(t):
    return  sum([TgivenRS(t,r,s)*JgivenR(j,r)*R(r)*S(s) for r in [0,1] for j in [0,1] for s in [0,1] ])   

def SgivenT(s,t):
    return ST(s,t)/T(t)
    
def probTableSgivenT():
    #print "P(S=0|T=0) = ", SgivenT(0,0), "P(S=0|T=1) = ", SgivenT(0,1)
    print "P(S=1|T=0) = ", SgivenT(1,0), "P(S=1|T=1) = ", SgivenT(1,1)
    

def STJ(s,t,j):
     return sum([TgivenRS(t,r,s)*JgivenR(j,r)*R(r)*S(s) for r in [0,1]])   

def TJ(t,j):
     return sum([TgivenRS(t,r,s)*JgivenR(j,r)*R(r)*S(s) for r in [0,1] for s in [0,1] ])   
    
def SgivenTJ(s,t,j):
    return STJ(s,t,j)/TJ(t,j)
    
def probTableSgivenTJ():
    for s in [1]:
        for t in [0,1]:
            for j in [0,1]:
                print "p(S=",s,"|T=",t,"J=",j,") = ", SgivenTJ(s,t,j)
    
    
                
probTableST()
print "\n"
probTableSgivenT()
print "\n"
probTableSgivenTJ()
