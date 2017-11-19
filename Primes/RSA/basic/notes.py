choose two prime numbers p1, p2 of similar size
find n = p1*p2
calculate phi(n): phi(n) = (p1-1)*(p2-1)
pick a small, public exponent e, must be odd, and be relatively prime with phi(n) [no shared factors]
find d, = (k * phi(n)+1)/e 
sends n & e to bob create the public key

bobs unencrypted message = m

m MUST BE < n. Otherwise, it all goes to shit. 

bob encrypts m by: (m**e) mod n = c



c = (m**e)%n

sends c to alice

alice performs decryption

(c**d) mod n = m

(c**d)%n = m


example:
p1 = 53
p2 = 59
n = 3127
phi(n) = 3016
e = 3
k = 2
d = ((2*3016)+1)/3 = 2011
m = 89


