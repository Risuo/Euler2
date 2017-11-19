from decimal import Decimal

def cycle(a,b):
    return [b, a+b]


a = 1
b = 4
    
for x in xrange(100):
    print a
    output = cycle(a,b)
    a,b = output[0], output[1]
    
