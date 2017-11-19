#euler project 127.py https://projecteuler.net/problem=127 defines rad(n) for this problem

import itertools

def product(collection):
    if len(collection) > 0:
        p = 1
        for i in collection:
            p *= i
        return p
    else:
        return 'empty set'

def rad(n, limit = 10**6):
  subSet = set()
  out = []
  if type(n) != int and type(n) != long:
    raise TypeError('must be integer')
  fs = []
  while n % 2 == 0:
    fs += [2]
    n /= 2
  if n == 1:
    for x in fs:
      subSet.add(x)
    for x in subSet:
        out.append(x)
    return product(out)
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
      subSet.add(x)
  subSet.add(n)
  for x in subSet:
      out.append(x)
  return product(out)

print rad(1323520)

def gcd(a,b):
    while b: a, b = b, a%b
    return abs(a)


base = []

zSum = 0
count = 0

for x in xrange(1,120000):
    for y in xrange(x+1,120000-x):
        z = x+y
        if rad(x)*rad(y)*rad(z) < z:
            if gcd(x,y) == 1:
                #if gcd(y,z) == 1:
                #    if gcd(x,z) == 1:
              zSum += z
              count += 1
              #if x == 5:
              print x, y, z, zSum, count
#             base.append([x,y,z])
print zSum





