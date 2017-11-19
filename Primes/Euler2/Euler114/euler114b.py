m, n = 3, 50
ways = [1] * (n+1)

for j in range(m, n+1):
    ways[j] = ways[j - 1] + 1
    for k in range(m, j):
        ways[j] += ways[j - k - 1]

print "Minimum block size =", m, "units"
print "A space", n, "units long can be filled", ways[n], "ways"