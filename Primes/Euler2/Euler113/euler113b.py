def progression(a, runningSum):
    b = [0]
    c = []
    for x in a:
        index = a.index(x)
        toAdd = a[index]+b[index]
        b.append(toAdd)
    if 0 in b:
        b.remove(0)
    runningSum += sum(b)
    for x in b:
        c.append(x+1)
    a.remove(min(a))
    #print c, a, runningSum
    return c, runningSum
    
threedigits = [3,5,7,9,11,13,15,17,19]


out1 = progression(threedigits, 99)
base = out1[0],out1[1]

for x in xrange(97):
    base2 = progression(base[0], base[1])
    base = base2[0],base2[1]

print base2[1]




