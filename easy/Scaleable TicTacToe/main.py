# https://www.codingame.com/ide/puzzle/scaleable-tictactoe

import sys,math

def setXY(x,y):
    return str(x)+"-"+str(y)
def getXY(XY):
    xy=XY.split("-")
    return int(xy[0]),int(xy[1])
def gewinner(graph,n,g,spieler):
    for y in range(n):
        for x in range(n-g+1):
            anzahl=0
            for i in range(g):
                if graph[setXY(x+i,y)] == spieler:
                    anzahl+=1
            if anzahl== g:
                for i in range(g):
                    graph[setXY(x+i,y)] = "-"
                return True
    for x in range(n):
        for y in range(n-g+1):
            anzahl=0
            for i in range(g):
                if graph[setXY(x,y+i)] == spieler:
                    anzahl+=1
            if anzahl== g:
                for i in range(g):
                    graph[setXY(x,y+i)] = "|"
                return True
    for y in range(n-g+1):
        for x in range(n-g+1):
            anzahl=0
            for i in range(g):
                if graph[setXY(x+i,y+i)] == spieler:
                    anzahl+=1
            if anzahl== g:
                for i in range(g):
                    graph[setXY(x+i,y+i)] = "\\"
                return True
    for y in range(n-g+1):
        for x in range(n-1,n-g-1,-1):
            anzahl=0
            for i in range(g):
                if setXY(x-i,y+i) in graph and graph[setXY(x-i,y+i)] == spieler:
                    anzahl+=1
            if anzahl== g:
                for i in range(g):
                    graph[setXY(x-i,y+i)] = "/"
                return True

    return False

###############
n=3;g=3;rowList=['X O', 'XO ', 'XOX']
n=5;g=4;rowList=['O XXX', 'OX   ', ' O   ', ' XXXX', '  O O']
n=3;g=3;rowList=['X O', 'XX ', 'OOX']
n=3;g=3;rowList=['X O', 'XO ', 'OOX']
n=7;g=4;rowList=['O    XO', 'XX   X ', 'OXOOX X', 'XO OX X', 'XO XXX ', '  XX OO', ' X  O O']
n=7;g=4;rowList=['O XXX  ','XOOO OO','  XX XX','  XOOOX',' XX O  ','X   XOO','X   O X']



graph={};leerFelder=[]
for y in range(n):
    row = rowList[y]
    for x in range(n):
        graph[setXY(x,y)] = row[x]
        if row[x] == " ":
            leerFelder.append(setXY(x,y))

ergebnisX = gewinner(graph,n,g,"X")
ergebnisO = gewinner(graph,n,g,"O")

for y in range(n):
    ausgabe=""
    for x in range(n):
        ausgabe+=graph[setXY(x,y)]
    print(ausgabe)
if ergebnisO:
    print("The winner is O.")
elif ergebnisX:
    print("The winner is X.")
elif len(leerFelder) == 0:
    print("The game ended in a draw!")
else:
    print("The game isn't over yet!")
