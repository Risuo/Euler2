#And this is the third solution, don't quite understand it, but I have figured out the math/code
from time import clock


def convertBase(n,base):
    base10 = n
    digitLoc=0
    converted={}
    while base**(digitLoc+1) < base10:
        digitLoc += 1
    
    while digitLoc >= 0:
        converted.update({digitLoc:base10 / (base**digitLoc)})
        base10 = base10 % (base**digitLoc)
        digitLoc -= 1
    
    numberStr = ''
    revTable = []
    for a in converted:
        revTable.insert(0,converted[a])
    for b in revTable:
        numberStr += str(b)
    return numberStr
    
    



def run(base10,solveFor):
    rowBase10 = base10
    solveNum = solveFor
    rows = convertBase(rowBase10, solveNum) # this is 10**9 in base 7
    
    power = len(rows)-1
    count = 0
    endCount = 0
    product = 1
    baseTri = (solveNum*(solveNum+1))/2
    
    
    for digit in rows:
        dig = int(digit)
        tri = (dig*(dig+1))/2
        #print product, power, tri, dig
        count = product*(baseTri**power)*tri
        endCount += count
        #print count
        product *= dig+1
        power -= 1
        
    return endCount

runTime = 0


for a in xrange(3000):
    b = 10**a
    start = clock()
    run(b,7)
    runTime += clock()-start
    #print 'Runtime:', clock()-start, 'seconds'
print runTime
