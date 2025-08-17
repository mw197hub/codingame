#https://www.codingame.com/ide/puzzle/city-lights-part-2

import sys,math,string

def setXY(x,y,z):
    return str(x)+"-"+str(y)+"-"+str(z)
def getXY(XYZ):
    xyz=XYZ.split("-")
    return int(xyz[0]),int(xyz[1]),int(xyz[2])

########

w=3;h=4;d=2;rowList=['...', '.3.', '...', '...', '', '...', '...', '...', '.2.']


zahlList=string.ascii_uppercase
graph={}
lichtList={};dRunde=0
for z in range(d):
    hStart=z*h+dRunde
    for y in range(h):
        row=rowList[y+hStart]
        for x in range(w):
            graph[setXY(x,y,z)] = 0
            if not row[x] == ".":
                lichtWert=9
                if row[x] in zahlList:
                    for i in range(len(zahlList)):
                        lichtWert+=1
                        if zahlList[i] == row[x]:
                            break
                else:
                    lichtWert=int(row[x])
                lichtList[setXY(x,y,z)] = lichtWert
                graph[setXY(x,y,z)] = lichtWert
    dRunde+=1

for licht,lichtWert in lichtList.items():
    xN,yN,zN=getXY(licht)
    for z in range(d):
        for y in range(h):
            for x in range(w):
                if x == xN and y == yN and z == zN:
                    a=0
                else:
                    wert= int(round(math.dist([xN,yN,zN],[x,y,z]),0))
                    if lichtWert - wert < 0:
                        a = 0#graph[setXY(x,y)] = 0
                    else:
                        graph[setXY(x,y,z)] = graph[setXY(x,y,z)] + lichtWert - wert

for z in range(d):
    for y in range(h):
        ausgabe=""
        for x in range(w):
            if graph[setXY(x,y,z)] > 9:
                if graph[setXY(x,y,z)] >= 36:
                    ausgabe+="Z"
                else:
                    ausgabe+=zahlList[graph[setXY(x,y,z)]-10]            
            else:
                ausgabe+=str(graph[setXY(x,y,z)])
        print(ausgabe)
    print("")