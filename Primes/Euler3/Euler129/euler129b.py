def gcd(a,b):
    while b: a, b = b, a%b
    return abs(a)
    
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


def A(n):
    if not is_prime(n) and gcd(n,10) == 1:
        x = 1
        k = 1
        while x != 0:
            x = (x*10 + 1) % n
            k += 1
        return k
    else:
        return None
        
L = 1000001
n = L

while A(n) < L:
    n += 2
    
print n