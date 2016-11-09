#Matrix - Credits to Marcus Quek
from copy import deepcopy
import math as m 

A = [[2,4], [7,0], [6,3]] #3x2 matrix
B = [[3,1], [-1,8], [-3, 3]] #3x2 matrix
C = [[3,-1,-3], [1,8,3]] #2x3 matrix
X = [[12,7,3],[4,5,6],[7,8,9]] #3x3 matrix
Y = [[5,8,1],[6,7,3],[4,5,9]] #3x3 matrix
v = [[2],[2]] #Vector in 2D
w = [[1],[0]] #Vector in 2D


#MATRIX ADDITION
def add(A,B):
    Z = []
    for i in range(len(A)): #Col iteration
        row = []
        for j in range(len(A[i])): # Row iteration
            row.append(A[i][j] + B[i][j])
        Z.append(row)
    #Z = [map(sum, zip(*t)) for t in zip(A, B)] #Shorter method
    return Z
#print add(X,Y)
#print add(A,B)
def sub(A,B):
    Z = []
    for i in range(len(A)): #Col iteration
        row = []
        for j in range(len(A[i])): # Row iteration
            row.append(A[i][j] - B[i][j])
        Z.append(row)
    #Z = [map(sum, zip(*t)) for t in zip(A, B)] #Shorter method
    return Z
#print sub(X,Y)
#print sub(A,B)
#SCALAR MULTIPLICATION
def scalarmulti(A,k):
    Z = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j]*k)
        Z.append(row)
    return Z
#print scalarmulti(A,2)
# MATRIX MULTIPLICATION
def matMulti(A,B):
    Z = []
    for i in range(len(A)): # iterate through rows of A
        row = []
        for j in range(len(B[0])): # iterate through columns of B
            add = 0
            for k in range(len(B)): # iterate through rows of B
                add += (A[i][k] * B[k][j])
            row.append(add)
        Z.append(row)
    #result = [[sum(a*b for a,b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A
    return Z
#print matMulti(B,C)
#print matMulti(A,C)
#DETERMINANT - Requires recursive function, not tested
#Minor is subcode for det
def minor(A,i):
    minor = deepcopy(A)
    del minor[0] #Delete first row
    for b in range(len(minor)): #Delete column i
        del minor[b][i]
    return minor
def det(A):
    if len(A) == 1: #Base case on which recursion ends
        return A[0][0]
    else:
        determinant = 0
        for x in list(range(len(A))): #Iterates along first row finding cofactors
            determinant += A[0][x] * (-1)**(2+x) * det(minor(A,x)) #Adds successive elements times their cofactors
        return determinant
#print det([[1,-2,3],[0,-3,-4],[0,0,-3]])
#TRACE
def trace(A):
    trace = 0
    for x in range(len(A)):
        trace += A[x][x]
    return trace
#print trace(Y)
#DIAGONAL
#Main diagonal in a list. [1,5,9]
def diagonal(A):
    diag = [A[i][i] for i in range(len(A)) ]
    return diag
#print diagonal(X)
#TRANSPOSE
def transpose(A):
    Z = [[] for i in range(len(A[0]))]
    for i in range(len(A[0])):
        Z[i] = [A[j][i] for j in range(len(A))]
    return Z
#print transpose(B)
#ADVANCED DIAGONAL, choose which i, j to start and d = 1 or -1 for direction of flow (\ or /)
def ADVdiagonal(A, i0, j0, d):
    return [A[(i0 + i - 1)%len(A)][(j0 + d*i - 1)%len(A[0])] for i in range(len(A))]
#print ADVdiagonal(X,1,1,1)
#print ADVdiagonal(X,2,1,1)
#print ADVdiagonal(X,1,2,1)
#print ADVdiagonal(X,1,1,-1)
def upperTriangle(A):
    Z = deepcopy(A)
    for i in range(len(A)):
        for j in range(len(A[0])):
            if i>j:
                Z[i][j] = 0
    return Z
#print upperTriangle(X)
def lowerTriangle(A):
    Z = deepcopy(A)
    for i in range(len(A)):
        for j in range(len(A[0])):
            if i<j:
                Z[i][j] = 0
    return Z
#print lowerTriangle(X)
#MainDiag = [1,0,0],[0,5,0],[0,0,9]
def mainDiagonal(A):
    Z = deepcopy(A)
    for i in range(len(A)):
        for j in range(len(A[0])):
            if i<j or i>j:
                Z[i][j] = 0
    return Z
#print mainDiagonal(X)
#TRANSLATION MATRIX FOR 2x2 VECTOR:
def translate2D(v,d):
    trans = [[1,0,d[0]],[0,1,d[1]],[0,0,1]]
    v.append([1])
    Z = matMulti(trans,v)
    del Z[2]
    return Z
#print translate2D(v,(0,1))
#ROTATION MATRIX FOR 2x2 VECTOR, angles in RADIANS:
#0 may appear as a very small number --> to change, modify multi() to return float for each element
def rotate2D(v,t):
    rotate = [[m.cos(t),-m.sin(t)],[m.sin(t),m.cos(t)]]
    Z = matMulti(rotate,v)
    return Z
#print rotate2D(w,m.pi) #rotate 180
#print rotate2D(w,m.pi/2) #rotate 90
#print rotate2D(w,m.pi/4) #rotate 45
#SCALE MATRIX for 2x2 VECTOR:
def scale2D(v,k):
    scale = [[k,0],[0,k]]
    Z = matMulti(scale,v)
    return Z
#print scale2D(v,0.5)