import cmath
import copy

def norm(z1,z2,z3):    
    r1 = z1 * z1.conjugate()
    r2 = z2 * z2.conjugate()
    r3 = z3 * z3.conjugate()
    
    return round((cmath.sqrt(r1+r2+r3)).real,3)

#print norm(1+3j,-1+3j,-1-3j)
#print norm(1+2j,-1+2j,-1-2j)           
    
def factors(n):
    returnable = []
    for i in xrange(1,n+1):
        if(n%i==0):
            returnable.append(i)
    return returnable
   
#print factors(6)
#print factors(12)
#print factors(21)

def combinations(n1,n2):
    returnable = []
    for i in xrange(n1,n2):
        for j in xrange(n1+1,n2+1):
            if i != j and j > i:
                returnable.append((i,j))
    returnable.append(len(returnable))
    return returnable

print combinations(1,7)
#print combinations(3,5)     
            
def readMatrix(f):
    dict = {}
    currentKey = ""
    for line in f:
        if(line.strip("\n ").isalpha() ==True):
            if (line.strip("\n ") == "DATA"):
                currentKey = "matrix"
                dict[currentKey] = []
            elif (line.strip("\n ") == "OP"):
                currentKey = "op"
                dict[currentKey] = []
            
        elif(line.strip("\n ").isalpha() == False):
            currLine = line.strip("\n ").split()
            if (currentKey == "matrix"):
                for i in xrange(len(currLine)):
                    currLine[i] = float(currLine[i])
            dict[currentKey].append(currLine)
    return dict        
            
    
#f=open("gauss2.txt","r")
#print readMatrix(f)

def mulRowByC(matA,i,c):
    for x in xrange(len(matA[i])):
        matA[i][x] *= c
    return matA

#A = [[0,2,1,-1],[0,0,3,1],[0,0,0,0]]
#print mulRowByC(A,0,2)

def addRowMulByC(matA,i,c,j):
    edited = []
    for x in xrange(len(matA[i])):
        edited.append(matA[i][x] *c)
    for x in xrange(len(matA[j])):
        matA[j][x] += edited[x]
    return matA

#A = [[0,2,1,-1],[0,0,3,1],[0,0,0,0]]
#print addRowMulByC(A,0,0.5,1)

def gaussElimination(data):
    return1 = data["matrix"]
    return2 = copy.deepcopy(return1)
    op = data["op"]
    
    for i in xrange(len(op)):
        if int(op[i][0]) == 1:
            return2 = mulRowByC(return2,int(op[i][1]),float(op[i][2]))
        elif int(op[i][0]) == 2:
            return2 = addRowMulByC(return2,int(op[i][1]),float(op[i][2]),int(op[i][3]))
    
    for i in xrange(len(return2)):
        for j in xrange(len(return2[0])):
            return2[i][j] = round(return2[i][j],2)
    
    return return1,return2
    
#f=open("gauss2.txt","r")
##print readMatrix(f)
#print gaussElimination(readMatrix(f))
 
            
def maxProductThree(num):
    posNum = []
    for i in xrange(len(num)):
        num[i] = int(num[i])
        if(num[i] <0):
            posNum.append(num[i]*-1)
        else:
            posNum.append(num[i])
    num = sorted(num)
    print sorted(num)  
    posNum = sorted(posNum)   
    print sorted(posNum) 
    largest = []    
    for i in xrange(3):
        largest.append(posNum.pop(posNum.index(max(posNum))))
    #largest = posNum[len(posNum)-3:]
  
    print largest

    while(True):
            
        negCount = 0
        for i in xrange(len(largest)):
            try:
                num.index(largest[i]) ==0
            except ValueError:
                negCount+=1
        print negCount
        
        if(negCount >=1 and negCount%2 != 0):
            #do more work
            print largest
            
            pass
        else:
            returnable = 1
            for i in xrange(len(largest)):
                returnable *= largest[i]
            return returnable
        
        return None
    
#print maxProductThree([6,-3,-10,0,2])
#print maxProductThree([6,3,-10,0,2])