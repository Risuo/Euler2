##84**4 is our top end

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
   
  
squaredPrimes = primes(7070)
cubedPrimes = primes(368)
fourthPrimes = primes(84)

limit = 50000000
table = set()


for x in squaredPrimes:
  for y in cubedPrimes:
    for z in fourthPrimes:
      value = z**4 + y**3 + x**2
      if value < limit:
        table.add(value)
print len(table)