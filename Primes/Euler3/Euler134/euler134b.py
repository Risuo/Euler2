    
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

def extended_GCD(a,b):
    x = 0
    lx = 1
    y = 1
    ly = 0
    while b != 0:
        quotient = a/b
        temp = b
        b = a%b
        a = temp
        
        temp = x
        x = lx - quotient*x
        lx = temp
        
        temp = y
        y = ly - quotient*y
        ly = temp
        
    return [lx, ly, a]

primeList = [a for a in xrange(5,1000010,2) if is_prime(a)] # 36605225 #replace with 1000010 when solving

def findLength(p1):
    length = 1
    while p1 > 0:
        length *= 10
        p1 /= 10
        #print length, p1
    return length


#print findLength(25), 'doin it here'

def calc(p1,p2):
    a = findLength(p1)
    b = p2-p1
    n = p2
    rs = extended_GCD(a,n)
    
    x = (rs[0]*b)%n
    
    if x < 0:
        x = n+x
    
    return x * a + p1

listSum = 0

for prime in primeList:
    if primeList.index(prime) != len(primeList)-1:
        p1 = prime
        p2 = primeList[primeList.index(p1)+1]
        value = calc(p1,p2)
        if primeList.index(p1)%5000 == 0:
            print value, p1, p2, primeList.index(p1)
        listSum += value

print listSum

    




