import fractions

#for solution to Euler 112, set bouncy to 1, nonBouncy to 100
bouncy = 0
nonBouncy = 0


number = 0

def strToArray(string):
    table = []
    for x in str(string):
        table.append(int(x))
    return table

test =  strToArray(45118)


def theTest(testB):
    test = strToArray(testB)
    busted = 'busted'
    bouncy = 'bouncy'
    nonBouncy = 'nonBouncy'
    index = 0
    decreasing = False
    increasing = False
    theSame = False
    if test.count(test[0]) == len(test):
        #print 'theSame', test
        return nonBouncy
    for x in test:
        index += 1
        if index < len(test):
            toTest = test[index]
            #print toTest, x, test, 'toTest, x, test'
            if toTest < x:
                decreasing = True
            if toTest > x:
                increasing = True
    if increasing == True:
        if decreasing == True:
            #print 'bouncy', test
            return bouncy
        elif decreasing == False:
            #print 'increasing', test
            return nonBouncy
    elif increasing == False:
        if decreasing == True:
            #print 'decreasing', test
            return nonBouncy


x = 8999
while x < 9999:
    x += 1
    testing = theTest(x)
    if testing == 'bouncy':
        bouncy += 1
        #print bouncy
    if testing == 'nonBouncy':
        nonBouncy += 1
        #print nonBouncy
    if testing == 'theSame':
        nonBouncy += 1
        #print nonBouncy
    #print bouncy, 'bouncy', nonBouncy+bouncy, 'nonBouncy+bouncy', fractions.Fraction(bouncy)/fractions.Fraction(nonBouncy+bouncy)
    #if x == 539:
    #    break
        
print bouncy, nonBouncy, fractions.Fraction(bouncy)/fractions.Fraction(nonBouncy+bouncy)


