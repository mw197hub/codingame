import sys
import math

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

    return "So sorry"
 

def aufbauGraph(tabelle,graph,punkte):
    for p in punkte:
        neuTab = []
        for tab in tabelle:
            x,y = tab.split(" ")
            if p == x:
                neuTab.append(y)
            if p == y:
                neuTab.append(x)
        graph[p] = neuTab

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
print("nodes: " + str(n) + "   links: " + str(l) + "  Num of exit: " +str(e),file=sys.stderr)
tabelle = []
ziele = []
graph = {}
punkte = set()


for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    punkte.add(str(n1))
    punkte.add(str(n2))
    tabelle.append(str(n1)+ " " + str(n2))
print(tabelle,file=sys.stderr)
print(punkte,file=sys.stderr)

for i in range(e):
    ei = int(input())  # the index of a gateway node
    ziele.append(str(ei))
    print("exit: " + str(ei),file=sys.stderr)

print("################",file=sys.stderr)
zielListe = []
aufbauGraph(tabelle,graph,punkte)
for ziel1 in ziele:    
    for ziel2 in ziele:
        if ziel1 != ziel2:
            ergebnis = bfs_shortest_path(graph,ziel1,ziel2)
            if len(ergebnis) == 3:
                treffer = 0
                for vorhanden in zielListe:
                    if vorhanden[1] == ergebnis[1]:
                        treffer = 1
                if treffer == 0:
                    zielListe.append(ergebnis)
print(zielListe,file=sys.stderr)

print("################",file=sys.stderr)
# game loop
while True:
    aufbauGraph(tabelle,graph,punkte)
   # print(graph,file=sys.stderr)
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    print("Skynet: " + str(si),file=sys.stderr)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    ergList = []
    for ziel in ziele:
        ergebnis = bfs_shortest_path(graph,ziel,str(si))
        if ergebnis != "So sorry":
            ergList.append(ergebnis)
            print(ergebnis,file=sys.stderr)

    # Example: 3 4 are the indices of the nodes you wish to sever the link between
    start = ""
    erg = ""
    laenge = 99
    for ergebnis in ergList:
        if len(ergebnis) < laenge:
            erg = ergebnis[1]
            start = ergebnis[0]
            laenge = len(ergebnis)
    print("laenge: " + str(laenge) + " ",file=sys.stderr)
    neuLaenge = 99
    if laenge > 2 and len(zielListe) > 0:
        print(zielListe,file=sys.stderr)
        entfernen = []
        for ziel in zielListe:
            for ergebnis in ergList:
                if ziel[0] == ergebnis[0]:
                  #  print(ergebnis,file=sys.stderr)
                    anzahl = len(ergebnis)
                    for e2 in range(1,len(ergebnis) -1):
                        e1 = int(ergebnis[e2])
                        for s1 in ziele:
                         #   print("1: " + str(e1) + " " + str(s1),file=sys.stderr)
                         #   print("2: " + str(s1) + " " + str(e1),file=sys.stderr)
                            if str(e1) + " " + str(s1) in tabelle or str(s1) + " " + str(e1) in tabelle:
                         #       print("treffer: " + str(e1) + " " + str(s1),file=sys.stderr)
                                anzahl = anzahl - 1
                    print("anzahl: " + str(anzahl),file=sys.stderr)
                    if anzahl < neuLaenge:                       
                        start = ziel[0]
                        erg = ziel[1]
                        entfernen = ziel
                        neuLaenge = anzahl
        zielListe.remove(entfernen)

    print(start + " " + erg)
    
    if start + " " + erg in tabelle:
        tabelle.remove(start + " " + erg)
    if erg + " " + start in tabelle:
        tabelle.remove(erg + " " + start)

