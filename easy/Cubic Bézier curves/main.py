import math
import sys

def calc_curve(pointList, granuality):
    'Calculate the cubic Bezier curve with the given granuality.'
    xList= []
    yList=[]
    for t in range(0, granuality):
        t = t / (granuality -1)
        x = ((1 - t) ** 3) * pointList[0][0] + 3 * ((1 - t) ** 2) * t * pointList[1][0] + 3 * (1 - t) * (t ** 2) * pointList[2][0] + (t ** 3) * pointList[3][0]
        y = ((1 - t) ** 3) * pointList[0][1] + 3 * ((1 - t) ** 2) * t * pointList[1][1] + 3 * (1 - t) * (t ** 2) * pointList[2][1] + (t ** 3) * pointList[3][1]
        xList.append(int(x+.5))
        yList.append(int(y+0.5))
    return xList,yList


width,height,steps=10,10,10
pointList=[[0, 0], [0, 9], [9, 9], [9, 0]]

width,height,steps=20,20,25
pointList=[[0, 0], [19, 19], [0, 19], [19, 0]]



xList,yList=calc_curve(pointList,steps)
for y in range(height-1,-1,-1):
    if y in yList:
        erg=["."]
        for _ in range(width-1):
            erg.append(" ")
        for i in range(len(yList)):
            if y == yList[i]:
                erg[xList[i]] = "#"
        outS = ("".join(map(str,erg)))
        print(outS.strip())
    else:
        print(".")
