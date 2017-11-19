import itertools

doubles = ['D1','D2','D3','D4','D5','D6','D7','D8','D9','D10','D11','D12','D13','D14','D15','D16','D17','D18','D19','D20','D25']
triples = ['T1','T2','T3','T4','T5','T6','T7','T8','T9','T10','T11','T12','T13','T14','T15','T16','T17','T18','T19','T20']
singles = ['S1','S2','S3','S4','S5','S6','S7','S8','S9','S10','S11','S12','S13','S14','S15','S16','S17','S18','S19','S20','S25']

oneThrows = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,50]


twoThrows2 = [list(itertools.product(triples,doubles))]
twoThrows3 = [list(itertools.product(singles,doubles))]
twoThrows4 = [list(itertools.product(doubles,doubles))]
twoThrows = twoThrows2+twoThrows3+twoThrows4


subTotalB = [list(itertools.product(singles,triples))]
subTotalE = [list(itertools.product(singles,doubles))]
subTotalD = [list(itertools.product(triples,doubles))]
subTotalF = [list(itertools.combinations_with_replacement(doubles,2))]
subTotalI = [list(itertools.combinations_with_replacement(triples,2))]
subTotalC = [list(itertools.combinations_with_replacement(singles,2))]
totalB = []
totalC = []
totalD = []
totalE = []
totalF = []
totalI = []

for a in subTotalB:
    for b in a:
        totalB.append(b)
for a in subTotalC:
    for b in a:
        totalC.append(b)
for a in subTotalD:
    for b in a:
        totalD.append(b)
for a in subTotalE:
    for b in a:
        totalE.append(b)
for a in subTotalF:
    for b in a:
        totalF.append(b)
for a in subTotalI:
    for b in a:
        totalI.append(b)




def combine(table):
    tempTable = []
    outTable = []
    for x in table:
        for y in x:
            for z in y:
                if z not in doubles:
                    for q in z:
                        tempTable.append(q)
            tempTable.append(z)
            outTable.append(tempTable)
            tempTable = []
    return outTable


threeThrowsBA = [list(itertools.product(totalB,doubles))]              
threeThrowsCA = [list(itertools.product(totalC,doubles))]
threeThrowsDA = [list(itertools.product(totalD,doubles))]
threeThrowsEA = [list(itertools.product(totalE,doubles))]
threeThrowsFA = [list(itertools.product(totalF,doubles))]
threeThrowsIA = [list(itertools.product(totalI,doubles))]

threeThrowsB = combine(threeThrowsBA)
threeThrowsD = combine(threeThrowsDA)
threeThrowsC = combine(threeThrowsCA)
threeThrowsE = combine(threeThrowsEA)
threeThrowsF = combine(threeThrowsFA)
threeThrowsI = combine(threeThrowsIA)

threeThrows = threeThrowsB+threeThrowsD+threeThrowsC+threeThrowsE+threeThrowsF+threeThrowsI

twoThrowsOut = set()
for x in twoThrows:
    for y in x:
        twoThrowsOut.add(y)
        
threeThrowsOut = threeThrows


print len(oneThrows), 'total single throw double outs'
print len(twoThrowsOut), 'total double throw double outs'
print len(threeThrowsOut), 'total triple throw double outs'
print len(threeThrowsOut)+len(twoThrowsOut)+len(oneThrows), 'total discrete double-out possibilities'



def sumTest(throw):
    throw1 = 0
    throw2 = 0
    throw3 = 0
    if len(throw) == 2:
        if throw[1] in triples or throw[1] in singles:
            return 1000
        else:
            if throw[0] in singles:
                if throw[0] == 'S25':
                    throw1 = 25
                else:
                    throw1 = singles.index(throw[0])+1
            if throw[0] in doubles:
                if throw[0] == 'D25':
                    throw1 = 50
                else:
                    throw1 = (doubles.index(throw[0])+1)*2
            if throw[0] in triples:
                throw1 = (triples.index(throw[0])+1)*3
            if throw[1] == 'D25':
                throw2 = 50
            else:
                throw2 = (doubles.index(throw[1])+1)*2
        return throw1+throw2
    if len(throw) == 3:
        if throw[2] in triples or throw[2] in singles:
            return 1000
        else:
            if throw[0] in singles:
                if throw[0] == 'S25':
                    throw1 = 25
                else:
                    throw1 = singles.index(throw[0])+1
            if throw[0] in doubles:
                if throw[0] == 'D25':
                    throw1 = 50
                else:
                    throw1 = (doubles.index(throw[0])+1)*2
            if throw[0] in triples:
                throw1 = (triples.index(throw[0])+1)*3
            if throw[1] in singles:
                if throw[1] == 'S25':
                    throw2 = 25
                else:
                    throw2 = singles.index(throw[1])+1
            if throw[1] in doubles:
                if throw[1] == 'D25':
                    throw2 = 50
                else:
                    throw2 = (doubles.index(throw[1])+1)*2
            if throw[1] in triples:
                throw2 = (triples.index(throw[1])+1)*3
            if throw[2] == 'D25':
                throw3 = 50
            else:
                throw3 = (doubles.index(throw[2])+1)*2
        return throw1+throw2+throw3
    
    
    
    
    
        
throwsOk = set()


testValue = 100

for x in twoThrowsOut:
    if sumTest(x) < testValue:
        throwsOk.add(x)
for x in oneThrows:
    if x < testValue:
        throwsOk.add(x)
for x in threeThrowsOut:
    if sumTest(x) < testValue:
        throwsOk.add(tuple(x))


throwsOkTest = []

for x in throwsOk:
    throwsOkTest.append(x)
    


print len(throwsOk), 'answer here'
print len(throwsOkTest), 'check here'

