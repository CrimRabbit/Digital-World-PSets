import math 

class Triangle:

    def __init__(self, color="green", filled=True, side1=1.0,side2=1.0,side3=1.0):
        self.color = color
        self.filled = filled
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        
    def getColor(self):
        return self.color
    def setColor(self,inColor):
        self.color = inColor
        
    def getSide1(self):
        return self.side1
    def getSide2(self):
        return self.side2
    def getSide3(self):
        return self.side3
        
    def getArea(self):
        s = (self.getSide1() + self.getSide2() + self.getSide3())/2
        return math.sqrt(s*(s-self.getSide1())*(s-self.getSide2())*(s-self.getSide3()))
    
    #def getArea(self):
    #    s = (self.getSide1() + self.getSide2() + self.getSide3())/2
    #    s1 = s-self.getSide1()
    #    s2 = s-self.getSide2()
    #    s3 = s-self.getSide3()
    #    return math.sqrt(s*s1*s2*s3)
        
#t = Triangle()
#print t.getColor()
#g = Triangle("blue")
#print g.getColor()
#g.setColor("red")
#print g.getColor()

t = Triangle(side1=4.0,side2=3.0,side3=5.0)
print(t.getSide1())1
print t.filled
print t.getArea()
