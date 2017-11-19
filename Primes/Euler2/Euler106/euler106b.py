import itertools


def create_subsets(full_set):
    subsets = []
    for i in range(1, len(full_set)):
        subsets.append(itertools.combinations(full_set, i))
    subsets = [list(item) for sublist in subsets for item in sublist]
    return subsets


def test_subsets(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    greater = False
    if s1[0] > s2[0]:
        greater = True

    for i in range(0, len(s1)):
        if s1[i] < s2[i] and greater:
            return True
        elif s1[i] > s2[i] and not greater:
            return True
    return False

145, 236
arr = range(1, 13)

outSet = set()
outSet2 = set()
outTable = []
outTable2 = []
sub_sets = create_subsets(arr)
count = 0
for i in sub_sets:
    for j in sub_sets:
        if i != j and len(i) == len(j) and len(i) > 1 and len(list(set(i) & set(j))) == 0 and j < i:
            if test_subsets(i, j):
                outSet.add(tuple([tuple(j),tuple(i)]))
                count += 1
for x in outSet:
    outTable.append(x)
    
outTable = sorted(outTable)

for x in outTable:
    outSet2.add(x)
    
for x in outSet2:
    outTable2.append(x)
    
outTable2 = sorted(outTable2)
    
#for x in outTable2:
    #print x

print count