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
#p1.x = input("Enter x coordinate of the first point of a triangle:")
#p1.y = input("Enter y coordinate of the first point of a triangle:")
p2 = Coordinate ()
#p2.x = input("Enter x coordinate of the second point of a triangle:")
#p2.y = input("Enter y coordinate of the second point of a triangle:")
p3 = Coordinate ()
#p3.x = input("Enter x coordinate of the third point of a triangle:")
#p3.y = input("Enter y coordinate of the third point of a triangle:")

p1.x, p1.y, p2.x, p2.y, p3.x, p3.y = input("Enter three points for a triangle: (commas as delimiters)")

print "Area of triangle is "+str(areaTriangle(p1,p2,p3))






####Wk 2 Qn 4b
#def compoundVal6Months (potIn ,rate):
#    rate = rate/12.0
#    pot = 0.0
#    for x in xrange(6):
#        pot += potIn
#        pot = pot * (1+rate)       
#        #print pot
#    return pot
#
#saving = input("Enter the monthly saving amount:")
#annualRate = input("Enter annual interest rate:")        
#print "After the sixth month, the account value is "+str(compoundVal6Months(saving ,annualRate))