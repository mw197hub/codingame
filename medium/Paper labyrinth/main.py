# https://www.codingame.com/ide/puzzle/paper-labyrinth

import sys,math

def setXY(x,y):
    return str(x)+"-"+str(y)
def getXY(XY):
    xy = XY.split("-")
    return int(xy[0]),int(xy[1])
def bfs_shortest_path(graph, start, goal):
    explored = [];queue=[]
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

#####
start="0-0";ziel="5-0";lList=['75555d'] #1
start="0-0";ziel="1-1";lList=['e65c', 'abea', '2519', '355d'] #2


####
graph={}
moveDict={'0':[[1,0],[-1,0],[0,1],[0,-1]],
          '1':[[1,0],[-1,0],[0,-1]],
          '2':[[1,0],[0,1],[0,-1]],
          '3':[[1,0],[0,-1]],
          '4':[[1,0],[-1,0],[0,1]],
          '5':[[1,0],[-1,0]],
          '6':[[1,0],[0,1]],
          '7':[[1,0],],
          '8':[[-1,0],[0,1],[0,-1]],
          '9':[[-1,0],[0,-1]],
          'a':[[0,1],[0,-1]],
          'b':[[0,-1]],
          'c':[[-1,0],[0,1]],
          'd':[[-1,0]],
          'e':[[0,1]],
          'f':[]
          }
for y in range(len(lList)):
    for x in range(len(lList[0])):
        key=setXY(x,y)
        graph[key]=[]
for y in range(len(lList)):
    for x in range(len(lList[0])):
        key=setXY(x,y)
        wege=[]
        for xy in moveDict[lList[y][x]]:
            xN=x+xy[0];yN=y+xy[1]
            keyN=setXY(xN,yN)
            if keyN in graph:
                wege.append(keyN)
        graph[key]=wege[:]
print(graph,file=sys.stderr)
hin=bfs_shortest_path(graph, start, ziel)
back=bfs_shortest_path(graph, ziel,start)
print(str(len(hin)-1)+" "+str(len(back)-1))