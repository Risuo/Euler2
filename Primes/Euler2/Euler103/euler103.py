import itertools
import math

# S(B)  S(C); that is, sums of subsets cannot be equal.
# If B contains more elements than C then S(B) > S(C).


tableAnswer =  [6,   9, 11, 12, 13]
table2Tripup = [11, 17, 20, 22, 23, 24] # this is not the minimum
table2Answer = [11, 18, 19, 20, 22, 25] # this is the minimum


testSet = [20, 25, 26, 27, 28, 29, 30]
testSuperSet = [list(itertools.combinations(range(8, 30), 6))]

print len(testSuperSet[0])


def runTestSetup(tableSet):
    sumTest = []
    testTable = []
    for x in xrange(2,len(tableSet)):
        testTable.append(list(itertools.combinations(tableSet, x)))
    for y in testTable:
        for z in y:
            if sum(z) not in sumTest:
                sumTest.append(sum(z))
            else:
                return False
    for y in testTable:
        for z in testTable:
            for w in y:
                for q in z:
                    if w != q:
                        if len(w) > len(q):
                            if sum(w) > sum(q):
                                continue
                            else:
                                return False
    return True
    

    
minSum = 1000
for x in testSuperSet:
    for y in x:
        if runTestSetup(y):
            newSum = sum(y)
            if newSum < minSum:
                minSum = newSum
                print y, minSum
                
print minSum
            
            

            
#print runTestSetup(testSet), sum(testSet)
    










