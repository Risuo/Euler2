import math
import copy
import itertools

def toArray(string):
    table = []
    for x in string:
        table.append(int(x))
    return table


def toStr(table):
    string = ''
    for x in table:
        string += str(x)
    return string
    

def fbase(r,l):
    outTable = []    
    nSet = [1 for a in xrange(l)]
    rSet = [a for a in xrange(r,l+1)]
    for r in rSet:
        index = 0
        for n in nSet:
            nTSet = copy.deepcopy(nSet)
            nTSet.pop(index)
            nTSet.insert(index,r)
            index += 1
            for x in xrange(r-1):
                nTSet.remove(1)
            if nTSet not in outTable:
                outTable.append(nTSet)
    return outTable
    
fullTable = []

def fFull(r,l):
    table = fbase(r,l)
    for a in table:
        if a.count(1) > 0:
            maximum = a.count(1)-1
        #if maximum >= r:
        #    for z in xrange(maximum,r-1,-1):
                
def cycleDown(count, rSet, l, iteration, table, fullTable):
    r2Set = [a for a in xrange(count, min(rSet)-1, -1)]
    count = 0
    for r in r2Set:
        print iteration
        table2 = copy.deepcopy(table[:iteration])
        print table2, 'this is table2', table, 'this is table'
        while sum(table2) <= l:
            table2.append(r)
            table2.append(1)
        while sum(table2) > l:
            table2.pop(len(table2)-1)
        count = 0
        while sum(table2) < l:
            table2.append(1)
            count += 1
        print table2, 'pre-test'
        if table2 not in fullTable:
            print table2, 'post-test'
            fullTable.append(table2)
            #print table
        if count >= min(rSet):
            cycleDown(count, rSet, l, iteration+2, table2, fullTable)
            print 'for now, within the cycle'
    #print 'about to return'
    print 'out of the cycle'
    return count, rSet, l, iteration, table2, fullTable
    

        
def fBuild(r,l):
    rSet = [a for a in xrange(l, r-1, -1)]
    #print rSet, 'rSet'
    table = []
    for r in rSet:
        table.append(r)
        table.append(1)
        while sum(table) > l:
            table.pop(len(table)-1)
        index = len(table)
        count = 0
        while sum(table) < l:
            count += 1
            table.append(1)
        if table not in fullTable:
            fullTable.append(table)
            #print table
        iteration = 2
        while count >= min(rSet):
            answer = cycleDown(count, rSet, l, iteration, table, fullTable)
            count = answer[0]
            #iteration += 1
            #print 'one loop in the while'
        table = []
    return fullTable
    
    

def removeOne(table):
    outTable = []
    for x in table:
        if x != 1:
            outTable.append(x)
    return outTable

def iteration(table):
    baseTable = []
    outTable = []
    for x in table:
        test = removeOne(x)
        length = (len(test)*2)-1
        base = test
        #print x, length, base
        baseTable = list(itertools.permutations(base,length))
        for a in baseTable:
            while baseTable.count(a) > 1:
                baseTable.remove(a)
        #print baseTable, 'baseTable here'
        for a in baseTable:
            toAdd = True
            #print a, 'a here'
            index = 0
            for x in a:
                index += 1
                if x != 1:
                    if index < len(a):
                        if a[index] == 1:
                            toAdd = True
                        else:
                            toAdd = False
                            break
            if toAdd:
                if a not in outTable:
                    outTable.append(a)
    return outTable #this does solve it, but i run into a memory limit.... :(


for x in fBuild(3,21):
    print x

