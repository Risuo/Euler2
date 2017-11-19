import itertools
import math




def compress():
  rows = []
  with open('euler105Data') as f:
    for line in f:
        rows.append([int(i) for i in line.rstrip('\n').split(",")])
  return rows
  
testSuperSet = compress()




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
    

totalValue = 0
for x in testSuperSet:
    if runTestSetup(x):
        totalValue += sum(x)

print totalValue