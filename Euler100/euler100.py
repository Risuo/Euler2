from fractions import Fraction
import math


topEnd = 708333333333
botEnd = 705882352941



for x in xrange(2, 250000):
  total = x
  firstTest = math.floor(total*.7) 
  secondTest = firstTest-1
  if Fraction(firstTest*secondTest)/Fraction(total*(total-1)) == Fraction(1)/Fraction(2): 
    print firstTest, secondTest, 'answer here'
  else:
    while firstTest + 1 < math.ceil(total*.8):
      firstTest += 1
      secondTest = firstTest-1
      if Fraction(firstTest*secondTest)/Fraction(total*(total-1)) == Fraction(1)/Fraction(2): 
        print firstTest, secondTest, total, 'answer here' 