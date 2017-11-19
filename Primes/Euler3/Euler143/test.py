from math import hypot
from math import sin
from math import tan
from math import cos
from math import degrees
from math import radians
from math import acos
from math import sqrt
from decimal import Decimal
from math import pi as pi

#AD = b
#AB = c
#BD = a

#Solve for AC, where C is the point of an equilateral triangle congruent with line BD




a = 399
b = 455
c = 511

A = acos(Decimal(b**2+c**2-a**2)/Decimal(2*b*c))
B = acos(Decimal(c**2+a**2-b**2)/Decimal(2*c*a))
C = acos(Decimal(a**2+b**2-c**2)/Decimal(2*a*b))

pqrSum = a**2 + c**2-2*a*c*(cos(radians(60)+(B)))

def isInt(p):
    if int(sqrt(p))*int(sqrt(p)) == p:
        return sqrt(p), "True"
    else:
        return False



def csc(x):
    return (sin(x+((pi))/((3)))**-1)


alpha= csc(A) 
beta = csc(B) 
gamma = csc(C)

def sssTriArea(a,b,c):
    p = Decimal(a+b+c)/Decimal(2)
    S = sqrt(p*(p-a)*(p-b)*(p-c))
    return S

s = sssTriArea(a, b, c)

#these are the perpendicular distances from side a to T, b to T, and c to T
#aka: 
alphaT = (2*alpha*s)/((a*alpha)+(b*beta)+(c*gamma))
betaT = (2*beta*s)/((a*alpha)+(b*beta)+(c*gamma))
gammaT = (2*gamma*s)/((a*alpha)+(b*beta)+(c*gamma))

print alphaT, betaT, gammaT, isInt(pqrSum)


first = Decimal(2*s)/Decimal(a)
second = Decimal(2*s)/Decimal(b)
third = Decimal(2*s)/Decimal(c)

triA = [first, 0, 0]
triB = [0, second, 0]
triC = [0, 0, third]

def p(triA, alphaT, betaT, gammaT, a, b, c):
    a2 = Decimal(alphaT)
    a1 = Decimal(triA[0])
    b2 = Decimal(betaT)
    b1 = Decimal(triA[1])
    c2 = Decimal(gammaT)
    c1 = Decimal(triA[2])
    A = Decimal(a*2)
    B = Decimal(b*2)
    C = Decimal(c*2)
    first = ((a1-a2)**2)*Decimal(sin(A))+((b1-b2)**2)*Decimal(sin(B))+((c1-c2)**2)*Decimal(sin(C))
    second = 2*sin(a)*sin(b)*sin(c)
    third = Decimal(first)/Decimal(second)
    d = sqrt(third)
    return d

#def q(triB, beta, gamma, A)

#def r(triC, gamma, alpha, B)

print p(triA, alphaT, betaT, gammaT, A, B, C) + p(triB, alphaT, betaT, gammaT, A, B, C) + p(triC, alphaT, betaT, gammaT, A, B, C) == pqrSum
