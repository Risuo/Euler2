def to_Array(aSet):
    t = []
    for x in aSet:
        t.append(x)
    return t

def product(collection):
    if len(collection) > 0:
        p = 1
        for i in collection:
            p *= i
        return p
    else:
        return 'empty set'

def rad(n, limit = 10**6):
  outSet = set()
  if type(n) != int and type(n) != long:
    raise TypeError('must be integer')
  fs = []
  while n % 2 == 0:
    fs += [2]
    n /= 2
  if n == 1:
    for x in fs:
        outSet.add(x)
    return product(to_Array(outSet))
  f = 3
  while f * f <= n:
    if limit < f:
      raise OverflowError('limit exceeded')
    if n % f == 0:
      fs += [f]
      n /= f
    else:
      f += 2
  for x in fs:
      outSet.add(x)
  outSet.add(n)
  return product(to_Array(outSet))
  
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

def gcd(a,b):
    while b: a, b = b, a%b
    return abs(a)

finalTableABC = {}

subTableABC = {}

baseTable = {}

for x in xrange(1,120000):
    baseTable[x] = 1

for i in xrange(2,120000):
    if baseTable[i] == 1:
        baseTable[i] = i
        j = i+i
        while j < 120000:
            baseTable[j] *= i
            j += i


baseTable[1] = 1

print len(baseTable)            

print baseTable[5], baseTable[27]

c = 0
count = 0

for a in xrange(1,120000):
    for b in xrange(a+1,120000-a):
        if b < a:
            print 'breaking'
            break
        if baseTable[a]*baseTable[b]*baseTable[a+b] >= a+b:
            continue
        if gcd(a,b) != 1:
            continue
        if count%50 == 0:
            print a, b, a+b, baseTable[a], baseTable[b], baseTable[a+b]
        c += a+b
        count += 1



print c, count

