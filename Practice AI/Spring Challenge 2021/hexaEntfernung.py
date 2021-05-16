import sys
import math

hexaNummer= {25:'0-3',24:'0-5',23:'0-7',22:'0-9',
26:'1-2', 11:'1-4',10:'1-6', 9:'1-8',21:'1-10',
27:'2-1',12:'2-3',3:'2-5',2:'2-7',8:'2-9',20:'2-11',
28:'3-0',13:'3-2',4:'3-4',0:'3-6',1:'3-8',7:'3-10',19:'3-12',
29:'4-1',14:'4-3',5:'4-5',6:'4-7',18:'4-9',36:'4-11',
30:'5-2',15:'5-4',16:'5-6',17:'5-8',35:'5-10',
31:'6-3',32:'6-5',33:'6-7',34:'6-9'}
nrHexa = {}

class Cell:
    def __init__(self, cell_index, richness, neighbors):
        self.cell_index = cell_index
        self.richness = richness
        self.neighbors = neighbors

cellList = {}
hexaList = [
    [0,0,0,1,0,1,0,1,0,1,0,0,0],
    [0,0,1,0,1,0,1,0,1,0,1,0,0],
    [0,1,0,1,0,1,0,1,0,1,0,1,0],
    [1,0,1,0,1,0,1,0,1,0,1,0,1], #Mitte
    [0,1,0,1,0,1,0,1,0,1,0,1,0],
    [0,0,1,0,1,0,1,0,1,0,1,0,0],
    [0,0,0,1,0,1,0,1,0,1,0,0,0]
]
f = open("C:\\Users\wiedm\Python\codingame\Practice AI\Spring Challenge 2021\input.txt", "r")
for x in f:
    inX = [int(n) for n in x.split(",")]
    cellList[inX[0]] = Cell(inX[0],inX[1],[inX[2], inX[3],inX[4],inX[5],inX[6],inX[7]])

posList = []
graph = {}

for nr,pos in hexaNummer.items():
    nrHexa[pos] = nr

print(nrHexa)
for r in range(7):
    for s in range(13):
        if hexaList[r][s] == 1:
            posList.append(str(r)+"-"+str(s))
#print(posList)
for pos in posList:
    r,s = pos.split("-")
    r = int(r)
    s = int(s)
    zielList = []
    zielHexa = []
    if str(r) + "-" + str(s +2) in posList:
        zielList.append(str(r) + "-" + str(s +2))
        zielHexa.append(nrHexa[(str(r) + "-" + str(s +2))])
    if str(r) + "-" + str(s -2) in posList:
        zielList.append(str(r) + "-" + str(s -2))
        zielHexa.append(nrHexa[(str(r) + "-" + str(s -2))])
    if str(r +1) + "-" + str(s +1) in posList:
        zielList.append(str(r +1) + "-" + str(s +1))
        zielHexa.append(nrHexa[(str(r +1) + "-" + str(s +1))])
    if str(r -1) + "-" + str(s +1) in posList:
        zielList.append(str(r -1) + "-" + str(s +1))
        zielHexa.append(nrHexa[(str(r -1) + "-" + str(s +1))])
    if str(r -1) + "-" + str(s -1) in posList:
        zielList.append(str(r -1) + "-" + str(s -1))
        zielHexa.append(nrHexa[(str(r -1) + "-" + str(s -1))])
    if str(r +1) + "-" + str(s -1) in posList:
        zielList.append(str(r +1) + "-" + str(s -1))
        zielHexa.append(nrHexa[(str(r +1) + "-" + str(s -1))])

    graph[nrHexa[pos]] = zielHexa

#print(graph)

