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

def setzeTypZiele(ziele,cellDict):
    eggsTrue,kristallTrue=False,False
    for z in ziele:
        if cellDict[z].type == 1:
            eggsTrue=True
        if cellDict[z].type == 2:
            kristallTrue=True
    return eggsTrue,kristallTrue

def getAntsCryEgg(cellDict):
    myAnts,oppAnts,sumCry,sumEgg,maxOppAnts=0,0,0,0,0
    optAnzDict={}
    for cId,cell in cellDict.items():
        if cell.type==1:
            sumEgg+=cell.resource
        if cell.type==2:
            sumCry+=cell.resource
        if cell.myAnts > 0:
            myAnts+=cell.myAnts
        if cell.oppAnts > 0:
            oppAnts+=cell.oppAnts
        if cell.myAnts > 0 and cell.oppAnts > 0:
            if cell.oppAnts > 0 and cell.myAnts > 0 and cell.oppAnts > maxOppAnts:
                maxOppAnts = cell.oppAnts
    for i in range(0,201):
         optAnzDict[i] = 0 if i == 0 else  myAnts//i

    print("Summen: myA:{} oppA:{} summCry:{} sumEgg:{}".format(myAnts,oppAnts,sumCry,sumEgg),file=sys.stderr)
    return myAnts,oppAnts,sumCry,sumEgg,optAnzDict,maxOppAnts

####### A ##
def setzeWeg(wegeOri,actions,start,ziel,cellDict,myBaseList,oppBaseList,resourceList,myZielDict,oppZielDict,beaconList,ziele,ressourceDict,optAnzDict,maxOppAnts,xy,zieleXY):
    wege = copy.deepcopy(wegeOri)
    if ziel == 20:
        a=0
    reDict = ressourceDict[ziel]
    for z in ziele:        
        zWeg = reDict[z]
        if len(wege[0]) > len(zWeg[0]):
            wege = zWeg
    wegWertBisher=optAnzDict[len(beaconList)]
    wegWert = optAnzDict[len(wege[0])+len(beaconList)]
    #if (wegWert < 2  or wegWert < maxOppAnts) and len(ziele) > 0:  #1
    if (wegWert < 3) and len(ziele) > 0:
        return 
    zusatzZiel = 0
    for i in range(wegWert,201):
        if optAnzDict[i] == wegWert:
            zusatzZiel+=1

    ziele.append(ziel);zieleXY.append(xy)
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
            actions=setBeacon(actions,w,cellDict,ziele);beaconList.append(w)
        for n in cellDict[w].nachbarList:
            if n > -1 and cellDict[n].type > 0 and cellDict[n].resource > 0:
                if zusatzZiel == 0:
                    break
                if not n in beaconList:
                    if not n in ziele:
                        ziele.append(n)
                        s1,z1=getXY(xy)
                        zieleXY.append(setXY(s1,n))
                    actions=setBeacon(actions,n,cellDict,ziele);beaconList.append(n)
                    zusatzZiel-= 1
                    
    return 

def getActions(cellDict,myBaseList,oppBaseList,resourceList,myZielDict,oppZielDict,ressourceDict,bisherZiele):
    myAnts,oppAnts,sumCry,sumEgg,optAnzDict,maxOppAnts=getAntsCryEgg(cellDict)
    actions=[] # BEACON y z;LINE x y z
    beaconList=[];ziele=[];eggsTrue=False;kristallTrue=False
    zieleXY=[]
  #  for xy in bisherZiele:  #2
  #      start,ziel = getXY(xy);wege=myZielDict[xy]
  #      if cellDict[ziel].resource > 0 and ziel not in ziele:
  #          setzeWeg(myZielDict[xy],actions,start,ziel,cellDict,myBaseList,oppBaseList,resourceList,myZielDict,oppZielDict,beaconList,ziele,ressourceDict,optAnzDict,maxOppAnts,xy,zieleXY)
  #          eggsTrue,kristallTrue=setzeTypZiele(ziele,cellDict)


    #Eier
    if  sumCry > myAnts:
        for myXY in sorted(myZielDict.items(), key=lambda kv: len(kv[1][0])):
            weg=myXY[1];start,ziel = getXY(myXY[0]);oppLaenge=cellDict[ziel].distOpp[0]
            if cellDict[ziel].resource > 0 and cellDict[ziel].type == 1 and ziel not in ziele:
                setzeWeg(myXY[1],actions,start,ziel,cellDict,myBaseList,oppBaseList,resourceList,myZielDict,oppZielDict,beaconList,ziele,ressourceDict,optAnzDict,maxOppAnts,myXY[0],zieleXY)
                eggsTrue,kristallTrue=setzeTypZiele(ziele,cellDict)
    print("Egg 1 Ziele:{}".format(ziele),file=sys.stderr)
    # Kristall
    for myXY in sorted(myZielDict.items(), key=lambda kv: len(kv[1][0])):
        weg=myXY[1];start,ziel = getXY(myXY[0]);oppLaenge=cellDict[ziel].distOpp[0]
        if cellDict[ziel].resource > 0 and cellDict[ziel].type == 2 and ziel not in ziele:            
            setzeWeg(myXY[1],actions,start,ziel,cellDict,myBaseList,oppBaseList,resourceList,myZielDict,oppZielDict,beaconList,ziele,ressourceDict,optAnzDict,maxOppAnts,myXY[0],zieleXY)
            eggsTrue,kristallTrue=setzeTypZiele(ziele,cellDict)
    print("Kristall Ziele:{}".format(ziele),file=sys.stderr)
    #Eier
    if not eggsTrue and not kristallTrue:
        for myXY in sorted(myZielDict.items(), key=lambda kv: len(kv[1][0])):
            weg=myXY[1];start,ziel = getXY(myXY[0]);oppLaenge=cellDict[ziel].distOpp[0]
            if cellDict[ziel].resource > 0 and cellDict[ziel].type == 1 and ziel not in ziele:
                setzeWeg(myXY[1],actions,start,ziel,cellDict,myBaseList,oppBaseList,resourceList,myZielDict,oppZielDict,beaconList,ziele,ressourceDict,optAnzDict,maxOppAnts,myXY[0],zieleXY)
                eggsTrue,kristallTrue=setzeTypZiele(ziele,cellDict)
        print("Eier 2 Ziele:{}".format(ziele),file=sys.stderr)
 

    actions.append("MESSAGE Ziele:{}".format(ziele))
    return actions,copy.deepcopy(zieleXY)

################################## 2 ##

cellDict={};myBaseList=[];oppBaseList=[]
initMap("input1",cellDict,myBaseList,oppBaseList)
####

resourceList,myZielDict,oppZielDict,ressourceDict=getResourceDist(cellDict,myBaseList,oppBaseList)
#print(cellDict[26])
print(myZielDict)
runde=0;actions=[];bisherZiele=['46-32','46-8','46-4','46-2']
while True:
    actions,bisherZiele = getActions(cellDict,myBaseList,oppBaseList,resourceList,myZielDict,oppZielDict,ressourceDict,bisherZiele)
    print(';'.join(actions) if len(actions) > 0 else 'WAIT')

    runde+=1
    if runde > 0:
        break
