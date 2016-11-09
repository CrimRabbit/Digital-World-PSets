#x=[1 ,2 ,3]
#x[0]=0
#y=x
#y[0]=1
#print x[0]

#x=[1 ,2 ,3]
#y=[x]
#a=[y,x]
#y [0][0] = (1 ,2)


#x=[1 ,2 ,3]
#def f(l):
#    l [0]= 'a'
#f(x)
#print x[0]

#x=[1 ,2 ,3]
#y1 =[x ,0]
#y2=y1 [:]
#y2 [0][0]=0
#y2 [1]=1
#y1 [0][0] # (a)
#y1 [1] # (b)
#y2 [0][0] # (c)
#y2 [1] # (d)


#import copy
#x=[1 ,2 ,3]
#y1 =[x ,0]
#y2= copy . deepcopy (y1)
#y2 [0][0]=0
#y2 [1]=1
#print y1 [0][0] # (a)
#print y1 [1] # (b)
#print y2 [0][0] # (c)
#print y2 [1] # (d)


#l=[1,2,3]
#l[2:3]=4 #(a)
#print l[1:3]
#l [1:3]=[0] # (b)
#print l
##l[1:1]=1 #(c)
#l[2:]=[] # (d)
#print l


def compoundVal6Months(monthlyAmt, annualRate, months):
    annualRate /= 12
    pot = 0.0
    for x in xrange(months):
        pot += monthlyAmt
        pot *= (1+annualRate)
    return round(pot,2)

#print compoundVal6Months(100,0.03,7)

####### Your function should return a tuple containing a list of average #####
####### and the overall average, e.g., ([3.5,6.0,1.4], 3.625) ################  

def findAverage(listOfLists):
    avgList = []
    sumTot = 0.0
    count = 0
    for x in xrange(len(listOfLists)):
        sumx = 0.0
        print type([])
        print type(listOfLists)
        if(listOfLists[x] != []):
            for y in xrange(len(listOfLists[x])):
                sumx+= listOfLists[x][y]
                sumTot += listOfLists[x][y]
                count += 1
            sumx /= len(listOfLists[x])
            avgList.append(sumx)
        else:
            avgList.append(0.0)
    
    ##main avgList done
    return avgList,(sumTot/count)
    
#print findAverage ([[13.13 ,1.1 ,1.1] ,[] ,[1 ,1 ,0.67]])

def transposeMatrix(a):
    b = [0] * len(a[0])
    for x in xrange(len(a[0])):
        b[x] = [0] * len(a)
    
    for x in xrange(len(b)):   
        for y in xrange(len(b[x])):
            #If check unecessary - they return same values.
            #if(x!=y):
                b[x][y] = a[y][x]
            #else:    
            #    b[x][y] = a[x][y]           
    return b

#print transposeMatrix([[1 ,2 ,3] , [4 ,5 ,6] , [7 ,8 ,9]])
print transposeMatrix([[-11,12,3], [4,-5,6]])



def getDetails(name, key, phonebook):
    for x in xrange(len(phonebook)):
        if (phonebook[x].get("name")==name):
            return phonebook[x][key]
    return None
    
#phonebook =[{'name':'Andrew','mobile_phone':9477865,'office_phone':6612345,'email':'andrew@sutd.edu.sg'},{'name':'Bobby','mobile_phone':8123498,'office_phone':6654321,'email':'bobby@sutd.edu.sg'}]
#print getDetails ('Bobby', 'office_phone', phonebook)

def getBaseCounts(dna):
    dictDna = {'A':0,'C':0,'G':0,'T':0}
    for x in xrange(len(dna)):
            curr = dictDna.get(dna[x])
            if(curr == None):
                return "The input DNA string is invalid"
            else:
                dictDna[dna[x]] =curr+1
                
    #destroying keys with 0 because tutor.
    if(dictDna['A'] == 0):
        dictDna.pop('A')
    if(dictDna['C'] == 0):
        dictDna.pop('C')
    if(dictDna['G'] == 0):
        dictDna.pop('G')
    if(dictDna['T'] == 0):
        dictDna.pop('T')
    return dictDna

print getBaseCounts("AACCG")