# https://www.codingame.com/ide/puzzle/there-is-no-spoon-episode-2

import sys,math,copy,time

def sucheVerbindungen(g1,g2,werteGraph,graph):
    antwort=[]
    wert1 = werteGraph[g1];wert2 = werteGraph[g2]
    if wert1 == 1 or wert2 == 1:
        antwort.append((g1,g2,1))
    else:
        if len(graph[g1]) * 2 == werteGraph[g1] or len(graph[g2]) * 2 == werteGraph[g2]:
            antwort.append((g1,g2,2))
        else:
            antwort.append((g1,g2,1))
            antwort.append((g1,g2,2))
    return antwort

def pruefeUeberKreuz(verbindungen,g1,g2):
    for verb in verbindungen:
        c1,c2,wert= verb
        #print("{} zu {} # {} zu {}".format(min(cy1,cy2),min(y,y1),max(cy1,cy2),max(y,y1)))
        if min(c1[0],c2[0]) > min(g1[0],g2[0]) and max(c1[0],c2[0]) < max(y,y1):
            if min(c1[1],c2[1]) < min(g1[1],g2[1]) and max(c1[1],c2[1]) > max(x,x1):
                return False
        if min(c1[1],c2[1]) > min(g1[1],g2[1]) and max(c1[1],c2[1]) < max(g1[1],g2[1]):
            if min(c1[0],c2[0]) < min(g1[0],g2[0]) and max(c1[0],c2[0]) > max(g1[0],g2[0]):
                return False
    return True

def pruefeAnzahl(werteGraph,verbindungen,g1,g2,r):
    wert1=werteGraph[g1];wert2=werteGraph[g2]
    bisher1,bisher2=0,0
    for verb in verbindungen:
        c1,c2,wert=verb
        if (c1 == g1 and c2 == g2) or (c1 == g2 and c2 == g1):
            return False
        if c1 == g1 or c2 == g1:
            bisher1+= wert
        if c1 == g2 and c2 == g2:
            bisher2+= wert
    if wert1 >= bisher1+r and wert2 >= bisher2 + r:
        return True
    return False

def endeErreicht(verbindungen,werteGraph):
    pGraph= copy.deepcopy(werteGraph)
    for verb in verbindungen:
        c1,c2,wert=verb
        pGraph[(c1)] -= wert
        pGraph[(c2)] -= wert
    for yx in pGraph:
        if not pGraph[yx] == 0:
            #if pGraph[yx] < 0:
              #  print(" da läuft was schief",file=sys.stderr)
              #  exit(1)
            return False
    
    return True





def bfs_shortest_path(wege,graph, startPos, posList,werteGraph,moeglicheWege):
    explored = [[startPos]]
    queue = [[startPos]]
    queueV = [[]]
 
    while queue:
        path = queue.pop(0)
        pathV = queueV.pop(0)
        print(pathV,file=sys.stderr)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:                
                if not neighbour in path:
                    vNeighbours = sucheVerbindungen(node,neighbour,werteGraph,graph)
                    for vN in vNeighbours:
                        if pruefeUeberKreuz(pathV,node,neighbour): 
                            if pruefeAnzahl(werteGraph,verbindungen,node,neighbour,vN[2]):             
                                new_path = list(path)
                                new_pathV = list(pathV)  
                                new_path.append(neighbour)
                                queue.append(new_path)
                                new_pathV.append(vN)
                                queueV.append(new_pathV)
                                #print(len(new_path))
                                #if sorted(new_path) == sorted(posList):     
                                if endeErreicht(new_pathV,werteGraph):
                                    wege.append(copy.deepcopy(new_pathV))      
                                    return wege  
                                #return new_path
          #  explored.append(node)

    return wege

##############

lineList=[['1', '.', '2'], ['.', '.', '.'], ['.', '.', '1']]   # 1
#lineList=[['2', '.'], ['4', '2']]  # 2
lineList=[['1', '.', '3'], ['.', '.', '.'], ['1', '2', '3']]  # 3
#lineList=[['1', '4', '.', '3'], ['.', '.', '.', '.'], ['.', '4', '.', '4']]   # 4
#lineList=[['2', '.', '.', '2', '.', '1', '.'], ['.', '3', '.', '.', '5', '.', '3'], ['.', '2', '.', '1', '.', '.', '.'], ['2', '.', '.', '.', '2', '.', '.'], ['.', '1', '.', '.', '.', '.', '2']]  # 6
#lineList=[['3', '.', '.', '2', '.', '2', '.', '.', '1', '.', '.', '.', '.', '3', '.', '.', '.', '.', '.', '.', '.', '.', '4'], ['.', '2', '.', '.', '1', '.', '.', '.', '.', '2', '.', '6', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', '.'], ['.', '.', '3', '.', '.', '6', '.', '.', '.', '.', '3', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '2', '.', '.', '.', '.', '.', '.', '.', '.', '1', '.', '.', '3', '.', '3', '.'], ['.', '.', '1', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '3', '.', '.', '3', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '3', '.', '.', '3', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '3', '.', '.', '.', '8', '.', '.', '.', '.', '.', '8', '.', '.', '.', '.', '.', '.', '.', '.', '.', '3', '.'], ['6', '.', '5', '.', '1', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '1', '.', '.', '3', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', '.', '.', '6', '.', '3', '1', '.', '.', '2', '.'], ['.', '.', '4', '.', '.', '4', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['5', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '7', '.', '.', '.', '7', '.', '.', '.', '3', '.', '3', '.'], ['.', '2', '.', '.', '3', '.', '.', '3', '.', '.', '3', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '2', '.', '.', '2', '.', '.', '.', '1', '.', '6', '.', '.', '.', '3', '.', '.', '.'], ['.', '.', '.', '.', '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '4', '.', '.', '.', '.', '5', '.', '.', '.', '3', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', '.', '3', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '3', '.', '3', '.', '.', '2', '.', '4', '4', '.', '.', '.', '.', '1', '.', '.'], ['3', '.', '.', '.', '1', '.', '3', '.', '2', '.', '3', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '2', '.', '.', '.', '.', '.', '3', '.', '.', '.', '6', '.', '.', '.', '.', '.', '.', '.', '.', '.', '5', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '1', '.', '.', '.', '.', '.', '.'], ['.', '1', '.', '.', '.', '.', '.', '.', '.', '3', '.', '6', '.', '2', '.', '.', '.', '2', '.', '.', '.', '4', '.'], ['5', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '3', '.', '.', '.', '.', '.', '3'], ['4', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '4', '.', '2']]


########

start=time.time()

graph={};graphVerbindungen={}
verbindungen=[];gesamtAnzahl=0
moeglicheWege=[]
posList=[];startPos=()
werteGraph={}
wege=[[1,0],[-1,0],[0,1],[0,-1]]
for y in range(len(lineList)):
    for x in range(len(lineList[0])):
        if not lineList[y][x] == ".":
            posList.append((y,x))
            nList=[]
            werteGraph[(y,x)] =(int(lineList[y][x]))
            for weg in wege:
                y1=y;x1=x
                while True:
                    y1+=weg[0];x1+=weg[1]
                    if y1 < 0 or x1 < 0 or y1 >= len(lineList) or x1 >= len(lineList[0]):
                        break
                    if not lineList[y1][x1] == ".":                        
                        nList.append((y1,x1))
                        break
            graph[(y,x)] = copy.deepcopy(nList)


for g1,gList in graph.items():
    startPos=g1
    for g2 in gList:
        vorhanden=False
        for mWeg in moeglicheWege:
            m1,m2,wert=mWeg
            if (g1 == m1 and g2 == m2) or (g1 == m2 and g2 == m1):
               vorhanden=True
        if not vorhanden:
            wert1 = werteGraph[g1];wert2 = werteGraph[g2]
            if wert1 == 1 or wert2 == 1:
                moeglicheWege.append((g1,g2,1))
            else:
                if len(graph[g1]) * 2 == werteGraph[g1] or len(graph[g2]) * 2 == werteGraph[g2]:
                    moeglicheWege.append((g1,g2,2))
                else:
                    moeglicheWege.append((g1,g2,1))
                    moeglicheWege.append((g1,g2,2))

print(graph,file=sys.stderr)
print((moeglicheWege),file=sys.stderr)

queue,wege=[],[]
queue = bfs_shortest_path(wege,graph, startPos, posList,werteGraph,moeglicheWege)
print("----------------")
print("{} :  {}".format("path",queue),file=sys.stderr)


for teil1 in queue:
    for verb in teil1:
        ## print("{} {} {} {} {}".format(verb[0][1],verb[0][0],verb[1][1],verb[1][0],verb[2]))
        print("{} {} {} {} {}".format(verb[0][0],verb[0][1],verb[1][0],verb[1][1],verb[2]))

print("Zeit: {}".format(time.time()-start),file=sys.stderr)