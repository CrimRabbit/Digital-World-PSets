def extractValues(values):
    a = values.split(" ")
    return int(a[0]),int(a[1])


def calcRatios(values):
    if (values[1] == 0):
        return None
    return float(values[0])/values[1]

#def moveDisks(n, fromTower, toTower, auxTower,sol):



#############################################################################
#Copied from Wk5 Pset Tutor
#############################################################################

def leapYear(year):
    if(year%4!=0):
        return False
    elif(year%100!=0):
        return True
    elif(year%400!=0):
        return False
    else:
        return True

def dayOfWeekJan1(year):
    return R(1+5*R(year-1,4) + 4*R(year-1,100) + 6*R(year-1,400),7)   
            
def R(y,x):
    return y%x
    
#print dayOfWeekJan1(1800) 

def numDaysInMonth(month_num,leap_year):
#jan31,feb28,mar31,apr30,
#may31,jun30,jul31,aug31,
#sept30,oct31,nov30,dec31
    year = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    if(leap_year and month_num==2):
        return year[month_num]+1
    else:
        return year[month_num]

def constructCalMonth(month_num, first_day_of_month, num_days_in_month):
    monthName = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
    returnable = [monthName[month_num]]    
    count = 1
    week = ""
    for x in xrange(-first_day_of_month+1, num_days_in_month+1):
        if(x <= 0):
            week+="   "
        elif(x >= 10):
            week+=" "+str(x)
        else:
            week+="  "+str(x)           
        if(count == 7):
            returnable.append(week[1:])
            week = ""
            count = 0
        count +=1
    if(week!=""):
        returnable.append(week[1:])   
    return returnable
        
#print constructCalMonth(1,4,31)   
#print constructCalMonth(2,1,29)
def constructCalYear(year):
    returnable = [year]
    #12 months in a year confirmed.
    initial = dayOfWeekJan1(year)
    for x in xrange(1,13):       
        returnable.append(constructCalMonth(x,initial%7,numDaysInMonth(x,leapYear(year))))
        initial +=numDaysInMonth(x,leapYear(year))
    return returnable

#############################################################################
#End Copy from Wk5 Pset Tutor
#############################################################################
             
def displayCalendar(calendar_year,month):
    if (month == None):
        calendar = constructCalYear(calendar_year)
        returnable = ""
        for x in xrange(1,len(calendar)):
            for y in xrange(len(calendar[x])):
                if (y == 1):
                    returnable+= " S  M  T  W  T  F  S\n"+calendar[x][y]+"\n"
                elif (y == 0 and x != 1):
                    returnable+= "\n"+calendar[x][y]+"\n"
                else:
                    returnable+= calendar[x][y]+"\n"
            if x==len(calendar):
                returnable+="\n"
        return returnable[:-1]
    else:
        calendar = constructCalYear(calendar_year)
        returnable = ""
        for x in xrange(1,len(calendar)):
            if(x == month):
                for y in xrange(len(calendar[x])):
                    if (y == 1):
                        returnable+= " S  M  T  W  T  F  S\n"+calendar[x][y]+"\n"
                    elif (y == 0 and x != 1):
                        returnable+= calendar[x][y]+"\n"
                    else:
                        returnable+= calendar[x][y]+"\n"
                if x==len(calendar):
                    returnable+="\n"
        return returnable[:-1]

print displayCalendar(1800,3)