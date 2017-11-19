import re

table = []

#the below regex will only allow numbers with only odd digits to continue into the loop
#^[^2468]*$

count = 0

for x in xrange(10**8,10**9):
    digits = str(x)
    rev = digits[::-1]
    if digits[0] == '0' or rev[0] == '0':
        pass
    if int(rev) < int(digits):
        pass
    else:
        total = str(int(digits)+int(rev))
        if re.match("^[^02468]*$", str(total)):
            count += 2
            #print count
            #print total, rev, digits
print count
        

    