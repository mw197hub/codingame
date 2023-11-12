import sys
import math

# The machines are gaining ground. Time to show them what we're really made of...
def aufbauTabelle(zeile, tabelle, y):
    i = 0
    while i < len(zeile):
        if zeile[i:i+1] != '.':
            wert = str(i) + '-' + str(y)
            tabelle[wert] = zeile[i:i+1]    
        i = i +1

def neuWerte(x,y,i):
    if i == 0:
        return x, y -1
    if i == 1:
        return x +1, y
    if i == 2:
        return x, y + 1
    if i == 3:
        return x -1, y

def aufbauGraph(tabelle,graph, maxX, maxY):
    for feld in tabelle:
        x,y = keyloesen(feld)
        nachbarListe = []
        for i in range(4):
            
            x1 = x
            y1 = y
            while True:
                x1, y1 = neuWerte(x1,y1,i)
                if x1 < 0 or x1 >= maxX or y1 < 0 or y1 >= maxY:
                    break
                key1 = str(x1) + "-" + str(y1)                
                if key1 in tabelle:
                   # print(feld + " : " + key1,file=sys.stderr)
                    nachbarListe.append(key1)
                    break
      #  print(nachbarListe,file=sys.stderr)
        graph[feld] = nachbarListe



def keyloesen(key):
    x,y = key.split("-")
    return int(x), int(y)

def ausgabe(von,nach,tabelle,anzahl):
    xS,yS = keyloesen(von)
    xZ,yZ = keyloesen(nach)
    print(str(xS) + " " + str(yS) + " " + str(xZ) + " " + str(yZ) + " " + str(anzahl))
    wert = int(tabelle[von])
    tabelle[von] = str(wert - anzahl)
    wert = int(tabelle[nach])
    tabelle[nach] = str(wert -  anzahl)
   # print(tabelle,file=sys.stderr)



tabelle = {}
graph = {}

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
print(str(width) + " - " + str(height),file=sys.stderr)
for i in range(height):
    line = input()  # width characters, each either a number or a '.'
    print(line,file=sys.stderr)
    aufbauTabelle(line,tabelle,i)

print(tabelle,file=sys.stderr)
aufbauGraph(tabelle,graph,width,height)
print(graph,file=sys.stderr)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

ergList = []
# Two coordinates and one integer: a node, one of its neighbors, the number of links connecting them.
for feld in tabelle:
    if int(tabelle[feld]) > 0:
        ziele = graph[feld]
        if int(tabelle[feld]) / len(ziele) == 2:
            for ziel in ziele:
                ausgabe(feld,ziel,tabelle,2)

for feld in tabelle:
    if int(tabelle[feld]) > 0:
        ziele = graph[feld]
        for ziel in ziele:
            if int(tabelle[ziel]) > 0 and int(tabelle[feld]) > 0:
                ausgabe(feld,ziel,tabelle,1)
                    
