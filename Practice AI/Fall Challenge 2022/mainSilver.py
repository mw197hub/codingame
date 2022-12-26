import sys,math
from dataclasses import dataclass
import operator

ME,OPP,NONE = 1,0,-1

mapDict={}
def initMap(width,height):
    eingabe = open('C:\\Users\\marku\\Python\\codingame\\Practice AI\\Fall Challenge 2022\\input1.txt','r')
    for zeile in eingabe:
        if not zeile[0] == "*":
            z=zeile.split(",")
            mapDict[str(z[0])+"-"+str(z[1])] = Feld(int(z[0]),int(z[1]),int(z[2]),int(z[3]),int(z[4]),int(z[5]),int(z[6]),int(z[7]),int(z[8]))

def getWerte(x,y):
    if str(x)+"-"+str(y) in mapDict:
        f = mapDict[str(x)+"-"+str(y)]
        return f.scrap_amount, f.owner, f.units, f.recycler, f.can_build, f.can_spawn, f.in_range_of_recycler
    else:
        return 0,0,0,-1,0,0,0,0,0
def naechsteRunde(actions,my_matter, opp_matter):
   # for act in actions:
    my_matter+=10;opp_matter+=10
    return my_matter, opp_matter

#@dataclass
#class Feld:
#    x: int;y: int;scrap_amount: int;owner: int;units: int
#    recycler: bool;can_build: bool;can_spawn: bool;in_range_of_recycler: bool
#  BUILD x y;MOVE a x y x y;SPAWN a x y;WAIT;MESSAGE text
def setXY(x,y):
    return str(x)+"-"+str(y)
def getXY(xy):
    x,y = xy.split("-")
    return int(x),int(y)
class Feld:
    def __init__(self,x,y,scrap_amount, owner, units, recycler, can_build, can_spawn, in_range_of_recycler):
        self.x=x;self.y=y;self.scrap_amount=scrap_amount;self.owner=owner;self.units=units;self.recycler=recycler
        self.can_build=can_build;self.can_spawn=can_spawn;self.in_range_of_recycler=in_range_of_recycler
        self.amount_all=0;self.amount_get=0;self.move=[];self.enemy_near=0;self.action="";self.enemy_pos=""
        self.moeglich={}

def setZielList(width, height,feldDict,enemyDict,myDict,recDict,myFeldDict,enemyFeldDict,neutralFeldDict):
    myMitte,enemyMitte,=0,0
    yList=[]
    for xy in myDict:
        x,y=getXY(xy);myMitte+=x
    for xy in enemyDict:
        x,y=getXY(xy);enemyMitte+=x
    links=False if myMitte > enemyMitte else True
    myMitte= int(myMitte/4) +1 if links else int(myMitte/4) -1
    for xy in myDict:
        x,y=getXY(xy) 
        if x == myMitte:
            yList.append(y)
            break
    
    zielList,startPhase=[],0
    if links:
        x=int(width/2) if width / 2 == width //2 else int((width+3)/2)
    else:
        x=int(width/2)-1 if width / 2 == width //2 else int((width-3)/2)
    if not 1 in yList:
        yList.append(1)
    if not height-2 in yList:
        yList.append(height-2)
    diff=int((yList[0]-yList[1])/2)
    if not yList[0]-diff in yList:
        yList.append(yList[0]-diff)
    if not yList[0]+diff in yList:
        yList.append(yList[0]+diff)
    yList.append(0);yList.append(height-1)
    for y in range(height):
        if not y in yList:
            yList.append(y)    
    for y in yList:
        xy = setXY(x,y)
        if xy in feldDict:
            zielList.append(xy)
    return zielList,x,links

def setzeWerte(feldDict,enemyDict,myDict,recDict,myFeldDict,enemyFeldDict,bereichList,zielList,width, height,neutralFeldDict):
    recDownDict={}
    for xy,feld in recDict.items():
        x,y=getXY(xy)
        if feld.owner == 1:
            recDownDict[xy] = feld.scrap_amount//2
            for n in [[0,-1],[1,0],[0,1],[-1,0]]:
                xN = x + n[0];yN = y + n[1];xyN=setXY(xN,yN)
                if xyN in feldDict:
                    feldN = feldDict[xyN]
                    wert = feldN.scrap_amount if feldN.scrap_amount >= feld.scrap_amount else feld.scrap_amount
                    if xyN in recDownDict:
                        wert = recDownDict[xyN] if recDownDict[xyN] > wert else wert
                    recDownDict[xyN] =  wert//2

    for xy,feld in feldDict.items():
        x,y=getXY(xy)
        amount_all=feld.scrap_amount;enemy_near=0;move=[]
        amount_get=feld.scrap_amount - recDownDict[xy] if xy in recDownDict else feld.scrap_amount
        amount_get = 0 if amount_get < 0 else amount_get        
        for n in [[0,-1],[1,0],[0,1],[-1,0]]:
            xN = x + n[0];yN = y + n[1];xyN=setXY(xN,yN)
            if xyN in feldDict:
                feldN=feldDict[xyN]    
                wert = feldN.scrap_amount - recDownDict[xyN]if xyN in recDownDict else feldN.scrap_amount
                wert = wert if wert > 0 else 0
                wert = wert if feld.scrap_amount >= wert else feld.scrap_amount                
                amount_get = amount_get + wert  
                amount_all = amount_all + feldN.scrap_amount if feld.scrap_amount >= feldN.scrap_amount else amount_all + feld.scrap_amount

                if feldN.owner == 0 and feld.owner == 1:
                    enemy_near+=feldN.units
                if feldN.owner == 1 and feld.owner == 0:
                    enemy_near+=feldN.units
                if feldN.scrap_amount > 0 and not xyN in recDict:
                    move.append(xyN)
        feld.amount_all = amount_all;feld.amount_get = amount_get;feld.enemy_near = enemy_near
        feld.move = move

    for xy,feld in feldDict.items():
        vorhanden=False
        for bereich in bereichList:
            if xy in bereich:
                vorhanden=True
                feld.moeglich=bereich
        if not vorhanden:
            wege={};wege[xy]=0
            wegeMoeglich(xy,feldDict,wege,0)
        # wege,queue,visited={},[],[]    # zu langsam
        # bfsMitWege(wege, queue, visited, feldDict, xy)
            feld.moeglich=wege
            bereichW=[]
            for weg in wege:
                bereichW.append(weg)
                
            vorhanden=False
            for bereich in bereichList:
                if bereichW[0] in bereich:
                    vorhanden = True
            if not vorhanden:
                bereichList.append(bereichW[:])

    #Zielbereich festlegen
    

###############################
###############################
def bfsStartZiel(feldDict, start, goal,myFeldDict):
    explored = []
    queue = [[start]]
    if start == goal:
        return []  # start = Ziel
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            if node in feldDict:
                neighbours = feldDict[node].move
            else:
                neighbours = myFeldDict[node].move
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path
            explored.append(node)
    return []  # kein Weg

def bfsMitWege(wege, queue, visited, feldDict, node):
    if node not in visited:
      #  print(node)
        visited.append(node)
        for neighbour in feldDict[node].move:
            bfsMitWege(wege, queue, visited,feldDict,neighbour)
        if visited[-1] in wege:
            if len(visited)-1 < wege[visited[-1]]:
                wege[visited[-1]] = len(visited)-1
        else:
            wege[visited[-1]] = len(visited)-1
        visited.pop()
##############################

def wegeMoeglich(xy,feldDict,visited,dist):
    dist+=1
    for moveXY in feldDict[xy].move:
        if not moveXY in visited:
            visited[moveXY] = dist
            wegeMoeglich(moveXY,feldDict,visited,dist)            
        else:
            if dist < visited[moveXY]:
                visited[moveXY] = dist
    dist-=1

def myNaeher(xyE,myDict,feldDict):
    dist=999
    xE,yE=getXY(xyE)
    for xy in myDict:
        x,y=getXY(xy)
        if abs(x-xE)+abs(y-yE) < dist:
            dist=abs(x-xE)+abs(y-yE)
    return dist

def getShortDist(myFeldDict,neutralFeldDict,feldDict,myDict,enemyFeldDict,bereichList,action):

    xS,yS,xZ,yZ,dist,=0,0,-1,-1,999
    xS2,yS2,xZ2,yZ2,dist2=0,0,-1,-1,999
    for xy in myFeldDict:        
        x,y=getXY(xy);my = myDict[xy]
        for m in my.move:
            if m in enemyFeldDict:
                xZ,yZ = getXY(m)
            if m in neutralFeldDict:
                xZ2,yZ2 = getXY(m)

        if xZ ==-1 and xZ2 == -1:                    
        #for xyE in feldDict[xy].moeglich:
            for xyE in myDict[xy].moeglich:
                xE,yE=getXY(xyE)
                if abs(x-xE)+abs(y-yE) < dist and not xy == xyE and (xyE in neutralFeldDict or xyE in enemyDict):
                    dist2=abs(x-xE)+abs(y-yE);xS2=x;yS2=y;xZ2=xE;yZ2=yE                
                    moeglich = feldDict[xy].moeglich
                    if xyE in moeglich:                    
                        if abs(x-xE)+abs(y-yE) <= myNaeher(xyE,myDict,feldDict):
                            dist = abs(x-xE)+abs(y-yE);xS=x;yS=y;xZ=xE;yZ=yE
            if dist == 999:
                xS=xS2;yS=yS2;xZ=xZ2;yZ=yZ2
    if not xZ == -1:
        setMove(my,my.units,x,y,xZ,yZ,action,feldDict,myFeldDict)
    elif not xZ2 == -1:
        setMove(my,my.units,x,y,xZ2,yZ2,action,feldDict,myFeldDict)

def getSpawnDist(myFeldDict,enemyDict,feldDict,myDict,bereicheList,action,links,my_matter,neutralFeldDict):    
    for bereich in sorted(bereicheList, key=len):
        if bereich[0] > 0 and bereich[1] > 0:
            wertDict={}
            for b in bereich[3:]:                
                if b in myFeldDict:
                    feld = myFeldDict[b];wert=0
                    if feld.enemy_near > feld.units:
                        wert += (feld.enemy_near - feld.units)*10
                    for m in feld.move:
                        if feldDict[m].owner == 0:
                            wert +=2                        
                        if feldDict[m].enemy_near > 0:
                            wert +=4
                        for m2 in feldDict[m].move:
                            if feldDict[m2].owner == 0:
                                wert +=1
                    wertDict[b] = wert
            for b in sorted(wertDict, key=wertDict.get, reverse=True):
                if my_matter >= 10 and wert > 0:
                    xS,yS=getXY(b)
                    action.append("SPAWN {} {} {}".format(1,xS,yS))
                    my_matter-=10

    if my_matter >= 10:
        xS,yS,xZ,yZ,dist,=-1,-1,-1,-1,999
        xS2,yS2,xZ2,yZ2,dist2=-1,-1,-1,-1,999
        for xy in myFeldDict:   
            for bereich in bereicheList:   
                if xy in bereich:
                    x,y=getXY(xy)
                    for xyE in enemyDict:
                        xE,yE=getXY(xyE)
                        if abs(x-xE)+abs(y-yE) < dist:
                            dist2=abs(x-xE)+abs(y-yE);xS2=x;yS2=y;xZ2=xE;yZ2=yE
                            if abs(x-xE)+abs(y-yE) <= myNaeher(xyE,myDict,feldDict):
                                dist = abs(x-xE)+abs(y-yE);xS=x;yS=y;xZ=xE;yZ=yE
        if dist == 999:
            xS=xS2;yS=yS2;xZ=xZ2;yZ=yZ2
            if dist2 == 999:            
                for bereich in bereichList:
                    myFeld="";ziele=False
                    for xy in bereich:
                        if xy in myFeldDict:
                            myFeld = xy
                        if xy in enemyDict or xy in neutralFeldDict:
                            ziele=True
                    if ziele and len(myFeld) > 0:
                        xS,yS=getXY(myFeld)
                        break
        if xS > -1:
            action.append("SPAWN {} {} {}".format(my_matter//10,xS,yS))

def setMove(f1,anz,xS,yS,xZ,yZ,action,feldDict,myFeldDict):
    f1.units -= anz
    diffX=xZ-xS;diffY=yZ-yS
    yN = yS -1 if diffY < 0 else yS + 1
    if abs(diffY) >= 1 and setXY(xS,yN) in f1.move:    # bevorzugt oben und unten
        weg = bfsStartZiel(feldDict, setXY(xS,yS), setXY(xS,yZ),myFeldDict)
        if len(weg) == 0 or len(weg) > abs(yS-yZ) +1:
            action.append("MOVE {} {} {} {} {}".format(anz,xS,yS,xZ,yZ))
        else:
            action.append("MOVE {} {} {} {} {}".format(anz,xS,yS,xS,yZ))
    else:
        action.append("MOVE {} {} {} {} {}".format(anz,xS,yS,xZ,yZ))
    
def setBereicheList(bereichList,feldDict):
    bereicheList=[]
    for bereich in bereichList:
        save=True;my,enemy,neutral=0,0,0
        for b in bereich:
            if feldDict[b].owner == -1 or feldDict[b].owner == 0:
                if b=='8-8':
                    a=0
                save=False
                if feldDict[b].owner == -1:
                    neutral+=1
                else:
                    enemy+=1
            if feldDict[b].owner ==1:
                my+=1
        if not save:
            bereiche=[];bereiche.append(my);bereiche.append(enemy);bereiche.append(neutral)
            bereiche.extend(bereich)
            bereicheList.append(bereiche)  
    return bereicheList

#########################
def moveAndSpawn(feldDict,enemyDict,myDict,recDict,myFeldDict,enemyFeldDict,my_matter,opp_matter,bereichList,runde,zielList,startPhase,links,neutralFeldDict):
    action=[];buildList=[]
    startPhase+=8
    #startPhase=0
    bereicheList = setBereicheList(bereichList,feldDict)

# build
    amountList=[]
    for xy in zielList:
        if xy in myFeldDict:
            feld = myFeldDict[xy]
            if feld.can_build and not xy in buildList:
                if my_matter >= 10:                    
                    action.append("BUILD {} {}".format(feld.x,feld.y))
                    my_matter-=10;zielList.remove(xy);buildList.append(xy)

    for xyFeld in myFeldDict:
        if myFeldDict[xyFeld].units == 0:
            amountList.append(myFeldDict[xyFeld])
    for feld in sorted(amountList, key=lambda x: x.amount_get, reverse=True):
            if runde <= startPhase and feld.amount_get > 30 and feld.can_build:
                xy=setXY(feld.x,feld.y)
                if my_matter >= 10 and not xy in buildList:                    
                    action.append("BUILD {} {}".format(feld.x,feld.y))
                    my_matter-=10;buildList.append(xy)
    if my_matter >= 10:
        for bereich in bereicheList:
            if bereich[1] > bereich[0]:
                for b in bereich[3:]:
                    feld = feldDict[b]
                    if feld.can_build and feld.amount_get > 18 and feld.enemy_near > 0:
                        action.append("BUILD {} {}".format(feld.x,feld.y))
                        my_matter-=10;xy=setXY(feld.x,feld.y);buildList.append(xy)

# move
    myMoveList=[]           
    for xy in myDict:
        if xy in zielList:
            getShortDist([xy],neutralFeldDict,feldDict,myDict,enemyFeldDict,bereichList,action)
        else:
            myMoveList.append(xy)
    if runde <= startPhase:                
        anz=0
        for ziel in zielList:
            xZ,yZ=getXY(ziel);dist=9999;xyS=""
            bereiche=[]
            for bereich in bereichList:
                if ziel in bereich:
                    bereiche=bereich;break
            for xy in myMoveList:
                if xy in bereich:
                    pathZ = bfsStartZiel(feldDict, xy, ziel,myFeldDict)
                    if len(pathZ) < dist:
                        dist=len(pathZ);xyS=xy
            if len(xyS) > 0:
                x,y=getXY(xyS)
                if myFeldDict[xyS].units > 1 and len(zielList) > anz:
                    setMove(myFeldDict[xyS],1,x,y,xZ,yZ,action,feldDict,myFeldDict);anz+=1
                else:
                    setMove(myFeldDict[xyS],1,x,y,xZ,yZ,action,feldDict,myFeldDict);anz+=1
                    myMoveList.remove(xyS)
            if len(myMoveList) == 0:
                break
    if runde > startPhase or len(myMoveList) > 0:
        for xy in myMoveList:
            my = myDict[xy]
            if my.units > 0:
                getShortDist([xy],neutralFeldDict,feldDict,myDict,enemyFeldDict,bereichList,action)
# spawn
    if my_matter >= 10:
        getSpawnDist(myFeldDict,enemyDict,feldDict,myDict,bereicheList,action,links,my_matter,neutralFeldDict)
                    
    return action
#########################
#########################
width, height = 18,9
my_matter, opp_matter=17,8
initMap(width,height)
zielList,startPhase,links=[],0,False
runde=1;test=True
while True:
    scrapSum,my_units,opp_units=0,0,0
    feldDict={};enemyDict={};myDict={};recDict={};myFeldDict={};enemyFeldDict={};neutralFeldDict={};bereichList=[]
   # my_matter, opp_matter=0,0
    for y in range(height):
        for x in range(width):
            xy=setXY(x,y)
            scrap_amount, owner, units, recycler, can_build, can_spawn, in_range_of_recycler = getWerte(x,y)
            if scrap_amount == 0 or (scrap_amount == 1 and in_range_of_recycler == 1) or recycler == 1:
                feld = Feld(x, y, scrap_amount, owner, units, recycler == 1, can_build == 1, can_spawn == 1, in_range_of_recycler == 1)
                if recycler == 1:
                    recDict[setXY(x,y)] = feld   
                if in_range_of_recycler == 1 and owner==1:
                    myFeldDict[setXY(x,y)] = feld
                    if units > 0:
                        myDict[setXY(x,y)] = feld
                        if xy in zielList:
                            zielList.remove(xy)
            else:
                feld = Feld(x, y, scrap_amount, owner, units, recycler == 1, can_build == 1, can_spawn == 1, in_range_of_recycler == 1)
                feldDict[setXY(x,y)] = feld
                if owner == 1:
                    myFeldDict[setXY(x,y)] = feld
                    if units > 0:
                        myDict[setXY(x,y)] = feld
                        if xy in zielList:
                            zielList.remove(xy)
                elif owner == 0:
                    enemyFeldDict[setXY(x,y)] = feld
                    if units > 0:
                        enemyDict[setXY(x,y)] = feld
                else:
                    neutralFeldDict[setXY(x,y)] = feld
                             
                scrapSum+=scrap_amount
            
    setzeWerte(feldDict,enemyDict,myDict,recDict,myFeldDict,enemyFeldDict,bereichList,zielList,width, height,neutralFeldDict)
    if runde== 1:
        zielList,startPhase,links=setZielList(width, height,feldDict,enemyDict,myDict,recDict,myFeldDict,enemyFeldDict,neutralFeldDict)
        print(zielList,file=sys.stderr)
        if test:
            zielList=[]
    #test    
   # print(bereichList,file=sys.stderr)

    actions = moveAndSpawn(feldDict,enemyDict,myDict,recDict,myFeldDict,enemyFeldDict,my_matter,opp_matter,bereichList,runde,zielList,startPhase,links,neutralFeldDict)
    print(';'.join(actions) if len(actions) > 0 else 'WAIT')

    my_matter, opp_matter = naechsteRunde(actions,my_matter,opp_matter)
    runde+=1
    if runde > 0:
        break