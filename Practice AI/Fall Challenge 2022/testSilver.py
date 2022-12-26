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
                if abs(x-xE)+abs(y-yE) < dist and not xy == xyE and xyE in neutralFeldDict:
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

def getSpawnDist(myFeldDict,enemyDict,feldDict,myDict,bereichList,action,links,my_matter,neutralFeldDict):
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
        return 
    for xy in myFeldDict:
     #   visited={};visited[xy]=0
     #   wegeMoeglich(xy,feldDict,visited,0)
        if xy in bereiche:
            x,y=getXY(xy)
            for xyE in enemyDict:
                xE,yE=getXY(xyE)
                if abs(x-xE)+abs(y-yE) < dist:
      #          if xyE in visited and abs(x-xE)+abs(y-yE) >= visited[xyE] -2:
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
    if abs(diffY) > 1 and setXY(xS,yN) in f1.move:    # bevorzugt oben und unten
        weg = bfsStartZiel(feldDict, setXY(xS,yS), setXY(xS,yZ),myFeldDict)
        if len(weg) == 0 or len(weg) > abs(yS-yZ) +1:
            action.append("MOVE {} {} {} {} {}".format(anz,xS,yS,xZ,yZ))
        else:
            action.append("MOVE {} {} {} {} {}".format(anz,xS,yS,xS,yZ))
    else:
        action.append("MOVE {} {} {} {} {}".format(anz,xS,yS,xZ,yZ))
    

#########################
def moveAndSpawn(feldDict,enemyDict,myDict,recDict,myFeldDict,enemyFeldDict,my_matter,opp_matter,bereichList,runde,zielList,startPhase,links,neutralFeldDict):
    action=[];buildList=[]
    startPhase+=8
    #startPhase=0
# build
    amountList=[]
    for xy in zielList:
        if xy in myFeldDict:
            feld = myFeldDict[xy]
            if feld.can_build:
                if my_matter >= 10:                    
                    action.append("BUILD {} {}".format(feld.x,feld.y))
                    my_matter-=10;zielList.remove(xy);buildList.append(xy)

    for xyFeld in myFeldDict:
        if myFeldDict[xyFeld].units == 0:
            amountList.append(myFeldDict[xyFeld])
    for feld in sorted(amountList, key=lambda x: x.amount_get, reverse=True):
            if runde <= startPhase and feld.amount_get > 30 and feld.can_build:
                if my_matter >= 10:                    
                    action.append("BUILD {} {}".format(feld.x,feld.y))
                    my_matter-=10;buildList.append(xy)

# move
    myMoveList=[]
    if runde <= startPhase:        
        for xy in myDict:
            if xy in zielList:
                getShortDist([xy],neutralFeldDict,feldDict,myDict,enemyFeldDict,bereichList,action)
            else:
                myMoveList.append(xy)
        anz=0
        for ziel in zielList:
            xZ,yZ=getXY(ziel);dist=9999;xyS=""
            for xy in myMoveList:
                pathZ = bfsStartZiel(feldDict, xy, ziel,myFeldDict)
                if len(pathZ) < dist:
                    dist=len(pathZ);xyS=xy
            x,y=getXY(xyS)
            if myFeldDict[xyS].units > 1 and len(zielList) > anz:
                setMove(myFeldDict[xyS],1,x,y,xZ,yZ,action,feldDict,myFeldDict);anz+=1
            else:
                setMove(myFeldDict[xyS],1,x,y,xZ,yZ,action,feldDict,myFeldDict);anz+=1
                myMoveList.remove(xyS)
            if len(myMoveList) == 0:
                break
    if runde > startPhase or len(myMoveList) > 0:
        for xy,my in myDict.items():
            if my.units > 0:
                getShortDist([xy],neutralFeldDict,feldDict,myDict,enemyFeldDict,bereichList,action)
# spawn
    if my_matter >= 10:
        getSpawnDist(myFeldDict,enemyDict,feldDict,myDict,bereichList,action,links,my_matter,neutralFeldDict)
        
            
    return action