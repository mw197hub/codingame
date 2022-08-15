import sys
import math

def suche(gList,laenge,gDict,maxL):
    laenge += 1
    for g in gList:
        laenge,maxL = suche(gDict[g],laenge,gDict,maxL)
        if laenge > maxL:
            maxL = laenge  
        laenge = laenge - 1  
    return laenge,maxL

xyList = [[1, 2], [1, 3], [3, 4]]
xyList = [[1, 2], [1, 3], [3, 4], [2, 4], [2, 5], [10, 11], [10, 1], [10, 3]]


gDict = {}

for xy in xyList:
    if not xy[1] in gDict:
        gDict[xy[1]] = []
    if xy[0] in gDict:
        wert = gDict[xy[0]]
        wert.append(xy[1])
        gDict[xy[0]] = wert
    else:
        gDict[xy[0]] = [xy[1]]

print(gDict,file=sys.stderr)

maxG=0;maxL=0
for g,gList in gDict.items():
    laenge = 0
    laenge,maxL = suche(gList,laenge,gDict,maxL)
    if maxL > maxG:
        maxG = maxL
print(maxG)