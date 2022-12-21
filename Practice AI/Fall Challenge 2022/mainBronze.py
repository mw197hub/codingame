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

def setzeWerte(feldDict,enemyDict,myDict,recDict,myFeldDict,enemyFeldDict,bereichList):
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


###############################
###############################
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

def getShortDist(myFeldDict,enemyDict,feldDict,myDict):
    xS,yS,xZ,yZ,dist,=0,0,0,0,999
    xS2,yS2,xZ2,yZ2,dist2=0,0,0,0,999
    for xy in myFeldDict:
        x,y=getXY(xy)
        for xyE in feldDict[xy].moeglich:
            xE,yE=getXY(xyE)
            if abs(x-xE)+abs(y-yE) < dist and not xy == xyE and xyE in enemyDict:
                dist2=abs(x-xE)+abs(y-yE);xS2=x;yS2=y;xZ2=xE;yZ2=yE                
                moeglich = feldDict[xy].moeglich
                if xyE in moeglich:                    
                    if abs(x-xE)+abs(y-yE) <= myNaeher(xyE,myDict,feldDict):
                        dist = abs(x-xE)+abs(y-yE);xS=x;yS=y;xZ=xE;yZ=yE
    if dist == 999:
        xS=xS2;yS=yS2;xZ=xZ2;yZ=yZ2
    return xS,yS,xZ,yZ

def getSpawnDist(myFeldDict,enemyDict,feldDict,myDict,bereichList):
    xS,yS,xZ,yZ,dist,=-1,-1,-1,-1,999
    xS2,yS2,xZ2,yZ2,dist2=-1,-1,-1,-1,999
    bereiche=[]
    for bereich in bereichList:
        save=True
        for b in bereich:
            if feldDict[b].owner == -1 or feldDict[b].owner == 0:
                save=False
        if not save:
            bereiche.extend(bereich)
    if len(bereiche) == 0:
        return -1,-1,-1,-1
    for xy in myFeldDict:
     #   visited={};visited[xy]=0
     #   wegeMoeglich(xy,feldDict,visited,0)
        if xy in bereiche:
            x,y=getXY(xy)
            for xyE in bereiche:
                xE,yE=getXY(xyE)
                if abs(x-xE)+abs(y-yE) < dist:
      #          if xyE in visited and abs(x-xE)+abs(y-yE) >= visited[xyE] -2:
                    dist2=abs(x-xE)+abs(y-yE);xS2=x;yS2=y;xZ2=xE;yZ2=yE
                    if abs(x-xE)+abs(y-yE) <= myNaeher(xyE,myDict,feldDict):
                        dist = abs(x-xE)+abs(y-yE);xS=x;yS=y;xZ=xE;yZ=yE
    if dist == 999:
        xS=xS2;yS=yS2;xZ=xZ2;yZ=yZ2
    return xS,yS,xZ,yZ

#########################
def moveAndSpawn(feldDict,enemyDict,myDict,recDict,myFeldDict,enemyFeldDict,my_matter,opp_matter,bereichList,runde):
    action=[]
# build
    amountList=[]
    for xyFeld in myFeldDict:
        if myFeldDict[xyFeld].units == 0:
            amountList.append(myFeldDict[xyFeld])
    for feld in sorted(amountList, key=lambda x: x.amount_get, reverse=True):
            if runde < 10 and feld.amount_get > 30:
                if my_matter >= 10:                    
                    action.append("BUILD {} {}".format(feld.x,feld.y))
                    my_matter-=10

# move
    for xy,my in myDict.items():
        x,y=getXY(xy)
        xZ,yZ=-1,-1
        for m in my.move:
            if m in enemyFeldDict:
                xZ,yZ = getXY(m)
                break
        if xZ ==-1:
            xS,yS,xZ,yZ = getShortDist([xy],enemyFeldDict,feldDict,myDict)
        action.append("MOVE {} {} {} {} {}".format(my.units,x,y,xZ,yZ))
# spawn
    if my_matter >= 10:
        xS,yS,xZ,yZ=getSpawnDist(myFeldDict,enemyDict,feldDict,myDict,bereichList)
        if xS >= 0 and yS >= 0:
            action.append("SPAWN {} {} {}".format(my_matter//10,xS,yS))
    return action
#########################
#########################
width, height = 13,6
my_matter, opp_matter=10,10
initMap(width,height)
runde=18
while True:
    scrapSum,my_units,opp_units=0,0,0
    feldDict={};enemyDict={};myDict={};recDict={};myFeldDict={};enemyFeldDict={};bereichList=[]
   # my_matter, opp_matter=0,0
    for y in range(height):
        for x in range(width):
            scrap_amount, owner, units, recycler, can_build, can_spawn, in_range_of_recycler = getWerte(x,y)
            if scrap_amount == 0 or (scrap_amount == 1 and in_range_of_recycler == 1 and not owner==1 and units ==0) or recycler == 1:
                if recycler == 1:
                    feld = Feld(x, y, scrap_amount, owner, units, recycler == 1, can_build == 1, can_spawn == 1, in_range_of_recycler == 1)
                    recDict[setXY(x,y)] = feld   
            else:
                feld = Feld(x, y, scrap_amount, owner, units, recycler == 1, can_build == 1, can_spawn == 1, in_range_of_recycler == 1)
                feldDict[setXY(x,y)] = feld
                if owner == 1:
                    myFeldDict[setXY(x,y)] = feld
                    if units > 0:
                        myDict[setXY(x,y)] = feld
                elif owner == 0 or owner == -1:
                    enemyFeldDict[setXY(x,y)] = feld
                    if units > 0:
                        enemyDict[setXY(x,y)] = feld
                             
                scrapSum+=scrap_amount
            
    setzeWerte(feldDict,enemyDict,myDict,recDict,myFeldDict,enemyFeldDict,bereichList)
    #test    
   # print(bereichList,file=sys.stderr)

    actions = moveAndSpawn(feldDict,enemyDict,myDict,recDict,myFeldDict,enemyFeldDict,my_matter,opp_matter,bereichList,runde)
    print(';'.join(actions) if len(actions) > 0 else 'WAIT')

    my_matter, opp_matter = naechsteRunde(actions,my_matter,opp_matter)
    runde+=1
    if runde > 0:
        break