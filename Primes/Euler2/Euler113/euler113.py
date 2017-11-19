total = 0

for a in xrange(9,0,-1):
    for b in xrange(a+1):
        for c in xrange(b+1):
            for d in xrange(c+1):
                for e in xrange(d+1):
                    for f in xrange(e+1):
                        if f == 0:
                            total += 1
                        else:
                            if a != b or a != c or a != d or a != e or a != f:
                                total += 2
                            else:
                                total += 1
print total, 'this is after the first set (6 digits)'
for a in xrange(9,0,-1):
    for b in xrange(a+1):
        for c in xrange(b+1):
            for d in xrange(c+1):
                for e in xrange(d+1):
                    if e == 0:
                        total += 1
                    else:
                        if a != b or a != c or a != d or a != e:
                            total += 2
                        else:
                            total += 1
print total, 'this is after the second set (+5 digits)'
for a in xrange(9,0,-1):
    for b in xrange(a+1):
        for c in xrange(b+1):
            for d in xrange(c+1):
                if d == 0:
                    total += 1
                else:
                    if a != b or a != c or a != d:
                        total += 2
                    else:
                        total += 1
print total, 'this is after the third set (+4 digits)'                    
for a in xrange(9,0,-1):
    for b in xrange(a+1):
        for c in xrange(b+1):
            if c == 0:
                total += 1
            else:
                if a != b or a != c:
                    total += 2
                else:
                    total += 1
print total, 'this is after the fourth set (+3 digits)'
for a in xrange(9,0,-1):
    for b in xrange(a+1):
        if b == 0:
            total += 1
        else:
            if a != b:
                total += 2
            else:
                total += 1
print total, 'this is after the fifth set (+2 digits)'


print total+9, 'answer'

print 9, 90, 375, 1200, 3279, 7998, 17865
                        

