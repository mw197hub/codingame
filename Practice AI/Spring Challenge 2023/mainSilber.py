# https://www.codingame.com/ide/challenge/spring-challenge-2023
import math,sys,copy

def initMap(name,cellDict,myBaseList,oppBaseList):
    pfad='C:\\Users\\marku\\Python\\codingame\\Practice AI\\Spring Challenge 2023\\'+name+'.txt'
    print(pfad)
    eingabe = open(pfad,'r')
    for zeile in eingabe:
        if zeile[0:4]=="cell":
            ccList = zeile[5:].split(";")
            for i in range(len(ccList)-1):
                cList = ccList[i]
                c = cList.split(",")
                cellDict[i]=Cell(i,int(c[0]),int(c[1]),[int(c[2]),int(c[3]),int(c[4]),int(c[5]),int(c[6]),int(c[7])])
        if zeile[0:4] == "myBa":
            rList = (zeile[7:-2]).split(",")
            for r in rList:
                myBaseList.append(int(r))
        if zeile[0:4] == "oppB":
            rList = (zeile[8:-2]).split(",")
            for r in rList:
                oppBaseList.append(int(r))
        if zeile[0:4] == "ants":
            aList = zeile[5:-2].split(",")
            for a in aList:
                wList = a.split(":")
                if int(wList[1]) > 0:
                    cellDict[int(wList[0])].myAnts = int(wList[1])
                else:
                    cellDict[int(wList[0])].oppAnts = int(wList[1]) *-1
################################## 0 ##

def nachbarUmstellen(cId,cell,cellDict):
    nList = []
    for n in cell.nachbarList:
        if n > -1 and cellDict[n].type == 1:
            nList.append(n)
    for n in cell.nachbarList:
        if n > -1 and cellDict[n].type == 2:
            nList.append(n)
    for n in cell.nachbarList:
        if n > -1 and cellDict[n].type == 0:
            nList.append(n)
        if n == -1:
            nList.append(n)
    cell.nachbarList = copy.deepcopy(nList)

def setBeacon(actions,y,cellDict,ziele):
    z = 1
    if cellDict[y].oppAnts > cellDict[y].myAnts:
        z = 2
   #    if y in ziele:
   #        z += 3
    actions.append("BEACON {} {}".format(y,z))
    return actions
def setLine(actions,x,y,z):
    actions.append("LINE {} {} {}".format(x,y,z))
    return actions

def setXY(x,y):
    return str(x)+"-"+str(y)
def getXY(xy):
    xyList = xy.split("-")
    return(int(xyList[0]),int(xyList[1]))

def sucheWeg(start,goal,cellDict):
    if start == 25 and goal == 31:
        a=0
    explored = []
    queue = [[start]] 
    wegList=[];ende=999
    if start == goal:
        return "That was easy! Start = goal"
    while queue:
        path = queue.pop(0)
        node = path[-1]        
        if node > -1 and node not in explored:
            neighbours = cellDict[node].nachbarList
            for neighbour in neighbours:
                if neighbour > -1: 
                    new_path = list(path)
                    new_path.append(neighbour)
                    if len(new_path) <= ende:
                        queue.append(new_path)
                        if neighbour == goal:
                            ende=len(new_path)
                            wegList.append(copy.deepcopy(new_path))
            explored.append(node)
    if len(wegList) == 0:
        return []
    else:
        return wegList


def getResourceDist(cellDict,myBaseList,oppBaseList):
    resourceList=[];myZielDict={};oppZielDict={};ressourceDict={}
    for cId,cell in cellDict.items():
        nachbarUmstellen(cId,cell,cellDict)
        if (cell.type == 2 or cell.type ==1) and cell.resource > 0:
            resourceList.append(cell.id)
            myL=990;oppL=990
            for i in range(len(myBaseList)):
                wegList = sucheWeg(myBaseList[i],cell.id,cellDict)
            # print("{}-{}:{}".format(myBaseList[i],cell.id,wegList),file=sys.stderr)
                myZielDict[setXY(myBaseList[i],cell.id)]=wegList
                cell.distMy[i] = len(wegList[0])-1
                if myL > len(wegList[0])-1:
                    myL=len(wegList[0])-1
            for i in range(len(oppBaseList)):
                wegList = sucheWeg(oppBaseList[i],cell.id,cellDict)
            # print("{}-{}:{}".format(myBaseList[i],cell.id,wegList),file=sys.stderr)
                oppZielDict[setXY(oppBaseList[i],cell.id)]=wegList
                cell.distOpp[i] = len(wegList[0])-1
                if oppL > len(wegList[0])-1:
                    oppL=len(wegList[0])-1
    for start in resourceList:
        rDict={}
        for ziel in resourceList:
            if not start == ziel:
                wegList = sucheWeg(start,ziel,cellDict)
                rDict[ziel] = wegList
        ressourceDict[start] = copy.deepcopy(rDict)
    return resourceList,myZielDict,oppZielDict,ressourceDict

class Cell:
    def __init__(self,id,type,resource,nachbarList):
        self.id=id;self.type=type;self.resource=resource;self.nachbarList=nachbarList
        self.distMy=[-1,-1,-1,-1,-1];self.distOpp=[-1,-1,-1,-1,-1];self.myAnts=0;self.oppAnts=0
    def __str__(self) -> str:
        return ("{}#{} {} ({}) ({}) ({})".format(self.id,self.type,self.resource,self.nachbarList,self.distMy[0],self.distOpp[0]))
############################ 1  ##

def getAntsCryEgg(cellDict):
    myAnts,oppAnts,sumCry,sumEgg=0,0,0,0
    for cId,cell in cellDict.items():
        if cell.type==1:
            sumEgg+=cell.resource
        if cell.type==2:
            sumCry+=cell.resource
        if cell.myAnts > 0:
            myAnts+=cell.myAnts
        if cell.oppAnts > 0:
            oppAnts+=cell.oppAnts
    print("Summen: myA:{} oppA:{} summCry:{} sumEgg:{}".format(myAnts,oppAnts,sumCry,sumEgg),file=sys.stderr)
    return myAnts,oppAnts,sumCry,sumEgg

####### A ##
def setzeWeg(wegeOri,actions,start,ziel,cellDict,myBaseList,oppBaseList,resourceList,myZielDict,oppZielDict,beaconList,cellLaenge,ziele,ressourceDict):
    wege = copy.deepcopy(wegeOri)
    if ziel == 20:
        a=0
    reDict = ressourceDict[ziel]
    for z in ziele:        
        zWeg = reDict[z]
        if len(wege[0]) > len(zWeg[0]):
            wege = zWeg


    ziele.append(ziel)
    wegX=[];nachbarPunkte=-1
    for weg in wege:
        n2Punkte=0
        for w in weg:            
            if cellDict[w].type > 0 and cellDict[w].resource > 0:
                n2Punkte+=30
            if w in beaconList:
                n2Punkte+=1
            for n in cellDict[w].nachbarList:
                if n > -1 and cellDict[n].type > 0 and cellDict[n].resource > 0:
                    n2Punkte+=2
        if n2Punkte > nachbarPunkte:
            wegX=weg;nachbarPunkte=n2Punkte
    for w in wegX:
        if not w in beaconList:
            actions=setBeacon(actions,w,cellDict,ziele);cellLaenge+=1;beaconList.append(w)
        for n in cellDict[w].nachbarList:
            if n > -1 and cellDict[n].type > 0 and cellDict[n].resource > 0:
                if not n in beaconList:
                    if not n in ziele:
                        ziele.append(n)
                    actions=setBeacon(actions,n,cellDict,ziele);cellLaenge+=1;beaconList.append(n)
    return cellLaenge

def getActions(cellDict,myBaseList,oppBaseList,resourceList,myZielDict,oppZielDict,ressourceDict):
    myAnts,oppAnts,sumCry,sumEgg=getAntsCryEgg(cellDict)
    actions=[] # BEACON y z;LINE x y z
    cellLaenge=0;beaconList=[];ziele=[]

    if len(ziele) <= 1 and myAnts < sumCry / 6:
        for myXY in sorted(myZielDict.items(), key=lambda kv: len(kv[1][0])):
            weg=myXY[1]
            start,ziel = getXY(myXY[0]);oppLaenge=cellDict[ziel].distOpp[0]
            if cellDict[ziel].resource > 0 and len(weg[0])-1 <= oppLaenge and cellDict[ziel].type == 1 and ziel not in ziele:
                cellLaenge=setzeWeg(myXY[1],actions,start,ziel,cellDict,myBaseList,oppBaseList,resourceList,myZielDict,oppZielDict,beaconList,cellLaenge,ziele,ressourceDict)

            if cellLaenge > 0 and ((myAnts / cellLaenge < 3 and runde <= 9) or (runde > 9 and myAnts / cellLaenge < 5)):
                break
    print("Egg 1 Ziele:{}".format(ziele),file=sys.stderr)
    if len(ziele) <= 1:
        for myXY in sorted(myZielDict.items(), key=lambda kv: len(kv[1][0])):
            weg=myXY[1]
            start,ziel = getXY(myXY[0]);oppLaenge=cellDict[ziel].distOpp[0]
            if cellDict[ziel].resource > 0 and len(weg[0])-1 <= oppLaenge and cellDict[ziel].type == 2 and ziel not in ziele:
                cellLaenge=setzeWeg(myXY[1],actions,start,ziel,cellDict,myBaseList,oppBaseList,resourceList,myZielDict,oppZielDict,beaconList,cellLaenge,ziele,ressourceDict)

            if cellLaenge > 0 and ((myAnts / cellLaenge < 3 and runde <= 9) or (runde > 9 and myAnts / cellLaenge < 5)):
                break
    print("Cry 1 Ziele:{}".format(ziele),file=sys.stderr)
    if len(ziele) <= 2 or myAnts//cellLaenge > 5:
        for myXY in sorted(myZielDict.items(), key=lambda kv: len(kv[1])):
            start,ziel = getXY(myXY[0]);weg=myXY[1]
            if cellDict[ziel].resource > 0 and cellDict[ziel].type == 2 and ziel not in ziele:
                cellLaenge=setzeWeg(myXY[1],actions,start,ziel,cellDict,myBaseList,oppBaseList,resourceList,myZielDict,oppZielDict,beaconList,cellLaenge,ziele,ressourceDict)

            if cellLaenge > 0 and myAnts / cellLaenge < 5:
                break
    print("Cry 1 Ziele:{}".format(ziele),file=sys.stderr)       
    if len(ziele) <= 1 or myAnts//cellLaenge > 4:
        for myXY in sorted(myZielDict.items(), key=lambda kv: len(kv[1])):
            start,ziel = getXY(myXY[0]);weg=myXY[1]
            if cellDict[ziel].resource > 0 and cellDict[ziel].type == 1 and ziel not in ziele:
                cellLaenge=setzeWeg(myXY[1],actions,start,ziel,cellDict,myBaseList,oppBaseList,resourceList,myZielDict,oppZielDict,beaconList,cellLaenge,ziele,ressourceDict)

            if cellLaenge > 0 and myAnts / cellLaenge < 5:
                break
    print("Egg 2 Ziele:{}".format(ziele),file=sys.stderr)

    actions.append("MESSAGE Ziele:{}".format(ziele))
    return actions

################################## 2 ##

cellDict={};myBaseList=[];oppBaseList=[]
initMap("input1",cellDict,myBaseList,oppBaseList)
####

resourceList,myZielDict,oppZielDict,ressourceDict=getResourceDist(cellDict,myBaseList,oppBaseList)
#print(cellDict[26])
print(myZielDict)
runde=0;actions=[]
while True:
    actions = getActions(cellDict,myBaseList,oppBaseList,resourceList,myZielDict,oppZielDict,ressourceDict)
    print(';'.join(actions) if len(actions) > 0 else 'WAIT')

    runde+=1
    if runde > 0:
        break
