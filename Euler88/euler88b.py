#Project Euler Problem 88

def prodsum(p, s, c, start):
    k = p - s + c     # product - sum + number of factors
    if k < kmax:
        if p < n[k]: n[k] = p
        for i in range(start, kmax//p * 2):
            prodsum(p*i, s+i, c+1, i)

kmax = 12000
n = [2*kmax] * kmax    # the minimal product-sum is < 2*k + 1 
prodsum(1, 1, 1, 2)

#  convert to set to remove duplicates from slice of n
print "Project Euler 88 Solution =", sum(set(n[2:]))