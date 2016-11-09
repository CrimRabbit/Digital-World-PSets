import time
#inList = [9,30,3,9,3,2,4]
#dicty = {}
#high = 1
#for x in xrange(len(inList)):
#    if(dicty.has_key(inList[x])):
#        dicty[inList[x]] += 1
#        if dicty[inList[x]] > high:
#            high = dicty[inList[x]]
#    else:
#        dicty[inList[x]] = 1
#        
#outList = []
#for x in dicty.keys():
#    if dicty[x] == high:
#        outList.append(x)
#
#print outList


#def countNumOpenLocker(K):
#    lockers=[-1]*int(K)
#    for p in range(K):
#        for i in range(0,K,p+1):
#            lockers[i]*=-1
#    return lockers.count(1)
#
#t1=time.time()
#print countNumOpenLocker(36)
#
#import math
#def countNumOpenLocker(K):
#    return math.floor(math.sqrt(K))
#print countNumOpenLocker(1000000)

def countNumOpenLocker(K):
    lockers = [True]*int(K+1)
    for y in range(K):
        for x in range(0,len(lockers),y+1):
            lockers[x] = not lockers[x]
    return lockers.count(False)
    
    #toggled when pass number is a factor of locker number.
    #floor(sqrt(K-1)) = num of opens.
#    
#t1 = time.time()
print countNumOpenLocker(2000)
#print time.time() - t1