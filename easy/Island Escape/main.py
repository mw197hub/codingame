# https://www.codingame.com/ide/puzzle/island-escape

import sys,math

def bfs_shortest_path(graph, start, goalList):
    explored = []
    queue = [[start]]
 
    if start in goalList:
        return "no"
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour in goalList:
                    #return new_path
                    return "yes"
            explored.append(node)

    return "no"

def aufbauGraph(mapList,richtungen):
    graph={};goalList=set()
    for y in range(len(mapList)):
        for x in range(len(mapList)):
            pos=str(y)+"-"+str(x)            
            wList=[]
            for r in richtungen:
                yN=y+r[0];xN=x+r[1]
                if yN < 0 or yN >= len(mapList) or xN < 0 or xN >=len(mapList):
                    continue
                else:
                    wert=mapList[y][x]
                    if abs(wert - mapList[yN][xN]) <= 1:
                        wList.append(str(yN)+"-"+str(xN))
                    if wert == 0 and (y == 0 or y == len(mapList)-1 or x == 0 or x == len(mapList)-1):
                        goalList.add(pos)
            graph[pos] = wList
    return graph,goalList

#####


mapList=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]
mapList=[[0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]

#####
start=str(int((len(mapList)-1)/2))+"-"+str(int((len(mapList)-1)/2))
richtungen=[[1,0],[-1,0],[0,1],[0,-1]]

graph,goalList=aufbauGraph(mapList,richtungen)
#print(graph,file=sys.stderr)
#print(goalList,file=sys.stderr)

erg = bfs_shortest_path(graph, start, goalList)
print(erg)