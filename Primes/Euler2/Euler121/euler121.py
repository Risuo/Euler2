import itertools
import math
import fractions

def testPull(table):
    losses = 0
    wins = 0
    for x in table:
        if x.count('R') >= x.count('B'):
            losses += 1
        else:
            wins += 1
        print x.count('R'), x.count('B'), x
    return losses, wins


#table1 = (itertools.product('RB', repeat = 2))
#print testPull(table1), 'table 1'
#table2 = (itertools.product('RRB', repeat = 3))
#print testPull(table2)
table3 = (itertools.combinations_with_replacement('RBRRRRRR', 3))
print testPull(table3), 'table3'
#table4 = (itertools.product('RRRRB', repeat = 5))
#print testPull(table4)
#table5 = (itertools.combinations_with_replacement('RRRRRB', 5))
#print testPull(table5)
#table6 = (itertools.combinations_with_replacement('RRRRRRB', 6))
#print testPull(table6)
#table7 = (itertools.combinations_with_replacement('RRRRRRRB', 7))
#print testPull(table7)
#table8 = (itertools.combinations_with_replacement('RRRRRRRRB', 8))
#print testPull(table8)
#table9 = (itertools.combinations_with_replacement('RRRRRRRRRB', 9))
#print testPull(table9)
#table10 = (itertools.combinations_with_replacement('RRRRRRRRRRB', 10))
#print testPull(table10)
#table11 = (itertools.combinations_with_replacement('RRRRRRRRRRRB', 11))
#print testPull(table11)


#table12 = (itertools.combinations_with_replacement('RRRRRRRRRRRRB', 12))
#print testPull(table12)
#table13 = (itertools.combinations_with_replacement('RRRRRRRRRRRRRB', 13))
#print testPull(table13)
#table14 = (itertools.combinations_with_replacement('RRRRRRRRRRRRRRB', 14))
#print testPull(table14)
#table15 = (itertools.combinations_with_replacement('RRRRRRRRRRRRRRRB', 15))
#print testPull(table15)

(1, 1)
(5, 1)
(16, 4)
(65, 5)
(231, 21)
(896, 28)
(3312, 120)
(12705, 165)
(47905, 715)
(183755, 1001)
(701064, 4368)
(2697968, 6188)
(10373468, 27132)
(40077840, 38760)
(154946976, 170544)
#249052 out of 20922789888000 are winning hands

print fractions.Fraction(20922789888000)/fractions.Fraction(249053)
print 20922789888000/249053
print fractions.Fraction(120)/fractions.Fraction(11)




        
















