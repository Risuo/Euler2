#utilizes pseudo-random generated numbers, not actually cryptologically secure
import random

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
def gcd(a,b):
    while b: a, b = b, a%b
    return abs(a)
def n_phin(): #returns n, phi(n)
  test = random.sample(xrange(10**13),1)
  while not is_prime(test[0]):
    test = random.sample(xrange(10**13),1)
  p1 = test[0]
  test2 = random.sample(xrange(10**13),1)
  while not is_prime(test2[0]):
    test2 = random.sample(xrange(10**13),1)
  p2 = test2[0]
  return [p1*p2,(p1-1)*(p2-1),[p1,p2]]
def find_e(phin):
  phin = phin
  test = random.sample(xrange(3,70,2),25)
  for e in test:
    if gcd(e,phin) == 1:
      return e

base =    n_phin()
n,phin =       base[0], base[1]

#p1 =     base[2][0]
#p2 =     base[2][1]

e = find_e(phin)

def find_d(phin, e):
  d1 = 1
  k = 1
  while d1 != 0:
    k += 1
    d1 = ((k*phin)+1)%e
  d = ((k*phin)+1)/e  
  #print k, 'k'
  return d

d = find_d(phin, e)

#print hex(n), ':n', hex(e), ':e', hex(d), ':d'

print n, 'n int', e, 'e int', d, 'd int'

def encode(message):
  return str(message).encode("hex")

def decode(hexMessage):
  return str(hexMessage).decode("hex")

#print encode('Hello World')

#print decode('48656c6c6f20776f726c64')
#Each of the characters is now concantenated into a 2 digit length
#hex string

#a1 = encode("Hello World")
#print a1, 'a1 here'
#m = int(encode("Hello World"), base=16)
#print m, 'base16'
#print str(hex(m)[2:-1])

#insert the message from Bob here:
c = 9516150917028000362981869
d = 21128896896187745021396417
n = 21957481088204606813417501



#c = int(str(ch),0)
#d = int(str(dh),0)
#n = int(str(nh),0)

#print hex(c)
#print hex(d)
#print hex(n)

m = pow(c,d,n)

print m
