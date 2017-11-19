from math import sqrt
squares = []

limit = 10**12

def isSquare(n):
    return int(sqrt(n))*int(sqrt(n)) == n

for a in xrange(2,10001):
    for b in xrange(1,a):
        if a**3 * b**2 + b**2 >= limit:
            break
        c = 1
        n = a**3 * b * c**2 + c * b**2
        while n <= limit:
            n = a**3 * b * c**2 + c * b**2
            if isSquare(n):
                print 'n is a square', a, b*b*c,a*b*c, a*a*c, n
                if n not in squares:
                    squares.append(n)
            c += 1
            
print sorted(squares)
print sum(squares)