import copy
import math

def comp(x):
	print "lol"
	return (x**3) +(6*x)+(4*x**2)+1
def genList(n1,n2):
	returnable = []
	for i in xrange(n1,n2+1,1):
		if(i%3==0):
			returnable.append(i)
	return returnable
def matAdd(A,B):
	C = copy.deepcopy(A)
	for x in xrange(len(A)):
		for y in xrange(len(A[0])):
			C[x][y] += B[x][y]
	return C
#print matAdd([[1,2,3], [4, 5, 6]],[[10,20,30], [40, 50, 60]])
def getSchedule(f):
	f = open(f,"r")
	#f = f.read()
	dict = {}
	current = ""
	for line in f:
		if line.find("y") != -1:
			dict[line.rstrip()] = []
			current = line.rstrip()
		else:
			dict[current].append(line.rstrip())
	return dict
def findLength(dictSchedule):
	returnable = {}
	for key in dictSchedule:
		returnable[key] = 0
		for i in xrange(len(dictSchedule[key])):
			times =  dictSchedule[key][i].split()
			returnable[key] += (int(times[1]) - int(times[0]))
	return returnable
def findConflict(dictSchedule):
	returnable = {}
	for key in dictSchedule:
		currentList = dictSchedule[key]
		total = []
		for i in xrange(len(currentList)):
			splitted = currentList[i].split()
			for x in xrange(int(splitted[0]), int(splitted[1])):
				total.append(x)
		if(len(total) != len(set(total))):
			returnable[key] = True
		else:
			returnable[key] = False
	return returnable

#print findConflict(getSchedule("D:\Libraries\Documents\SUTD\SUTD Term 3\Digital World\Problem Sets\Files\data1.txt"))

