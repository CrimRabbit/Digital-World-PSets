#Qn1
def mayIgnore(item):
    if(type(item) is int):
        item += 1
        return item
    return None
    
#print mayIgnore("4")

#Qn2
def myReverse(list1):
    newList = []
    for x in xrange(len(list1)):
        newList.append(list1[-(x+1)])
    return newList
    
#print myReverse(["e", 4, 6.0, 'wololo'])

#Qn3
import math
def piR(n):
    nSum = 0.0
    for k in xrange(0,n):
        nSum += ((math.factorial(4*k)) * (1103+26390*k)) / (((math.factorial(k))**4) * (396.0**(4*k)))
    return (((2*math.sqrt(2.0))/9801) * (nSum))**-1

print piR(2)

#Qn4
def getGCD(a,b):
#using pesudo off wiki
    d = 0
    while(a%2 == 0 and b%2 == 0):
        a = a/2
        b = b/2
        d += 1
    while(a != b):
        if(a%2==0):
            a /= 2
        elif(b%2==0):
            b /= 2
        elif(a>b):
            a = ((a-b)/2)
        else:
            b = ((b-a)/2)
    return a*2**d

print getGCD(10,20)