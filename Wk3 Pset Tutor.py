#Qn1
def letterGrade(score):
    int(score)
    #add a check for out of bounds.
    if(score >= 90):
        return 'A'
    elif(score >= 80):
        return 'B'
    elif(score >= 70):
        return 'C'
    elif(score >= 60):
        return 'D'
    elif(score < 60):
        return 'E'
    else:
        return 'None'
    
print letterGrade(70)

#Qn2
def check1(num1, num2):
    if(num1>num2):
        return True
    return False
    
print check1(-1,2)

#Qn3
def listSum(list):
    sum = 0.0
    for x in range(len(list)):
        sum += list[x]
    return sum
        
lista = [3, 5.0, 9]
print listSum(lista)

#Qn4
def maxList(list):
    try:
        max = list[0]
        min = list[0]
        for x in xrange(len(list)):
            if (list[x] > max):
                max = list[x]
            if (list[x] < min):
                min = list[x]
        return min, max
    except IndexError:
        return None,None
    

    
lista = [101,56,49,33,29,4]
print maxList(lista)

#Qn5
def isPalindrome(num):
    num = str(num)
    halfNum = len(num)/2
    for x in xrange(halfNum):
        if(num[x] != num[-(x+1)]):
            return False
    return True
    
print isPalindrome(123)

#Qn6a
x=int( raw_input ("Enter :"))
y=int( raw_input ("Enter :"))
if x<y:
    print x
elif x>y:
    print y
else :
    print x+y
    
#Case 1 prints x
#Case 2 prints y
#Case 3 prints sum of x&y

#Qn6b
x=int( raw_input ("Enter :"))
y=int( raw_input ("Enter :"))
if x<y:
    print x+y
elif x>y:
    print y
if(x+y) >50:
    print x-y
else :
    print x
    
#If sum of x & y are > 50, add x-y after Case 1 & 2, before Case 3
#Case 1 prints sum of x&y
#Case 2 prints y
#Case 3 prints x