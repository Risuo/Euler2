a=10**4
a+=1
n=a
while 1:
    t,v= n*n,2
    for i in xrange(2,n):
        if t%i == 0:
            v+=1
    if v > a-1:
        print n
        break
    n +=a