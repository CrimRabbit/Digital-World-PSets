def getConversionTable():
    ######Enter your code below ########
    conversion=   [[0 , 10, 20, 30, 40, 50, 60, 70, 80, 90, 100] , [ -17.8 , -12.2 , -6.7,
-1.1, 4.4 , 10.0 , 15.6 , 21.1 , 26.7 , 32.2 , 37.8] , [ -15.0 , -10.0 ,
-5.0, 0.0 , 5.0 , 10.0 , 15.0 , 20.0 , 25.0 , 30.0 , 35.0]]  #this is the table mentioned in the questions 
    ######Ignore code below ############
    return conversion
    
def maxList(inp):
    outp = []
    for x in xrange(len(inp)):
        outp.append(max(inp[x]))
    return outp
    
#inp = [[1 ,2 ,3] ,[4 ,5]]
#print maxList (inp)

def nBynMultiplicationTable(N):
    #retard check
    if(N < 2):
        return None
    returnable = []
    for x in xrange(1,N+1):
        printable = []
        for y in xrange(1, N+1):
            printable.append(x*y)
        returnable.append(printable)
    
    return returnable
    
#print nBynMultiplicationTable(4)


def mostFrequent(numList):
    maxoccur = 0
    diction = {}
    for x in xrange(len(numList)):
        if(diction.has_key(numList[x])):
            diction[numList[x]] +=1
            if (diction[numList[x]] > maxoccur):
                maxoccur = diction[numList[x]]
        else:
            diction[numList[x]] = 1
            
    returnable = []
    iDk = diction.iterkeys()
    for x in xrange(len(diction)):
        a = iDk.next()
        if(diction.get(a) == maxoccur):
            returnable.append(a)
    return returnable
    
            
#input=[2,3,40,3,5,4,-3,3,3,2,0]
#input=[9,30,3,9,3,2,4]
#print mostFrequent(input)

def diff(p):
    #remove 0's
    p.pop(0,None)
    q = {}
    ite = p.iterkeys()
    for x in xrange(len(p)):
        curr = ite.next()
        q[curr-1] = p.get(curr)*curr
    return q    
            
            
    
#p={0:-3, 3:2, 5:-1}
p={1:-3, 3:2, 5:-1, 6:2}
print diff(p)



