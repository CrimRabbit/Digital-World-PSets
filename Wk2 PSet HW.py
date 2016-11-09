import math
##Wk 2 Qn 1
def cToF(c):
    return c*(9.0/5)+32

print cToF(100)

##Wk 2 Qn 2
def areaCylinder(rad,leng):
    area = rad * rad * math.pi
    volume = area * leng
    return area, volume
    
print areaCylinder(2.2, 5.0)

##Wk 3 Qn 3
def windChillTemp(ta, v):
    ta = float(ta)
    v = float(v)

    if (ta < -58 or ta > 41):
        print ("Error in Outside Temp")
        return None
    if (v < 2):
        print ("Error in Wind Speed")
        return None
        
    return 35.74 + 0.6215*ta - (35.75*(v**0.16)) + (0.4275*ta*(v**0.16))
    
print windChillTemp(2.2,4)

##Wk 3 Qn 4
#expects weight in pounds & height in inches
def bmi(weight,height):
    weightKg = 0.45359237*float(weight)
    heightM = 0.0254*float(height)
    
    return weightKg / (heightM**2)

print bmi (120 ,60)


##Wk 3 Qn 5
#float, float, int
def investmentVal(amount, annualRate, years):
    return round(amount * (1+annualRate/12/100)**(years*12),2)
    
print investmentVal (1000,4.25,1)
  