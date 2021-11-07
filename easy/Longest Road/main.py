import sys
import math
import copy

def aufbauGraph(tab,graph,player):
    for y in range(len(tab)):
        for x in range(len(tab)):
            feld = str(x) + "-" + str(y)
            wege = []
            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                x1 = x + new_position[0]
                y1 = y + new_position[1]
                if x1 >= 0 and x1 < len(tab) and y1 >= 0 and y1 < len(tab):
                    if tab[y1][x1].lower() == player:
                        wege.append(str(x1)+"-"+str(y1))
            graph[feld] = wege

def pruefeWeg(graph,x,y,player,lineList):
    laenge = 0
    visited = []
    queue = []
    weg = []    
    dfs(visited,graph,str(x) + "-" + str(y),queue,weg)
    #
    #bfs(visited,graph,str(x) + "-" + str(y),queue)
    #print(queue,file=sys.stderr)
    for qu in queue:
        lae = 0
        for feld in qu:
            x,y = feld.split("-")
            if lineList[int(y)][int(x)] == player:
                lae += 1
        if lae > laenge:
            laenge = lae
    return laenge

def bfs(visited,graph,node,queue):
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0) 
        #print (s, end = " ") 
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


def dfs(visited,graph,feld,queue,weg):
    if feld not in visited:
        visited.append(feld)        
        weg.append(feld)
        for nachbar in graph[feld]:
            dfs(visited,graph,nachbar,queue,weg)
        queue.append(copy.deepcopy(weg))
        weg.pop()

lineList = ['aaaaa', 'A#a#a', 'aaaa#', '#a###', 'aaaaa'] # A 13
lineList = ['Bb###aA###', 'b#Cc#a####', '###c#a####', '###ccCccc#', '#####a####', '#####aAaaa', '######d###', '#dBbb#D###', '#d####d###', '#D####d###']
#lineList = ['Aa###', '#a###', '#a###', '#aa##', '##a##'] # A 6
#lineList = ['a#a','aaa','a#a'] # 5

playerList = {}
for line in lineList:
    for l in line:
        if not l == "#":
            playerList[l.lower()] = 0
#print(playerList,file=sys.stderr)

graph = {}
for player in playerList:
    #print(player,file=sys.stderr)
    aufbauGraph(lineList,graph,player)
    #print(graph,file=sys.stderr)
    for y in range(len(lineList)):
        for x in range(len(lineList)):
            if lineList[y][x].lower() == player:
                laenge = pruefeWeg(graph,x,y,player,lineList)
                if playerList[player] < laenge:
                    playerList[player] = laenge

print(playerList,file=sys.stderr)         
sortList = sorted(playerList.items(),reverse=True,key=lambda x: x[1])
player,anzahl = sortList[0]
if anzahl < 5:
    print("0")
else:
    print(player.upper()+" " + str(anzahl))
    