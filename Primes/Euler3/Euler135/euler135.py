
#needs to be gone about via the n method, not the x method. need an upper-bound (n==10**6), whereas working off of x does not give that to us

limit = 1250000

nSolutions = {}

def arithmetic(x,a):
    n = x**2-((x-a)**2)-((x-(2*a))**2)
    if n > 10**6:
        return -1
    else:
        return n


b = 1
for x in xrange(1,limit):
    if x%10000 == 0:
        print x
    if x%5 == 0:
        b += 1
    if x%2 == 0:
        for a in xrange(b,x/2):
            n = arithmetic(x,a)
            if n == -1:
                continue
            else:
                if n in nSolutions:
                    nSolutions[n] += 1
                else:
                    nSolutions[n] = 1
            #print n, x, a, 'even'
    else:
        for a in xrange(b,x/2+1):
            n = arithmetic(x,a)
            if n == -1:
                continue
            else:
                if n in nSolutions:
                    nSolutions[n] += 1
                else:
                    nSolutions[n] = 1
                
            #print n, x, a, 'odd'
        

count = 0

for n in nSolutions:
    if nSolutions[n] == 10:
        print n
        count += 1
print count
