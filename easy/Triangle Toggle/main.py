# https://www.codingame.com/ide/puzzle/triangle-toggle

import sys,math

def is_inside_polygon(pList,p):
    pos,neg = 0,0
    if p in pList:
        return True
    for i in range(len(pList)):
        x1 = pList[i][0]
        y1 = pList[i][1]
        i2 = 0
        if i < len(pList) -1:
            i2 = i + 1
        x2 = pList[i2][0]
        y2 = pList[i2][1]
        x,y = p[0],p[1]

        d = (x - x1)*(y2 - y1) - (y - y1)*(x2 - x1)
        if d > 0:
            pos += 1
        if d < 0:
            neg += 1
        if pos > 0 and neg > 0:
            return False
    return True

def getDreiecke(triList):
    wegList=[]
    for tri in triList:        
        x1,y1,x2,y2,x3,y3=tri
        v1=[y1-y2,x1-x2];v2=[y1-y3,x1-x3];v3=[y2-y3,x2-x3]
        print("v1:{}  v2:{}   v3:{}".format(v1,v2,v3),file=sys.stderr)
        for y in range(min([y1,y2,y3]),max([y1,y2,y3])+1,1):
            for x in range(min([x1,x2,x3]),max([x1,x2,x3])+1,1):
                if is_inside_polygon([[y1,x1],[y2,x2],[y3,x3]],[y,x]):
                    wegList.append([y,x])
    return wegList


hi=12;wi=14;style="expanded";triList=[[3, 2, 10, 2, 3, 9]]

wegList = getDreiecke(triList)
ergList=[]
for y in range(hi):
    ergList.append([("*") for x in range(wi)])

for y,x in wegList:
    if y>=0 and y < hi and x >= 0 and x < wi:
        ergList[y][x]=" " if ergList[y][x] == "*" else "*"

if style == "expanded":
    for y in range(hi):
        e = ("".join([str(ergList[y][x])+" " for x in range(wi)]))
        print(e[:-1])
else:
    for y in range(hi):
        print("".join([str(ergList[y][x]) for x in range(wi)]))
        