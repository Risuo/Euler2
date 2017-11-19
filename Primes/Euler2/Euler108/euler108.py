import fractions

from math import sqrt
from collections import Counter
from itertools import product
 
answer = [1, 3, 6, 12, 24, 36, 70, 108, 140, 180, 240, 360, 420, 840, 1260, 1680, 2520, 4620, 7560, 9240, 13860, 18480, 27720, 55440, 83160, 110880, 120120, 180180]
 
MUL = int.__mul__
 
 
def prime_factors(n):
    'Map prime factors to their multiplicity for n'
    d = _divs(n)
    d = [] if d == [n] else (d[:-1] if d[-1] == d else d)
    pf = Counter(d)
    return dict(pf)

def _divs(n):
    'Memoized recursive function returning prime factors of n as a list'
    for i in range(2, int(sqrt(n)+1)):
        d, m  = divmod(n, i)
        if not m:
            return [i] + _divs(d)
    return [n]
 
 
def proper_divs(n):
    '''Return the set of proper divisors of n.'''
    pf = prime_factors(n)
    pfactors, occurrences = pf.keys(), pf.values()
    multiplicities = product(*(range(oc + 1) for oc in occurrences))
    divs = {reduce(MUL, (pf**m for pf, m in zip(pfactors, multis)), 1)
            for multis in multiplicities}
    try:
        divs.remove(n)
    except KeyError:
        pass
    return divs or ({1} if n != 1 else set())

n = 0
nMax = 0
answerTable = []
primeMax = 2

test = (len(proper_divs(n**2))/2)+1

def turnToSet(n):
    outTable = set()
    for x in n:
        outTable.add(x)
    return outTable

while test < 10000:
    n += 1
    if len(turnToSet(_divs(n))) >= primeMax:
        if len(turnToSet(_divs(n))) == primeMax + 1:
            primeMax += 1
        test = (len(proper_divs(n**2))/2)+1
        if test > nMax:
            print nMax, test, n, _divs(n), turnToSet(_divs(n))
            nMax = test
            answerTable.append(n)
            if n < 20:
                n += 1
            elif n < 30:
                n += 10
            else:
                n += 30
            
        
        
print answerTable

print _divs(91891800)

        
