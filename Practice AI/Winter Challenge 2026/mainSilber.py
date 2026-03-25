import sys,math,copy

my_id=0;width=0;height=0
richtungList={'UP':['UP','RIGHT','LEFT'],'DOWN':['DOWN','RIGHT','LEFT'],'LEFT':['DOWN','LEFT','UP'],'RIGHT':['DOWN','UP','RIGHT']}

def setXY(x,y):
    return str(x)+"-"+str(y)
def getXY(xy):
    hList=xy.split("-")
    return int(hList[0]),int(hList[1])
def getRichtungWerte(richtung):
    richtDict={'UP':[0,-1],"DOWN":[0,+1],"LEFT":[-1,0],"RIGHT":[1,0]}
    return richtDict[richtung]
def getRichtung(start,ziel):
    x1,y1=getXY(start);x2,y2=getXY(ziel)
    if x1 > x2:
        return "LEFT"
    if x1 < x2:
        return "RIGHT"
    if y1 > y2:
        return "DOWM"
    return "UP"

def initMap(graph,myDict,oppDict,moveList,powerList,snakeDict,feldList):
    runde=0
    pfad='C:\\Users\\marku\\Python\\codingame\\Practice AI\\Winter Challenge 2026\\'+'eingabe'+'.txt'
    eingabe = open(pfad,'r')
    for zeile in eingabe:
        zeile = zeile[:-1]
        if zeile[0:5] == "runde":
            runde=int(zeile[6:7])
        if zeile[0:5] == "my_id":
            wertList=zeile.split(";")
            my_id=int(wertList[0][-1])
            hList=wertList[1].split("=");width=int(hList[1])
            hList=wertList[2].split("=");height=int(hList[1])
            hList=wertList[3][7:-1].split(",")
            for h in hList:
                myDict[int(h[1:2])] = h[h.find("'")+1:-1]
            hList=wertList[4][8:-1].split(",")
            for h in hList:
                oppDict[int(h[1:2])] = h[h.find("'")+1:-1]        
        if zeile[0:5] == "rowLi":
            hList=zeile[8:-1].split(",")
            rowList=[]
            for h in hList:
                rowList.append(h[2:-1])
            for y in range(len(rowList)):
                for x in range(len(rowList[0])):
                    if rowList[y][x] == ".":
                        moveList.append(setXY(x,y))
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
        if zeile[0:5] == "power":
            hList=zeile[10:-1].split(",")
            for h in hList:
                powerList.append(h[2:-1])
        if zeile[0:5] == "snake":
            hList=zeile[9:-2].split("]")
            for h in hList:
                pos=h.find(":");zList=[];aList=h[pos+2:].split(",")
                for a in aList:
                    zList.append(a[2:-1])
                snakeDict[int(h[2:pos])]=zList[:]
    feldList = copy.deepcopy(moveList)                
    for snake,bodyList in snakeDict.items():
        for body in bodyList:
            moveList.remove(body)
    return runde   
######################################init################
###########################################################
############################################################
def suchePath(graph, start, goal,snakeBody,richtung,moveList):
    explored = [];queue = [[start]];lauf=0 
    if start == goal:
        return [] # start ist ziel
    while queue:
        path = queue.pop(0);node = path[-1]
        if node not in explored and node in moveList:
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
def powerErreichbar(graph,powerList,moveList,snakeDict):
    snakeL=[]
    for sn,sL in snakeDict.items():
        for s in sL:
            snakeL.append(s)  
    powerErDict={}
    for power in powerList:
        besucht=[];offen=[];abstand=0;startList=[]
        offen.append(power)
        while offen:
            aktuell = offen.pop(0);besucht.append(aktuell);zList=[]
            for neighbours in graph[aktuell]:  
                if not neighbours in besucht and not neighbours in offen:                              
                    x,y=getXY(neighbours)
                    if setXY(x,y-1) in moveList or y-1 < 0:                        
                        offen.append(neighbours)
                    if not setXY(x,y+1) in moveList and not setXY(x,y+1) in snakeL:
                        startList.append(neighbours)          
            abstand+=1     
            if abstand > 60:
                break
        powerErDict[power] = copy.deepcopy(startList)
    return powerErDict      
def sucheRichtung(start,richtung,graph,powerList,moveList,mRichtungen,snakeLen,powerErDict,snakeBody):
    newRichtung="";power=False;posSave="";mWege =0;mrList=[];mrSave=""
    for mR in mRichtungen:
        xV,yV=getRichtungWerte(mR);x,y=getXY(start)
        xN=x+xV;yN=y+yV;newPos=setXY(xN,yN)
        if newPos in graph:
            mWege=len(graph[newPos])
        else:
            mWege =0
        if newPos in moveList and not power and mWege > 1:
            newRichtung=mR;mrList.append(mR)
            if newPos in powerList:
                power=True;posSave=newPos;mrSave=mR
    if not power:
        erreichbarDict={};distMin=99;distP=0;nearPos="";dist=99;newPath=[];savePowerXY=""    
        for powerXY,powerL in powerErDict.items():
            distP = getDistanz(powerXY,snakeBody[-1])
            if distP < 10:
                if distP < distMin:
                    distMin=distP;savePowerXY=powerXY
                zList=[]
                for p in powerL:
                    dist = getDistanz(powerXY,p)
                    if dist <= snakeLen:
                        zList.append(p)
                if len(zList) > 0:
                    erreichbarDict[powerXY] = zList[:]
        if len(savePowerXY) > 0:
            moveR = getRichtung(start,savePowerXY)
            if moveR in mrList:
                newRichtung=moveR
        

      #  for powerXY,erreichbarList in erreichbarDict.items():            
      #      path = suchePath(graph,start,powerXY,snakeBody,richtung,moveList)
      #      if len(path) > 0 and len(path) < dist:
      #          newPath = path[:];dist=len(path)
      #          savePowerXY=powerXY
      #  if len(savePowerXY) > 0:
      #      powerErDict.pop(savePowerXY)
      #      moveR = getRichtung(start,newPath[1])
      #      if moveR in mrList and newPath[1] in moveList:
      #          newRichtung = moveR; posSave=newPath[1]
    else:
        newRichtung = mrSave                
    if posSave in moveList:
        moveList.remove(posSave)
    return newRichtung

def bewegung(runde,graph,myDict,oppDict,moveList,powerList,snakeDict,ergList,powerErDict):
    ergList.clear()
    if len(powerErDict) == 0:
        powerErDict= powerErreichbar(graph,powerList,moveList,snakeDict)
    else:
        remList=[]
        for powerP in powerErDict:
            if not powerP in powerList:
                remList.append(powerP)
        for rem in remList:
            powerErDict.pop(rem)
    
    for my,richtung in myDict.items():
        start=snakeDict[my][0]
        newRichtung=sucheRichtung(start,richtung,graph,powerList,moveList,richtungList[richtung],len(snakeDict[my]),powerErDict,snakeDict[my])
        if len(newRichtung) > 0:
            ergList.append([my,newRichtung])
            myDict[my]=newRichtung


def removeMyOppList(snakeDict,myDict,oppDict):
    newDict={};sList=[]
    for snake in snakeDict:
        sList.append(snake)
    for my,wert in myDict.items():
        if my in sList:
            newDict[my]=wert
    myDict.clear();myDict = copy.deepcopy(newDict);newDict.clear()
    for opp,wert in oppDict.items():
        if opp in sList:
            newDict[opp]=wert
    oppDict.clear();oppDict = copy.deepcopy(newDict) 
    return myDict,oppDict
#################
#################
#################

graph={};myDict={};oppDict={};moveList=[];powerList=[];snakeDict={};ergList=[];feldList=[];powerErDict={}
runde=initMap(graph,myDict,oppDict,moveList,powerList,snakeDict,feldList)

myDict,oppDict = removeMyOppList(snakeDict,myDict,oppDict)

while True:
    bewegung(runde,graph,myDict,oppDict,moveList,powerList,snakeDict,ergList,powerErDict)
    
    if len(ergList) == 0:
        print("WAIT")
    else:
        ausgabe=""
        for erg in ergList:
            ausgabe+=str(erg[0]) +" "+erg[1]+";"
        print(ausgabe[:-1])

    
    print(runde)
    break