# https://www.codingame.com/ide/puzzle/shoot-enemy-aircraft

import sys
import math

lineList=['....................', '.>..................', '...................<', '....................', '....................', '_________^__________']

oList=[]
flak=[]
for y in range(len(lineList)):
    line = lineList[y]
    for x in range(len(line)):
        if line[x] in ['>','<']:
            oList.append([y,x])
        if line[x] == "^":
            flak=[y,x]
print(oList,file=sys.stderr)
print(flak,file=sys.stderr)
shootList=[]
for objekt in oList:
    xDist = abs(objekt[1] - flak[1])
    yDist = flak[0] - objekt[0]
    shootList.append(xDist-yDist)
print(shootList,file=sys.stderr)

for i in range(max(shootList)):
    if i+1 in shootList:
        print("SHOOT")
    else:
        print("WAIT")