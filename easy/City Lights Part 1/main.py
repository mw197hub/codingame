# https://www.codingame.com/ide/puzzle/city-lights-part-1

import sys,math,string

def setXY(x,y):
    return str(x)+"-"+str(y)
def getXY(XY):
    xy=XY.split("-")
    return int(xy[0]),int(xy[1])

########

h=5;w=5;rowList=['.....', '.....', '..3..', '.....', '.....']
h=7;w=5;rowList=['.....', '....5', '.....', '.....', '.4...', '.....', '.....']
h=7;w=5;rowList=['.....', '....5', '.....', '.....', '.4...', '.....', '.....']
h=15;w=10;rowList=['......F...', '..........', '...1.....1', '.......2..', '........E.', '..........', '2.........', '..........', '........H.', '..........', '..........', '..........', '...4......', '..........', '.....2...1']

zahlList=string.ascii_uppercase
graph={}
lichtList={}
for y in range(h):
    row=rowList[y]
    for x in range(w):
        graph[setXY(x,y)] = 0
        if not row[x] == ".":
            lichtWert=9
            if row[x] in zahlList:
                for i in range(len(zahlList)):
                    lichtWert+=1
                    if zahlList[i] == row[x]:
                        break
            else:
                lichtWert=int(row[x])
            lichtList[setXY(x,y)] = lichtWert
            graph[setXY(x,y)] = lichtWert

for licht,lichtWert in lichtList.items():
    xN,yN=getXY(licht)
    for y in range(h):
        for x in range(w):
            if x == xN and y == yN:
                a=0
            else:
                wert= int(round(math.dist([xN,yN],[x,y]),0))
                if lichtWert - wert < 0:
                    a = 0#graph[setXY(x,y)] = 0
                else:
                    graph[setXY(x,y)] = graph[setXY(x,y)] + lichtWert - wert

for y in range(h):
    ausgabe=""
    for x in range(w):
        if graph[setXY(x,y)] > 9:
            if graph[setXY(x,y)] >= 36:
                ausgabe+="Z"
            else:
                ausgabe+=zahlList[graph[setXY(x,y)]-10]            
        else:
            ausgabe+=str(graph[setXY(x,y)])
    print(ausgabe)