# https://www.codingame.com/ide/puzzle/hexagonal-maze

import sys,math

def setXY(y,x):
    return str(y)+"-"+str(x)
def getXY(XY):
    xy=XY.split("-")
    return int(xy[0]),int(xy[1])
def bfs_shortest_path(graph, start, goal):
    explored = []
    queue = [[start]]
 
    if start == goal:
        return "That was easy! Start = goal"
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path
            explored.append(node)

    return "So sorry, but a connecting path doesn't exist :("

###

rowList=['#####', '#S#E#', '#_#_#', '#_#_#', '#___#', '#####']
rowList=['#E_____#', '##_###_#', '##_____#', '#_#_####', '##_____#', '####_#_#', '#S_____#', '########']
rowList=['#___##', '_#__#_', '#__##_', '###E#_', '__S#_#', '###_##'] #3


####
graph={}
rList=[]
start="";ende=""
for y in range(len(rowList)):
    row = rowList[y]
    for x in range(len(row)):
        if not rowList[y][x] =="#":
            rList.append(setXY(y,x))
        if rowList[y][x] == "S":
            start=setXY(y,x)
        if rowList[y][x] == "E":
            ende=setXY(y,x)
#print(rList,file=sys.stderr)
moveList1=[[0,1],[0,-1],[-1,0],[-1,-1],[1,-1],[1,0]]
moveList2=[[0,1],[0,-1],[-1,0],[-1,1],[1,1],[1,0]]
for XY in rList:
    y,x = getXY(XY)
    mList=[]
    moveList = moveList2[:]
    if y % 2 == 0:
        moveList = moveList1[:]
    for move in moveList:
        yN=y+move[0];xN=x+move[1]
        if yN < 0:
            yN = len(rowList)-1
        if yN == len(rowList):
            yN = 0
        if xN < 0:
            xN = len(rowList[0]) -1
        if xN == len(rowList[0]):
            xN = 0
        xyN = setXY(yN,xN)
        if xyN in rList:
            mList.append(xyN)
    graph[XY] = mList[:]
#print(graph,file=sys.stderr)

ergebnis= bfs_shortest_path(graph, start, ende)
print(ergebnis,file=sys.stderr)
for y in range(len(rowList)):
    erg=""
    for x in range(len(row)):
        XY = setXY(y,x)
        if XY in ergebnis and rowList[y][x] == "_":
            erg+="."
        else:
            erg+=rowList[y][x]
    print(erg)