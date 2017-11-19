
answer = 0

for a in xrange(3,1001):
    table = []
    for n in xrange(1500):
        table.append(int((((a-1)**n)+((a+1)**n))%(a**2)))
    print max(table), a, table.index(max(table))
    answer += max(table)
    
print answer