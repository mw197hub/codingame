# https://www.codingame.com/ide/puzzle/there-is-no-spoon-episode-2

import sys,math,copy,time

class Cell:
    def __init__(self,y,x,anzahl):   # immer einzelne Verbindungen eintragen
        self.y=y;self.x=x;self.anzahl=anzahl;self.yx=(y,x)
        self.nachbarn=[];self.verbindung=[];self.rest=self.anzahl
        self.restList=[]
    def aktualisieren(self):
        self.rest=self.anzahl-len(self.verbindung)
        self.restList = copy.deepcopy(self.nachbarn)
        #self.restList=list(set(self.nachbarn) - set(self.verbindung))
    def eintrag(self,ver,graphCell):
       
        c2 = graphCell[ver]
        # problem doppelverbindungen aufzubauen
        if (ver in self.verbindung or c2.anzahl == 1) and ver in self.restList:
            self.restList.remove(ver)
        self.rest-=1
        if self.rest == 0:
            for nach in self.nachbarn:
                cN = graphCell[nach]
                loeList=[]
                for r in cN.restList:
                    if r == self.yx:
                        loeList.append(r)
                for loe in loeList:
                    cN.restList.remove(loe)
            #self.restList.clear()
        self.verbindung.append(ver)
                
        if (ver in c2.verbindung or self.anzahl == 1) and self.yx in c2.restList:
            c2.restList.remove(self.yx)
        c2.rest-=1
        if c2.rest == 0:
            for nach in c2.nachbarn:
                cN = graphCell[nach]
                loeList=[]
                for r in cN.restList:
                    if r == c2.yx:
                        loeList.append(r)
                for loe in loeList:
                    cN.restList.remove(loe)
            #c2.restList.clear()
        c2.verbindung.append(self.yx)

    def __str__(self) -> str:
        return ("{}-{}  anzahl={}  nachbarn={}  restlist={}".format(self.y,self.x,self.anzahl,self.nachbarn,self.restList))
 


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

# einnachbar, doppelnachbar oder (einser und doppelverbindungen)

def einNachbar(graphCell):
    mVerbindungen=[]
    for pos,cell in graphCell.items():
        if len(cell.restList) == 1:   
            for i in range(cell.rest):
                mVerbindungen.append((pos[0],pos[1],cell.restList[0][0],cell.restList[0][1]))       
    return mVerbindungen

def pruefeFertig(graphCell):
    for pos,cell in graphCell.items():
        if cell.anzahl > len(cell.verbindung):
            return False
    return True

def testVerbindung(graphCell,verbindungen):
    for pos,cell in graphCell.items():
        if cell.rest > 0:
            return (pos[0],pos[1],cell.restList[0][0],cell.restList[0][1])




def verarbeitung(graph,graphCell,verbindungen,moeglicheWege,speicherList,fertig):
    speicherList.append(copy.deepcopy(graphCell))
    mVerb = einNachbar(graphCell)
    if len(mVerb) > 0:
        for m in mVerb:        
            cell = graphCell[(m[0],m[1])]
            cell.eintrag((m[2],m[3]),graphCell)
            verbindungen.append(m)
        fertig=pruefeFertig(graphCell)
        if fertig:
            return True
        fertig = verarbeitung(graph,graphCell,verbindungen,moeglicheWege,speicherList,fertig)
        if fertig:
            return True
    else:
        # teste eine verbindung
        m = testVerbindung(graphCell,verbindungen)
        cell = graphCell[(m[0],m[1])]
        cell.eintrag((m[2],m[3]),graphCell)
        verbindungen.append(m[:])
        fertig = verarbeitung(graph,graphCell,verbindungen,moeglicheWege,speicherList,fertig)

        # nicht erfolgreich
        graphCell = speicherList.pop()
        verbindungen.pop()
        return False


##############

lineList=[['1', '.', '2'], ['.', '.', '.'], ['.', '.', '1']]   # 1
lineList=[['2', '.'], ['4', '2']]  # 2
lineList=[['1', '.', '3'], ['.', '.', '.'], ['1', '2', '3']]  # 3
#lineList=[['1', '4', '.', '3'], ['.', '.', '.', '.'], ['.', '4', '.', '4']]   # 4
#lineList=[['2', '.', '.', '2', '.', '1', '.'], ['.', '3', '.', '.', '5', '.', '3'], ['.', '2', '.', '1', '.', '.', '.'], ['2', '.', '.', '.', '2', '.', '.'], ['.', '1', '.', '.', '.', '.', '2']]  # 6
#lineList=[['3', '.', '.', '2', '.', '2', '.', '.', '1', '.', '.', '.', '.', '3', '.', '.', '.', '.', '.', '.', '.', '.', '4'], ['.', '2', '.', '.', '1', '.', '.', '.', '.', '2', '.', '6', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', '.'], ['.', '.', '3', '.', '.', '6', '.', '.', '.', '.', '3', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '2', '.', '.', '.', '.', '.', '.', '.', '.', '1', '.', '.', '3', '.', '3', '.'], ['.', '.', '1', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '3', '.', '.', '3', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '3', '.', '.', '3', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '3', '.', '.', '.', '8', '.', '.', '.', '.', '.', '8', '.', '.', '.', '.', '.', '.', '.', '.', '.', '3', '.'], ['6', '.', '5', '.', '1', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '1', '.', '.', '3', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', '.', '.', '6', '.', '3', '1', '.', '.', '2', '.'], ['.', '.', '4', '.', '.', '4', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['5', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '7', '.', '.', '.', '7', '.', '.', '.', '3', '.', '3', '.'], ['.', '2', '.', '.', '3', '.', '.', '3', '.', '.', '3', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '2', '.', '.', '2', '.', '.', '.', '1', '.', '6', '.', '.', '.', '3', '.', '.', '.'], ['.', '.', '.', '.', '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '4', '.', '.', '.', '.', '5', '.', '.', '.', '3', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', '.', '3', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '3', '.', '3', '.', '.', '2', '.', '4', '4', '.', '.', '.', '.', '1', '.', '.'], ['3', '.', '.', '.', '1', '.', '3', '.', '2', '.', '3', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '2', '.', '.', '.', '.', '.', '3', '.', '.', '.', '6', '.', '.', '.', '.', '.', '.', '.', '.', '.', '5', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '1', '.', '.', '.', '.', '.', '.'], ['.', '1', '.', '.', '.', '.', '.', '.', '.', '3', '.', '6', '.', '2', '.', '.', '.', '2', '.', '.', '.', '4', '.'], ['5', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '3', '.', '.', '.', '.', '.', '3'], ['4', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '4', '.', '2']]


########

start=time.time()

speicherList=[]
graph={};graphVerbindungen={};graphCell={}
verbindungen=[];gesamtAnzahl=0
moeglicheWege=[]
posList=[];startPos=()
werteGraph={}
wege=[[1,0],[-1,0],[0,1],[0,-1]]
for y in range(len(lineList)):
    for x in range(len(lineList[0])):
        if not lineList[y][x] == ".":
            cell = Cell(y,x,int(lineList[y][x]))
            posList.append((y,x))
            nList=[]
            werteGraph[(y,x)] =(int(lineList[y][x]))
            gesamtAnzahl += int(lineList[y][x])
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
            cell.nachbarn = copy.deepcopy(nList)
            cell.aktualisieren()
            graphCell[(y,x)] = cell

print(gesamtAnzahl,file=sys.stderr)
verarbeitung(graph,graphCell,verbindungen,moeglicheWege,speicherList,False)


for verb in verbindungen:    
    #for verb in teil1:
        ## print("{} {} {} {} {}".format(verb[0][1],verb[0][0],verb[1][1],verb[1][0],verb[2]))
    print("{} {} {} {} {}".format(verb[0],verb[1],verb[2],verb[3],1))

print("Zeit: {}".format(time.time()-start),file=sys.stderr)