# https://www.codingame.com/ide/puzzle/the-other-side

import sys,math

rowList=[['+', '+', '+'], ['+', '#', '+']]


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


def aufbauGraph(tab2,graph, maxY,maxX):
    for y in range(maxY):
        for x in range(maxX):
            feld = str(x) + "-" + str(y)
            wege = []
            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                x1 = x + new_position[0]
                y1 = y + new_position[1]
                if x1 >= 0 and x1 < maxX and y1 >= 0 and y1 < maxY:
                    if tab2[y1][x1] == "+":
                        wege.append(str(x1)+"-"+str(y1))
            graph[feld] = wege

graph = {}        
aufbauGraph(rowList,graph, len(rowList),len(rowList[0]))
#print(graph,file=sys.stderr)
startList,zielList=[],[]
for y in range(len(rowList)):
    if rowList[y][0] == "+":
        startList.append(str(0) + "-" + str(y))
    x = len(rowList[0])-1
    if rowList[y][x] == "+":
        zielList.append(str(x) + "-" + str(y))
#print(startList)
#print(zielList)
summe=0
for start in startList:
    tsum=0
    for ziel in zielList:
        erg = bfs_shortest_path(graph, start, ziel)
        if erg == None:
            a=0
        else:
            tsum=1
        #print(erg)
    summe+=tsum

print(summe)        