
endIn89 = set([85, 89, 145, 42, 20, 4, 16, 37, 58])
endIn1 = set([44, 32, 13, 10, 1])
 
endIn89.add(45)

def intSquare(value):
  number = str(value)
  square = 0
  for x in xrange(len(number)):
     square += int(number[x])**2
  return square

count89 = 0
count1 = 0

for x in xrange(1,10000000):
  firstTest = intSquare(x)
  end = False
  while end == False:
    if firstTest == 1:
      end = True
      count1 += 1
    elif firstTest == 89:
      end = True
      count89 += 1
    else:
      firstTest = intSquare(firstTest)

print count89, count1

 



