# https://www.codingame.com/ide/puzzle/maze


def setXY(x,y):
    return str(x)+"-"+str(y)
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

    return "Kein Weg"

####
import sys,math

start=[1, 1];rList=['#######', '#.....#', '#####.#', '#.#...#', '#.#.###', '#......', '#######']


#####
graph={};goalList=[]
for y in range(len(rList)):
    for x in range(len(rList[0])):
        if rList[y][x] == ".":
            graph[setXY(x,y)]=[]
            if y == 0 or x == 0 or y == len(rList)-1 or x == len(rList[0])-1:
                goalList.append(setXY(x,y))
for XY in graph:
    x,y = getXY(XY)
    xyList=[]
    for xN,yN in [[1,0],[-1,0],[0,1],[0,-1]]:
        if setXY(x+xN,y+yN) in graph:
            xyList.append(setXY(x+xN,y+yN))
    graph[XY] = xyList[:]
#print(goalList)
ergList=[]
for goal in goalList:
    erg = bfs_shortest_path(graph, setXY(start[0],start[1]), goal)
    if not erg == "Kein Weg":
        x,y=getXY(goal)
        ergList.append([x,y])
print(len(ergList))
for xy in sorted(ergList):    
    print(str(xy[0])+" "+str(xy[1]))
