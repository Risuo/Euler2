m = 50



def ways2(n):
    ways = [1] * (n+1)

    for j in range(m, n+1):
        ways[j] = ways[j - 1] + 1
        for k in range(m, j):
            ways[j] += ways[j - k - 1]
    return ways[n]
        
        

for x in xrange(51,250):
    test = ways2(x)
    if test < 10**6:
        print test, x
