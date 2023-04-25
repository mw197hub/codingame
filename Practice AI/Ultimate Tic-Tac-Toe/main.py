#  https://www.codingame.com/ide/puzzle/tic-tac-toe

import sys,math,time,copy,random

def printUTT(spielfeldDict):
    print("      0   1   2      3   4   5      6   7   8",file=sys.stderr)
    print("------------------------------------------------",file=sys.stderr)
    zaehl = 0
    for i in range(3):
        z = i * 3        
        for f in range(3):       
            print(str(zaehl) +":| ",file=sys.stderr,end="")
            for y in range(3):
                f1 = spielfeldDict[z+y]
                for x in range(3):
                    print(" %2d" % (f1.feld[f][x]),file=sys.stderr,end=" ")
                print(" | ",file=sys.stderr,end="")                
            print(" ",file=sys.stderr)
            zaehl+=1
        print("------------------------------------------------",file=sys.stderr)

def setZug(zug,idNr):
    y = idNr // 3; x = idNr % 3
    return [zug[0]+(y*3),zug[1]+(x*3)]

def getZug(zug,idNr):
    return([zug[0] % 3,zug[1] % 3])

def setZuginFeld(zug,spieler,spielfeldDict,zuordnungDict,hauptfeldZuordnung,hauptfeld,idzuhauptDict):
    idNr=99
    for zuId,zList in zuordnungDict.items():
        if zug in zList:
            idNr = zuId;break
    f1 = spielfeldDict[idNr]
    zugImFeld = getZug(zug,idNr)
    f1.setFeld(zugImFeld,spieler)
    if not f1.owner == 0:
        yx = idzuhauptDict[idNr]
        hauptfeld.feld[yx[0]][yx[1]] = spieler

    #print("Feld "+ str(f1.id) + ":",file=sys.stderr)
    #print(f1,file=sys.stderr)

def getFeld(zug):
    zugImFeld = getZug(zug,0)
    return zugImFeld[0] * 3 + zugImFeld[1]

def setIdNrList(zug,spielfeldDict,zuordnungDict,hauptfeldZuordnung,hauptfeld,idzuhauptDict):
    idNr = getFeld(zug)
    f1 = spielfeldDict[idNr]
    if not f1.entschieden:
        return [idNr]
    moeglichIdNrList=[]
    for idNr,f1 in spielfeldDict.items():
        if not f1.entschieden:
            moeglichIdNrList.append(idNr)
    return moeglichIdNrList

class Spielfeld:
    def __init__(self,id):
        self.id=id;self.owner=0;self.entschieden=False;self.mySiegMoeglich=1;self.opSiegMoeglich=-1
        self.feld=initFeld();self.leerList=[[0,0],[0,1],[0,2], [1,0],[1,1],[1,2], [2,0],[2,1],[2,2]]
        self.siegen=True
    def __str__(self):
        return ("%2d %2d %2d\n%2d %2d %2d\n%2d %2d %2d" % (self.feld[0][0],self.feld[0][1],self.feld[0][2],self.feld[1][0],self.feld[1][1],self.feld[1][2],self.feld[2][0],self.feld[2][1],self.feld[2][2]))
    def setFeld(self,action,wert):
        self.feld[action[0]][action[1]] = wert
        self.leerList.remove(action)
        self.owner = pruefeEntschieden(self.feld)
        if not self.owner == 0:
            self.entschieden=True
        # teste, ob gewinn noch moeglich
        versuchFeld = copy.deepcopy(self.feld)
        for leer in self.leerList:
            versuchFeld[leer[0]][leer[1]] = 1
        self.mySiegMoeglich = pruefeEntschieden(versuchFeld)
        versuchFeld = copy.deepcopy(self.feld)
        for leer in self.leerList:
            versuchFeld[leer[0]][leer[1]] = -1
        self.opSiegMoeglich = pruefeEntschieden(versuchFeld)
        if self.mySiegMoeglich == 0 and self.opSiegMoeglich == 0:
            self.entschieden=True

#####2####
pruefList=[[[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]],[[0,0],[1,0],[2,0]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]],[[0,0],[1,1],[2,2]],[[2,0],[1,1],[0,2]]]
def initFeld():
    return [[0 for y in range(3)] for x in range(3)]

def pruefeEntschieden(feld):
    for fList in pruefList:
        wert=0
        for f in fList:
            wert += feld[f[0]][f[1]]
        if abs(wert) == 3:
            return wert//3
    return 0

def pruefeSieg(feld,moveList,erg):
    leerList=[]
    for fList in pruefList:
        wert=0;leer=[]
        for f in fList:
            if feld[f[0]][f[1]] == 0:
                leer=[f[0],f[1]]
            else:
                wert += feld[f[0]][f[1]]
        if wert == erg:
            leerList.append(leer)
    return leerList

def setYX(wahlList):
    nr = random.randint(0,len(wahlList)-1)
    return str(wahlList[nr][0])+"-"+str(wahlList[nr][1])
def getYX(wert):
    nr = wert.split("-")
    return [int(nr[0]),int(nr[1])]
    

def setBewertung(feld,leerList,siegen):
    ecken=[[0,0],[0,2],[2,0],[2,2]]
    rand= [[0,1],[1,0],[1,2],[2,1]]
    bewertungsDict={}
    if len(leerList) == 9:
        # eckfeld
        bewertungsDict['0-0'] = 10
    elif len(leerList) == 8:
        # wenn eck, dann Mitte
        if [1,1] in leerList:
            bewertungsDict['1-1'] = 10
        else: # eckfeld
            bewertungsDict['0-0'] = 10
    else:
        if siegen and [1,1] in leerList and len(leerList) == 7:
            anzE=0;restEcken=[]
            for e in ecken:
                if e in leerList:
                    anzE+=1
                    restEcken.append(e)
            if anzE ==2 and len(leerList) == 7:
                bewertungsDict[setYX([restEcken[0]])] = 5
            else:
                bewertungsDict['1-1'] = 5
        else:
            for versuch in leerList:
                testfeld = copy.deepcopy(feld)
                testfeld[versuch[0]][versuch[1]] = 1
                pList = pruefeSieg(testfeld,[],2)            
                if len(pList) > 1:
                    bewertungsDict[setYX([versuch])] = 5;return bewertungsDict
                elif len(pList) == 1:
                    testfeld[pList[0][0]][pList[0][1]] = -1
                    pList = pruefeSieg(testfeld,[],-2)
                    if len(pList) > 1:
                        bewertungsDict[setYX([versuch])] = -1
                    else:
                        bewertungsDict[setYX([versuch])] = len(pList)
                else:
                    bewertungsDict[setYX([versuch])] = 0
                    gegenList = copy.deepcopy(leerList);gegenList.remove(versuch)
                    for gegen in gegenList:
                        gegenfeld = copy.deepcopy(testfeld)
                        gegenfeld[gegen[0]][gegen[1]] = -1
                        pList = pruefeSieg(gegenfeld,[],-2)
                        if len(pList) > 1:
                            bewertungsDict[setYX([versuch])] = -1

        #bewertungsDict[setYX(leerList)] = 1

    return bewertungsDict

#######################################
    


def setMove(spielfeldDict,zuordnungDict,hauptfeldZuordnung,hauptfeld,moveList,idzuhauptDict,moeglichIdNrList):
    # nur ein feld => prüfen, ob gewinn oder verlust incl. auswirken auf hauptfeld
    # nur ein feld => auswirkung auf die anderen Felder: 1. kein gewinn mehr moeglich, 2. leere Felder bzw. moeglichst wenig - kein gewinn
    # mehr Felder => pruefen, ob gewinn bzw. auswirkungen hauptfeld


    action = []
    f1 = spielfeldDict[moeglichIdNrList[0]]
    # selbst siegen, op sieg verhindern
    pList = pruefeSieg(f1.feld,moveList,2)
    if len(pList) > 0:
        action = pList[0]
    if len(action) == 0:
        pList = pruefeSieg(f1.feld,moveList,-2)
        if len(pList) > 0:
            action = pList[0]
    # suche nach besten Zug
    if len(action) == 0:
        #action = moveList[0]
        bewertungsDict=setBewertung(f1.feld,f1.leerList,f1.siegen)
        for bFeld in sorted(bewertungsDict,key=bewertungsDict.get, reverse=True):        
            action = getYX(bFeld);break
    
    action = setZug(action,f1.id)
    return action

#######################################
# [0,0],[0,1],[0,2], [1,0],[1,1],[1,2], [2,0],[2,1],[2,2]
start = time.time()

moeglichIdNrList = [0]
spielfeldDict={};zuordnungDict={};hauptfeldZuordnung={};idzuhauptDict={}
hauptfeld = Spielfeld(99)
for i in range(9):
    spielfeldDict[i] = Spielfeld(i)
    xadd = i % 3 * 3;yadd = i // 3 * 3
    zuFelder=[]
    for y in range(yadd,yadd+3):
        for x in range(xadd,xadd+3):
            zuFelder.append([y,x])
    zuordnungDict[i] = copy.deepcopy(zuFelder)    
nr=0
for y in range(3):
    for x in range(3):
        hauptfeldZuordnung[setYX([[y,x]])] = spielfeldDict[nr]
        idzuhauptDict[nr] = [y,x]
        nr+=1

moveList,myMoveList,opMoveList,gespieltList=[],[],[],[]
runde=1
# game loop

gespielteZuege=[[0,1],[0,3],[0,0],[0,2],[0,6],[1,1],[3,3],[2,0]]
player=-1
for g in gespielteZuege:
    setZuginFeld(g,player,spielfeldDict,zuordnungDict,hauptfeldZuordnung,hauptfeld,idzuhauptDict)
    player = player * -1

printUTT(spielfeldDict)

while True:    
    op_row, op_col = [int(i) for i in input().split()]    
    
  #  moveList.remove([op_row,op_col])
    if not op_row == -1:
        opMoveList.append([op_row,op_col]);gespieltList.append([op_row,op_col])
        setZuginFeld([op_row,op_col],-1,spielfeldDict,zuordnungDict,hauptfeldZuordnung,hauptfeld,idzuhauptDict)
        moeglichIdNrList = setIdNrList([op_row,op_col],spielfeldDict,zuordnungDict,hauptfeldZuordnung,hauptfeld,idzuhauptDict)
   # print(moeglichIdNrList,file=sys.stderr)

    action = setMove(spielfeldDict,zuordnungDict,hauptfeldZuordnung,hauptfeld,moveList,idzuhauptDict,moeglichIdNrList)
    print("{} {}".format(action[0],action[1]))
    setZuginFeld([action[0],action[1]],1,spielfeldDict,zuordnungDict,hauptfeldZuordnung,hauptfeld,idzuhauptDict)
    myMoveList.append(action);gespieltList.append(action)
    moeglichIdNrList = setIdNrList([action[0],action[1]],spielfeldDict,zuordnungDict,hauptfeldZuordnung,hauptfeld,idzuhauptDict)
    #print(moeglichIdNrList,file=sys.stderr)
    printUTT(spielfeldDict)
    #print(gespieltList,file=sys.stderr)
    runde += 1
    if runde > 5:
        break

print("--- Hauptfeld ---",file=sys.stderr)
print(hauptfeld,file=sys.stderr)
if hauptfeld.owner == 0:
    print("Unentschieden",file=sys.stderr)
else:
    print("Der Gewinner ist {}".format(hauptfeld.owner),file=sys.stderr)
print("Zeit: ",file=sys.stderr,end="")
print(time.time() - start,file=sys.stderr)