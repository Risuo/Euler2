
def compress():
  rows = []
  with open('euler102Data') as f:
    for line in f:
        rows.append([int(i) for i in line.rstrip('\n').split(",")])
  return rows


def areaTriangle(A,B,C):
    return abs(((A[0]*B[1])-(A[1]*B[0]))+((B[0]*C[1])-(B[1]*C[0]))+((C[0]*A[1])-(C[1]*A[0]))/2)
    
def areaCalculate(triPlots):
    first = [triPlots[0],triPlots[1]]
    second = [triPlots[2],triPlots[3]]
    third = [triPlots[4],triPlots[5]]
    triangleArea = areaTriangle(first,second,third)
    originArea = areaTriangle([0,0],second,third)+areaTriangle(first,[0,0],third)+areaTriangle(first,second,[0,0])
    if triangleArea == originArea:
        return True
    
count = 0
print len(plotTable), 'total triangles tested'
for x in cells:
    if areaCalculate(x):
        #print 'okay'
        count += 1
print count, 'the answer'

