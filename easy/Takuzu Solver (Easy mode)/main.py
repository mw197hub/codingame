#https://www.codingame.com/ide/puzzle/takuzu-solver-easy-mode

import sys,math

def setXY(x,y):
    return str(x)+"-"+str(y)
def getXY(XY):
    xy = XY.split("-")
    return int(xy[0]),int(xy[1])

def dreiPruefen(graph,leereFelder,n):
    for y in range(n):
        for x in range(n-2):
            if graph[setXY(x,y)] == graph[setXY(x+1,y)] and graph[setXY(x+2,y)] == "." and not graph[setXY(x,y)] == "." :
                if graph[setXY(x,y)] == '0':
                    graph[setXY(x+2,y)] = '1'
                else:
                    graph[setXY(x+2,y)] = '0'
                leereFelder.remove(setXY(x+2,y))
            if graph[setXY(x,y)] == "." and graph[setXY(x+1,y)] == graph[setXY(x+2,y)] and not graph[setXY(x+1,y)] == "." :
                if graph[setXY(x+1,y)] == '0':
                    graph[setXY(x,y)] = '1'
                else:
                    graph[setXY(x,y)] = '0'
                leereFelder.remove(setXY(x,y))
    for x in range(n): 
        for y in range(n-2):    
            if graph[setXY(x,y)] == graph[setXY(x,y+1)] and graph[setXY(x,y+2)] == "." and not graph[setXY(x,y)] == "." :
                if graph[setXY(x,y)] == '0':
                    graph[setXY(x,y+2)] = '1'
                else:
                    graph[setXY(x,y+2)] = '0'
                leereFelder.remove(setXY(x,y+2))
            if graph[setXY(x,y)] == "." and graph[setXY(x,y+1)] == graph[setXY(x,y+2)] and not graph[setXY(x,y+1)] == "." :
                if graph[setXY(x,y+1)] == '0':
                    graph[setXY(x,y)] = '1'
                else:
                    graph[setXY(x,y)] = '0'
                leereFelder.remove(setXY(x,y))

def gleicheVerteilung(graph,leereFelder,n):
    for y in range(n):
        anzahlNull=0;anzahlEins=0;zwFeld=[]
        for x in range(n):
            if graph[setXY(x,y)] == '1':
                anzahlEins+=1
            elif graph[setXY(x,y)] == '0':
                anzahlNull+=1
            else:
                zwFeld.append(setXY(x,y))
        if anzahlNull == n //2:
            for feld in zwFeld:
                leereFelder.remove(feld)
                graph[feld] = '1'
        if anzahlEins == n //2:
            for feld in zwFeld:
                leereFelder.remove(feld)
                graph[feld] = '0'
    for x in range(n):
        anzahlNull=0;anzahlEins=0;zwFeld=[]
        for y in range(n):
            if graph[setXY(x,y)] == '1':
                anzahlEins+=1
            elif graph[setXY(x,y)] == '0':
                anzahlNull+=1
            else:
                zwFeld.append(setXY(x,y))
        if anzahlNull == n //2:
            for feld in zwFeld:
                leereFelder.remove(feld)
                graph[feld] = '1'
        if anzahlEins == n //2:
            for feld in zwFeld:
                leereFelder.remove(feld)
                graph[feld] = '0'
def dazwischen(graph,leereFelder,n):
    for y in range(n):
        for x in range(n-2):
            if graph[setXY(x,y)] == graph[setXY(x+2,y)] and graph[setXY(x+1,y)] == "." and not graph[setXY(x,y)] == "." :
                if graph[setXY(x,y)] == '0':
                    graph[setXY(x+1,y)] = '1'
                else:
                    graph[setXY(x+1,y)] = '0'
                leereFelder.remove(setXY(x+1,y))
    for x in range(n):
        for y in range(n-2):
            if graph[setXY(x,y)] == graph[setXY(x,y+2)] and graph[setXY(x,y+1)] == "." and not graph[setXY(x,y)] == "." :
                if graph[setXY(x,y)] == '0':
                    graph[setXY(x,y+1)] = '1'
                else:
                    graph[setXY(x,y+1)] = '0'
                leereFelder.remove(setXY(x,y+1))                


########################

rowList=['.0...1', '0.11..', '..1..0', '.1...0', '....1.', '11.0.0']
rowList=['.....00.', '.1......', '11.0..0.', '..0....1', '.1...0..', '0.0..0..', '....1..0', '0.11.11.']

# anzahl 0 und 1 immer gleich
# keine drei gleichen werte
# keine gleichen reihen oder spalten

graph={}
leereFelder=[]
for y in range(0,len(rowList)):
    row = rowList[y]
    for x in range(0,len(row)):
        if row[x] == ".":
            leereFelder.append(setXY(x,y))
        graph[setXY(x,y)] = row[x]
#print(graph,file=sys.stderr)
runde=0
while leereFelder:
   # print(len(leereFelder))
    dreiPruefen(graph,leereFelder,len(rowList))
    #print(len(leereFelder))
    gleicheVerteilung(graph,leereFelder,len(rowList))
    #print(len(leereFelder))
    dazwischen(graph,leereFelder,len(rowList))
    runde+=1
    if runde > 40:
        break

for y in range(len(rowList)):
    ausgabe = ""
    for x in range(len(rowList)):
        ausgabe+= (graph[setXY(x,y)])
    print(ausgabe)