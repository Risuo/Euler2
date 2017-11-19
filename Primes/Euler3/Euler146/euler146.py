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

count = 0

def checkPrimes(base):
    if is_prime(base+27):
        if is_prime(base+13):
            if is_prime(base+9):
                if is_prime(base+7):
                    if is_prime(base+3):
                        if is_prime(base+1):
                            return True
    else:
        return False
        
base = 10
limit = 150000000

while base < limit:
  for a in xrange(base, limit, 10):
    if checkPrimes(a**2):
      count += a
      print a, 'a here'
      global base
      base = a*2
      print base, 'base after being multiplied by 2'
      break

    
print count, 'count'

#This is incomplete, see 146b.py for the application of the 'consecutive' check, and the final answer