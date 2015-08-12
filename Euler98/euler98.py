import re
import itertools


w1 = []
w2 = []
w3 = []
w4 = []
w5 = []
w6 = []
w7 = []
w8 = []
w9 = []
w10 = []
w11 = []
w12 = []
w13 = []
w14 = []

words = []
inp = open("euler98Data")
count = 0
out = ''
 
 
squares = []

for x in xrange(1,100000):
  if x*x < 999999999:
    squares.append(x*x)
  else:
    break

for x in inp.readlines():
  out = x

out = re.sub('"', '', out)
  
for x in out.split(','):
  words.append([len(x), x])
  words.sort()
  
for y in words:
  if y[0] == 1:
    w1.append(y[1])
  if y[0] == 2:
    w2.append(y[1])
  if y[0] == 3:
    w3.append(y[1])
  if y[0] == 4:
    w4.append(y[1])
  if y[0] == 5:
    w5.append(y[1])
  if y[0] == 6:
    w6.append(y[1])
  if y[0] == 7:
    w7.append(y[1])
  if y[0] == 8:
    w8.append(y[1])
  if y[0] == 9:
    w9.append(y[1])
  if y[0] == 10:
    w10.append(y[1])
  if y[0] == 11:
    w11.append(y[1])
  if y[0] == 12:
    w12.append(y[1])
  if y[0] == 13:
    w13.append(y[1])
  if y[0] == 14:
    w14.append(y[1])
  
print len(w1)+len(w2)+len(w3)+len(w4)+len(w5)+len(w6)+len(w7)+len(w8)+len(w9)+len(w10)+len(w11)+len(w12)+len(w13)+len(w14), 'total words'

def findAnagrams(wordList):
  tableOut = []
  remove = []
  toAdd = []
  for x in wordList:
    for y in wordList:
      if x != y:
        count = 0
        for z in y:
          if z in x and x.count(z) == y.count(z):
            count += 1
        if count == len(x):
          remove.append(x) 
          remove.append(y)
          remove.sort()
          for k in remove:
            toAdd.append(k)
          tableOut.append(toAdd)
          toAdd = []
          remove = []
  tableOut.sort()
  for x in tableOut:
    if tableOut.count(x) != 1:
      tableOut.remove(x)
  return tableOut
          
outTable = []
if len(findAnagrams(w1))>0:
  outTable.append(findAnagrams(w1))
if len(findAnagrams(w2))>0:
  outTable.append(findAnagrams(w2))
if len(findAnagrams(w3))>0:
  outTable.append(findAnagrams(w3))
if len(findAnagrams(w4))>0:
  outTable.append(findAnagrams(w4))
if len(findAnagrams(w5))>0:
  outTable.append(findAnagrams(w5))
if len(findAnagrams(w6))>0:
  outTable.append(findAnagrams(w6))
if len(findAnagrams(w7))>0:
  outTable.append(findAnagrams(w7))
if len(findAnagrams(w8))>0:
  outTable.append(findAnagrams(w8))
if len(findAnagrams(w9))>0:
  outTable.append(findAnagrams(w9))
if len(findAnagrams(w10))>0:
  outTable.append(findAnagrams(w10))
if len(findAnagrams(w11))>0:
  outTable.append(findAnagrams(w11))
if len(findAnagrams(w12))>0:
  outTable.append(findAnagrams(w12))
if len(findAnagrams(w13))>0:
  outTable.append(findAnagrams(w13))
if len(findAnagrams(w14))>0:
  outTable.append(findAnagrams(w14))

print len(outTable[0])+len(outTable[1])+len(outTable[2])+len(outTable[3])+len(outTable[4])+len(outTable[5])+len(outTable[6]), 'total anagramatic pairs'

finalTable = []


for x in outTable:
  print x

print list(enumerate('COURRSE')) 
letter_set = {x:y for y, x in enumerate('COURRSE')}
print letter_set


#for x in outTable:
 # for y in x:
  #  finalTable.append(y)
    
 
#def numberCycle(word, word2):


#for x in finalTable:
 # for y in x[0]: 
    
    
  #print x[0], x[1]




