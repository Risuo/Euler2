a = [10, 315410, 927070, 2525870, 8146100, 16755190, 39313460, 97387280, 119571820, 121288430, 130116970, 139985660, 144774340]
test = [5, 11, 15, 17, 19, 21, 23, 25]

ok = []

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


for x in a:
    toAdd = True
    for y in test:
        if is_prime(x**2 + y):
            print 'busted', x, y
            toAdd = False
    if toAdd == True:
        ok.append(x)
print ok
print sum(ok)
            