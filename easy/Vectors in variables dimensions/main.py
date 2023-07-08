# https://www.codingame.com/ide/puzzle/vectors-in-variables-dimensions

import sys,math


def distance(p1,p2):
    wert=0
    for i in range(len(p1)):
        wert+=((p1[i]-p2[i])**2)
    return math.sqrt(wert)

def setOut(l1,l2):
    out=""
    for i in range(len(l1)):
        out+=str(l2[i]-l1[i])+","

    return out[:-1]

#1
pointList=[['A', '1,2)'], ['C', '0,8)'], ['D', '0,9)'], ['E', '6,2)'], ['F', '6,4)']]


pointDict={}
for pList in pointList:
    pL=pList[1][:-1].split(",")
    p2=[]
    for p in pL:
        p2.append(int(p))
    pointDict[pList[0]] = p2[:]
print(pointDict,file=sys.stderr)

shortWay="";longWay="";shortOut="";longOut=""
shortWert=999;longWert=0
for i1 in range(len(pointList)-1):
    for i2 in range(i1,len(pointList)):
        if not i1 == i2:
            wert=distance(pointDict[pointList[i1][0]],pointDict[pointList[i2][0]])
           # print("{} {} = {}".format(i1,i2,wert),file=sys.stderr)
            if wert >= 0 and wert < shortWert:
                shortWert=wert;shortWay=pointList[i1][0]+pointList[i2][0]
                shortOut=setOut(pointDict[pointList[i1][0]],pointDict[pointList[i2][0]])
            if wert > longWert:
                longWert=wert;longWay=pointList[i1][0]+pointList[i2][0]
                longOut=setOut(pointDict[pointList[i1][0]],pointDict[pointList[i2][0]])

print("{}({})".format(shortWay,shortOut))
print("{}({})".format(longWay,longOut))