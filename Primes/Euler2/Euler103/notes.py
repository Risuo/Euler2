# condition a) the sum of every subset a through g is unique
# condition b) for any two subsets, the subset of more elements must have a larger sum of the subset elements


# S(B) != S(C)
# if elementS(B) > elementS(C), then sumS(B) must be > sumS(C)

consequences:
    the two smallest numbers must be greater in sum than the single largest numbers
    the three smallest numbers must be greater in sum than the largest number & second largest number
    the four smallest numbers must be greater in sum than the largest number & second largest number & third largest number
    
    a+b > g
    a+b+c > f+g
    a+b+c+d > e+f+g
    
    
when choosing values, first choose a & b, then determine a max for g, which is (a+b)-1


the pupose is to satisfy the qualifications, while also minimizing sumS(A), all of the elements of the set

                                '27'
                            1       '37'                        1
    0                   1       2       '40'                    3
    1              2       3       4        '39'                9
    1           3       5       6       7       '35'            21
    3       6       9       11      12      13      '25'        51
    5   11      18      19      20      22      25      'x'    115
    a       b       c       d       e       f       g
    
    
    24      29      31      32      33      34      48

        
    24+30 (54) > 49
    24+30+31 (85) > 49+34 (83)
    24+30+31+32 (117) > 33+34+49 (116)
    
    
Then test each subset sum:
    
    ac,  bd/be/bf/bg
    ad,  bc/be/bf/bg/ce/cf/cg
    ae,  bc/bd/bf/bg/cd/cf/cg/df/dg
    af,  bc/bd/be/bg/cd/ce/cg/de/dg/eg
    acd, bef/beg/bfg/efg
    ace, bdf/bdg/bfg/dfg
    acf, bde/bdg/beg/deg
    acg, bde/bdf/bef/def
    
    
    
    
from below here:


def isTriangle(A,B,C):
    if B[0] and B[1] and C[0] and C[1] != 0:
        slopeB = abs(B[0]-A[0])/abs(B[1]-A[1])
        slopeC = abs(C[0]-A[0])/abs(C[1]-A[1])
        if slopeB == slopeC:
            return False
    elif B[1] == C[1] == A[1] or B[0] == C[0] == A[0]:
        return False
    else:
        return True

def lineLength(p1,p2):
    a = abs(p1[0]-p2[0])
    b = abs(p1[1]-p2[1])
    return math.sqrt(a**2+b**2)


def isRightTriangle(A,B,C): #find three segments, AB, AC, BC
    AB = lineLength(A,B)
    AC = lineLength(A,C)
    BC = lineLength(B,C)
    table = sorted([AB, AC, BC], reverse=True)
    if table[0] == table[1]:
        return False
    else:
        if math.sqrt(table[1]**2+table[2]**2) == table[0]:
            return True


def threePointTest(coordinates):
    A = (0,0)
    B = coordinates[0]
    C = coordinates[1]
    if isTriangle(A,B,C):
        return True
    
    
    #return A, B, C
count = 0
for x in table2:
    if threePointTest(x):
        A = (0,0)
        B = x[0]
        C = x[1]
        if isRightTriangle(A,B,C):
            count += 1
        
print count