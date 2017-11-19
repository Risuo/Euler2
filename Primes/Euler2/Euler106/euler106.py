import itertools

def runTestSetup(tableSet):
    sumTest = []
    testTable = []
    testTable2 = []
    checkSum = 0

    overCheck = 0
    for x in xrange(2,7):
        testTable.append(list(itertools.combinations(tableSet, x)))

    for x in testTable:
        for z in testTable:
            for y in x:
                for q in z:
                    toAdd = True
                    if y != q:
                        for a in y:
                            if a in q:
                                toAdd = False
                        if toAdd == True:
                            if len(y) == len(q):
                                if y > q:
                                    testTable2.append([q,y])
                                else:
                                    testTable2.append([y,q])
    print len(testTable2)
    tableToRemove = []
    toTestTable = set()
    for a in testTable2:
        for x in xrange(1,len(a)):
            if a[1][x] < max(a[0]):
                tableToRemove.append(a)
    
    testTable2 = []
    
    for x in tableToRemove:
        count = 0
        if (2,4,7) in x:
            print x

        for y in xrange(0,len(x[0])):
            if x[1][y] > x[0][y]:
                #print x[1], x[0], x[1][y], x[0][y]
                count += 1
            if count == len(x[0]):
                while x in tableToRemove:
                    #print x, 'removed'
                    #print x, count, len(x[0])
                    tableToRemove.remove(x)
    


    for x in tableToRemove:
        if (2,4,7) in x:
            if (1,3,5) in x:
                print x
        toTestTable.add(tuple(x))
        

    
    for x in toTestTable:
        testTable2.append(x)
    testTable2 = sorted(testTable2)
    #for x in testTable2:
        #print x, testTable2.count(x)
    print len(toTestTable)
    
                
    #toTestTable.add(tuple(a))
     #           print a

    #for x in toTestTable:
        #print x
    print len(toTestTable)

testSuperSet = [1,2,3,4,5,6,7]

totalValue = 0
print runTestSetup(testSuperSet)

#2 3 6 vs 1 4 5
#
