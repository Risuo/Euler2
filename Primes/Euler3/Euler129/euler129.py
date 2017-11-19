def gcd(a,b):
    while b: a, b = b, a%b
    return abs(a)
    
    
    
n = 2
k = '1'
count = 1

values = {}

while len(k) < 1000:
    k = '1'
    if gcd(n,10) == 1:
        while int(k)%n != 0:
            k = k+'1'
        #print len(k), n #len(k) == A(n)
        if len(k) in values:
            values[len(k)] += [n]
        else:
            values[len(k)] = [n]
    n += 1
    

for key in sorted(values.iterkeys()):
    print key, values[key]
        