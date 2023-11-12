# https://www.codingame.com/ide/puzzle/there-is-no-spoon-episode-2

import sys,math,copy,time

class Cell:
    def __init__(self,y,x,anzahl):
        self.y=y;self.x=x;self.anzahl=anzahl
        self.nachbarn=[];self.verbindung=[];self.rest=anzahl-len(self.verbindung)
        self.restList=list(set(self.nachbarn) - set(self.verbindung))
    def __str__(self) -> str:
        return ("{}-{}  anzahl={}  nachbarn={}  uebrig={}".format(self.y,self.x,self.anzahl,self.nachbarn,self.restList))
 

def sucheEins(graph):
    antwortList=[]
    for gr in graph:
        cell = graph[gr]
        if cell.anzahl == 1 and len(cell.verbindung) == 0 and len(cell.nachbarn) == 1:
            antwortList.append((gr[0],gr[1],cell.nachbarn[0][0],cell.nachbarn[0][1]))
    #print("antwortList={}".format(antwortList),file=sys.stderr)
    return antwortList

def sucheDoppel(graph):
    antwortList=[]
    for gr in graph:
        cell = graph[gr]
        if cell.anzahl == (len(cell.nachbarn) - len(cell.verbindung) )*2:
            antwortList.append((gr[0],gr[1],cell.nachbarn[0][0],cell.nachbarn[0][1]))
    print("antwortList={}".format(antwortList),file=sys.stderr)
    return antwortList

def sucheZwingend(graph):
    antwortList=[]
    for gr in graph:
        cell = graph[gr]
        if cell.anzahl > len(cell.verbindung):
            einser=[]
            for nachbar in cell.nachbarn:
                c2 = graph[nachbar]
                if c2.anzahl == 1:
                    einser.append(nachbar)     
            if cell.anzahl-len(einser) == (len(cell.nachbarn) - len(einser) - len(cell.verbindung) )*2 and cell.anzahl-len(einser) > 0:
                aList=[]
                for e in einser:
                    antwortList.append((gr[0],gr[1],e[0],e[1]))
                for nachbar in cell.nachbarn:
                    if not nachbar in einser:
                        antwortList.append((gr[0],gr[1],cell.nachbarn[0][0],cell.nachbarn[0][1]))
                        antwortList.append((gr[0],gr[1],cell.nachbarn[0][0],cell.nachbarn[0][1]))
                print("antwortList={}".format(antwortList),file=sys.stderr)                    
                return antwortList
    return antwortList


def eintrag(verbindungen,graph,eList):
    y1,x1,y2,x2 = eList
    verbindungen.append((y1,x1,y2,x2,1))
    cell1 = graph[(y1,x1)];cell2=graph[(y2,x2)]
    cell1.verbindung.append((y2,x2))
    cell2.verbindung.append((y1,x1))



def schleife(verbindungen,graph,gesamtAnzahl):
    while len(verbindungen) < gesamtAnzahl//2:
        einsList = sucheEins(graph)
        if len(einsList) > 0:
            eintrag(verbindungen,graph,einsList[0])
            schleife(verbindungen,graph,gesamtAnzahl)
        doppelList = sucheDoppel(graph)
        if len(doppelList) > 0:
            eintrag(verbindungen,graph,doppelList[0])
            eintrag(verbindungen,graph,doppelList[0])
            schleife(verbindungen,graph,gesamtAnzahl)
        zwingendList = sucheZwingend(graph)
        if len(zwingendList) > 0:
            for zw in zwingendList:
                eintrag(verbindungen,graph,zw)
            schleife(verbindungen,graph,gesamtAnzahl)
#######


lineList=[['1', '.', '2'], ['.', '.', '.'], ['.', '.', '1']]   # 1
lineList=[['2', '.'], ['4', '2']]  # 2
lineList=[['1', '.', '3'], ['.', '.', '.'], ['1', '2', '3']]  # 3
#lineList=[['1', '4', '.', '3'], ['.', '.', '.', '.'], ['.', '4', '.', '4']]   # 4


########
start=time.time()

graph={}
verbindungen=[];gesamtAnzahl=0
moeglicheWege={}
for y in range(len(lineList)):
    for x in range(len(lineList[0])):
        if not lineList[y][x] == ".":
            cell = Cell(y,x,int(lineList[y][x]))
            graph[(y,x)] = cell
            gesamtAnzahl+=int(lineList[y][x])
#print(graph,file=sys.stderr)
wege=[[1,0],[-1,0],[0,1],[0,-1]]
for cl in graph:
    y,x = cl
    cell = graph[cl];nList=[]
    for weg in wege:
        y1=y;x1=x
        while True:
            y1+=weg[0];x1+=weg[1]
            if y1 < 0 or x1 < 0 or y1 >= len(lineList) or x1 >= len(lineList[0]):
                break
            if (y1,x1) in graph:
                nList.append((y1,x1))
                if not (y1,x1) in moeglicheWege:
                    if (y,x) in moeglicheWege:
                        eList=moeglicheWege[(y,x)]
                        eList.append([y1,x1,1])
                    else:
                        moeglicheWege[(y,x)] = [[y1,x1,1]]
                if int(lineList[y][x]) >1 and int(lineList[y1][x1]) > 1:
                    if not (y1,x1) in moeglicheWege:
                        eList=moeglicheWege[(y,x)]
                        eList.append([y1,x1,2])
                break
    cell.nachbarn=copy.deepcopy(nList)
    #print(cell,file=sys.stderr)
print(moeglicheWege,file=sys.stderr)

schleife(verbindungen,graph,gesamtAnzahl)

for verb in verbindungen:
    print("{} {} {} {} {}".format(verb[1],verb[0],verb[2],verb[3],verb[4]))

print("Zeit: {}".format(time.time()-start),file=sys.stderr)