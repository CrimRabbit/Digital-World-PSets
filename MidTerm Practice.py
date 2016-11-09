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

print findConflict(getSchedule("D:\Libraries\Documents\SUTD\SUTD Term 3\Digital World\Problem Sets\Files\data1.txt"))

def multi(A,B):
    Z = []
    for i in range(len(A)): # iterate through rows of A
        row = []
        for j in range(len(B[0])): # iterate through columns of B
            add = 0
            for k in range(len(B)): # iterate through rows of B
                add += (A[i][k] * B[k][j])
            row.append(add)
        Z.append(row)
    return Z

def transposeMatrix(a):
    b = [0] * len(a[0])
    for x in xrange(len(a[0])):
        b[x] = [0] * len(a)
    
    for x in xrange(len(b)):   
        for y in xrange(len(b[x])):
                b[x][y] = a[y][x]        
    return b

#A = [[1,2,3],[3,4,5]]
#B = [[1,2],[3,4],[5,6]]
#print multi(B,A)