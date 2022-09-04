import sys
import math

def search(mapList,t,r,c):
    bisherList=[];moveList=[[0,0]];anzahl=1;bew=[[1,0],[-1,0],[0,1],[0,-1]]    
    bisherList.append([0,0])
    while moveList:
        get = moveList.pop(0)
        print(str(len(moveList)) + "  zu  " + str(len(bisherList)) + "  anzahl: " + str(anzahl),file=sys.stderr)
        if anzahl > 630:
            test = 0
        for b in bew:
            rN= get[0] + b[0];cN=get[1]+b[1]
            if rN >= 0 and rN < r and cN >= 0 and cN < c:                
                if mapList[rN][cN] <= t:
                    if not [rN,cN] in bisherList:
                        moveList.append([rN,cN])
                        bisherList.append([rN,cN])
                        anzahl+=1
    return anzahl

def getWert(z):
    sum = 0
    for i in str(z):
        sum += int(i)
    return sum

r,c,t=3,3,1
r,c,t=36,27,12 # 636
#r,c,t=12,10,2  # 6

if t < 9 and r > 9:
    r=9
if t < 9 and c > 9:
    c=9

anzahl = 0
mapList=[]
for i in range(r):
    line=[]
    for j in range(c):
        wert = getWert(i)+getWert(j)
        line.append(wert)
        if t >= wert:
            anzahl+=1
    mapList.append(line)

for ma in mapList:
    for m in ma:
        print("{a:2d} ".format(a=m),end="")
    print("")
anzahl = search(mapList,t,r,c)

#print(mapList,file=sys.stderr)
print(anzahl)