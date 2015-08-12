import math
from decimal import *
getcontext().prec = 100

ratio = 3.125
pFirst = 16 
pSecond  = 50 

perimeterSums = [16, 50]
count = 0


a = 18
while a < (10**9)/3:   
    b = a+1
    area = (Decimal(b)*(Decimal(4*(a**2)-(b**2)).sqrt()))/Decimal(4)
    p = 2*a + b
    if len(str(area)) < 100:
        perimeterSums.append(p)
        pFirst = pSecond
        pSecond = p
        a *= ratio
        a  = int(a//1)  
    b2 = a-1
    area = (Decimal(b2)*(Decimal(4*(a**2)-(b2**2)).sqrt()))/Decimal(4)
    p = 2*a + b2
    if len(str(area)) < 100:
        perimeterSums.append(p) 
        pFirst = pSecond
        pSecond = p 
        ratio = (Decimal(pSecond)/Decimal(pFirst))
        a = Decimal(ratio)*Decimal(a)
        a = int(a//1)
    else:
        a += 1
        count += 1
        
print count, sum(perimeterSums)   
    