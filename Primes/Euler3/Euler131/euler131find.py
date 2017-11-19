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

primes = []
limit = 100
p = 2

while p < limit:
    if is_prime(p):
        primes.append(p)
    p += 1
        
print 'done'

cubes = [x**3 for x in xrange(100)]

#for x in cubes:
#    print x

n = 1
x = 1
p = 2
count = 0

for p in primes:
    n = 1
    cubes = [x**3 for x in xrange(n,p**2)]
    #print cubes, p
    while n < p**3 and count < 4:
        if n**3 + (n**2)*p in cubes:
            print 'n:', n, 'p:', p, 'x:', (n**3 + (n**2)*p)**(1./3)
            count += 1
            break
        else:
            n += 1


