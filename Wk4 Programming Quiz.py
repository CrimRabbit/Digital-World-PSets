def printvals(n):
    returnList = []
    for x in xrange(1,n+1):
        if(x%3 == 0 and x%5==0):
            returnList.append('AB')
        elif(x%3 == 0):
            returnList.append('A')
        elif(x%5 == 0):
            returnList.append('B')
        else:
            returnList.append(x)
    return returnList
    
print printvals(15)