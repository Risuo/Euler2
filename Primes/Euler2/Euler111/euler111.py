import itertools
import time
import math

def is_prime(n):
  if type(n) != int and type(n) != long:
    raise TypeError('must be integer')
  if n < 2:
    return False
  ps = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
  def is_spsp(n, a):
    d, s = n-1, 0
    while d % 2 == 0:
      d /= 2; s += 1
    t = pow(a,d,n)
    if t == 1:
      return True
    while s > 0:
      if t == n-1:
        return True
      t = (t*t) % n
      s -= 1
    return False
  if n in ps: return True
  for p in ps:
    if not is_spsp(n,p):
      return False
  return True
  
integers = [0,1,2,3,4,5,6,7,8,9,10]

powersTen = [1, 10**1, 10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9, 10**10]


base9 = 9999999999
base8 = 8888888888
base7 = 7777777777
base6 = 6666666666
base5 = 5555555555
base4 = 4444444444
base3 = 3333333333
base2 = 2222222222
base1 = 1111111111
base0 = 1000000000

baseTable = [base9,base8,base7,base6,base5,base4,base3,base2,base1,base0]

def multiplier(a,b):
    tableOut = []
    for x in a:
        for y in b:
            tableOut.append(x*y)
    return tableOut
def addSub(a,b):
    tableOut = []
    for x in a:
        for y in b:
            if x+y not in tableOut:
                tableOut.append(x+y)
            if x-y not in tableOut:
                tableOut.append(x-y)
    return tableOut

remove1 = multiplier(integers,powersTen)
print len(remove1)
remove2 = addSub(remove1,remove1)
print len(remove2)
remove3 = addSub(remove2,remove1)
print len(remove3)

tableOutsA = []
tableOutsB = []
table2Test = []

for y in baseTable:
    tableTest = []
    for x in remove1:
        value = is_prime((y-x))
        value2 = is_prime(y+x)
        if str((y-x)).count(str(y)[9]) == 9:
            if len(str((y-x))) == 10:
                #print y-x, 'subtraction'
                if y-x not in table2Test:
                    table2Test.append(y-x)
        if str(y+x).count(str(y)[9]) == 9:
            if len(str((y+x))) == 10:
                #print y+x, 'addition'
                if y+x not in table2Test:
                    table2Test.append(y+x)
        if value:
            if str((y-x)).count(str(y)[9]) == 9:
                if len(str((y-x))) == 10:
                    if (y-x) not in tableTest:
                        tableTest.append((y-x))
        if value2:
            if str(y+x).count(str(y)[9]) == 9:
                if len(str(y+x)) == 10:
                    if y+x not in tableTest:
                        tableTest.append(y+x)
    if len(tableTest) > 0:
        tableOutsA.append(tableTest)
    else:
        tableOutsA.append(tableTest)
        tableOutsB.append(y)
print tableOutsA, 'tableOutsA, or 9 instances'

tableOutsC = []
tableOutsD = []

#print len(table2Test)

#for y in tableOutsB:
 #   tableTest = []
  #  for x in table2Test:
   #     for z in remove1:
    #        valueTest = x+z  
     #       value = is_prime((y-((valueTest))))
      #      value2 = is_prime(y+x+z)
       #     if value:
        #        if len(str((y-((valueTest))))) == 10:
         #           if str((y-((valueTest)))).count(str(y)[9]) == 8:
          #              if (y-((valueTest))) > 0:
           #                 if (y-((valueTest))) not in tableTest:
            #                    tableTest.append((y-((valueTest))))
#            if value2:
 #               if len(str(y+x+z)) == 10:
  #                  if str(y+x+z).count(str(y)[9]) == 8:
   #                     if y+x+z not in tableTest:
    #                        tableTest.append(y+x+z)
#    for x in remove1:
 #       for z in remove1:
  #          valueTest = x+z  
   #         value = is_prime((y-((x-z))))
    #        value2 = is_prime(y+x+z)
     #       if value:
      #          if len(str((y-((x-z))))) == 10:
       #             if str((y-((x-z)))).count(str(y)[9]) == 8:
        #                if (y-((x-z))) > 0:
         #                   if (y-((x-z))) not in tableTest:
          #                      tableTest.append((y-((x-z))))
           # if value2:
            #    if len(str(y+x+z)) == 10:
             #       if str(y+x+z).count(str(y)[9]) == 8:
              #          if y+x+z not in tableTest:
               #             tableTest.append(y+x+z) 
#    if len(tableTest) > 0:
 #       tableOutsC.append(tableTest)
  #  else:
   #     tableOutsD.append(y)
        
        
#print tableOutsC, 'tableOutsC, or 8 instances'
#print tableOutsD, 'still need'

#tableOutsE = []
#tableOutsF = []





#for y in tableOutsD:
#    tableTest = []
#    for x in remove1:
#        for z in remove1:
#            for a in remove1:
#                value = is_prime(y-x-z-a)
#                value2 = is_prime(y+x+z+a)
#                if value:
#                    if len(str(y-x-z-a)) == 10:
#                        if str(y-x-z-a).count(str(y)[7]) == 7:
#                            tableTest.append(y-x-z-a)
#                if value2:
#                    if len(str(y+x+z+a)) == 10:
#                        if str(y+x+z+a).count(str(y)[7]) == 7:
#                            tableTest.append(y+x+z+a)
#    if len(tableTest) > 0:
#        tableOutsE.append(tableTest)
#    else:
#        tableOutsF.append(y)

#print tableOutsE, 'or 7 instances'
#tableOutsG = []
#tableOutsH = []

#for y in tableOutsB:
#    tableTest = []
#    for x in remove1:
#        for z in remove1:
#            for a in remove1:
#                for b in remove1:
#                value = is_prime(y-(x-(z-(a))))
#                value2 = is_prime(y+x+z+a)
#                if value:
#                    if y-(x-(z-(a))) not in tableTest:
#                        if y-(x-(z-(a))) > 0:
#                           if len(str(y-(x-(z-(a))))) == 10:
#                                if str(y-(x-(z-(a)))).count(str(y)[7]) == 8:
#                                    tableTest.append(y-(x-(z-(a))))
#                                    print y-(x-(z-(a))), 'value'
#                if value2:
#                    if y+x+z+a not in tableTest:
#                        if len(str(y+x+z+a)) == 10:
#                            if str(y+x+z+a).count(str(y)[7]) == 8:
#                                tableTest.append(y+x+z+a)
#                                print y+x+z+a, 'value2'
#    if len(tableTest) > 0:
#        tableOutsG.append(tableTest)
#    else:
#        tableOutsH.append(y)

#print tableOutsG, 'or 8 instances'

value = 0

for x in tableOutsA:
    for y in x:
        #print y, value
        value += y
#for z in tableOutsC:
 #   for a in z:
  #      print a, value
   #     value += a
        
print value