from __future__ import division

def factors(n):    
    step = 2 if n%2 else 1
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1, step) if n % i == 0)))


def quarticSolve(N):
    output = []
    A = -5
    B = 6
    C = -1
    F = N
    K = 4
    factored = factors(-4*A*F)
    for ui in factored:
        y = (ui + ((4*A*-F)/ui))/(2*K)
        x = (ui-((B+K)*y))/(2*A)
        if y%int(y) == 0 and x%int(x) == 0 and y-2*x > 0:
            output.append([x,y])
            if len(output) > 1:
                return False
    if len(output) == 1:
        #print output, N
        return True
    else:
        return False

count = 0

for x in xrange(2, 50*10**6):
    if quarticSolve(x):
        count += 1
        if count%1000 == 0:
            print x, count
print count
