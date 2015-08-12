def solve():
  table = compress()
  n = len(table)
  m = len(table[0])
  valueMin = 10**7
  for i in xrange(n):
    starter = i
    j = 0
    value = table[i][0]
    lastUp = False
    lastDown = False
    while j < m-1:
      if i < m-1 and i > 1:
        if lastUp == False and lastDown == False:
          low = min(table[i][j+1], table[i+1][j], table[i-1][j]) if i*j > 0 else \
          min(table[i][j+1], table[i-1][j]) if i>0 else \
            min(table[i+1][j], table[i][j+1])
        if lastDown == True:
          low = min(table[i-1][j], table[i][j+1]) if i > 1 else \
            table[i][j+1]
        if lastUp == True:
          low = min(table[i+1][j], table[i][j+1]) if i < m-2 else \
            table[i][j+1]
      if i == m-1:
        if lastDown == True:
          low = table[i][j+1]
        else:
          low = min(table[i][j+1], table[i-1][j])
        value += low
        print 'starter', starter, 'j', j, 'i', table[i][j], 'm', m
        print low, starter
        if low == table[i][j+1]:
          lastUp = False 
          lastDown = False
          j += 1
        elif low == table[i+1][j]:
          lastDown = True
          i += 1
        elif low == table[i-1][j]:
          lastUp = True
          i -= 1
    if value <= valueMin:
      valueMin = value
  return valueMin
  
  
  def compress():
  rows = []
  with open('euler82Test') as f:
    for line in f:
      rows.append([int(i) for i in line.rstrip('\n').split(",")])
  n = len(rows)
  for i in xrange(n):
    rows[i][1] += rows[i][0]
    rows[i].remove(rows[i][0]) 
  return rows

def dijkstra():
  baseTable = compress()
  n = len(baseTable) 
  m = len(baseTable[0])
  valueMin = 10**8
  sumTable = [[10**7]*m]*n 
  baseTable = compress()
  for i in xrange(n):
    for j in xrange(m-1):
      if i == 0:
        down = baseTable[i][j] + baseTable[i+1][j]
        if down < sumTable[i+1][j]:
          sumTable[i+1][j] = down
          baseTable[i+1][j] = down
        right = baseTable[i][j] + baseTable[i][j+1]
        if right < sumTable[i][j+1]:
          sumTable[i][j+1] = right
          baseTable[i][j+1] = right
      if i == n-1:
        up = baseTable[i][j] + baseTable[i-1][j]
        if up < sumTable[i-1][j]:
          sumTable[i-1][j] = up
          baseTable[i-1][j] = up
        right = baseTable[i][j] + baseTable[i][j+1]
        if right < sumTable[i][j+1]:
          sumTable[i][j+1] = right
          baseTable[i][j+1] = right
      else:
        up = baseTable[i][j] + baseTable[i-1][j]
        if up < sumTable[i-1][j]:
          sumTable[i-1][j] = up
          baseTable[i-1][j] = up
        down = baseTable[i][j] + baseTable[i+1][j]
        if down < sumTable[i+1][j]:
          sumTable[i+1][j] = down
          baseTable[i+1][j] = down
        right = baseTable[i][j] + baseTable[i][j+1]
        if right < sumTable[i][j+1]:
          sumTable[i][j+1] = right
          baseTable[i][j+1] = right
    valueEnd = sumTable[i][m-1] + baseTable[i][m-1]
    if valueEnd < valueMin: 
      valueMin = valueEnd
    print valueMin
  

def solve2():
  table = compress()
  n = len(table) # = 80 Y axis, each row
  m = len(table[0]) # = 79 X axis, each cell
  print 'n =', n, 'm =', m
  valueMin = 10**7
  for i in xrange(n):
    j = 0
    value = table[i][0]
    lastUp = False
    lastDown = False
    while j < m-1:
      if i == 0:
        if lastUp == False:
          low = min(table[i][j+1], table[i+1][j])
        if lastUp == True:
          low = table[i][j+1]
      elif i == n-1:
        if lastDown == False:
          low = min(table[i][j+1], table[i-1][j])
        if lastDown == True:
          low = table[i][j+1]
      else:
        if lastUp == False and lastDown == False:
          low = min(table[i][j+1], table[i-1][j], table[i+1][j])
        elif lastUp == True:
          low = min(table[i][j+1], table[i-1][j])
        elif lastDown == True:
          low = min(table[i][j+1], table[i+1][j])
      value += low
      if i == 0:
        if low == table[i][j+1]:
          j += 1
        elif low == table[i+1][j]:
          lastDown = True
          i += 1
      elif i == n-1:
        if low == table[i][j+1]:
          j += 1
        elif low == table[i-1][j]:
          lastUp = True
          i -= 1
      else:
        if low == table[i-1][j]:
          lastUp = True
          i -= 1
        elif low == table[i][j+1]:
          j += 1
        elif low == table[i+1][j]:
          lastDown = True
          i += 1
    if value <= valueMin:
      valueMin = value
  return valueMin
  #print table[79][78] # bottom right cell




print dijkstra()