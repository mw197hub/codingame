import sys
import math
import copy

def xy(a,b):
    return str(a)+"-"+str(b)

n=3
rowList=[['~', '~', '#'], ['~', '~', '#'], ['~', '~', '#']]

n=6
rowList=[['#', '#', '~', '~', '#', '~'], ['#', '#', '~', '~', '~', '~'], ['~', '~', '~', '~', '#', '~'], ['~', '~', '~', '#', '#', '~'], ['~', '#', '#', '#', '#', '~'], ['~', '~', '~', '~', '~', '~']]



island,water,land=1,0,0
islandList={}
ergList=[];isNr=1
suchList=[[1,0],[-1,0],[0,1],[0,-1]]
for i in range(n):
    for j in range(n):
        if not xy(i,j) in ergList and rowList[i][j] == "#":
            trefferList=[]
            trefferList.append(xy(i,j))
            ergList.append(xy(i,j))
            zwList=[xy(i,j)]
            while zwList:
                getXY = zwList.pop()
                wertN = getXY.split("-")
                for s in suchList:
                    x1 =int(wertN[0])+int(s[0])
                    y1 = int(wertN[1])+int(s[1])
                    if x1 >= 0 and x1 < n and y1 >= 0 and y1 < n and rowList[x1][y1] == "#" and not xy(x1,y1) in ergList:
                        ergList.append(xy(x1,y1))
                        zwList.append(xy(x1,y1))
                        trefferList.append(xy(x1,y1))
            islandList[isNr] = copy.deepcopy(trefferList)
            isNr+=1
print(islandList,file=sys.stderr)

for isNr,landList in islandList.items():
    w=0
    wList=set()
    for l in landList:
        wert = l.split("-")
        for s in suchList:
            x1 =int(wert[0])+int(s[0])
            y1 = int(wert[1])+int(s[1])
            if x1 >= 0 and x1 < n and y1 >= 0 and y1 < n and not rowList[x1][y1] == "#":
                wList.add(xy(x1,y1))
    if len(wList) > water or (len(wList) == water and len(landList) < land):
        water = len(wList);land=len(landList);island=isNr

print(str(island) + " " + str(water))
