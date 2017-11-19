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

Zero =  [0,0,0,0,0,0,0,0,0,0]
One =   [1,1,1,1,1,1,1,1,1,1]
Two =   [2,2,2,2,2,2,2,2,2,2]
Three = [3,3,3,3,3,3,3,3,3,3]
Four =  [4,4,4,4,4,4,4,4,4,4]
Five =  [5,5,5,5,5,5,5,5,5,5]
Six =   [6,6,6,6,6,6,6,6,6,6]
Seven = [7,7,7,7,7,7,7,7,7,7]
Eight = [8,8,8,8,8,8,8,8,8,8]
Nine =  [9,9,9,9,9,9,9,9,9,9]

zeroCase =  [1,0,0,0,0,0,0,0,0,1] # special case

testCases9 = [One]+[Three]+[Four]+[Five]+[Six]+[Seven]+[Nine]
testCases8 = [Zero]+[Two]+[Eight]
testCase0 = [1000000001, 1000000003, 1000000007, 1000000009, 2000000001, 2000000003, 2000000007, 2000000009, 3000000001, 3000000003, 3000000007, 3000000009, 4000000001, 4000000003, 4000000007, 
                4000000009, 5000000001, 5000000003, 5000000007, 5000000009, 6000000001, 6000000003, 6000000007, 6000000009, 7000000001, 7000000003, 7000000007, 7000000009, 8000000001, 8000000003, 
                8000000007, 8000000009, 9000000001, 9000000003, 9000000007, 9000000009]
                
                
def toInt(table):
    string = ''.join(str(n) for n in table)
    return int(string)
    
#            testN.insert(index, value)
#            testN.pop((index)+1)
#            testNumber = toInt(testN)
#            testCase.insert(testDigit,x)
#            testCase.pop((x)+1)
#            testNumber = toInt(testCase)

hasNine = []
needsEight = []

primeGroup = set()

for case in testCases8:
    testCase = copy.deepcopy(case)
    for x in xrange(10):
        for y in xrange(10):
            testCase.insert(x,y)
            testCase.pop((x)+1)
            testCase2 = copy.deepcopy(testCase)
            for a in xrange(10):
                for b in xrange(10):
                    testCase2.insert(a,b)
                    testCase2.pop((a)+1)
                    testNumber = toInt(testCase2)
                    if len(str(testNumber)) == 10:
                        #print testNumber
                        if is_prime(testNumber):
                            primeGroup.add(testNumber)
                        testCase2 = copy.deepcopy(testCase)
            testCase = copy.deepcopy(case)


for case in testCases9:
    testCase = copy.deepcopy(case)
    for x in xrange(10):
        for y in xrange(10):
            testCase.insert(x,y)
            testCase.pop((x)+1)
            testNumber = toInt(testCase)
            if len(str(testNumber)) == 10:
                if is_prime(testNumber):
                    primeGroup.add(testNumber)
            testCase = copy.deepcopy(case)

print primeGroup
print len(primeGroup)
print sum(primeGroup)
