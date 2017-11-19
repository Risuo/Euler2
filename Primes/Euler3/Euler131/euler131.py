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
#      n         n     p
print (1  **3 + (1**2)*7)    **(1./3) # + 12 yields 19
print (8  **3 + (8 **2)*19)  **(1./3) # + 18 yields 37
print (27 **3 + (27**2)*37)  **(1./3) # + 24 yields 61
print (64 **3 + (64**2)*61)  **(1./3) # + 30 yields 91
print (125**3 + (125**2)*91) **(1./3) # + 36 yields 127 !!!!! 91 is not prime, however, we need 91 for the next value of p, + 36, yields 127
print (216**3 + (216**2)*127)**(1./3) # + 40, etc etc etc

#interestingly, every perfect cube has an answer here in terms of representation for the n values

#all we have to solve for is the p sequence, which progresses 7, 19, 37, 61, 91, 127, and then run through the sequence removing the non-primes, and the prime values is our answer
# this sequence is: 7+12, 19+18, 37+24, 61+30, 91+36, etc. recursive. 

#10**6

limit = 10**6

x = 1
count = 0
pCount = 0
while x < limit:
    x = x+(6*(count))
    if is_prime(x):
        print x
        pCount += 1
    count += 1
    
print pCount