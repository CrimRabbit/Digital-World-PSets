import math

def trapezoidal(a,b):
    res = (b-a)*(funct(b) + funct(a))/2  
    return round(res,2)

def funct(a):
    return (a**3)*math.exp(-1)
     
    
print trapezoidal(6,2.5)