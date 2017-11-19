import itertools


#length = [2] + [1 for a in xrange(5)]

#print len(length)

#print len(list(itertools.permutations(length, length-1)))


def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0
        
        
        
l = 6
r = 2

twoSum = 0
threeSum = 0
fourSum = 0

def prob116(l,r):
    outValue = 0
    for x in xrange(1, l):
        a = l-(r*x)+x
        value = choose(a,x)
        outValue += value
    return outValue
    
print prob116(5,2)
print prob116(5,3)
print prob116(5,4)
print prob116(5,5)*2
print prob116(5,6)*2
