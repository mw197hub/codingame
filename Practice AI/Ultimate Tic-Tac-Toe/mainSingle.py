#  https://www.codingame.com/ide/puzzle/tic-tac-toe

import sys,math,time,copy,random

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


def setMove(f1,moveList):
  #  if f1.feld[1][1] == 0:
  #      return [1,1]
    # selbst siegen, op sieg verhindern
    pList = pruefeSieg(f1.feld,moveList,2)
    if len(pList) > 0:
        return pList[0]
    pList = pruefeSieg(f1.feld,moveList,-2)
    if len(pList) > 0:
        return pList[0]
    # suche nach besten Zug
    action = moveList[0]
    bewertungsDict=setBewertung(f1.feld,f1.leerList,f1.siegen)
    for bFeld in sorted(bewertungsDict,key=bewertungsDict.get, reverse=True):        
        action = getYX(bFeld);break
    return action

#######################################
# [0,0],[0,1],[0,2], [1,0],[1,1],[1,2], [2,0],[2,1],[2,2]
start = time.time()
moveList=[[0,0],[0,1],[0,2], [1,0],[1,1],[1,2], [2,0],[2,1],[2,2]]
myMoveList,opMoveList=[],[]

spielfeldDict={};zuordnungDict={}
for i in range(9):
    spielfeldDict[i] = Spielfeld(i)
    xadd = i % 3 * 3;yadd = i // 3 * 3
    zuFelder=[]
    for y in range(yadd,yadd+3):
        for x in range(xadd,xadd+3):
            zuFelder.append([y,x])
    zuordnungDict[i] = copy.deepcopy(zuFelder)
hauptfeld = Spielfeld(99)
# game loop
runde=1
exit(0)
while True:    
    if not runde == 0:
        op_row, op_col = [int(i) for i in input().split()]    
        opMoveList.append([op_row,op_col])
        moveList.remove([op_row,op_col])
        spielfeldDict[0].setFeld([op_row,op_col],-1)
        if not spielfeldDict[0].entschieden == 0:
            break
        print(moveList,file=sys.stderr)

    action = setMove(f1,moveList)
    print("{} {}".format(action[0],action[1]))
    myMoveList.append(action)
    moveList.remove(action)
    spielfeldDict[0].setFeld(action,1)
    print(spielfeldDict[0],file=sys.stderr)
    if not spielfeldDict[0].entschieden == 0:
        break
    runde += 1

print("--------------",file=sys.stderr)
print(spielfeldDict[0],file=sys.stderr)
if spielfeldDict[0].owner == 0:
    print("Unentschieden",file=sys.stderr)
else:
    print("Der Gewinner ist {}".format(spielfeldDict[0].owner),file=sys.stderr)
print("Zeit: ",file=sys.stderr,end="")
print(time.time() - start,file=sys.stderr)