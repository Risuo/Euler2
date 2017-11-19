from math import floor

def gcd(a,b):
    while b: a, b = b, a%b
    return abs(a)


def euclids_Formula_Primals(limit):
    basics = 1
    table = []
    limit = limit
    for n in xrange(limit):
        limit2 = int(floor((-1+((1+2*limit)**.5))/2))
        for m in xrange(n, limit2):
            if m-n%2!=0 and m>n and n>0:
                if gcd(m,n) == 1:
                    a = m**2-n**2
                    b = 2*m*n
                    c = m**2 + n**2
                    difference = b-a
                    if difference == 1 or difference == -1:
                        table.append([a,b,c])
                        print basics
                        basics += int(floor((10**8)/(c+b+a)))
                        print basics
    print basics
    return table
    
print euclids_Formula_Primals(25000000)