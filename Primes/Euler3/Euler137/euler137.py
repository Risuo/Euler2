print '1120149658760 is the solution, runs as #12 in the code below, which skips actual #s 4, 5, and 6 for real'



from decimal import *
from fractions import Fraction


def fib(k1,k2):
    return [k2,k2+k1]

#Fib = (phi**n - (-phi)**-n)/((2*phi)-1)

#Fib = ((phi**n)-(psi**n))/(5**.5)


#.41421356237
#.50000000000        .08578643762
#.53518375848        .03518375848            .05060267914
#.55424764150        .01906388302            .01611987546
#.56619037896        .01194273746            .00712114556

#solve for x: ((((x*phi)*sqrt5)/(1-(x*phi)))-((x*psi)*sqrt5)/((1-(x*psi))))/5= 2

phi = (1+(2.236067977499789696409173668731276235440618359611525724270897245410520925637804899414414408378782275))/2
psi = ((1-(2.236067977499789696409173668731276235440618359611525724270897245410520925637804899414414408378782275))/2)

def fibs(n):
    return ((phi**n)-(psi**n))/(5**.5)

sqrt5 = 2.236067977499789696409173668731276235440618359611525724270897245410520925637804899414414408378782275

def closedForm(x):
    return ((((x*phi)*sqrt5)/(1-(x*phi)))-((x*psi)*sqrt5)/((1-(x*psi))))/5

#print closedForm(((34**.5)-3)/5)


#for q in xrange(-1,2):
#    for r in xrange(-1,2):
#        for s in xrange(-1,2):
#            a = 89-q
#            b = 5-r
#            c = 8-s
#            x = ((a**.5)-b)/c
#            value = closedForm(x)
#            #print value, round(value), round(value)-value
#            if value > 0:
#                if round(value)-value > 0 and round(value)-value < .0000000001:
#                    print value
#                if round(value)-value < 0 and round(value)-value > -.00000000001:
#                    print value



def closedTwo(x):
    return (x/((x**2)+x-1))/-1

tested = set()
floor = Fraction(1000000,618034)
ceiling = Fraction(100,62)

#74049690, 10th value

count = 2
x = 0

while count < 16:
    x += 1
    for y in xrange(x//floor,x//ceiling):
        #print y, x
        fraction = Fraction(y,x)
        #print fraction, y,x

        value = closedTwo(fraction)
        if value not in tested and value > 0:
            if value == round(value):
                print fraction, value, count
                count += 1
                tested.add(value)
                x *= 2.618
                x = int(x)

#for x in xrange(1,150):
#    print fibs(x), x

    
#k1 = 1
#k2 = 1
#fibonacci = []
#for x in xrange(2500):
#    fibs = fib(k1,k2)
#    fibonacci += [k1]
#    k1 = fibs[0]
#    k2 = fibs[1]
    
    
test = (.6)
power = 0
value = 0
#print test

#for x in xrange(1,1):
#    power += 1
#    b1 = value
#    value += (test**power)*fibs(x)
#    print value, (test**power)*fibs(x), power, value-b1



#1/2 2 1
#3/5 15 2
#8/13 104 3
#55/89 4895 4
#21/34 714 5
#144/233 33552 6
#377/610 229970 7
#987/1597 1576239 8
#2584/4181 10803704 9
#6765/10946 74049690 10



#CHECK IT: Ratio between demoniator and PREVIOUS denomiator approaches phi+1......which is just ridiculous. 