def reverse(s):
    returnable = ""
    for x in xrange(1,len(s)+1):
        returnable += s[-x]
    return returnable 
      
#print reverse("I have no time for games.")

#import string
def isValidPassword(password):
    #validChar = set(string.ascii_letters + string.digits)
    
    #should have better way
    numCount = 0
    for x in xrange(len(password)):
        if(password[x].isdigit()):
            numCount+=1
    if (password.isalnum()) and (len(password) >= 8) and (numCount >= 2):
        return True
    #if (set(password) <= validChar) and (len(password) >= 8) and (numCount >= 2):
    #    return True
    return False      
    
#print isValidPassword("bctwe24wesa")

def prefix(s1,s2):
    tgt = [s1,s2]
    for i,x in enumerate(min(tgt)):
        if(x != max(tgt)[i]):
            return min(tgt)[:i]
    return min(tgt)     

#print prefix('crossessssssss','crossesss')
import math
class Coordinate:
    x = 0 
    y = 0

def read2columns(f):
    f=open(f,"r")
    #f.read()
    biggest = Coordinate()
    smallest = Coordinate()
    
    for line in f:
        curr = Coordinate()
        linSplit = line.split(".")
        curr.x = (float((linSplit[0]+"."+linSplit[1][:4]).replace(" ","")))
        curr.y = (float((linSplit[1][5:]+"."+linSplit[2]).replace(" ","")))
        if(testMag(curr) > testMag(biggest)):
            biggest = curr
        elif(testMag(curr) < testMag(smallest)):
            smallest = curr
        smallest.x = float(smallest.x) 
        smallest.y = float(smallest.y)       
        return biggest,smallest

def testMag(coord):
    return math.sqrt((coord.x**2 + coord.y**2))   

print read2columns("xy.dat")



def replace(f, oldS, newS):
    f=open(f,"r")
    f = f.read()
    f = str(f).replace(oldS,newS)
    return f
    
print replace("replace.txt","a","a")