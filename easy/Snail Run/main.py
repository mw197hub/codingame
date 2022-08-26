import sys
import math

snailDict = {1: 2, 2: 3, 3: 5}
mapList = [['1', '*', '*', '*', '*', '#'], ['2', '*', '*', '*', '*', '#'], ['3', '*', '*', '*', '*', '#']]

zielList=[];startDict={}
for i in range(len(mapList)):
    for j in range(len(mapList[i])):
        if mapList[i][j] == "#":
            zielList.append(str(i)+"-"+str(j))
        elif not mapList[i][j] == "*":
            startDict[int(mapList[i][j])] = str(i)+"-"+str(j)
print(zielList,file=sys.stderr)
print(startDict,file=sys.stderr)
erg = 9999;dist=9999

for nr,move in snailDict.items():
    start = startDict[nr].split("-")
    for zielP in zielList:
        ziel = zielP.split("-")
        d = (abs(int(ziel[0]) - int(start[0]))) + (abs(int(ziel[1]) - int(start[1]))) / move
        if d < dist:
            dist = d; erg = nr
print(erg)