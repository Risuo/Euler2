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

s = set()
limit = 10**5
l = 1
n = 5

second = [2,3]
x = 5
while x < limit:
    if is_prime(x):
        second.append(x)
    x += 2
print len(second)

#Can also just run the factors of k = 10**20 (anything > 16, actually) and you'll get the full set of factors under 100,000

for l in xrange(17):
    k = 10**l
    n = 5
    while n < limit:
        if is_prime(n) and pow(10, k, n) == 1:
            if n not in s:
                print l, n
            s.add(n)
        n += 2

print s, len(s)



for x in s:
    second.remove(x)
        
print sum(second)
