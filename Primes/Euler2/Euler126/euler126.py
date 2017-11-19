
cuboidSolves = {}
solutionSet = set()
count = 0

def cuboid(baseZ, baseY, baseX, targetN, cuboidSolves, solutionSet):
    for x in xrange(1, targetN):
        a = 2*(baseX * baseY) 
        b = (((2*x)-1)*(2*baseX + 2*baseY))*baseZ
        c = (4*((x-1)**2))*baseZ
        solution2 = a + b + c
        if solution2 == 154:
            print baseX, baseY, baseZ, x, 'solution2'
        if solution2 in cuboidSolves:
            cuboidSolves[solution2] += 1
        else:
            cuboidSolves[solution2] = 1
    return cuboidSolves

tested = []

for x in xrange(1,50):
    for y in xrange(1,50):
        for z in xrange(1,50):
            test = sorted([x,y,z])
            if test not in tested:
                tested.append(test)
                y = test[0]
                x = test[1]
                z = test[2]
                cuboid(y,x,z,5,cuboidSolves,solutionSet)


print cuboidSolves[154]