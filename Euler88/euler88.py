from functools import reduce
import operator

def product(table):
  return reduce(operator.mul, table, 1)

def secondSmallest(table):
  tableSet = set()
  for x in table:
    tableSet.add(x)
  tableSet.remove(1)
  return min(tableSet)
 
def productSum(size):
  finalSet = set()
  for k in xrange(2, size):
    if k < 2**2:
      v = 2
    elif k < 2**3:
      v = 3
    elif k < 2**4:
      v = 4
    elif k < 2**5:
      v = 5
    elif k < 2**6:
      v = 6
    elif k < 2**7:
      v = 7
    elif k < 2**8:
      v = 8
    elif k < 2**9:
      v = 9
    elif k < 2**10:
      v = 10
    elif k < 2**11:
      v = 11
    elif k < 2**12:
      v = 12
    elif k < 2**13:
      v = 13
    elif k < 2**14:
      v = 14
    baseSet = [2]*v
    add = sum(baseSet)+ (k - v)
    mult = product(baseSet)
    minValue = 2
    while mult < add:
      baseSet[baseSet.index(minValue)] += 1
      add = sum(baseSet)+ (k - v)
      mult = product(baseSet)
    minValue = 2
    if mult != add:
      baseSet[baseSet.index(2)] -= 1
    while mult != add:
      minValue = secondSmallest(baseSet)
      add = sum(baseSet)+ (k - v)
      mult = product(baseSet)
      if mult < add:
        #print 'in mult < add, this is the before', baseSet
        indexChange = baseSet.index(minValue)
        baseSet[indexChange] += 1
        #print 'and this is the after', baseSet, 'this is mult and add', mult, add
        add = sum(baseSet)+ (k - v)
        mult = product(baseSet)
        if mult > add:
          baseSet[indexChange] -= 1
          baseSet[baseSet.index(minValue)] += 1
      elif mult > add:
        #print 'in mult > add, and this is the before', baseSet, 'and mult and add', mult, add
        baseSet[baseSet.index(minValue)] -= 1
        maxValue = max(baseSet)
        baseSet[baseSet.index(maxValue)] += 1
        #print 'and this is the after', baseSet
      add = sum(baseSet)+ (k - v)
      mult = product(baseSet) 
    firstValue = mult
    if k < 2**2:
      v = 2
    elif k < 2**3:
      v = 3
    elif k < 2**4:
      v = 4
    elif k < 2**5:
      v = 5
    elif k < 2**6:
      v = 6
    elif k < 2**7:
      v = 7
    elif k < 2**8:
      v = 8
    elif k < 2**9:
      v = 9
    elif k < 2**10:
      v = 10
    elif k < 2**11:
      v = 11
    elif k < 2**12:
      v = 12
    elif k < 2**13:
      v = 13
    elif k < 2**14:
      v = 14
    baseSet = [2]*v
    add = sum(baseSet)+ (k - v)
    mult = product(baseSet)
    minValue = 2
    while mult < add:
      baseSet[baseSet.index(minValue)] += 1
      add = sum(baseSet)+ (k - v)
      mult = product(baseSet)
    minValue = 2
    if mult != add:
      baseSet[baseSet.index(2)] -= 1
    while mult != add:
      minValue = secondSmallest(baseSet)
      add = sum(baseSet)+ (k - v)
      mult = product(baseSet)
      if mult < add:
        #print 'in mult < add, this is the before', baseSet
        indexChange = baseSet.index(minValue)
        baseSet[indexChange] += 1
        #print 'and this is the after', baseSet, 'this is mult and add', mult, add
        add = sum(baseSet)+ (k - v)
        mult = product(baseSet)
        if mult > add:
          baseSet[indexChange] -= 1
          baseSet[baseSet.index(max(baseSet))] += 1
      elif mult > add:
        #print 'in mult > add, and this is the before', baseSet, 'and mult and add', mult, add
        baseSet[baseSet.index(minValue)] -= 1
        maxValue = max(baseSet)
        baseSet[baseSet.index(maxValue)] += 1
        #print 'and this is the after', baseSet
      add = sum(baseSet)+ (k - v)
      mult = product(baseSet) 
    secondValue = mult
    if secondValue < firstValue:
      #print k, secondValue, baseSet
      finalSet.add(secondValue)   
    else:
      #print k, firstValue, baseSet
      finalSet.add(firstValue)
  return sum(finalSet)
       
      
    #   minValue += 1
    #   baseSet[baseSet.index(minValue)] -= 1
    #   add = sum(baseSet)
    #   mult = product(baseSet)
    #   print baseSet
    #   print mult, add
    #   while mult != add:
    #     preChange = baseSet
    #     testValue = minValue-1
    #     testValue += 1
    #     baseSet[baseSet.index(testValue)] += 1
    #     add = sum(baseSet)
    #     mult = product(baseSet)
    #     if mult > add:
    #       baseSet = preChange
    #       minValue += 1
    # else:
    #   print baseSet, mult, add

print productSum(12000)  










