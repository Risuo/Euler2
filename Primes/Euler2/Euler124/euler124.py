import math

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

def rho_factors(n, limit = 10**6):
  if type(n) != int and type(n) != long:
    raise TypeError('must be integer')
  def gcd(a,b):
    while b: a, b = b, a%b
    return abs(a)
  def rho_factor(n, c, limit):
    f = lambda(x): (x*x*c) % n
    t, h, d = 2, 2, 1
    while d == 1:
      if limit == 0:
        raise OverflowError('limit exceeded')
      t = f(t); h = f(f(h)); d = gcd(t-h, n)
    if d == n:
      return rho_factor(n, c+1, limit)
    if is_prime(d):
      return d
    return rho_factor(d, c+1, limit)
  if -1 <= n <= 1: return[n]
  if n < -1: return [-1] + rho_factors(-n, limit)
  fs = []
  while n % 2 == 0:
    n = n/2; fs = fs + [2] # use // notation in python 3.0 and later
  if n == 1: return fs
  while not is_prime(n):
    f = rho_factor(n, 1, limit)
    n = n/f
    fs = fs + [f]
  return sorted(fs + [n])
  
def rad(n):
    outSet = set()
    base = rho_factors(n)
    for x in base:
        outSet.add(x)
    return reduce(lambda x, y: x*y, outSet)
    
baseTable = []
for n in xrange(100000):
    baseTable.append([rad(n), n])
baseTable.sort()
print baseTable[9999][1]
