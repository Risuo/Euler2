import itertools


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
  


eights = itertools.permutations('123456789', 8)

eightPrimes = []



for x in eights:
    test = ''
    for y in x:
        test += y
    if is_prime(int(test)):
        eightPrimes.append(int(test))







def primes(n):
  if type(n) != int and type(n) != long:
    raise TypeError('must be integer')
  if n < 2:
    raise ValueError('must be greater than one')
  m = (n-1) / 2      # use floor division // in python 3.0 or later. as this is 2.7, no need for it here
  b = [True] * m     # creates a list of m terms, all of which are True
  i, p, primeList = 0, 3, [2]  # begins our sieving at 3, begins our prime list at 2
  while p*p < n:     # if for our sieve test (p) p*p is > n, then we quit, no more non-primes to sieve
    if b[i]:         # if b[i], referencing our True list of length m, at location i, is still True
      primeList.append(p)
      j = 2*i*i + 6*i + 3      # begin the sieving, by progressing upward through factors, remebering the
                               # total list is only 1/2 the length of m, indicating the removal of all
                               # the even numbers
      while j < m:             # so long as our value j, the factor, is smaller than the largest odd below n
        b[j] = False           # modify the location of b[j] to be false, removing it from our report
        j = j + 2*i + 3        
    i += 1; p += 2             # move to the next b[i], but move to the next odd value, thus + 2
  while i < m:                 
    if b[i]:
      primeList.append(p)
    i += 1; p += 2
  return primeList

basePrimes = primes(10000000) #gives us all the primes up to 7 digits long, still need the 8 and 9 digits long, but with only 1 of each of the numbers
print len(basePrimes)

newList = []

print len(basePrimes), 'before add'

basePrimes = basePrimes + eightPrimes

print len(basePrimes), 'after add'

for x in basePrimes:
    toAdd = True
    for y in str(x):
        if str(x).count(y)> 1:
            toAdd = False
        if y == '0':
            toAdd = False
    if toAdd == True:
        if x not in newList:
            newList.append(x)

print len(newList), 'after subtraction'

newList = sorted(newList)

testSet = []

for x in newList:
    if len(str(x)) < 5:
        for y in newList:
            if y > x: 
                if len(str(x)+str(y)) > 9:
                    break
                if len(str(x)+str(y)) < 9:
                    for q in newList:
                        if q > y:
                            if len(str(x)+str(y)+str(q)) > 9:
                                break
                            if len(str(x)+str(y)+str(q)) < 9:
                                for a in newList:
                                    if a > q:
                                        if len(str(x)+str(y)+str(q)+str(a)) > 9:
                                            break
                                        if len(str(x)+str(y)+str(q)+str(a)) < 9:
                                            for b in newList:
                                                if b > a:
                                                    if len(str(x)+str(y)+str(q)+str(a)+str(b)) > 9:
                                                        break
                                                    if len(str(x)+str(y)+str(q)+str(a)+str(b)) < 9:
                                                        for c in newList:
                                                            if c > b:
                                                                if len(str(x)+str(y)+str(q)+str(a)+str(b)+str(c)) > 9:
                                                                    break
                                                                if len(str(x)+str(y)+str(q)+str(a)+str(b)+str(c)) == 9:
                                                                    toAdd = True
                                                                    test = str(x)+str(y)+str(q)+str(a)+str(b)+str(c)
                                                                    for z in test:
                                                                        if test.count(z) > 1:
                                                                            toAdd = False
                                                                    if toAdd == True:
                                                                        if len(test) == 9:
                                                                            if [x,y,q,a,b,c] not in testSet:
                                                                                testSet.append([x,y,q,a,b,c])
                                                                                print [x,y,q,a,b,c]
                                                                        if len(test) < 9:
                                                                            print 'under 9', [x,y,q,a,b,c]

                                                    else:
                                                        toAdd = True
                                                        test = str(x)+str(y)+str(q)+str(a)+str(b)
                                                        for z in test:
                                                            if test.count(z) > 1:
                                                                toAdd = False
                                                        if toAdd == True:
                                                            if len(test) == 9:
                                                                if [x,y,q,a,b] not in testSet:
                                                                    testSet.append([x,y,q,a,b])
                                                            if len(test) < 9:
                                                                print 'under 9', [x,y,q,a,b]

                                        else:
                                            toAdd = True
                                            test = str(x)+str(y)+str(q)+str(a)
                                            for z in test:
                                                if test.count(z) > 1:
                                                    toAdd = False
                                            if toAdd == True:
                                                if len(test) == 9:
                                                    if [x,y,q,a] not in testSet:
                                                        testSet.append([x,y,q,a])
                                                    else:
                                                        print [x,y,q,a], 'duplicate'
                                                if len(test) < 9:
                                                    print 'under 9', [x,y,q,a]

                            else:
                                toAdd = True
                                test = str(x)+str(y)+str(q)
                                for z in test:
                                    if test.count(z) >1:
                                        toAdd = False
                                if toAdd == True:
                                    if len(test) == 9:
                                        if [x,y,q] not in testSet:
                                            testSet.append([x,y,q])
                                        else:
                                            print [x,y,q], 'duplicate'
                                    if len(test) < 9:
                                        print 'under 9', [x,y,q]

                else:
                    toAdd = True
                    test = str(x)+str(y)
                    for z in test:
                        if test.count(z) > 1:
                            toAdd = False
                    if toAdd == True:
                        if len(test) == 9:
                            if [x,y] not in testSet:
                                testSet.append([x,y])
                            else:
                                print [x,y], 'duplicate'
                        if len(test) < 9:
                            print 'under 9', [x,y]

    else:
        break
#2, 17, 463, 5
            
print len(testSet)
