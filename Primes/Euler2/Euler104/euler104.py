#for the last 10 digits: mod 10^10 (mod 10 = last 1, mod 100 [10^2] = last 2, mod 1000 [10^3] = last 3, etc)

#for the first 10: while value > 10^10, value = value/10^10
import math
import decimal




print 'okay world!'  

decimal.getcontext().prec = 1000
phi = (1+decimal.Decimal(5).sqrt())/decimal.Decimal(2)
#print phi

def fib(n):
    final = math.floor((phi**n)/(decimal.Decimal(5).sqrt()))
    return final

def fibonacci_last9(n):
    final = fib(n)
    return str(int(final)%10**10)
    
def fibonacci_first9(n):
    final = fib(n)
    while final > 10**9:
        final = final/10
    return str(int(final))
    
def pandigitalCheck(fibo):
    for a in fibo:
        if fibo.count(a) > 1:
            output = False
            break
    if output == True:
        return True
    else:
        return False
    
#print fibonacci_first9(2749)
#print fibonacci_last9(2749)
print fib(2749)

print pandigitalCheck(fibonacci_first9(2749))

