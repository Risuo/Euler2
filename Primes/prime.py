import time 
import math

  
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
  
def td_prime(n, limit = 10**6):
  if type(n) != int and type(n) != long:
    raise TypeError('must be integer')
  if n % 2 == 0:
    return n == 2
  d = 3
  while d * d <= n:
    if limit < d:
      raise OverflowError('limit exceeded')
    if n % d == 0:
      return False
    d += 2
  return True

def td_factors(n, limit = 10**6):
  if type(n) != int and type(n) != long:
    raise TypeError('must be integer')
  fs = []
  while n % 2 == 0:
    fs += [2]
    n /= 2
  if n == 1:
    return fs
  f = 3
  while f * f <= n:
    if limit < f:
      raise OverflowError('limit exceeded')
    if n % f == 0:
      fs += [f]
      n /= f
    else:
      f += 2
  return fs + [n]

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


start = time.time()
result = rho_factors(600851475143)
elapsed = time.time() - start
  
print result
print elapsed

start2 = time.time()
result2 = td_factors(600851475143)
elapsed2 = time.time() - start2

print result2
print elapsed2