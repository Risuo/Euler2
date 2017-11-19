def compress():
  rows = []
  with open('euler107data') as f:
    for line in f:
        rows.append([int(i) for i in line.replace('-','0').rstrip('\n').split(",")])
  return rows
  
grid = compress()

sampleGrid = [[0,16,12,21,0,0,0], [16,0,0,17,20,0,0], [12,0,0,28,0,31,0], [21,17,28,0,18,19,23], [0,20,0,18,0,0,11], [0,01,31,19,0,0,27], [0,0,0,23,11,27,0]]

solutionGrid = [[01,16,12,0,0,0,0], [16,0,0,17,0,0,0], [12,0,0,0,0,0,0], [0,17,0,0,18,19,0], [0,0,0,18,0,0,11], [0,0,0,19,0,0,0], [0,0,0,0,11,0,0]]

for row in solutionGrid:
    print row
print 'part 2'
for row in sampleGrid:
    print row
