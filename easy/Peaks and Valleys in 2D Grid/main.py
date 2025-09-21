# https://www.codingame.com/ide/puzzle/peaks-and-valleys-in-2d-grid

import sys,math

def setXY(x,y):
    return str(x)+"-"+str(y)
def getXY(XY):
    xy=XY.split("-")
    return xy[0],xy[1]

####

hList=[['1', '1', '1', '2'], ['1', '2', '1', '1'], ['1', '1', '1', '2'], ['1', '0', '1', '1']]  #1
hList=[['8', '9', '4', '1'], ['3', '4', '8', '7'], ['1', '5', '4', '4'], ['1', '3', '8', '9'], ['1', '4', '4', '4']] #2


#####

highList=[]
lowList=[]
graph={}
for y in range(len(hList)):
    for x in range(len(hList[0])):
        graph[setXY(x,y)]=int(hList[y][x])
print(graph,file=sys.stderr)
for y in range(len(hList)):
    for x in range(len(hList[0])):
        wert=int(hList[y][x]);higher=-1;lower=9999
        for xN,yN in [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]:
            xN=xN+x;yN=yN+y
            xy=setXY(xN,yN)
            if xy in graph:
                wertN=graph[xy]
                if wertN > higher:
                    higher=wertN
                if wertN < lower:
                    lower = wertN
        if wert > higher:
            highList.append([x,y])
        if wert < lower:
            lowList.append([x,y])

ausgabe=""
for h in highList:
    ausgabe+="("+str(h[0])+", "+str(h[1])+"), "
if len(ausgabe) < 2:
    print("NONE")
else:
    print(ausgabe[:-2])
ausgabe=""
for h in lowList:
    ausgabe+="("+str(h[0])+", "+str(h[1])+"), "
if len(ausgabe) < 2:
    print("NONE")
else:
    print(ausgabe[:-2])
