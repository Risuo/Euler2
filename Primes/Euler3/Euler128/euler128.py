def is_Prime(n):
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

def difference_A(A, Z, A2, Z2):
    if is_Prime((A2+1)-A):
        if is_Prime(Z2-A):
            if is_Prime(Z-A):
                return True

def difference_Z(A1, Z1, A, Z, A2, Z2):
    if is_Prime(Z-A1):
        if is_Prime((Z2-1)-Z):
            if is_Prime(Z-A):
                return True

count = 2
A = 2
Z = 7
tier = 2
tierMin = 2

limit = 2000

while count < limit:
    A1 = A
    Z1 = Z
    A = tierMin+(6*(tier-1))
    Z = A+(6*tier)-1
    A2 = Z+1
    Z2 =  A2+(6*(tier+1))-1
    #if count%100 == 0:
    #    print A1, Z1, A, Z, A2, Z2, count
    if difference_A(A, Z, A2, Z2):
        #print A, 'A'
        count += 1
        if count == limit:
            print A
    if difference_Z(A1, Z1, A, Z, A2, Z2):
        #print Z, 'Z'
        count += 1
        if count == limit:
            print Z
    #print A1, Z1, A, Z, A2, Z2, 'bottom print'
    tierMin = A
    tier += 1