import sys
import math
import copy


def bfs_shortest_path(graph, start, goal,links):
    allPath=[]
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
                if neighbour not in explored:
                    new_path = list(path)
                    new_path.append(neighbour)                
                    if neighbour == goal:
                        allPath.append(copy.deepcopy(new_path))
                    else:
                        if len(new_path) < int(8):
                            queue.append(new_path)
            #explored.append(node)

    return allPath


def sucheLeer(graph,si,exList,mehrFachDict,ergList,links,outList):
    distDict={}
    for p,zList in mehrFachDict.items():
        allPath = (bfs_shortest_path(graph,si,p,links))
        laenge = 999
        for path in allPath:
            anz = 0
            for z in path:                
                if not z in outList:
                    anz += 1
            if anz < laenge:
                laenge = anz
        distDict[p] = laenge

    print(distDict,file=sys.stderr)
    return distDict

def isZeit(graph,si,exList,mehrFachDict,ergList,links,outList):
    print(exList,file=sys.stderr)
    print(ergList,file=sys.stderr)
    print(mehrFachDict,file=sys.stderr)
    erg = [0,0]
    distDict = sucheLeer(graph,si,exList,mehrFachDict,ergList,links,outList)
    for p in sorted(distDict, key=distDict.get, reverse=False):
        zList = mehrFachDict[p]
        treffer = -1
        for z in zList:
            if not [p,z] in ergList and not [z,p] in ergList:
                erg = [p,z];treffer=z
        if treffer > -1:
            zList.remove(z);break
            
    if erg == [0,0]:
        for ex in exList:
            for p in graph[ex]:
                if not [ex,p] in ergList and not [p,ex] in ergList:
                    return [ex,p]
    
    if len(mehrFachDict[erg[0]]) == 1:
        mehrFachDict.pop(erg[0])
    return erg

def sucheOne(graph,si,exList,ergList):
    for p in graph[si]:
        if p in exList and not [si,p] in ergList and not [p,si] in ergList:
            return True,[si,p]
    return False,[0,0]

def setGraph(graph,g1,g2):
    if g1 in graph:          
        gList = graph[g1]
        gList.append(g2)
        graph[g1] = copy.deepcopy(gList)
    else:
        graph[g1] = [g2]

n,l,e=8,13,2
graph={6: [2, 3, 5], 2: [6, 0, 3], 7: [3, 1, 4], 3: [7, 6, 5, 4, 0, 1, 2], 5: [3, 6], 4: [3, 7], 1: [7, 0, 3], 0: [2, 1, 3]}
exList=[4,3]
si = 3

n,l,e=22,37,7
graph={5: [1, 4, 0, 7, 13], 1: [5, 2, 0, 8, 15, 12], 2: [1, 3, 0, 9, 8], 3: [2, 4, 0, 10, 9, 21], 4: [3, 5, 0, 10, 14], 0: [1, 2, 3, 4, 5], 7: [5, 8, 12, 17, 20], 8: [1, 7, 9, 2], 9: [2, 8, 3, 19, 21], 10: [3, 6, 4, 18, 21], 6: [10, 14, 13, 16, 17, 11], 12: [7, 1], 14: [4, 6], 13: [5, 6], 15: [1], 16: [6], 17: [7, 6], 18: [10], 19: [9], 11: [6], 20: [7], 21: [9, 10, 3]}
exList=[11, 12, 15, 16, 18, 19, 20]
si=5


mehrFachDict={};outList=set()
ergList=[[1,12]]
for g,pList in graph.items():
    anzList = []
    for p in pList:
        if p in exList:
            anzList.append(p)
            outList.add(g)
    if len(anzList) > 1:
        mehrFachDict[g] = copy.deepcopy(anzList)
print(mehrFachDict,file=sys.stderr)
print(outList,file=sys.stderr)

#one,erg = sucheOne(graph,si,exList,ergList)
#print(one)

erg = isZeit(graph,si,exList,{7: [12, 20], 6: [16, 11]},ergList,l,outList)
#erg = isZeit(graph,si,exList,mehrFachDict,ergList,l,outList)
print(erg)
ergList.append(erg)
