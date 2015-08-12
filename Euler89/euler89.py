import time

start = time.time() 
romanTable = []
with open('euler89Data') as f:
  for line in f:
    romanTable.append([i for i in line.rstrip('\n').split(" ")])

#romanTable.sort()

#print romanTable[999][0]
#print romanTable[999][0].count('I'), len(romanTable[999][0])

romanValues = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}


romanTableBaseSum = 0
for x in romanTable:
  for y in x:
    romanTableBaseSum += len(y)

romanNumeralTable = []

for x in romanTable:
  skip = False
  for y in x: # includes '' around the item
    romanSum = 0
    for z in y: # y is the string only 
      if y.index(z) < len(y)-1:
        if skip == True:
          skip = False
        else:
          if z == "I": # cycles through each character
            checkIndex = y.index(z)
            if "V" == y[checkIndex+1]:
              romanSum += 4
              skip = True
            elif "X" == y[checkIndex+1]:
              romanSum += 9
              skip = True
            else:
              romanSum += romanValues[z]
          elif z == "X":
            checkIndex = y.index(z)
            if "L" == y[checkIndex+1]:
              romanSum += 40
              skip = True
            elif "C" == y[checkIndex+1]:
              romanSum += 90
              skip = True
            else:
              romanSum += romanValues[z]
          elif z == "C":
            checkIndex = y.index(z)
            if "D" == y[checkIndex+1]:
              romanSum += 400
              skip = True
            elif "M" == y[checkIndex+1]:
              romanSum += 900
              skip = True
            else:
              romanSum += romanValues[z]
          else:
            romanSum += romanValues[z]
      elif skip == False:
        romanSum += romanValues[z]
    romanNumeralTable.append(romanSum)
#romanNumeralTable.sort()



romanSum = 0
for z in romanNumeralTable: 
  y = str(z)
  romanLength = 0
  if z > 999:
    romanLength += int(y[0])
    #print 'length after the thousands', romanLength
    if y[1] == '0':
      romanLength += 0
    elif y[1] == '2' or y[1] == '4' or y[1] == '6' or y[1] == '9':
      romanLength += 2
    elif y[1] == '1' or y[1] == '5':
      romanLength += 1
    elif y[1] == '3' or y[1] == '7':
      romanLength += 3
    elif y[1] == '8':
      romanLength += 4
    #print 'length after the hundreds', romanLength
    if y[2] == '0':
      romanLength += 0
    elif y[2] == '2' or y[2] == '4' or y[2] == '6' or y[2] == '9':
      romanLength += 2
    elif y[2] == '1' or y[2] == '5':
      romanLength += 1
    elif y[2] == '3' or y[2] == '7':
      romanLength += 3
    elif y[2] == '8':
      romanLength += 4
    #print 'length after the tens', romanLength
    if y[3] == '0':
      romanLength += 0
    elif y[3] == '2' or y[3] == '4' or y[3] == '6' or y[3] == '9':
      romanLength += 2
    elif y[3] == '1' or y[3] == '5':
      romanLength += 1
    elif y[3] == '3' or y[3] == '7':
      romanLength += 3
    elif y[3] == '8':
      romanLength += 4
    #print 'length after the ones', romanLength
  elif z > 99:
    if y[0] == '2' or y[0] == '4' or y[0] == '6' or y[0] == '9':
      romanLength += 2
    elif y[0] == '1' or y[0] == '5':
      romanLength += 1
    elif y[0] == '3' or y[0] == '7':
      romanLength += 3
    elif y[0] == '8':
      romanLength += 4
    if y[1] == '0':
      romanLength += 0
    elif y[1] == '2' or y[1] == '4' or y[1] == '6' or y[1] == '9':
      romanLength += 2
    elif y[1] == '1' or y[1] == '5':
      romanLength += 1
    elif y[1] == '3' or y[1] == '7':
      romanLength += 3
    elif y[1] == '8':
      romanLength += 4
    if y[2] == '0':
      romanLength += 0
    elif y[2] == '2' or y[2] == '4' or y[2] == '6' or y[2] == '9':
      romanLength += 2
    elif y[2] == '1' or y[2] == '5':
      romanLength += 1
    elif y[2] == '3' or y[2] == '7':
      romanLength += 3
    elif y[2] == '8':
      romanLength += 4
  elif z > 9:
    if y[0] == '2' or y[0] == '4' or y[0] == '6' or y[0] == '9':
      romanLength += 2
    elif y[0] == '1' or y[0] == '5':
      romanLength += 1
    elif y[0] == '3' or y[0] == '7':
      romanLength += 3
    elif y[0] == '8':
      romanLength += 4
    if y[1] == '0':
      romanLength += 0
    elif y[1] == '2' or y[1] == '4' or y[1] == '6' or y[1] == '9':
      romanLength += 2
    elif y[1] == '1' or y[1] == '5':
      romanLength += 1
    elif y[1] == '3' or y[1] == '7':
      romanLength += 3
    elif y[1] == '8':
      romanLength += 4
  else:
    romanLength = 4
  print romanLength, z
  romanSum += romanLength
print romanSum, romanTableBaseSum, romanTableBaseSum-romanSum
  
 
elapsed = time.time() - start
print elapsed 