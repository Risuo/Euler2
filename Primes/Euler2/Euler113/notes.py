total = 0
for a in xrange(9,0,-1):
    for b in xrange(a+1):
        #for c in xrange(b+1):
            #for d in xrange(c+1):
             #   for e in xrange(d+1): 
                    if b == 0:
                        total += 1
                    else:
                        if a != b: #or a != c:# or a != d or a != e:
                            total += 2
                        else:
                            total += 1
                    print a, b, total