from math import sqrt

def isSquare(n):
    return int(sqrt(n))*int(sqrt(n)) == n

a, b, c, d, e, f = 0, 0, 0, 0, 0, 0
solved = False
result = 0

i = 4


while not solved:
    i += 1
    a = i*i
    if not solved:
        j = 3
        while j < i:
            j += 1
            c = j * j
            f = a - c
            if f >= 0 and isSquare(f):
                if j%2 == 1:
                    kstart = 1
                else:
                    kstart = 2
                k = kstart
                while k < j:
                    k += 2
                    d = k * k
                    e = a - d
                    b = c - e
                    
                    if b >= 0 and e >= 0 and isSquare(b) and isSquare(e):
                        x = (d + c) / 2
                        y = (e + f) / 2
                        z = (c - d) / 2
                        if y != z and z != x and x > y and y > z and z > 0 and y > 0 and x > 0:
                            result = x + y + z
                            solved = True
                            break
print result, x, y, z
