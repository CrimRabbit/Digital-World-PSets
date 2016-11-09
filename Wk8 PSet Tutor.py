import math
import time

class Coordinate:
    def __init__(self,x=0,y=0):
        self.setXY(x,y)
        
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getXY(self):
        return self.x,self.y
    def setXY(self,x,y):
        self.x = x
        self.y = y    
        
    def getMagnitude(self):
        return math.sqrt((self.x)**2 + (self.y)**2)
        
        
class Square:
    def __init__(self,inDimen):
        self.x = (inDimen)
    def __str__(self):
        return "Square of height and width "+str(self.x)+"."
    
    def getArea(self):
        return float(self.x*self.x)
    def setArea(self,inDimen):
        self.x = math.sqrt(inDimen)


class StopWatch:
    def __init__(self):
        self.start()
    
    def getStartTime(self):
        return self.startTime
    def getEndTime(self):
        return self.endTime
        
    def start(self):
        self.startTime = time.time()
        self.endTime = -1
    def stop(self):
        self.endTime = time.time()
    def getElapsedTime(self):
        if self.endTime != -1:
            return int((self.endTime - self.startTime)*1000)


########## Define your class Line below this line ###########
class Line:
    def __init__(self,c0,c1):
        self.c = c0
        self.m = c1
    def __call__(self,x):
        return float(self.m*x + self.c)
        
    def table(self,L,R,n):
        if n == 0:
            return "Error in printing table"
        elif L==R:
            return "%10.2f%10.2f\n" % (round(L,2),round(self(L),2))
        n -= 1
        R = (float(R)-L)/n
        printable = ""
        for x in xrange(n+1):
            point = float(L+R*x)
            printable1 = "%10.2f" % round(point,2)
            printable2 = "%10.2f\n" % round(self(point),2)
            printable += printable1 + printable2
        return printable
        
########## Ignore the code below this line ##################

def testLine(c0,c1,x,L,R,N):
    line=Line(c0,c1)
    return line(x),line.table(L,R,N)

line = Line(3,4)
print line(2)
print line.table(1,1,15)

#print testLine(3,4,2,1,1,15)