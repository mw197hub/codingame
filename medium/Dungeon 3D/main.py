# https://www.codingame.com/ide/puzzle/dungeon-3d

import sys,math,copy


def bfs_shortest_path(graph, start, goal):
    explored = []
    queue = [[start]]
 
    if start == goal:
        return [] #"That was easy! Start = goal"
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

    return []  #"So sorry, but a connecting path doesn't exist :("

def aufbauGraph(wege,lineList):
    graph={}
    for z in range(len(lineList)):
        for y in range(len(lineList[0])):
            for x in range(len(lineList[0][0])):
                if not lineList[z][y][x] == "#":
                    tab=[]
                    for weg in wege:
                        z1=z+weg[0];y1=y+weg[1];x1=x+weg[2]
                        if z1 > -1 and z1 < len(lineList) and y1 > -1 and y1 < len(lineList[0]) and x1 > -1 and x1 < len(lineList[0][0]):
                            if not lineList[z1][y1][x1] == "#":
                                tab.append((z1,y1,x1))
                    graph[(z,y,x)] = copy.deepcopy(tab)
    return graph



# 1
lineList=[[['.', '.', '#'], ['.', '#', '#'], ['A', '#', '#']], [['#', '.', '#'], ['#', '.', 'S'], ['#', '.', '.']]]
# 2
#lineList=[[['.', '.', '.', '#'], ['#', '#', '#', '.'], ['#', '#', '#', 'S']], [['.', '#', '.', '.'], ['#', '#', '#', '.'], ['#', '#', '#', '#']], [['.', '#', '#', '#'], ['#', '#', '.', '.'], ['#', '#', '#', '#']], [['.', '#', '#', '#'], ['#', '#', '#', '#'], ['#', '#', '.', '#']], [['A', '.', '.', '#'], ['#', '#', '#', '#'], ['#', '#', '#', '#']]]

lineList=[[['A', '.', '.'], ['#', '#', '#'], ['.', '.', 'S']], [['.', '#', '.'], ['.', '#', '#'], ['#', '#', '.']]]


erg=0
start=[]
ziel=[]

for z in range(len(lineList)):
    for y in range(len(lineList[0])):
        for x in range(len(lineList[0][0])):
            if lineList[z][y][x] == "A":
                start=(z,y,x)
            if lineList[z][y][x] == "S":
                ziel=(z,y,x)
#print("{}   {}".format(start,ziel))

wege=[[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]
graph=aufbauGraph(wege,lineList)
#print(graph,file=sys.stderr)


path = bfs_shortest_path(graph,start,ziel)
print(path,file=sys.stderr)

if len(path) > 0:
    print(len(path)-1)
else:
    print("NO PATH")
