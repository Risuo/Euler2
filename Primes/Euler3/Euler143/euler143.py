from math import hypot
from math import sin
from math import tan
from math import cos
from math import degrees
from math import radians
from math import acos
from math import sqrt
from math import pi
from decimal import Decimal
from decimal import *


#AD = b
#AB = c
#BD = a

#Solve for AC, where C is the point of an equilateral triangle congruent with line BD


#a = 399
#b = 455
#c = 511


#pqrSum = a**2 + c**2-2*a*c*(cos(radians(60)+(B)))

table = set()

def fermatPoint(x):
    return (sin(x+((pi))/((3)))**-1)

def trilinear(a,b,c,table):
    #print a,b,c
    value = under119(a,b,c)
    if value != 0:
        if value:
            A = acos(float(b**2+c**2-a**2)/float(2*b*c))
            B = acos(float(c**2+a**2-b**2)/float(2*c*a))
            C = acos(float(a**2+b**2-c**2)/float(2*a*b))
            #print degrees(A), degrees(B), degrees(C), 'these are the internal angles of the only 1-600 valid triangle'
        else:
            return "Stop"
    elif value == 0:
        #print 'stopped here'
        return "Stop"
    alpha= fermatPoint(A) 
    beta = fermatPoint(B) 
    gamma = fermatPoint(C)
    #print alpha, beta, gamma, 'these are the distance ratios to the perpendicular opposite side for the fermat point, to a, b, and c'
    p = float(a+b+c)/float(2)
    s = sqrt(p*(p-a)*(p-b)*(p-c))
    alphaT = (2*alpha*s)/((a*alpha)+(b*beta)+(c*gamma))
    betaT = (2*beta*s)/((a*alpha)+(b*beta)+(c*gamma))
    gammaT = (2*gamma*s)/((a*alpha)+(b*beta)+(c*gamma))
    first = float(2*s)/float(a)
    second = float(2*s)/float(b)
    third = float(2*s)/float(c)
    triA = [first, 0, 0]
    triB = [0, second, 0]
    triC = [0, 0, third]
    
    def isInt(x):
        if x**2 == int(x)*int(x):
            return True
        else:
            return False
    
    def r(triA, alphaT, betaT, gammaT, a, b, c):
        a2 = float(alphaT)
        a1 = float(triA[0])
        b2 = float(betaT)
        b1 = float(triA[1])
        c2 = float(gammaT)
        c1 = float(triA[2])
        A = float(a*2)
        B = float(b*2)
        C = float(c*2)
        first = ((a1-a2)**2)*float(sin(A))+((b1-b2)**2)*float(sin(B))+((c1-c2)**2)*float(sin(C))
        second = 2*sin(a)*sin(b)*sin(c)
        third = abs(float(first)/float(second))
        getcontext().prec = 10
        d = Decimal(third).sqrt()
        return d
    rA = r(triA, alphaT, betaT, gammaT, A, B, C)
    rB = r(triB, alphaT, betaT, gammaT, A, B, C)
    rC = r(triC, alphaT, betaT, gammaT, A, B, C)
    if isInt(rA) and isInt(rB) and isInt(rC):
        #print rA, rB, rC, 'and finally, these are the actual distances from the vertexes A,B,C, to the fermat point'
        t = [rA, rB, rC]
        t = sorted(t)
        print t
        table.add(str(t))
    return table


def under119(a,b,c):
    if a+b <= c:
        return False
    if a+c <= b:
        return False
    if b+c <= a:
        return False
    A = acos(float(b**2+c**2-a**2)/float(2*b*c))
    B = acos(float(c**2+a**2-b**2)/float(2*c*a))
    C = acos(float(a**2+b**2-c**2)/float(2*a*b))
    if A >= 120 or B >= 120 or C >= 120:
        return 0
    else:
        return True

count = 0

for a in range(1,600):
    print a, count
    for b in range(a,600):
        for c in range(b,600):
            output = trilinear(a,b,c,table)
            if output != "Stop":
                count += 1
            if output == "Stop":
                break


#print table

trilinear(399,455,511,table)