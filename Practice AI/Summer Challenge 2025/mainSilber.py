import sys,math,copy

def initMap(feldDict,moveList,wallDict,agentGrundDict,graph,agentDict,myList,enemyList):
    runde=0;my_player=0
    pfad='C:\\Users\\marku\\Python\\codingame\\Practice AI\\Summer Challenge 2025\\'+'eingabe'+'.txt'
    eingabe = open(pfad,'r')
    for zeile in eingabe:
        if zeile[0:4] == "my_player":
            my_player=int(zeile[10:11])

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
            agentDict[tabList[0]]=Agent(tabList[0],tabList[1],tabList[2],tList[0],tList[1],tList[2],tList[3],tabList[3],tabList[4],tabList[5])
            if tList[0] == my_player:
                myList.append(tabList[0])
            else:
                enemyList.append(tabList[0])
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
    return runde,my_player
##########################

class Agent:
    def __init__(self,id,x,y,owner,shoot_cooldown,optimal_range,soaking_power,splash_bombs,cooldown,wetness):
        self.id=id;self.x=x;self.y=y;self.owner=owner;self.shoot_cooldown=shoot_cooldown;self.optimal_range=optimal_range
        self.soaking_power=soaking_power;self.splash_bombs=splash_bombs;self.cooldown=cooldown;self.wetness=wetness
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
def moveRichtung(start,richtung):
    x,y=getXY(start)
    if richtung == "S":
        return setXY(x,y+1)
    if richtung == "N":
        return setXY(x,y-1)
    if richtung == "E":
        return setXY(x+1,y)
    if richtung == "W":
        return setXY(x-1,y)
def bfs_shortest_path(graph, start, goal):
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
        feldBombDict[feld] = anzahl
    feldBombDict = dict(sorted(feldBombDict.items(), key=lambda x: x[1],reverse=True))
    #print(feldBombDict,file=sys.stderr)
#############################
#######
#######
#######
feldDict={};moveList=[];ergDict={};wallDict={};agentGrundDict={};graph={};agentDict={};myList,enemyList=[],[]
runde,my_player=initMap(feldDict,moveList,wallDict,agentGrundDict,graph,agentDict,myList,enemyList)
feldWertDict={};feldBombDict={}


setfeldWertDict(feldDict,agentDict,feldWertDict,my_player,wallDict)
setfeldBombDict(feldDict,agentDict,feldBombDict,my_player,wallDict,enemyList)
tempMoveList = moveList[:]
for id in agentDict:
    agent = agentDict[id]
    tempMoveList.remove(agent.xy)
while True:
    for i in range(len(myList)):
        ## ab hier kopieren
        agentId=myList[i]
        agent=agentDict[agentId];xZ,yZ,enemy=0,0,0
        move='';artW=0
        for feld in graph[setXY(agent.x,agent.y)]:
            if feldWertDict[feld][0] > artW:
                artW=feldWertDict[feld][0];move=feld
 

        distEnemy=999;waterZiel=enemyList[0];waterWert=999
        for enemyId in enemyList:
            eAgent=agentDict[enemyId]
            distanz=getDistanz(setXY(agent.x,agent.y),setXY(eAgent.x,eAgent.y))
            if distanz <= 6:
                wert = dazwischen(eAgent.xy,agent.xy,wallDict,feldDict)
                if wert < waterWert+distanz:
                    waterWert=wert+distanz;waterZiel=enemyId
        
        waterBomb=0;xB=0;yB=0;maxBomb=0
        for key in dict(sorted(feldBombDict.items(), key=lambda x: x[1],reverse=True)):
            maxBomb = feldBombDict[key]
            break
        for zielBomb,anzahlE in feldBombDict.items():
            distanz = getDistanz(agent.xy,zielBomb)
            if anzahlE == maxBomb:
                if distanz <= 4 and anzahlE > waterBomb:
                    xB,yB = getXY(zielBomb);waterBomb=anzahlE
                    move=""
                else:
                    richtung = getRichtung(agent.xy,zielBomb)
                    move = moveRichtung(agent.xy,richtung)

        if len(move) > 0:
            xZ,yZ=getXY(move) 
        if len(move) > 0 and move in tempMoveList and waterBomb > 0:            
            print("{};MOVE {} {};THROW {} {}".format(agentId,xZ,yZ,xB,yB))
        else:
            if len(move) > 0 and move in tempMoveList: 
                print("{};MOVE {} {}".format(agentId,xZ,yZ))                
            else:
                print("{};THROW {} {}".format(agentId,xB,yB))
                #print("{};SHOOT {}".format(agentId,waterZiel))
    break
#for i in range(1):
#    #aktion = sucheZug(feldDict,runde,i,required_actions_count,myProtList,oppProtList,moveList,ergDict,sporeZiel)
#    print("{} {} {} {} {} {}".format(aktion[0],aktion[1],aktion[2],aktion[3],aktion[4],aktion[5]))
#    print("sporeList={}".format(sporeZiel),file=sys.stderr)
