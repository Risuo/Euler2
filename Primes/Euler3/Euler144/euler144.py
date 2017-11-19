import numpy
from numpy import roots as roots


running = True


class Ellipse:
    
    def __init__(self, table):#p1x, p1y, p2x, p2y):
        p1x = table[0]
        p1y = table[1]
        p2x = table[2]
        p2y = table[3]
    
        self.slope = (p2y-p1y)/(p2x-p1x)
        self.tangent = -4*(p2x/p2y)
        self.normal = -1/(self.tangent)
        m1 = self.normal
        m2 = self.slope
        m =  (m1*2 + (m2 * m1**2 - m2)) / (2*m1*m2 - m1**2 + 1)
        self.reflectSlope = m
        #y = mx + b
        #y-mx = b
        #b = y-mx
        b1 = p2y - (m*p2x)
        #print b1
        a = (m**2)+4
        b2 = 2*(b1*m)
        c = (b1**2)-100
        #print a, b2, c
        self.xIntercepts = numpy.roots([a,b2,c])
        #print self.xIntercepts, p2x
        for a in self.xIntercepts:
            if abs(a-p2x) > 1*10**-10:
                b = -(-(m*a)-b1)
                if a < 0.01 and a > -0.01 and b > 9.999:
                    global running
                    running = False
                    self.newPoints = [p2x, p2y, a, b]
                    break
                else:
                    #print [p2x, p2y, a, b]
                    self.newPoints = [p2x, p2y, a, b]
            
        
            
            
            #p2y2 = -(-(m*a)-b1)
            #print p2y2, a
            

        # need to find p2y now, and then we can just need to loop it!!!
        
        

        
        
# ((2 * M1) + (M2 * pow(M1, 2)) - M2) / (2 * M1 * M2 - pow(M1, 2) + 1);
# M3 = (M1^2 * M2 + 2*M1 - M2) / (1 + 2*M1*M2 - M1^2) #        
        
table1 = [0.0, 10.1, 1.4, -9.6]
        

    
count = 0
while running:
    test = Ellipse(table1).newPoints
    count += 1
    print test, count
    global table1
    table1 = test
    
    



