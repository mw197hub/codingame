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

def setBeacon(actions,y,z):
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
    resourceList=[];myZielDict={};oppZielDict={}
    for cId,cell in cellDict.items():
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
    return resourceList,myZielDict,oppZielDict

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

def getActions(cellDict,myBaseList,oppBaseList,resourceList,myZielDict,oppZielDict):
    myAnts,oppAnts,sumCry,sumEgg=getAntsCryEgg(cellDict)
    actions=[] # BEACON y z;LINE x y z
    cellLaenge=0
    for myXY in sorted(myZielDict.items(), key=lambda kv: len(kv[1][0])):
        weg=myXY[1]
        start,ziel = getXY(myXY[0]);oppLaenge=cellDict[ziel].distOpp[0]
        if cellDict[ziel].resource > 0 and len(weg[0])-1 <= oppLaenge and cellDict[ziel].type == 1:
            actions=setLine(actions,start,ziel,1)
            cellLaenge+=len(weg[0])
        if cellLaenge > 0 and myAnts / cellLaenge < 2:
            break
    if len(actions) <= 1:
        for myXY in sorted(myZielDict.items(), key=lambda kv: len(kv[1][0])):
            weg=myXY[1]
            start,ziel = getXY(myXY[0]);oppLaenge=cellDict[ziel].distOpp[0]
            if cellDict[ziel].resource > 0 and len(weg[0])-1 <= oppLaenge and cellDict[ziel].type == 2:
                actions=setLine(actions,start,ziel,1)
                cellLaenge+=len(weg[0])
            if cellLaenge > 0 and myAnts / cellLaenge < 1:
                break
    if len(actions) <= 1:
        for myXY in sorted(myZielDict.items(), key=lambda kv: len(kv[1])):
            start,ziel = getXY(myXY[0])
            if cellDict[ziel].resource > 0 and cellDict[ziel].type == 2:
                actions=setLine(actions,start,ziel,1)
                cellLaenge+=len(weg[0])
            if cellLaenge > 0 and myAnts / cellLaenge < 1:
                break

    return actions

################################## 2 ##

cellDict={};myBaseList=[];oppBaseList=[]
initMap("input1",cellDict,myBaseList,oppBaseList)
####

resourceList,myZielDict,oppZielDict=getResourceDist(cellDict,myBaseList,oppBaseList)
#print(cellDict[26])
print(myZielDict)
runde=0;actions=[]
while True:
    actions = getActions(cellDict,myBaseList,oppBaseList,resourceList,myZielDict,oppZielDict)
    print(';'.join(actions) if len(actions) > 0 else 'WAIT')

    runde+=1
    if runde > 0:
        break
