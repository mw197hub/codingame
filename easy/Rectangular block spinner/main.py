import sys
import math

def setFirst(size,x,y,xFirst):
    if xFirst:
        if x == 0 or x == size-1:
            xFirst = False
    else:
        if y == 0 or y == size-1:
            xFirst = True

    return xFirst


size,angle=5,45
mList = [['1', '#', '#', '#', '4'], ['#', '-', '.', '.', '#'], ['#', '#', '-', '.', '#'], ['#', '#', '#', '-', '#'], ['2', '#', '#', '#', '3']]

size,angle=12,495
mList=[['A', 'A', 'H', 'G', 'S', 'R', 'U', 'B', 'J', 'Q', 'B', 'O'], ['N', 'W', 'E', 'D', 'L', 'M', 'M', 'V', 'T', 'L', 'U', 'H'], ['R', 'S', 'D', 'N', 'B', 'N', 'Y', 'W', 'A', 'T', 'O', 'O'], ['D', 'L', 'D', 'Z', 'V', 'A', 'R', 'C', 'C', 'D', 'I', 'Q'], ['R', 'P', 'N', 'F', 'E', 'Q', 'I', 'C', 'I', 'I', 'D', 'G'], ['H', 'V', 'K', 'S', 'Y', 'Z', 'P', 'C', 'N', 'S', 'I', 'C'], ['X', 'G', 'J', 'Y', 'T', 'L', 'V', 'B', 'S', 'Y', 'Q', 'B'], ['Y', 'Q', 'Z', 'J', 'Q', 'N', 'I', 'T', 'R', 'D', 'X', 'E'], ['L', 'U', 'U', 'M', 'T', 'D', 'H', 'D', 'H', 'R', 'V', 'E'], ['L', 'M', 'Z', 'M', 'R', 'V', 'T', 'V', 'D', 'G', 'E', 'N'], ['G', 'Q', 'A', 'X', 'E', 'Y', 'B', 'J', 'D', 'H', 'A', 'J'], ['R', 'A', 'M', 'K', 'O', 'U', 'J', 'O', 'G', 'V', 'U', 'Z']]

#size,angle=16,315
#mList=[['G', 'W', 'A', 'U', 'V', 'V', 'U', 'E', 'O', 'J', 'X', 'I', 'Z', 'I', 'H', 'A'], ['T', 'B', 'Z', 'K', 'Y', 'U', 'B', 'Y', 'C', 'W', 'Z', 'E', 'M', 'Z', 'B', 'F'], ['C', 'P', 'E', 'A', 'H', 'U', 'V', 'O', 'I', 'L', 'Y', 'H', 'P', 'J', 'U', 'H'], ['G', 'T', 'C', 'J', 'M', 'C', 'N', 'H', 'Q', 'U', 'G', 'M', 'M', 'H', 'N', 'H'], ['F', 'D', 'B', 'G', 'K', 'B', 'T', 'E', 'N', 'R', 'B', 'Y', 'S', 'A', 'U', 'R'], ['M', 'G', 'R', 'V', 'E', 'D', 'W', 'B', 'D', 'R', 'U', 'N', 'J', 'E', 'F', 'Y'], ['Y', 'F', 'F', 'F', 'I', 'P', 'O', 'I', 'D', 'M', 'Y', 'I', 'Z', 'O', 'Q', 'X'], ['O', 'L', 'T', 'I', 'P', 'Y', 'I', 'Q', 'V', 'D', 'S', 'M', 'G', 'S', 'Y', 'C'], ['H', 'I', 'V', 'A', 'U', 'C', 'U', 'E', 'Q', 'X', 'Y', 'F', 'I', 'W', 'W', 'K'], ['M', 'O', 'N', 'I', 'S', 'W', 'M', 'G', 'I', 'H', 'Q', 'N', 'H', 'R', 'L', 'J'], ['H', 'S', 'Z', 'C', 'V', 'Q', 'B', 'B', 'W', 'N', 'D', 'Y', 'K', 'N', 'Z', 'D'], ['H', 'I', 'B', 'N', 'Q', 'R', 'V', 'Z', 'A', 'E', 'F', 'L', 'P', 'J', 'G', 'M'], ['W', 'U', 'Z', 'A', 'T', 'K', 'X', 'W', 'G', 'N', 'K', 'M', 'U', 'P', 'R', 'Q'], ['W', 'X', 'I', 'U', 'H', 'D', 'S', 'Y', 'Z', 'K', 'N', 'F', 'L', 'E', 'W', 'H'], ['R', 'Y', 'U', 'B', 'N', 'U', 'E', 'M', 'F', 'T', 'N', 'U', 'I', 'S', 'T', 'H'], ['X', 'Q', 'T', 'E', 'Z', 'O', 'U', 'E', 'B', 'Z', 'W', 'D', 'X', 'X', 'O', 'E']]


sizeN = size*2 -1
rot = int(angle %360) 
x,y,xM,yM,xFirst,mm=0,0,1,1,True,[-1,1]
if rot == 45:
    x,y,xM,yM,xFirst,mm=size-1,0,-1,1,True,[1,1]
elif rot == 135:
    x,y,xM,yM,xFirst,mm=size-1,size-1,-1,-1,True,[1,-1]
elif rot == 225:
    x,y,xM,yM,xFirst,mm=0,size-1,1,-1,True,[-1,-1]

startPos=size
for i in range(sizeN):
    startPos = startPos -1 if i < size else startPos +1
    lList=[]
    for j in range(sizeN):
        lList.append(" ")
    mPos = startPos
    j = i + 1 if i < size else size*2 - i -1
    xS,yS=x,y
    for p in range(j):
        lList[mPos] = mList[yS][xS]
        mPos +=2
        yS += mm[0];xS+=mm[1]
#    if i > 0:
    xFirst=setFirst(size,x,y,xFirst)
    if xFirst:
        x = x + xM
    else:
        y = y + yM
    for z in lList:
        print(z,end="")
    print("")
    
