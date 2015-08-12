file = open('euler98Data', 'r')
arr = [a.replace("\"","") for a in file.read().split(',')]
arr.sort()

h = dict()
for a in arr:
  if len(a) > 4:
    key = ''.join(sorted(a))
    h.setdefault(key,[]).append(a)

for key in h.keys():
  if len(h[key]) == 1:
    h.pop(key, None)

squares = [x*x for x in range(0,10000)]

max_value = []
for key in h.keys():
  for square in squares:
    if len(str(square)) < len(key):
      continue
    if len(str(square)) > len(key):
      break
  
    word = h[key][0]
    sq = str(square)
  
    d = { word[i]:sq[i] for i in range(len(word))[::-1] }

    valid = max([d.values().count(v) for v in d.values()]) == 1
    if not valid:
      continue
    
    other = h[key][1]
    othersqr = int(''.join([d[o] for o in other]))
     
    if (len(str(square)) != len(str(othersqr))):
      continue
            
    if othersqr in squares:
      max_value.append(square)
      print square, othersqr, word, other
  
print h
print max(max_value)