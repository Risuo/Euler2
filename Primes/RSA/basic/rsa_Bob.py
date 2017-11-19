#insert the values of n & e from Alice program:
import random

n = long(21957481088204606813417501)
e = long(53)

#n = int(str(nh), 0)
#e = int(str(eh), 0)

output = ''
message = 'hello world, code test'


for x in message:
  a = ord(x)
  if a<100:
    a*=10
  #print a, 'a here', x, 'x here'
  output += str(a)

m = int(output)
#print m, 'm here'


#        22222222222222222222222222
m = long(21957481088204600000000000)
#        21957481087999999999999999

c = long(pow(m,e,n))
d = long(21128896896187745021396417)
n = long(21957481088204606813417501)



#c = int(str(ch),0)
#d = int(str(dh),0)
#n = int(str(nh),0)

#print hex(c)
#print hex(d)
#print hex(n)

m = pow(c,d,n)

print m




