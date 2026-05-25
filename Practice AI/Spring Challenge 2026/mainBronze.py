import sys,math,copy

def initMap(lineList,scoreDict,treeDict,trollDict,ergList,grundList):
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
    for y in range(len(lineList)):
        for x in range(len(lineList[0])):
            if lineList[y][x] == "1":
                oppBase=setXY(x,y)
            if lineList[y][x] == "0":
                myBase=setXY(x,y)           
            if lineList[y][x] == ".":
                grundList.append(setXY(x,y))

    return width,height,runde,myBase,oppBase
###################################
### intern initMap     ############
###################################

class Tree:
    def __init__(self,i,_type,x,y,size,health,fruits,cooldown):
        self.nr=i;self.type=_type;self.x=x;self.y=y;self.size=size;self.health=health;self.fruits=fruits;self.cooldown=cooldown        
    def __str__(self) -> str:
        return ("nr={},type={},x={},y={},size={},health={},fruits={},cooldown={}".format(self.nr,self.type,self.x,self.y,self.size,self.health,self.fruits,self.cooldown))
class Troll:
    def __init__(self,id, player, x, y, movement_speed, carry_capacity, harvest_power, chop_power, carry_plum, carry_lemon, carry_apple, carry_banana, carry_iron, carry_wood):
        self.id=id;self.player=player;self.x=x;self.y=y;self.speed=movement_speed;self.capacity=carry_capacity;self.harvest=harvest_power;self.chop=chop_power
        self.plum=carry_plum;self.lemon=carry_lemon;self.apple=carry_apple;self.banana=carry_banana;self.iron=carry_iron;self.wood=carry_wood
        self.aktualisieren();self.treeDict={}
    def __str__(self) -> str:
        return("id={},player={},x={},y={},speed={},capacity={},harvest={},chop={},plum={},lemon={},apple={},banana={},iron={},wood={}".format(self.id,self.player,self.x,self.y,self.speed,self.capacity,self.harvest,self.chop,self.plum,self.lemon,self.apple,self.banana,self.iron,self.wood))
    def aktualisieren(self):
        self.waren=self.plum+self.lemon+self.apple+self.banana+self.iron+self.wood
        self.xy=setXY(self.x,self.y)
    def getShortTree(self):
        treeList = sorted(self.treeDict.items(), key=lambda item: item[1])
        return treeList[0][0]
def setXY(x,y):
    return str(x)+"#"+str(y)
def getXY(xy):
    hList=xy.split("#")
    return int(hList[0]),int(hList[1])

def suchePath(graph, start, goal,moveList):
    explored = [];queue = [start];lauf=0 
    suchList=copy.deepcopy(moveList);suchList.append(start)
    if start == goal:
        return [] # start ist ziel
    while queue:
        path,snBody = queue.pop(0);node = path[-1]
        if node not in explored and node in suchList:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path
            explored.append(node)
    return [] # kein Weg zum Ziel

def getDistanz(xyA,xyB):
    x1,y1=getXY(xyA);x2,y2=getXY(xyB)
    return abs(x1-x2)+abs(y1-y2)
def setGraph(grundList,treeDict,myBase,oppBase,lineList):
    moveList = copy.deepcopy(grundList);graph={}           
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
        graph[move]=zList[:]
    return moveList,graph
def setTreeDistanz(treeDict,xyPos):
    distanzDict={}
    for treeId,tree in treeDict.items():
        dist = getDistanz(xyPos,setXY(tree.x,tree.y))
        if tree.fruits > 0 or (tree.size == 4 and dist > tree.cooldown):
            distanzDict[treeId] = dist
    return distanzDict
####
def bewegung(width,height,runde,myBase,oppBase,lineList,scoreDict,treeDict,trollDict,ergList,grundList,moveList,graph):
    treeList=[]
    for treeId,tree in treeDict.items():                              
        treeList.append(setXY(tree.x,tree.y))
    for trollId,troll in trollDict.items():
        troll.aktualisieren()
        if trollId == 0:            
            if troll.capacity == troll.waren: # gehe ins Lager
                if getDistanz(troll.xy,myBase) == 1:
                    ergList.append(["DROP",str(troll.id)])
                else:
                    xBase,yBase=getXY(myBase)
                    ergList.append(["MOVE",str(troll.id),str(xBase),str(yBase)])
            elif troll.xy in treeList and treeDict[troll.xy].fruits > 0:
                ergList.append(["HARVEST",str(troll.id)])
            elif troll.capacity > troll.waren: # suche waren
                troll.treeDict=setTreeDistanz(treeDict,troll.xy)
                zielXY = troll.getShortTree();xZiel,yZiel=getXY(zielXY)
                ergList.append(["MOVE",str(troll.id),str(xZiel),str(yZiel)])

##############################################
##############################################

lineList=[];runde=0;scoreDict={};treeDict={};trollDict={};ergList=[];grundList=[]
width,height,runde,myBase,oppBase = initMap(lineList,scoreDict,treeDict,trollDict,ergList,grundList)
# gameplay #
moveList,graph = setGraph(grundList,treeDict,myBase,oppBase,lineList)
while True:
    bewegung(width,height,runde,myBase,oppBase,lineList,scoreDict,treeDict,trollDict,ergList,grundList,moveList,graph)

    if len(ergList) == 0:
        print("WAIT")
    else:
        for erg in ergList:
            if len(erg) == 4:
                print("{} {} {} {}".format(erg[0],erg[1],erg[2],erg[3]))
            else:
                print("{} {}".format(erg[0],erg[1]))    
    ####
    if runde > 1:
        break