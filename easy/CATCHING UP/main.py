import sys
import math
import copy


def setXY(y,x):
    return str(y)+'-'+str(x)
def getXY(yx):
    return [int(i) for i in yx.split("-")]

def setGraph(mapList,graph):
    start=''
    for y in range(10):
        for x in range(10):
            if mapList[y][x] in ['-','P','E']:
                if mapList[y][x] == "P":
                    start = setXY(y,x)
                nList=[]
                for n in [[1,0],[-1,0],[0,1],[0,-1]]:
                    nY= y + n[0]
                    nX= x + n[1]
                    if nY >=0 and y + n[0] < 10 and nX >=0 and x+n[1] <10:
                        
                        if mapList[nY][nX] in ['-','P','E']:
                            nList.append(setXY(nY,nX))
                graph[setXY(y,x)] = copy.deepcopy(nList)
    return start

def sucheWeg(start,ziel,mapList,graph):
    explored = []
    queue=[[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == ziel:
                    return new_path
            explored.append(node)

def setzeR(start,z):
    startYX = getXY(start);wegYX=getXY(z)
    if startYX[0] +1 == wegYX[0] or startYX[0] -9 == wegYX[0]:
        return "D"
    if startYX[0] -1 == wegYX[0] or startYX[0] +9 == wegYX[0]:
        return "U"
    if startYX[1] +1 == wegYX[1] or startYX[1] -9 == wegYX[1]:
        return "R"
    if startYX[1] -1 == wegYX[1] or startYX[1] +9 == wegYX[1]:
        return "L"



mapList=[['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '-', '-', '-', '-', 'P', '-', '-', '-', '*'], ['*', '-', '-', '-', '-', '-', '-', '-', '-', '*'], ['*', '-', '-', '-', '-', '-', '-', '-', '-', '*'], ['*', '-', '*', '*', '*', '*', '*', '-', '-', '*'], ['*', '-', '-', '-', '-', '-', 'E', '-', '-', '*'], ['*', '-', '-', '-', '-', '-', '-', '-', '-', '*'], ['*', '-', '-', '-', '-', '-', '-', '-', '-', '*'], ['*', '-', '-', '-', '-', '-', '-', '-', '-', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
mapList=[['*', '-', '-', '-', '-', '-', '-', '-', '-', '*'], ['*', '*', '-', 'P', '-', '-', '-', '-', '*', '*'], ['*', '-', '*', '*', '*', '*', '*', '-', '*', '*'], ['*', '*', '-', '-', '*', '*', '*', '-', '*', '*'], ['*', '*', '-', '-', '*', '*', '-', '-', '*', '*'], ['*', '*', '-', '-', '-', 'E', '-', '-', '*', '*'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['*', '-', '-', '-', '-', '-', '-', '-', '-', '*'], ['*', '*', '*', '-', '-', '-', '-', '-', '*', '*'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]
mapList=[['P', '*', '-', '-', '-', '*', '-', '-', '-', '*'], ['-', '*', '-', '*', '-', '*', '-', '*', '-', '*'], ['-', '*', '-', '*', '-', '*', '-', '*', '-', '*'], ['E', '*', '-', '*', '-', '*', '-', '*', '-', '*'], ['-', '*', '-', '*', '-', '*', '-', '*', '-', '*'], ['-', '*', '-', '*', '-', '*', '-', '*', '-', '*'], ['-', '*', '-', '*', '-', '*', '-', '*', '-', '*'], ['-', '*', '-', '*', '-', '*', '-', '*', '-', '*'], ['-', '*', '-', '*', '-', '*', '-', '*', '-', '-'], ['-', '-', '-', '*', '-', '-', '-', '*', '-', '-']]



graph={}
start = setGraph(mapList,graph)
print(graph,file=sys.stderr)
start='7-8'
ziel='9-9'
weg = sucheWeg(start,ziel,mapList,graph)
print(weg)
richtung = setzeR(start,weg[1])
print(richtung)
start=weg[1]