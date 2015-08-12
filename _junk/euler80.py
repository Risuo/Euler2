def findP(table):
  strIn = ''
  for x in table:
    strIn += str(x)
  return int(strIn)


def cycle(n, m): # n == # digits, m == range of square roots
  tally = 0
  for q in xrange(0, m):
    if q not in [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]:
      table = []
      c = q
      for z in xrange(1, n):
        x = 0
        if len(table) > 0:
          p = findP(table)
        else:
          p = 0
        while x*((20*p)+x) <= c:
          x += 1
        k = x-1
        table.append(k)
        y = k*((20*p)+k)
        c = (c-y)*100
      tally += sum(table)
  return tally

print cycle(101, 101)
      