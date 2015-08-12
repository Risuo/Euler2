import time

rows = []
with open('euler81Data') as f:
  x = 0
  for line in f:
    rows.append([int(i) for i in line..split("","")])
   # print rows[x]
   # x += 1
   
def recSumAtRow(rows, cellStart):
  outTable = []
  # iterate over the given row
  # cellStart = x by x matrix
  y = 0
  start = [cellStart-1, cellStart-1]
  tableX = start[0]
  tableY = start[1]
  reportTable = []
  finalReportTable = []
  newTable = [[tableX, tableY]]
  finalTable = []
  while tableY > 0:
    tableY -= 1
    newTable.append([tableX, tableY])
  while tableX > 0:
    tableX -= 1
    newTable.append([tableX, tableY])
  for x in newTable:
    outTable = [x]
    if x[0] != x[1]:
      difference = max(x)-min(x)
      for z in xrange(1, difference+1):
        outTable.append([x[0]-z, x[1]+z])
    finalTable.append(outTable)
  for x in finalTable:
    reportTable = []
    for y in x:
      reportTable.append(rows[y[0]][y[1]])
    finalReportTable.append(reportTable)
  return finalReportTable
  # finalReportTable[row][cell], with row being 0 to 8 ((cellStart*2)-2), 
  # cell being 0 to (len-1)
    
    
def findMin(rows, cellStart):
  table = recSumAtRow((rows), len(rows))
  for row in xrange(1, len(table)):
    if row < cellStart:
      for cell in xrange(len(table[row])):
        if cell == 0:
          table[row][cell] += table[row-1][cell]
        elif cell > 0 and cell < len(table[row])-1: 
          table[row][cell] += min(table[row-1][cell-1], table[row-1][cell])
        else:
          table[row][cell] += table[row-1][cell-1]
    else:
      for cell in xrange(len(table[row])):
        table[row][cell] += min(table[row-1][cell], table[row-1][cell+1])
  return table[(cellStart*2)-2][0]


start = time.time()
result = findMin(rows, len(rows))
elapsed = time.time() - start

print result
print elapsed