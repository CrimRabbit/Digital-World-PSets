import math

class Time:
    def __init__(self, hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def getHour(self):
        return self.hour
    def getMinute(self):
        return self.minute
    def getSecond(self):
        return self.second
        
    def setTime(self, elapsedTime):
        self.second = elapsedTime % 60
        self.minute = (elapsedTime / 60)%60
        self.hour = elapsedTime / 3600
        while self.hour >= 12:
            self.hour -=12

class Account:    
    def __init__(self,name,number,balance):
        self.name = name
        self.number = number
        self.balance = balance
        
    def __str__(self):
        return str(self.name)+", "+str(self.number)+", balance: "+str(self.balance)
        
    def deposit(self,amt):
        self.balance += amt
    def withdraw(self,amt):
        self.balance -= amt
    
class Diff:
    def __init__(self,f, h=0.1):
        self.f = f
        self.h = h
    def __call__(self, x):
        return float(((f(x+self.h))-f(x))/self.h)
    
def f(x):
    return math.log(x)

#df = Diff(f,0.5)
#print df(10.0)

#For Test case 2: return a tuple with coeff list and evaluated value
import copy
class Polynomial:
    def __init__(self,coeff):
        self.coeff = coeff
    #compute the polynomial    
    def __call__(self,coeff):
        result = 0.0
        #coeff1 * x^0 + + coeff2 * x^1 till end of poly 
        for y in xrange(len(self.coeff)):
            result += self.coeff[y]*(coeff**y)
        return int(result)    
    def __add__(self, tgt):
        #return the sum of x & y of self and target to add with in new polynomial
        #start with longer polynomial, loop with shorter to add
        if(len(self.coeff) < len(tgt.coeff)):
            shorter = copy.deepcopy(self)
            longer = copy.deepcopy(tgt)
        else:
            longer = copy.deepcopy(self)
            shorter = copy.deepcopy(tgt)
        
        for i in xrange(len(shorter.coeff)):
            longer.coeff[i] += shorter.coeff[i]
        return longer        
        
    def __sub__(self,tgt):
       
        tgtList = [x*-1 for x in tgt.coeff]
        return self+Polynomial(tgtList)
        
        #something abit off
        #first = copy.deepcopy(self)
        #second = copy.deepcopy(tgt)
        #if(len(first.coeff) < len(second.coeff)):
        #    for i in xrange(len(first.coeff)):
        #        first.coeff[i] -= second.coeff[i]
        #    for i in xrange(len(first.coeff),len(second.coeff)):
        #        first.coeff.append(second.coeff[i])
        #else:
        #    for i in xrange(len(second.coeff)):
        #        first.coeff[i] -= second.coeff[i]
        #return first
        
    def __mul__(self,tgt):
        newCoeff = len(self.coeff) + len(tgt.coeff)
        returnable = [0 for coeff in xrange(newCoeff-1)]
        
        for z in xrange(len(self.coeff)):
            for y in xrange(len(tgt.coeff)):
                i = z+y
                returnable[i] += self.coeff[z]*tgt.coeff[y]
        return Polynomial(returnable)
        
    def differentiate(self):        
        #no return
        self.coeff =[ i*self.coeff[i] for i in range(1,len(self.coeff))]
        
    def derivative(self):
        return Polynomial([ i*self.coeff[i] for i in range(1,len(self.coeff))])
        
p = Polynomial([1,1])
p2 = Polynomial([0,1,0,0,-6,-1])
p3 = p - p2
print p.coeff
print p.coeff
print p3.coeff
print Polynomial(p3.coeff)

#p4 = Polynomial([2,4,6,8,10])
#p4.differentiate()
#print p4.coeff
#print p4.derivative().coeff