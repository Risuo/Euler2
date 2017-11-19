import itertools
import time
import math
import copy

def is_prime(n):
  if type(n) != int and type(n) != long:
    raise TypeError('must be integer')
  if n < 2:
    return False
  ps = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
  def is_spsp(n, a):
    d, s = n-1, 0
    while d % 2 == 0:
      d /= 2; s += 1
    t = pow(a,d,n)
    if t == 1:
      return True
    while s > 0:
      if t == n-1:
        return True
      t = (t*t) % n
      s -= 1
    return False
  if n in ps: return True
  for p in ps:
    if not is_spsp(n,p):
      return False
  return True


#unlike other euler###b.py files, at first this will still be my own coding

A = [1,2,3,4,5,6,7,8,9]
B = [1,2,3,4,5,6,7,8,9,0]
C = [1,2,3,4,5,6,7,8,9,0]
D = [1,2,3,4,5,6,7,8,9,0]
E = [1,2,3,4,5,6,7,8,9,0]
F = [1,2,3,4,5,6,7,8,9,0]
G = [1,2,3,4,5,6,7,8,9,0]
H = [1,2,3,4,5,6,7,8,9,0]
I = [1,2,3,4,5,6,7,8,9,0]
J = [1,3,7,9]

number = [A]+[B]+[C]+[D]+[E]+[F]+[G]+[H]+[I]+[J]


fixSet = [0,1,2,3,4,5,6,7,8,9]

def minV(value):
    out = []
    for x in number:
        if value in x:
            out.append(value)
        else:
            out.append(min(x))
    return out
    
def toInt(table):
    string = ''.join(str(n) for n in table)
    return int(string)




baseSet = [minV(n) for n in fixSet]

tableOutA = []
tableOutB = []

digitCount = -1


for n in baseSet:
    tableTest = []
    if is_prime(toInt(n)):
        if n not in tableTest:
            tableTest.append(n)
    index = -1
    digitCount += 1
    for digit in n:
        testN = copy.deepcopy(n)
        index += 1
        for value in number[index]:
            testN.insert(index, value)
            testN.pop((index)+1)
            testNumber = toInt(testN)
            if is_prime(testNumber):
                if testN not in tableTest:
                    if testN.count(digitCount) == 9:
                        tableTest.append(testN)
    if len(tableTest) == 0:
        tableOutB.append(n)
    else:
        tableOutA.append(tableTest)



#for x in tableOutA:
#    print x, 'has 9'
#for x in tableOutB:
#    print x, 'still need'
    

tableOutC = []

digitCount = [0,2,8]
digitCountIndex = -1

for n in tableOutB:
    print n, 'n here'
    tableTest = []
    if is_prime(toInt(n)):
        if n not in tableTest:
            tableTest.append(n)
    index = -1
    digitCountIndex += 1
    for digit in n:
        testN = copy.deepcopy(n)
        index += 1
        for value in number[index]:
            testN.insert(index, value)
            testN.pop((index)+1)
            index2 = -1
            for digit2 in n:
                testN2 = copy.deepcopy(testN)
                index2 += 1
                for value in number[index2]:
                    testN2.insert(index2,value)
                    testN2.pop((index2)+1)
                    testNumber = toInt(testN2)
                    if is_prime(testNumber):
                        if testN2 not in tableTest:
                            if testN2.count(digitCount[digitCountIndex]) == 8:
                                #print testN2, digitCount[digitCountIndex]
                                tableTest.append(testN2)
    tableOutC.append(tableTest)
   
outTable = []   
for x in tableOutC:
    for y in x:
        if toInt(y) not in outTable:
            outTable.append(toInt(y))
        
for x in tableOutA:
    for y in x:
        if toInt(y) not in outTable:
            outTable.append(toInt(y))
            
outSet = set()
for x in outTable:
    for z in str(x):
        if str(x).count(z) == 8 or str(x).count(z) == 9:
            if not is_prime(x):
                print x, 'this isnt prime...'
            if is_prime(x):
                outSet.add(x)
    

answer = 0
for x in outSet:
    print x
    answer += x
print answer
 
valueCount = -1
hasEight = []
hasNine = []

for x in tableOutA:
    test = []
    valueCount += 1
    for y in x:
        if y.count(valueCount) == 9:
            test.append(y)
    hasNine.append(test)
    test = []
    for y in x:
        if y.count(valueCount) == 8:
            test.append(y)
    hasEight.append(test)

