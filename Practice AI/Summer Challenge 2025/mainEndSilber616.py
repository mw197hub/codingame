import sys,math,copy

def initMap(feldDict,moveList,wallDict,agentGrundDict,graph,agentDict,myList,enemyList,verteidigungList):
    runde=0;my_player=0;width,height=0,0;wegRichtung=0
    pfad='C:\\Users\\marku\\Python\\codingame\\Practice AI\\Summer Challenge 2025\\'+'eingabe'+'.txt'
    eingabe = open(pfad,'r')
    for zeile in eingabe:
        if zeile[0:5] == "my_pl":
            my_player=int(zeile[10:11])
        if zeile[0:5] == "runde":
            runde=int(zeile[6:])
        if zeile[0:5] == "width":
            tList = zeile.split("=")
            zList=tList[1].split(",")
            width=int(zList[0]);height=int(zList[1])
        if zeile[0:5] == "wegRi":
            wegRichtung=int(zeile[12:])
        if zeile[0:5] == "feldD":
            zList=zeile[9:-2].split(",")
            for z in zList:
                feldDict[z[2:len(z)-4]] = int(z[-1])
                if int(z[-1]) == 0:
                    moveList.append(z[2:len(z)-4])
                else:
                    wallDict[z[2:len(z)-4]] = int(z[-1])
        if zeile[0:6] == "agentG":
            zList = zeile[15:-3].split("],")
            for z in zList:
                tList = z[z.find(":")+3:].split(",")
                tabList=[]
                for t in tList:
                    tabList.append(int(t.strip()))
                agentGrundDict[int(z[1:z.find(":")])] = tabList[:]
                
        if zeile[0:6] == "agent_":
            zList = zeile[:-1].split(";");tabList=[]
            for z in zList:
                zL=z.split("=");tabList.append(int(zL[1]))                
            #agentDict[tabList[0]]=tabList[1:]
            tList=agentGrundDict[tabList[0]]
            agentDict[tabList[0]]=Agent(tabList[0],tabList[1],tabList[2],tList[0],tList[1],tList[2],tList[3],tabList[3],tabList[4],tabList[5],[],[])
            if tList[0] == my_player:
                myList.append(tabList[0])
            else:
                enemyList.append(tabList[0])
        if zeile[0:6] == "vertei" and len(zeile) > 20:
            zList = zeile[18:-2].split(",")
            for z in zList:
                z = z.strip()
                verteidigungList.append(z[1:-1])
    eingabe.close()
    for move in feldDict:
        if move in moveList:
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
        if move in wallDict:
            x,y=getXY(move);zList=[]
            if setXY(x+1,y) in moveList:
                zList.append(setXY(x+1,y))
            if setXY(x-1,y) in moveList:
                zList.append(setXY(x-1,y))
            if setXY(x,y+1) in moveList:
                zList.append(setXY(x,y+1))
            if setXY(x,y-1) in moveList:
                zList.append(setXY(x,y-1))
            wallDict[move] = [wallDict[move],zList]

    #print(agentDict,file=sys.stderr)
    return runde,my_player,width,height,wegRichtung
##########################

class Agent:
    def __init__(self,id,x,y,owner,shoot_cooldown,optimal_range,soaking_power,cooldown,splash_bombs,wetness,moeglicheZiele,moveZiel):
        self.id=id;self.x=x;self.y=y;self.owner=owner;self.shoot_cooldown=shoot_cooldown;self.optimal_range=optimal_range
        self.soaking_power=soaking_power;self.splash_bombs=splash_bombs;self.cooldown=cooldown;self.wetness=wetness,
        self.moeglicheZiele=moeglicheZiele;self.moveZiel=moveZiel
        self.xy=str(x)+"-"+str(y)
    def __str__(self) -> str:
        return ("owner:{} xy:{} id:{} cooldown:{} wetness:{}".format(self.owner,str(self.x)+"-"+str(self.y),self.id,self.cooldown,self.wetness))

def setXY(x,y):
    return str(x)+"-"+str(y)
def getXY(xy):
    xyz = xy.split("-")
    return int(xyz[0]),int(xyz[1])
def getRichtung(startXY,zielXY):
    richtung="N"
    x,y=getXY(startXY);xN,yN=getXY(zielXY)
    if xN > x:
        return "E"
    if xN < x:
        return "W"
    if yN > y:
        return "S"
    if yN < y:
        return "N"
    return richtung
def moveRichtung(start,ziel,moveList,feldDict):
    x,y=getXY(start);xN,yN=getXY(ziel);ziele=[]
    diffX=xN-x;diffY=yN-y
    if diffY > 0 and setXY(x,y+1) in moveList:
        ziele.append(setXY(x,y+1))
    if diffY < 0 and setXY(x,y-1) in moveList:
        ziele.append(setXY(x,y-1))
    if diffX > x and setXY(x+1,y) in moveList:
        ziele.append(setXY(x+1,y))
    if diffX < x and setXY(x-1,y) in moveList:
        ziele.append(setXY(x-1,y))
    if len(ziele) == 0:
        return ziel
    if len(ziele) == 1:
        return ziele.pop(0)
    else:
        artW=-1;move=ziel
        for z in ziele:
            richtung = getRichtung(z,ziel)
            nZug=z;xz,yz=getXY(z)
            if richtung == "N":
                nZug = setXY(xz,yz-1)
            if richtung == "S":
                nZug = setXY(xz,yz+1)    
            if richtung == "E":
                nZug = setXY(xz+1,yz) 
            if richtung == "W":
                nZug = setXY(xz-1,yz) 
            if feldDict[nZug] > artW:
                artW=feldDict[nZug];move=z
    return move
def A_path(graph, start, goal):
    explored = [];queue = [[start]] 
    if start == goal:
        return [] # start ist ziel
    while queue:
        path = queue.pop(0);node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path);new_path.append(neighbour);queue.append(new_path)
                if neighbour == goal:
                    return new_path
            explored.append(node)
    return [] # kein Weg zum Ziel
def getDistanz(xyA,xyB):
    x1,y1=getXY(xyA);x2,y2=getXY(xyB)
    return abs(x1-x2)+abs(y1-y2)
def dazwischen(feld,xyA,wallDict,feldDict):
    wert=0
    for wall,wList in wallDict.items():
        if feld in wList[1]:
            if getRichtung(feld,wall) == getRichtung(feld,xyA):
                wert=50
                if feldDict[wall] == 2:
                    wert=75
    return wert
def setfeldWertDict(feldDict,agentDict,feldWertDict,my_player,wallDict):
    for feld,tile in feldDict.items():
        wert=0;anzahl=0
        if tile == 0:
            for agentId,agent in agentDict.items():
                if not agent.owner == my_player:
                    distanz = getDistanz(feld,agent.xy)
                    if distanz <= 6:
                        anzahl+=1
                        wert += dazwischen(feld,agent.xy,wallDict,feldDict)
        feldWertDict[feld] = [wert,anzahl]
    #print(feldWertDict,file=sys.stderr)
def setfeldBombDict(feldDict,agentDict,feldBombDict,my_player,wallDict,enemyList):
    for feld,tile in feldDict.items():
        anzahl=0;x,y=getXY(feld)
        for xN,yN in ([[0,0],[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]):
            for enemy in enemyList:
                if setXY(x+xN,y+yN) == agentDict[enemy].xy:
                    anzahl+=1
            for my in myList:
                if setXY(x+xN,y+yN) == agentDict[my].xy:
                    anzahl-=1
        feldBombDict[feld] = anzahl
    feldBombDict = dict(sorted(feldBombDict.items(), key=lambda x: x[1],reverse=True))
    #print(feldBombDict,file=sys.stderr)
def setEnemyTrefferDict(feldDict,agentDict,feldBombDict,my_player,wallDict,enemyList,myList,enemyTrefferDict):
    for myId in myList:
            myAgent = agentDict[myId];myAgent.moeglicheZiele.clear()
    for enemyId in enemyList:
        eAgent = agentDict[enemyId];moeglicherSchaden=0;soakList=[]
        for myId in myList:
            myAgent = agentDict[myId]
            distanz = getDistanz(eAgent.xy,myAgent.xy)            
            if myAgent.splash_bombs > 0 and distanz > 1 and distanz <= 4:
                moeglicherSchaden+=30;myAgent.moeglicheZiele.append(enemyId)                
            else:
                if myAgent.cooldown == 0:
                    if distanz <= myAgent.optimal_range *2:                    
                        moeglicherSchaden+=myAgent.soaking_power
                        soakList.append(myId);myAgent.moeglicheZiele.append(enemyId)                    
                   # elif distanz == myAgent.optimal_range *2 +1:                        
                   #     if moveRichtung(agent.xy,eAgent.xy,moveList,feldDict) in moveList:
                   #         moeglicherSchaden+=myAgent.soaking_power
                   #         soakList.append(myId);myAgent.moeglicheZiele.append(enemyId)
        enemyTrefferDict[enemyId] = [moeglicherSchaden,soakList]
    #print(enemyTrefferDict,file=sys.stderr)
def setReihenfolge(feldDict,agentDict,feldBombDict,my_player,wallDict,enemyList,myList,enemyTrefferDict,tempVerteidigungList,moveZielList,width,height,wegRichtung):
    reiheDict={};tempMyList=myList[:];xWert={}
    for myId in myList:        
        mZiele=agentDict[myId].moeglicheZiele;xWert[myId]=agentDict[myId].y
        wert=len(mZiele)*10
        wert+=agentDict[myId].optimal_range
        if wert != 0:
            reiheDict[myId] =[wert]; tempMyList.remove(myId)
    for key in dict(sorted(reiheDict.items(), key=lambda x: x[1],reverse=False)):
        reihenfolgeList.append(key)
    nr=1;mitte=width//2;abstand=(height-4)//2;wert=1
    if wegRichtung == -1:
        mitte-=1
    for key in dict(sorted(xWert.items(), key=lambda x: x[1],reverse=False)):
        if nr == 1:
            agentDict[key].moveZiel.clear();agentDict[key].moveZiel.append(setXY(mitte,1))
        elif nr == len(xWert) -1:            
            agentDict[key].moveZiel.clear();agentDict[key].moveZiel.append(setXY(mitte,height-2))
        else:            
            wert+=1
            agentDict[key].moveZiel.clear();agentDict[key].moveZiel.append(setXY(mitte,wert*abstand))
        nr+=1
    #print(reihenfolgeList,file=sys.stderr)
def setVerteidigung(feldDict,agentDict,feldBombDict,my_player,wallDict,enemyList,myList,verteidigungList):
    mitte=abs(agentDict[myList[0]].x - agentDict[enemyList[0]].x) //2
    richtung=1
    if agentDict[myList[0]].x - agentDict[enemyList[0]].x > 0:
        richtung = -1
    for wall,wallNachbar in wallDict.items():
        xW,yW = getXY(wall)
        if richtung > 0:
            if xW < mitte and xW > mitte -3:
                key = setXY(xW-1,yW)
                if feldDict[key] == 0:
                    verteidigungList.append(key)
        else:
            if xW > mitte and xW < mitte -3:
                key = setXY(xW+1,yW)
                if feldDict[key] == 0:
                    verteidigungList.append(key)
    print("verteidigungList={}".format(verteidigungList),file=sys.stderr)
    return richtung
#############################
#######
#######
#######
feldDict={};moveList=[];ergDict={};wallDict={};agentGrundDict={};graph={};agentDict={};myList,enemyList=[],[]

feldWertDict={};feldBombDict={};enemyTrefferDict={};reihenfolgeList=[];verteidigungList=[]

runde,my_player,width,height,wegRichtung=initMap(feldDict,moveList,wallDict,agentGrundDict,graph,agentDict,myList,enemyList,verteidigungList)
wegRichtung=1;moveZielList=[]

if runde == 1 and len(verteidigungList) == 0:
    wegRichtung = setVerteidigung(feldDict,agentDict,feldBombDict,my_player,wallDict,enemyList,myList,verteidigungList)
tempVerteidigungList=verteidigungList[:]
setfeldWertDict(feldDict,agentDict,feldWertDict,my_player,wallDict)
setfeldBombDict(feldDict,agentDict,feldBombDict,my_player,wallDict,enemyList)
setEnemyTrefferDict(feldDict,agentDict,feldBombDict,my_player,wallDict,enemyList,myList,enemyTrefferDict)
setReihenfolge(feldDict,agentDict,feldBombDict,my_player,wallDict,enemyList,myList,enemyTrefferDict,tempVerteidigungList,moveZielList,width,height,wegRichtung)


###
tempMoveList = moveList[:]
for id in agentDict:
    agent = agentDict[id]
    tempMoveList.remove(agent.xy)
while True:
    for i in range(len(myList)):
        ## ab hier kopieren
        agentId=reihenfolgeList.pop(0)
        agent=agentDict[agentId];xZ,yZ,enemy,waterBomb=0,0,0,0
        move='';artW=0;xB=0;yB=0;shooter=-1;xS=0;yS=0

#Deckung suchen
        #for feld in graph[setXY(agent.x,agent.y)]:
        #    if feldWertDict[feld][0] > artW:
        #        artW=feldWertDict[feld][0];move=feld
# move 
        mitte=width//2
        if wegRichtung == -1:
            mitte += wegRichtung
        if runde < mitte +2:
            ziel=agent.moveZiel[0]
            if not agent.moveZiel[0] in graph:
                for xN,yN in ([[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]):
                    if setXY(agent.x+xN,agent.y+yN) in graph:
                        ziel = setXY(agent.x+xN,agent.y+yN) 
                        break
            weg = A_path(graph,agent.xy,ziel)
            if weg[1] in tempMoveList:
                move = weg[1]
                tempMoveList.append(agent.xy);agent.xy = move

        setEnemyTrefferDict(feldDict,agentDict,feldBombDict,my_player,wallDict,enemyList,myList,enemyTrefferDict)
        if len(agent.moeglicheZiele) > 0:
            ziel=agentDict[agent.moeglicheZiele[0]].xy
            distN=999;waterWert=0
            if len(agent.moeglicheZiele) > 1:
                for eId in agent.moeglicheZiele:
                    distanz = getDistanz(agent.xy,agentDict[eId].xy)
                    if len(move) > 0:
                        distanz = getDistanz(move,agentDict[eId].xy)                    
                    if distanz < distN:
                        distN=distanz;waterWert=agentDict[eId].wetness
                        ziel=agentDict[eId].xy;shooter=eId
            
            if len(move) == 0:
                move = moveRichtung(agent.xy,ziel,tempMoveList,feldDict)
            if agent.splash_bombs > 0:
                wert=0;bZiel="";start=agent.xy
                if getDistanz(agent.xy,move) == 1:
                    start=move
                setfeldBombDict(feldDict,agentDict,feldBombDict,my_player,wallDict,enemyList)
                for bombZiel,bWert in feldBombDict.items():
                    distanz = getDistanz(start,bombZiel)
                    if distanz <= 4 and distanz > 2 and bWert > wert:
                        bZiel=bombZiel;wert=bWert
                if len(bZiel) > 0:
                    waterBomb=30;xB,yB=getXY(bZiel)
            if shooter == -1:
                shooter=agent.moeglicheZiele[0]
        else:
            if len(move) == 0:
                ziel="";nDist=999;sWeg=[]
                for enemy in enemyList:
                    eAgent=agentDict[enemy]
                    weg = A_path(graph,agent.xy,eAgent.xy)
                    distanz = len(weg)
                    if distanz < nDist and weg[1] in tempMoveList:
                        nDist=distanz;ziel=eAgent.xy;sWeg=weg[:]  
                if len(ziel) > 0:
                    if len(myList) >= 1 and len(enemyList) == 1:
                        move = sWeg[1]
                    else:
                        move = moveRichtung(agent.xy,ziel,tempMoveList,feldDict)
                

      #  distEnemy=999;waterZiel=enemyList[0];waterWert=999
      #  for enemyId in enemyList:
      #      eAgent=agentDict[enemyId]
      #      distanz=getDistanz(setXY(agent.x,agent.y),setXY(eAgent.x,eAgent.y))
      #      if distanz <= 6:
      #          wert = dazwischen(eAgent.xy,agent.xy,wallDict,feldDict)
      #          if wert < waterWert+distanz:
      #              waterWert=wert+distanz;waterZiel=enemyId
      #  
      #  maxBomb=0
      #  for key in dict(sorted(feldBombDict.items(), key=lambda x: x[1],reverse=True)):
      #      maxBomb = feldBombDict[key]
      #      break
      #  for zielBomb,anzahlE in feldBombDict.items():
      #      distanz = getDistanz(agent.xy,zielBomb)
      #      if anzahlE == maxBomb:
      #          if distanz <= 4 and anzahlE > waterBomb:
      #              xB,yB = getXY(zielBomb);waterBomb=anzahlE
      #              move=""
      #          else:
      #              move = moveRichtung(agent.xy,zielBomb,moveList,feldDict)

         
        if len(move) > 0:
            tempMoveList.append(agent.xy);agent.xy = move
         #   tempMoveList.remove(move);agent.xy = move
            xZ,yZ=getXY(move)
            if waterBomb > 0:            
                print("{};MOVE {} {};THROW {} {}".format(agentId,xZ,yZ,xB,yB))
            elif shooter > -1:
                print("{};MOVE {} {};SHOOT {}".format(agentId,xZ,yZ,shooter))
            else:
                print("{};MOVE {} {};HUNKER_DOWN".format(agentId,xZ,yZ))
        else:
            if waterBomb > 0:
                print("{};THROW {} {}".format(agentId,xB,yB))
            elif shooter > -1:
                print("{};SHOOT {}".format(agentId,shooter))
            else:
                print("{};HUNKER_DOWN".format(agentId))


    break
#for i in range(1):
#    #aktion = sucheZug(feldDict,runde,i,required_actions_count,myProtList,oppProtList,moveList,ergDict,sporeZiel)
#    print("{} {} {} {} {} {}".format(aktion[0],aktion[1],aktion[2],aktion[3],aktion[4],aktion[5]))
#    print("sporeList={}".format(sporeZiel),file=sys.stderr)
