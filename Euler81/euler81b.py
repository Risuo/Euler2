from timeit import timeit

def solve():
  a = [map(int, m.split(',')) for m in open('euler81Data', 'r').read().split('\n')]
  n, m = len(a), len(a[0])
  for i in xrange(n):
    for j in xrange(m):
      a[i][j] += min(a[i-1][j], a[i][j-1]) if i*j > 0 else \
        (a[i-1][j] if i else (a[i][j-1] if j else 0))
  print a[-1][-1] # this is == a[len(a)-1][len(a)-1
   
print timeit(solve, number = 1), 's'