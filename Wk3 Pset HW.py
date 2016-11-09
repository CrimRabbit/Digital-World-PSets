#Qn1
def check2(n1, n2, n3, x):
    if(x > n1 and x > n2 and x < n3):
        return True
    return False
    
#print check2(1,10,8,7)

#Qn2
def fToC(F):
    C = (F-32)*float(5)/9
    return C

def cToF(C):
    F = C*float(9)/5 + 32
    return F
    
def tempConvert(metric, num):
    if(metric == 'C'):
        return fToC(num)
    elif(metric == 'F'):
        return cToF(num)
    else:
        return None
        
#print tempConvert('F', 32)

#Qn3
def getEvenNumber(inList):
    try:
        newList = []
        for x in xrange(len(inList)):
            if(inList[x] % 2 == 0):
                newList.append(inList[x])
        return newList
    except IndexError:
        return []
        
#print getEvenNumber([11 ,22 ,33 ,44 ,55])

#Qn4
def isPrime(inNum):
    #Referencing pseudocode off wikipedia - more efficient than checking downwards by factorial
    #
    if (inNum <= 1):
        return False
    elif (inNum <= 3):
        return True
    elif (inNum % 2 == 0 or inNum % 3 == 0):
        return False
    i = 5
    while(i*i <= inNum):
        if (inNum % i == 0 or inNum % (i+2) == 0):
            return False
        i += 6
    return True
    
#print isPrime(3499)

#Qn5
import math
def approx_ode(h,t0,y0,tn):
######### h - step size
######### t0 - initial t value (at step 0)
######### y0 - initial y value (at step 0)
######### tn - t value at step n

######### Add you code below this line
######### Return your answer correct to 3 decimal places
    step = 0
    y=y0
    while(step < tn-0.05):
        y = y + h*f(step,y)
        step += h
    return round(y,3)

#def y(h, tn):
#    if (tn == 0):
#        return 1
#    return y(h,tn-1) + h*f(tn, y(h,tn-1)) 

######### Ignore code below this line ######################################
def f(t, y):
    return 3.0+math.exp(-t)-0.5*y
######### Resume code ######################################
#suma = 0.0
#for x in xrange(3):
#    suma += approx_ode(0.1,0,0,3)
#    print suma
print approx_ode(0.1,0,1,5)