def split(arr, size):
     arrs = []
     while len(arr) > size:
         pice = arr[:size]
         arrs.append(pice)
         arr = arr[size:]
     arrs.append(arr)
     return arrs
     
limit = 1000


squares = [n**2 for n in xrange(1,limit)]
print len(squares)

sumsM = {}

index = []

for x in squares:
    for y in squares:
        if y != x and y > x and y > 500**2:
            for z in squares:
                if z != y and z != x and z > y and z > x and y > x:
                    s = x+y+z
                    t = [x,y,z]
                    print t
                    t = sorted(t)
                    if s not in sumsM:
                        index.append(t)
                        sumsM[s] = [t]
                        sumsM[s,'count'] = 1
                    elif s in sumsM:
                        sumsM[s,'count'] += 1
                        sumsM[s] += [t]

totalCount = 0
for a in xrange(limit**2+limit**2+limit**2):
    if a in sumsM:
        if sumsM[a,'count'] >= 8:
            print sumsM[a]
            #print sumsM[a], 'a'
            t = []
            associatedA = []
            for trio in sumsM[a]:
                for i in trio:
                    t.append(i)
            associatedA = split(t,3)
            counts = []
            for i in t:
                counts.append(t.count(i))
            counts = split(counts, 3)
            yCounts = 0
            c1, c2, c3 = 0, 0, 0
            indexTable = []
            #print 'new'
            #print associatedA, 'associatedA'
            #print counts, 'counts'
            counter = -1
            for q in counts:
                counter += 1
                if q == [2,3,3] or q == [3,3,2] or q == [3,2,3]:
                    c1 += 1
                    index = counter
                    indexTable.append(index)
                if q == [3,3,4] or q == [3,4,3] or q == [4,3,3]:
                    c2 += 1
                    index = counter
                    indexTable.append(index)
                if q == [2,2,4] or q == [2,4,2] or q == [4,2,2]:
                    c3 += 1
                    index = counter
                    indexTable.append(index)
            if c1 >= 4:
                if c2 >= 2:
                    if c3 >= 2:
                        print indexTable, 'index table'
                        for a in indexTable:
                            print associatedA[a], 'index'

            



