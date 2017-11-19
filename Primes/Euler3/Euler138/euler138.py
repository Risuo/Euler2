



count = 0
b = 8

lSum = 0


while count < 12:
    h1 = (2*b)+1
    h2 = (2*b)-1
    L1 = (b**2+h1**2)
    L2 = (b**2+h2**2)
    L1T = (b**2+h1**2)**.5//1
    L2T = (b**2+h2**2)**.5//1
    if L1 == L1T**2:
        count += 1
        lSum += L1
        print b, 2*b, h1, L1, 'L1, b+1', count, lSum
    if L2 == L2T**2:
        count += 1
        lSum += L2
        print b, 2*b, h2, L2, 'L2, b-1', count, lSum
    b += 1
    
print lSum