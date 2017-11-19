1/x + 1/y = 1/n

1/x + 1/y = x+y/x*y

x+y/x*y = 1/n

x+y   1
--- = -
x*y   n 


7+x    1
7*x    4


6+12   1    (x+y) 
6*12   4    72 = 18*4 72 = (6+12)*4 = (x+y)*n = 


x*y = (x+y)*n

x*y = x*n + y*n

testing for x or y = 2:
    2y = 2*4 + 4y
    2y = 8 + 4y
    y  = 4 + 2y
    -1y = 4
    4 = -4
    fail, all integers must be positive
testing for x = 9:
    9y = 9*4 + 4y
    9y = 36 + 4y
    5y = 36
    y = 36/5, non-decimal answer, fail (7.22222)  *** So do we stop at 2n, once the value is less than that, there are no more answers? possibly.......

testing for x = 7:
    7y = 7*4 + 4y
    7y = 28 + 4y
    3y = 28
    y = 28/3, non-decimal answer, (9.3333333)
    
testing for x = 5:
    5y = 5*4 + 4y
    5y = 20 + 4y
    y = 20
    solution




x+y must == 1/n of x*y 

x*y = (1/n)*(x+y)

so if n = 4:
    x*y = 1/4 (x+y)
    
test multiples of n as y first:
    y = 2n, 3n, 4n, 5n, 6n, 7n
    y = 8,  12, 16, 20, 24, 28
    
with those y values:
    x*8 = 1/4(8+x)
    
    
    
x*y = x*n + y*n
x*y - y*n = x*n

9y = 9*4 + 4y
    9y = 36 + 4y
    5y = 36
    y = 36/5


so, we set values: we're testing for y, and we're doing so by iterating up x from n+1 to 2n


countMax = 0
countingMax = 0

def solveForY(n,countMax):
    count = 0
    base = n+1
    top = (2*n)+1
    for x in xrange(base, top):
        testValue = fractions.Fraction((x*n),(x-n))
        if testValue/1 == int(testValue):
            count += 1
    return count


    
n = 60

table = [30, 60, 120]

while solveForY(n,countMax) < 1001:
    countMax = solveForY(n,countMax)
    if countMax > countingMax:
        countingMax = countMax
        print countingMax, n
        n += 60

print solveForY(n,countMax), n
