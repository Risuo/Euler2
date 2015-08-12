

difference = 2000000
difMin = 2000000

def factSum(value): 
  x = 0
  for z in xrange(value+1):
    x += z
  return x 

for z in xrange(100):
  for i in xrange(100): 
    total = factSum(z)*factSum(i)  
    if total > 2000000:
      break
    subDif = abs(difference-total)
    if subDif < difMin:
      difMin = subDif
      table = [z, i]
print difMin, table, table[0]*table[1]


