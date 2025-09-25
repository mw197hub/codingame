# 

import sys,math


xyList=[[1, 1]]
#xyList=[[0, 0]]
xyList=[[-4, 3], [3, -2]]


###
xMax=0;yMax=0;xMin=0;yMin=0
for xy in xyList:
    if xy[0] > xMax:
        xMax=xy[0]
    if xy[0] < xMin:
        xMin=xy[0]
    if xy[1] > yMax:
        yMax=xy[1]
    if xy[1] < yMin:
        yMin=xy[1]
centerX=1+abs(xMin)
centerY=1+abs(yMax)
newPoint=[]
for xy in xyList:
    newPoint.append([centerX+xy[0],centerY-xy[1]])
#print(newPoint)
for y in range(3+yMax+abs(yMin)):
    zeile=""
    for x in range(3+xMax+abs(xMin)):
        treffer=False
        for xy in newPoint:
            if xy[0] == x and xy[1] == y:
                zeile+="*"
                treffer=True
        if not treffer:
            if y == centerY:
                if x == centerX:
                    zeile+="+"
                else:
                    zeile+="-"
            else:
                if x == centerX:
                    zeile+="|"
                else:
                    zeile+="."
    print(zeile)