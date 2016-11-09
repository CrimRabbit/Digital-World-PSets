def isValid(number):

    sumTotal = sumOfDoubleEvenPlace(number) 
    sumTotal += sumOfOddPlace(number)
    sumTotal %= 10
    if sumTotal == 0:
        return True
    return False

#I assume this method does steps a & b
def sumOfDoubleEvenPlace(number):
    strNum = str(number)[::-1]
    sumTotal = 0
    lissa = []
    for i in xrange(1,len(strNum),2):
            lissa.append(getDigit((int(strNum[i]))*2))
    for i in xrange(len(lissa)):
        sumTotal+=lissa[i]                
    return sumTotal
    
def sumOfOddPlace(number):
    strNum = str(number)[::-1]
    sumTotal = 0
    for i in xrange(0,len(strNum),2):
        sumTotal += int(strNum[i])                
    return sumTotal

#relies on legit inputs
def getDigit(number):
    strNum = str(number)
    #number has more than 1 digit
    if(len(strNum) > 1):
        sumNum = 0
        for i in xrange(len(strNum)):
            sumNum+= int(strNum[i])
        return sumNum
    return number    

def getSize(d):
    return len(str(d))


# Return sum of odd place digits in number. Assume given.
#def sumOfOddPlace(number):
#    sumDE=0
#    while number!=0:
#        digit=number%10
#        sumDE+=digit
#        number/=100
#    return sumDE


# Return true if the digit d is a prefix for number. Assume given.
def prefixMatched(number, d):
    size=getSize(d)
    prefix=getPrefix(number,size)
    return prefix==d


# Return the first k number of digits from number. If the
# number of digits in number is less than k, return number.
# Assume given.
def getPrefix(number,k):
    d=getSize(number)
    divisor=1
    for i in range(d-1-(k-1)):
        divisor*=10
    return number/divisor

#print getDigit(16)
#print sumOfDoubleEvenPlace(4388576018402626)
print isValid(371826291433349)
print isValid(5411045872559122)
print isValid(6011432717792989)