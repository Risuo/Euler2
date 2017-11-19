squares = [[n**2, n, 2] for n in xrange(2,20000)]

cubes = [[n**3, n, 3] for n in xrange(2,20000)]

fours = [[n**4, n, 4] for n in xrange(2,20000)]

fives = [[n**5, n, 5] for n in xrange(2,20000)]

sixes = [[n**6, n, 6] for n in xrange(2,20000)]

sevens = [[n**7, n, 7] for n in xrange(2,20000)]

eights = [[n**8, n, 8] for n in xrange(2,20000)]

powers = squares+cubes+fours+fives+sixes+sevens+eights

powers = sorted(powers)

def sum_digits(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r


count = 1
while count < 31:
    for x in powers:
        if sum_digits(x[0]) == x[1]:
            print x, count
            count += 1

