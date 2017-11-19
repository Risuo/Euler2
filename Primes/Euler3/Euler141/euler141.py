from fractions import Fraction


table = []
for x in xrange(2,10**4):
    table.append(x**2)
    
limit = 1

for square in table:
    #print square, 'testing this number here'
    for x in xrange(2,square):
        a = square%x
        b = square/x
        c = x
        #print a, b, c, square
        if a>b or c>b or c>square**.5:
            #print 'broke here'
            break
        values = sorted([a,b,c])
        if a > 0:
            if Fraction(values[1])/Fraction(values[0])*values[1] == values[2]:
                print a, b, c, square
                break
