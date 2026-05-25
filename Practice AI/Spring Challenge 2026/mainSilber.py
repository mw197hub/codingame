import sys,math,copy

ANZAHLTROLLE=4

def initMap(lineList,scoreDict,treeDict,trollDict,ergList,grundList,ironList,waterList,zielDict):
    width,height,runde=0,0,0;myBase="";oppBase=""
    pfad='C:\\Users\\marku\\Python\\codingame\\Practice AI\\Spring Challenge 2026\\'+'eingabe'+'.txt'
    eingabe = open(pfad,'r')
    for zeile in eingabe:
        zeile=zeile[:-1]
        if zeile[0:5] == "width":
            wertList=zeile.split(";")
            hList=wertList[0].split("=");width=int(hList[1])
            hList=wertList[1].split("=");height=int(hList[1])
            hList=wertList[2][9:-1].split(",")
            for h in hList:
                lineList.append(h[2:-1])
        if zeile[0:5] == "runde":
            wertList=zeile.split(";")
            hList=wertList[0].split("=");runde=int(hList[1])            
            hList=wertList[1][10:-2].split("},")
            for hL in hList:
                srDict={}
                pos=hL.index(":");nr=int(hL[1:pos])
                wL=hL[pos+2:].split(",")
                for wert in wL:
                    tList=wert[2:].split(":")
                    srDict[tList[0][:-1]]=int(tList[1][1:])
                scoreDict[nr]=copy.deepcopy(srDict)
        if zeile[0:5] == "treeD":
            wertList=zeile[9:-1].split(";")
            for wert in wertList:
                hList=wert.split(",");aList=[]
                for h in hList:
                    wL=h.split("=")
                    aList.append((wL[1]))
                treeDict[setXY(int(aList[2]),int(aList[3]))]=Tree(int(aList[0]),aList[1],int(aList[2]),int(aList[3]),int(aList[4]),int(aList[5]),int(aList[6]),int(aList[7]))
        if zeile[0:6] == "trollD":
            wertList=zeile[10:-1].split(";")
            for wert in wertList:
                hList=wert.split(",");aList=[]
                for h in hList:
                    wL=h.split("=")
                    aList.append((wL[1]))
                trollDict[int(aList[0])]=Troll(int(aList[0]),int(aList[1]),int(aList[2]),int(aList[3]),int(aList[4]),int(aList[5]),int(aList[6]),int(aList[7]),int(aList[8]),int(aList[9]),int(aList[10]),int(aList[11]),int(aList[12]),int(aList[13]))
        if zeile[0:6] == "zielDi":
            if len(zeile) > 11:
                wertList=zeile[9:-1].split(";")  
                for wert in wertList:
                    hList=wert.split(",");aList=[]
                    for h in hList:
                        wL=h.split("=")
                        aList.append((wL[1]))
                    zielDict[int(aList[0])]=Ziel(int(aList[0]))
                    zielDict[int(aList[0])].name=aList[1];zielDict[int(aList[0])].ziel=aList[2];zielDict[int(aList[0])].aufgabe=aList[3]

    for y in range(len(lineList)):
        for x in range(len(lineList[0])):
            if lineList[y][x] == "1":
                oppBase=setXY(x,y)
            if lineList[y][x] == "0":
                myBase=setXY(x,y)    
            if lineList[y][x] == ".":
                grundList.append(setXY(x,y))
            if lineList[y][x] == "+":
                ironList.append(setXY(x,y))
            if lineList[y][x] == "~":
                waterList.append(setXY(x,y))                
    return width,height,runde,myBase,oppBase
###################################
### intern initMap     ############
###################################

class Ziel:
    def __init__(self,id):
        self.id=id;self.name="";self.ziel="";self.aufgabe=""
    def __str__(self) -> str:
        return ("id={},name={},ziel={},aufgabe={}".format(self.id,self.name,self.ziel,self.aufgabe))
class Tree:
    def __init__(self,i,_type,x,y,size,health,fruits,cooldown):
        self.nr=i;self.type=_type;self.x=x;self.y=y;self.size=size;self.health=health;self.fruits=fruits;self.cooldown=cooldown        
    def __str__(self) -> str:
        return ("nr={},type={},x={},y={},size={},health={},fruits={},cooldown={}".format(self.nr,self.type,self.x,self.y,self.size,self.health,self.fruits,self.cooldown))
class Troll:
    def __init__(self,id, player, x, y, movement_speed, carry_capacity, harvest_power, chop_power, carry_plum, carry_lemon, carry_apple, carry_banana, carry_iron, carry_wood):
        self.id=id;self.player=player;self.x=x;self.y=y;self.speed=movement_speed;self.capacity=carry_capacity;self.harvest=harvest_power;self.chop=chop_power
        self.plum=carry_plum;self.lemon=carry_lemon;self.apple=carry_apple;self.banana=carry_banana;self.iron=carry_iron;self.wood=carry_wood
        self.aktualisieren();self.treeDict={};self.name=""
    def __str__(self) -> str:
        return("id={},player={},x={},y={},speed={},capacity={},harvest={},chop={},plum={},lemon={},apple={},banana={},iron={},wood={}".format(self.id,self.player,self.x,self.y,self.speed,self.capacity,self.harvest,self.chop,self.plum,self.lemon,self.apple,self.banana,self.iron,self.wood))
    def aktualisieren(self):
        self.waren=self.plum+self.lemon+self.apple+self.banana+self.iron+self.wood;self.plant=self.plum+self.lemon+self.apple+self.banana
        self.xy=setXY(self.x,self.y);self.name=""
    def getShortTree(self):
        treeList = sorted(self.treeDict.items(), key=lambda item: item[1])
        return treeList[0][0]
    def getPlant(self):
        if self.plum > 0:
            return "PLUM"
        if self.lemon > 0:
            return "LEMON"
        if self.apple > 0:
            return "APPLE"
        if self.banana > 0:
            return "BANANA"
def setXY(x,y):
    return str(x)+"#"+str(y)
def getXY(xy):
    hList=xy.split("#")
    return int(hList[0]),int(hList[1])

def suchePath(graph, start, goal,moveList):
    explored = [];queue = [[start]]
    if start == goal:
        return []
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
    return []    


def getDistanz(xyA,xyB):
    x1,y1=getXY(xyA);x2,y2=getXY(xyB)
    return abs(x1-x2)+abs(y1-y2)
def setGraph(grundList,treeDict,myBase,oppBase,lineList,ironList,waterList,baseDict):
    moveList = copy.deepcopy(grundList);graph={};newWater=[]
    moveList.append(myBase)
    for move in moveList:
        x,y=getXY(move);zList=[]
        if setXY(x+1,y) in moveList:
            zList.append(setXY(x+1,y))
        if setXY(x-1,y) in moveList:
            zList.append(setXY(x-1,y))
        if setXY(x,y+1) in moveList:
            zList.append(setXY(x,y+1))
        if setXY(x,y-1) in moveList:
            zList.append(setXY(x,y-1))   
        for xy in [setXY(x+1,y),setXY(x-1,y),setXY(x,y+1),setXY(x,y-1)]:            
            if xy in waterList and not move in newWater:
                newWater.append(move)
        graph[move]=zList[:]
    waterList = copy.deepcopy(newWater)        
    # alle Wege von myBase aus
    for ziel in grundList:
        if not ziel == myBase:
            erg = suchePath(graph,myBase,ziel,moveList)
        baseDict[ziel] = erg[1:]
    ironZiel="";ironLen=999
    for iron in ironList:
        x,y=getXY(iron)
        for nXY in [setXY(x+1,y),setXY(x-1,y),setXY(x,y+1),setXY(x,y-1)]:
            if nXY in baseDict and len(baseDict[nXY]) < ironLen:
                ironZiel=nXY;ironLen=len(baseDict[nXY])
    ironList.clear();ironList.append(ironZiel)  
    moveList.remove(myBase)              
    return moveList,graph
def setTreeDistanz(treeDict,xyPos,moveZiel,zielDict):    
    distanzDict={};fehltWas=""
    if 'hole' in zielDict:
        fehltWas = zielDict['hole']
    for treeId,tree in treeDict.items():
        if not treeId in moveZiel:
            dist = getDistanz(xyPos,setXY(tree.x,tree.y))
            if tree.fruits > 0 or (tree.size == 4 and dist > tree.cooldown):
                if tree.type == fehltWas:
                    dist = dist - 6
                distanzDict[treeId] = dist
    return distanzDict
def pruefePlant(trollDict,treeDict,myBase,oppBase,scoreList,zielDict):
    treeDist={};warenList=[]
    if getDistanz(myBase,oppBase) > 0:  # wenn zu nah dann einfach beim Opp bedienen oder suchen
        for trollId,troll in trollDict.items():
            if troll.plum > 0:
                warenList.append("PLUM")
            if troll.lemon > 0:
                warenList.append("LEMON")
            if troll.apple > 0:
                warenList.append("APPLE")
        treeDist = {"APPLE":999,"PLUM":999,"LEMON":999}
        for treeId,tree in treeDict.items():
            dist = getDistanz(myBase,setXY(tree.x,tree.y))
            if tree.type in treeDist and dist < treeDist[tree.type]:
                treeDist[tree.type] = dist
        for tree,dist in treeDist.items():
            if dist > 2 and not tree in warenList:
                for trollId,ziel in zielDict.items():
                    if ziel.ziel == "" and (not ziel.name == "PICK" and not ziel.name=="HOLE"):
                        if scoreList[tree.lower()] > 0:
                            ziel.name="PICK";ziel.aufgabe=tree;break
                        else:
                            size4=False
                            for tId,baum in treeDict.items():
                                if baum.type == tree and ((baum.size == 4 and baum.cooldown < 4) or baum.fruits > 0):
                                    size4=True
                            if size4:
                                ziel.name="HOLE";ziel.aufgabe=tree;break
    return treeDist
####
def bewegung(width,height,runde,myBase,oppBase,lineList,scoreDict,treeDict,trollDict,ergList,grundList,moveList,graph,ironList,waterList,baseDict,zielDict):
    treeList=[];trollList=[];ziele={};ironId=-1;ironWert=0;moveZiel=[]
    scoreList=scoreDict[0]
    for treeId,tree in treeDict.items():                              
        treeList.append(setXY(tree.x,tree.y))
    #  werte ermitteln
    for trollId,troll in trollDict.items():
        troll.aktualisieren()
        if troll.player == 0:
            if not trollId in zielDict:
                zielDict[trollId] = Ziel(trollId)
            trollList.append(trollId)
            if troll.speed + troll.capacity > ironWert:
                ironWert = troll.speed + troll.capacity; ironId = trollId
    for trollId,ziel in zielDict.items():
        if ziel.name == "iron" and len(ziel.ziel) > 0:  # noch nicht aktiv
            ironId=-1
    if ironId >= 0:
        for trollId,ziel in zielDict.items():
            if ziel.name == "iron":
                zielDict[trollId].name="";zielDict[trollId].aufgabe=""
        trollDict[ironId].name="iron";zielDict[trollId].name="iron"

    if runde > 1 and len(trollList) < ANZAHLTROLLE:
        pruefePlant(trollDict,treeDict,myBase,oppBase,scoreList,zielDict)
    fehltWas="";vorhandenList=[]
    for wert,anzahl in scoreList.items():
        if wert in ['plum','lemon','apple']:
            if anzahl < 10:
                fehltWas=wert
            else:
                vorhandenList.append(wert)

    #####        
    #  befehle setzen
    for trollId,troll in trollDict.items():
        if troll.player == 0:
            if zielDict[trollId].name == "PICK":
                if len(zielDict[trollId].ziel) == 0:
                    ergList.append(["PICK",str(troll.id),zielDict[troll.id].aufgabe])
                    zielXY="";x,y=getXY(myBase);sG=1;sV=0
                    while True:
                        for nXY in [setXY(x+sG,y),setXY(x-sG,y),setXY(x,y+sG),setXY(x,y-sG),setXY(x+sV,y+sV),setXY(x+sV,y-sV),setXY(x-sV,y+sV),setXY(x-sV,y-sV)]:
                            if nXY in moveList and not nXY in treeList:
                                zielDict[troll.id].ziel=nXY  
                                break                              
                        sG+=1;sV+=1
                        if len(zielDict[troll.id].ziel) > 0:
                            break
                else:
                    if troll.xy == zielDict[trollId].ziel:
                        ergList.append(["PLANT",str(troll.id),zielDict[troll.id].aufgabe])
                        zielDict[trollId].ziel = "";zielDict[trollId].aufgabe="";zielDict[trollId].name=""
                    else:
                        x,y=getXY(zielDict[trollId].ziel)
                        ergList.append(["MOVE",str(troll.id),str(x),str(y)]) 
            elif zielDict[trollId].name == "HOLE" and troll.waren == 0:
                if len(zielDict[trollId].ziel) == 0:
                    dist=999;zielXY=""
                    for treeId,tree in treeDict.items():
                        if zielDict[trollId].aufgabe == tree.type and ((tree.size == 4 and tree.cooldown < 4) or tree.fruits > 0):
                            d = getDistanz(troll.xy,setXY(tree.x,tree.y))
                            if d < dist:
                                dist=d;zielXY=setXY(tree.x,tree.y)
                    zielDict[trollId].ziel = zielXY
                    x,y=getXY(zielDict[trollId].ziel)
                    ergList.append(["MOVE",str(troll.id),str(x),str(y)]) 
                else:
                    if troll.xy == zielDict[trollId].ziel:
                        ergList.append(["HARVEST",str(troll.id)])
                        if troll.capacity == troll.waren +1:
                            zielDict[trollId].ziel = "";zielDict[trollId].aufgabe="";zielDict[trollId].name=""
                    else:
                        x,y=getXY(zielDict[trollId].ziel)
                        ergList.append(["MOVE",str(troll.id),str(x),str(y)]) 
            elif troll.capacity == troll.waren: # gehe ins Lager
                troll.ziel=""                
                if getDistanz(troll.xy,myBase) == 1:                    
                    if not troll.xy in treeList and troll.plant > 0:
                        ergList.append(["PLANT",str(troll.id),str(troll.getPlant())])
                    else:
                        freierNachbar="";x=troll.x;y=troll.y
                        for nXY in [setXY(x+1,y),setXY(x-1,y),setXY(x,y+1),setXY(x,y-1)]:
                            if nXY in moveList and not nXY in treeDict:
                                freierNachbar=nXY
                        if len(freierNachbar) > 0:
                            x,y=getXY(freierNachbar)
                            ergList.append(["MOVE",str(troll.id),str(x),str(y)])
                        else:
                            ergList.append(["DROP",str(troll.id)]) 
                        if troll.iron > 0:  # erledigt
                            zielDict[trollId].ziel = ""
                        eisen = 1
                        if len(trollList) == 3:
                            eisen = 5
                        if scoreList['iron'] < len(trollList) + eisen and zielDict[trollId].name == "iron" and len(trollList) < ANZAHLTROLLE:
                            zielDict[trollId].ziel = ironList[0];zielDict[trollId].aufgabe="MINE"
                            ergList.append(["MSG iron-ziel gesetzt"])

                else:
                    if getDistanz(troll.xy,myBase) == 2 and not troll.xy in treeList and troll.plant > 0:
                        ergList.append(["PLANT",str(troll.id),str(troll.getPlant())])
                    else:
                        xBase,yBase=getXY(myBase)
                        ergList.append(["MOVE",str(troll.id),str(xBase),str(yBase)])    
            elif len(zielDict[trollId].ziel) > 0 and zielDict[trollId].aufgabe == "MINE":
                if getDistanz(ironList[0],troll.xy) == 0:
                    ergList.append(["MINE",str(troll.id)])
                else:
                    xZiel,yZiel=getXY(ironList[0])
                    ergList.append(["MOVE",str(troll.id),str(xZiel),str(yZiel)])                                      
            elif troll.xy in treeList and treeDict[troll.xy].fruits > 0:                 
                ergList.append(["HARVEST",str(troll.id)])
            elif troll.capacity > troll.waren: # suche waren
                troll.treeDict=setTreeDistanz(treeDict,troll.xy,moveZiel,zielDict)
                if len(troll.treeDict) > 0:
                    zielXY = troll.getShortTree()
                else:
                    ## was dann
                    zielXY = myBase
                xZiel,yZiel=getXY(zielXY)
                ergList.append(["MOVE",str(troll.id),str(xZiel),str(yZiel)])
                moveZiel.append(zielXY)  # damit nicht der selbe Baum gesteuert wird
    # neuen Troll trainieren
    if len(trollList) < ANZAHLTROLLE and runde < 200:
        minWert=len(trollList)+1
        if scoreList['plum'] >= minWert and scoreList['lemon'] >= minWert and scoreList['apple'] >= minWert and scoreList['iron'] >= minWert-1:
            eisen=0
            for trollId,troll in trollDict.items():
                eisen+=troll.iron
            if eisen == 0:
                ergList.append(["TRAIN",str(int(math.sqrt(scoreList['plum']-len(trollList)))),str(int(math.sqrt(scoreList['lemon']-len(trollList)))),str(int(math.sqrt(scoreList['apple']-len(trollList)))),str(int(math.sqrt(scoreList['iron']-len(trollList))))])



##############################################
##############################################

lineList=[];runde=0;scoreDict={};treeDict={};trollDict={};ergList=[];grundList=[];ironList=[];waterList=[];baseDict={};zielDict={}
width,height,runde,myBase,oppBase = initMap(lineList,scoreDict,treeDict,trollDict,ergList,grundList,ironList,waterList,zielDict)
# gameplay #
moveList,graph = setGraph(grundList,treeDict,myBase,oppBase,lineList,ironList,waterList,baseDict)
while True:
    bewegung(width,height,runde,myBase,oppBase,lineList,scoreDict,treeDict,trollDict,ergList,grundList,moveList,graph,ironList,waterList,baseDict,zielDict)

    if len(ergList) == 0:
        print("WAIT")
    else:
        ausgabe=""
        for erg in ergList:            
            for e in erg:
                ausgabe+=e+" "
            ausgabe = ausgabe[:-1]+";"
        print(ausgabe[:-1])    
    ####
    runde+=1
    if runde > 1:
        break