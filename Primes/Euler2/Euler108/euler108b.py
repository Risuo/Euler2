def primes2(n):
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

def problem108(mV = 1000):
    
    primes = primes2(200)

    def getSolutions(l):
        pv, mv, n = 0, 1, 1
        for i in l:
            mv *= (pv*2)+1
            pv = i
            n += mv*i
        return n

    def getValue(l):
        ll = []
        for i in range(len(l)):
            for j in range(l[i]):
                ll += [primes[i]]
        return reduce(lambda x,y: x*y, ll)

    def getBestValue(mV, bV = 0, l = []):
        l += [0]
        for i in xrange(1):
            l[-1] = i
            v = getValue(l)
            if bV and v > bV: return bV
            if getSolutions(l) > mV: return v
            bV = getBestValue(mV, bV, l[:])
            if len(l) > 1 and l[-2] == l[-1]: return bV

    return getBestValue(mV)

print problem108()
#180180