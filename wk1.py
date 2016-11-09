## -*- coding: utf-8 -*-
#print type("This is the first Week!")
#print "This is the first Week!"
#print type(24)
#print 24
#print type(2.4)
#print 2.4
#print type("24")
#print "24"
#print type('2.4')
#print type("""2.4""")
#print type('''2.4''')
#print 10300
#print 10,300
#print 10.300
#print type(10.300)
#
#print int(1.1)
#print int(9.81)
#print int(-9.81)
##print int("9.81")
##print int("9.81m/s2")
#print float("9.81")
#print str(9.81)
#print type(str(9.81))
#print str(int(9.81))
#print type(str(int(9.81)))
#
#message = " What ’s up , Doc ? "
#n = 17
#pi = 3.14159
#pi = 3.14
#
#print message
#print n
#print pi

#
#class Coordinate :
#    x = 3.2
#    y = -1.5
#p1 = Coordinate ()
#p2 = Coordinate ()
#p2.x = 0.3
#p2.y = 1.0
#
#print type(p1)
#print type(p2)
#print type(Coordinate)
#print p1.x, p1.y
#print p2.x, p2.y
#
#print 17-3*7/4+1 
#print 2**2**4*3

#x = 3
#print x,
#x = x + 2
#print x


##Wk 2 Qn 1
#def fToC(f):
#    return (5.0/9)*(f - 32)
#
#print fToC(212)


##Wk 2 Qn 2
#def yearsDays(minutes):
#    return (minutes / 525600), (minutes/1440)%365
#    
#print yearsDays(2000000000)


##Wk 2 Qn 3
#def posVel(v,t):
#    g = 9.81
#    yt = (v*t)-(.5*g*(t**2))
#    dyt = v - g*t
#    return yt, round(dyt, 3)
#    
#print posVel(0.0,5.0)


##Wk 2 Qn 4a
import math

class Coordinate:
    x=0.0
    y=0.0

#expects coordinates
def sideLength(p1,p2):
    return math.sqrt(((abs(p1.x - p2.x)**2) + abs(p1.y - p2.y)**2))

#expects coordinates
def areaTriangle(p1,p2,p3):
    side1 = sideLength(p1,p2)
    side2 = sideLength(p2,p3)
    side3 = sideLength(p3,p1)

    s = (side1 + side2 + side3)/2.0

    return math.sqrt(s*(s-side1)*(s-side2)*(s-side3))

p1 = Coordinate ()
p1.x = input("Enter x coordinate of the first point of a triangle:")
p1.y = input("Enter y coordinate of the first point of a triangle:")
p2 = Coordinate ()
p2.x = input("Enter x coordinate of the second point of a triangle:")
p2.y = input("Enter y coordinate of the second point of a triangle:")
p3 = Coordinate ()
p3.x = input("Enter x coordinate of the third point of a triangle:")
p3.y = input("Enter y coordinate of the third point of a triangle:")

print areaTriangle(p1,p2,p3)

##Wk 2 Qn 4b
def compoundVal6Months (potIn ,rate):
    rate = rate/12
    pot = 0.0
    for x in xrange(6):
        pot += potIn
        pot = pot * (1+rate)       
        #print pot
    return pot

saving = input("Enter the monthly saving amount:")
annualRate = input("Enter annual interest rate:")        
print "After the sixth month, the account value is "+str(compoundVal6Months(saving ,annualRate))