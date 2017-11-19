from math import sqrt

squaresT = [x**2 for x in xrange(1, 10**6)]
squaresO = [x**2 for x in xrange(1, 10**6, 2)]
squaresE = [x**2 for x in xrange(2, 10**6, 2)]

def isSquare(n):
    return int(sqrt(n))*int(sqrt(n)) == n

def xyzFind(test, squareX, squareT):
    start = test
    index = squareX.index(start)+1
    for xz in squareX[index:]:
        if xz-start > start:
            break
        else:
            x = ((xz-start)/2)+start
            z = xz-x
            #print x, z, xz
            index2 = squareT.index(xz)+1
            for xy in squareT[index2:]:
                if xy-x > x:
                    break
                else:
                    y = (xy-x)
                    if y > 0 and z > 0 and x!= y:
                        #print x-y, x-z, x, xz, xy
                        if isSquare(x-y):
                            #print 'x-y, x-z, x, xz, xy', x-y, x-z, x, xz, xy
                            if isSquare(y-z):
                                print 'and y-z is square', y-z, x-y, x-z, x, xz, xy
                                if isSquare(y+z):
                                    print x, y, z
                                    return x, y, z
                                    
                                    


    
    
for e in squaresT:
    if e%2 == 0:
        xyzFind(e,squaresE, squaresT)
    else:
        xyzFind(e,squaresO, squaresT)
