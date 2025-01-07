import sys,math,copy,time

def initMap(feldDict,moveList,sporeZiel):
    runde=0;required_actions_count=0;myProtList=[];oppProtList=[];myRootIdList=[]
    pfad='C:\\Users\\marku\\Python\\codingame\\Practice AI\\Winter Challenge 2024\\'+'input'+'.txt'
    eingabe = open(pfad,'r')
    for zeile in eingabe:
        #print(zeile[:-1])        
        if len(zeile) > 4:
            zeile=zeile[:-1]
            if zeile[0:4] == 'rund':
                zList = zeile.split(";");zL = zList[0].split("=");runde = int(zL[1])
                zL=zList[1].split("=");required_actions_count=int(zL[1])
                zL=zList[2].split("=");zW=zL[1][1:-1].split(", ")
                for w in zW:
                    myProtList.append(int(w))
                zL=zList[3].split("=");zW=zL[1][1:-1].split(", ")
                for w in zW:
                    oppProtList.append(int(w))
            else:
                if zeile[0:4] == "move":
                    zL=zeile.split("=");zL=zL[1][1:-1].split(", ")
                    for z in zL:
                        moveList.append(z[1:-1])
                if zeile[0:4] == "feld":
                    zList = zeile.split(" ")
                    owner=zList[0].split(":");owner=int(owner[1])
                    xy=zList[1].split(":");x,y=getXY(xy[1])
                    typ=zList[2].split(":");typ=typ[1]
                    organ_id=zList[3].split(":");organ_id=int(organ_id[1])
                    organ_dir=zList[4].split(":");organ_dir=organ_dir[1]
                    organ_parent_id=zList[5].split(":");organ_parent_id=int(organ_parent_id[1])
                    organ_root_id=zList[6].split(":");organ_root_id=int(organ_root_id[1])
                    feldDict[setXY(x,y)]  = Feld(x,y,typ,owner,organ_id,organ_dir,organ_parent_id,organ_root_id)
                if zeile[0:4] == "spor":
                    zL=zeile.split("=");zL=zL[1][1:-1].split("]")                    
                    for zT in zL:
                        tList=[]
                        if len(zT) > 3:
                            zT1 = zT.split(", ")
                            for z in zT1:
                                if '[' in z:
                                    tList.append(z[2:-1])
                                elif ']' in z:
                                    tList.append(z[1:-2])
                                else:
                                    tList.append(z[1:-1])
                            if len(tList) > 0:
                                sporeZiel.append(tList[:])
                if zeile[0:6] == "myRoot":
                    zL=zeile.split("=");zW=zL[1][1:].split(", ")
                    for w in zW:
                        if len(w) > 1:
                            myRootIdList.append(int(w[:-1]))
                        else:
                            myRootIdList.append(int(w))
    eingabe.close()

    return runde,required_actions_count,myProtList,oppProtList,myRootIdList
##########################

class Feld:
    def __init__(self,x,y,typ,owner,organ_id,organ_dir,organ_parent_id,organ_root_id):
        self.id=id;self.x=x;self.y=y;self.typ=typ;self.owner=owner;self.organ_id=organ_id
        self.organ_dir=organ_dir;self.organ_parent_id=organ_parent_id;self.organ_root_id=organ_root_id
    def __str__(self) -> str:
        return ("owner:{} xy:{} type:{} id:{} dir:{} parendId:{} rootId:{}".format(self.owner,str(self.x)+"-"+str(self.y),self.typ,self.organ_id,self.organ_dir,self.organ_parent_id,self.organ_root_id))

def setXY(x,y):
    return str(x)+"-"+str(y)
def getXY(xy):
    x,y=xy.split("-")
    return int(x),int(y)
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
def pruefeNachbar(xy,feldDict,sTyp):
    x,y=getXY(xy)
    for xyN in [setXY(x+1,y),setXY(x-1,y),setXY(x,y+1),setXY(x,y-1)]:
        if xyN in feldDict:
            if feldDict[xyN].typ == sTyp and feldDict[xyN].owner == 1:
                return True
    return False
def freieNachbarn(xy,feldDict,moveList):
    freieN=0
    x,y=getXY(xy)
    for xyN in [setXY(x+1,y),setXY(x-1,y),setXY(x,y+1),setXY(x,y-1)]:
        if xyN in feldDict:
            if feldDict[xyN].owner < 1:
                freieN+=1
        elif xyN in moveList:
            freieN+=1
    return freieN
def pruefeGegner(xy,feldDict,moveList):
    gegnerAbstand = 99; gegnerRichtung = "N"
    x,y=getXY(xy)
    for richtung in ['E','W','N','S']:
        xN=x;yN=y
        for i in range(2):            
            if richtung == 'E':
                xN+=1
            if richtung == 'W':
                xN-=1
            if richtung == 'N':
                yN-=1
            if richtung == 'S':
                yN+=1
            xyN=setXY(xN,yN)
            if xyN in feldDict and feldDict[xyN].owner == 0 and i < gegnerAbstand:
                gegnerAbstand = i; gegnerRichtung=richtung
                break
            if not xyN in moveList:
                break
    return gegnerAbstand, gegnerRichtung
def bfs_shortest_path(graph, start, goal,sucheTiefe):
    tiefe=0
    explored = []
    queue = [[start]] 
    if start == goal:
        return [] # start ist ziel
    while queue:        
        path = queue.pop(0)
        if len(path) >= sucheTiefe:
            return []
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path
            explored.append(node)
    return [] # "So sorry, but a connecting path doesn't exist :("
def setInGraph(feldDict,graph,mList,xy,ownList):
    if xy in feldDict:
        feld = feldDict[xy]
        if feld.owner in ownList:
            mList.append(xy)
    else:
        mList.append(xy)
def setGraph(zielDict,moveDict,myList,protList,moveList,feldDict,oppList,toteFelderList):
    graph={};removeList=[];hilfsMoveList=[]
    for xy in moveList:
        if xy in feldDict:
            feld = feldDict[xy]
            if feld.typ in ["A","B","C","D"]:
                if pruefeNachbar(xy,feldDict,"HARVESTER"):
                    removeList.append(xy);hilfsMoveList.append(xy)
    ### pruefe Tentakel
    if myProtList[1] > 0 and myProtList[2] > 1:
        for xy in moveList:
            mList=[]
            x,y=getXY(xy)
            if setXY(x+1,y) in moveList:
                setInGraph(feldDict,graph,mList,setXY(x+1,y),[0,-1])            
            if setXY(x-1,y) in moveList:
                setInGraph(feldDict,graph,mList,setXY(x-1,y),[0,-1])
            if setXY(x,y+1) in moveList:
                setInGraph(feldDict,graph,mList,setXY(x,y+1),[0,-1])
            if setXY(x,y-1) in moveList:
                setInGraph(feldDict,graph,mList,setXY(x,y-1),[0,-1])
            graph[xy]=mList[:]
        for my in myList:            
            zDict={}
            if my in graph and len(graph[my]) > 0:
                for opp in oppList:
                    xM,yM=getXY(my);xO,yO=getXY(opp)
                    if abs(xM-xO)+abs(yM-yO) < 4:
                        erg = bfs_shortest_path(graph, my, opp,4)
                        if len(erg) > 1 and not erg[1] in oppList and not erg[1] in toteFelderList:
                            gegnerRichtung = getRichtung(erg[1],erg[2])
        #gegnerAbstand, gegnerRichtung = pruefeGegner(zielXY,feldDict,moveList)
        #if gegnerAbstand < 9:  
                            return my,erg[1],len(erg)-1,erg[1],"TENTACLE",gegnerRichtung
    #######
    graph.clear()
    for remove in removeList:
        moveList.remove(remove)
    for xy in moveList:
        mList=[]
        x,y=getXY(xy)
        if setXY(x+1,y) in moveList:
            setInGraph(feldDict,graph,mList,setXY(x+1,y),[-1])            
        if setXY(x-1,y) in moveList:
            setInGraph(feldDict,graph,mList,setXY(x-1,y),[-1])
        if setXY(x,y+1) in moveList:
            setInGraph(feldDict,graph,mList,setXY(x,y+1),[-1])
        if setXY(x,y-1) in moveList:
            setInGraph(feldDict,graph,mList,setXY(x,y-1),[-1])
        graph[xy]=mList[:]
        #print(graph,file=sys.stderr)
    laenge=100;ziel="";start="";weg=[];moveXY=""
    if len(protList) > 0:                
        for my in myList:            
            zDict={}
            if my in graph and len(graph[my]) > 0:
                for prot in protList:
                    erg = bfs_shortest_path(graph, my, prot,8)
                    if len(erg) > 0:
                        zDict[prot] = erg[:]
                        if len(erg)-1 < laenge and laenge > 1 and not erg[1] in feldDict:
                            laenge=len(erg)-1;ziel=prot;start=my;weg=erg[:]
            moveDict[my] = copy.deepcopy(zDict)
       # for prot in protList:
       #     zDict={}
       #     for my in myList:
       #         erg = bfs_shortest_path(graph, prot, my)
       #         zDict[my] = erg[:]
       #     zielDict[prot] = copy.deepcopy(zDict)
        if len(weg) > 1:
            moveXY=weg[1]

    if len(protList) == 0 or len(weg) == 0:
        for my in myList:
            if my in graph and len(graph[my]) > 0:
                for gr in graph[my]:
                    if gr not in feldDict:
                        start=my;moveXY=gr;ziel=gr;weg.append(start);laenge=1
        if len(weg) == 0 and len(hilfsMoveList) > 0:
            freie=0
            for hilfsM in hilfsMoveList:                
                freieN= freieNachbarn(hilfsM,feldDict,moveList)
                if freieN > freie:
                    freie=freieN;moveXY = hilfsM;ziel=hilfsM
                    x,y = getXY(hilfsM)
                    for xN,yN in [[1,0],[-1,0],[0,1],[0,-1]]:
                        xyN = setXY(x+xN,y+yN)
                        if xyN in feldDict and feldDict[xyN].owner == 1:
                            start=xyN;weg.append(start);laenge=1
        if len(weg) == 0:
            for my in myList:
                if my in graph and len(graph[my]) > 0:
                    for gr in graph[my]:
                        if feldDict[gr].owner == -1:
                            start=my;moveXY=gr;ziel=gr;weg.append(start);laenge=1

    return start,moveXY,laenge,ziel,"BASIC","N"

def pruefeSporer(startXY, zielXY,richtung,moveDict,myList,protList,moveList,feldDict,oppList,sporeZiel,myRootId):
    setzeSporer=False; organSP="BASIC"; zielXYSP=zielXY;richtungSP=richtung;rootId=myRootId
    umgebungFrei=0;reichweiteZiel=0                            
    
    for ri in [[1,0],[-1,0],[0,1],[0,-1]]:
        xS,yS = getXY(zielXY);reichweite=0
        for i in range(15):            
            xyS=setXY(xS+ri[0],yS+ri[1])
            owner = -1
            if xyS in feldDict:
                owner = feldDict[xyS].owner
            if not xyS in moveList or owner >= 0:
                break
            reichweite+=1
            xS+=ri[0];yS+=ri[1]
        xyS=setXY(xS,yS)
        xyS2=setXY(xS+ri[0],yS+ri[1])
        if (xyS in feldDict and feldDict[xyS].owner == -1) or (xyS2 in feldDict and feldDict[xyS2].owner == 0):
            reichweite-=1;xS-=ri[0];yS-=ri[1]
        if reichweite > 3:
            richtungN = getRichtung(zielXY,setXY(xS,yS))
            freiU=0
            for fN in [[1,0],[-1,0],[0,1],[0,-1]]:
                if setXY(xS+fN[0],yS+fN[1]) in moveList:
                    freiU+=1
            if freiU > umgebungFrei:
                sporeZiel.clear();umgebungFrei=freiU
                organSP="SPORER";richtungSP=richtungN
                sporeZiel.append([zielXY,setXY(xS,yS),str(rootId)])
    return organSP,zielXYSP,richtungSP

def setzeSpore(zielDict,moveDict,myList,protList,moveList,feldDict,oppList,sporeZiel,myRootId):
    startXY=sporeZiel[0][0];zielXY=sporeZiel[0][1]
    xM,yM = getXY(sporeZiel[0][0])
    xP,yP = getXY(sporeZiel[0][1])
    richtung=getRichtung(sporeZiel[0][0],sporeZiel[0][1])
    xZ=1;yZ=1
    if xP==xM:
        xZ=0;yZ=2
    if yP==yM:
        xZ=2;yZ=0
    if richtung == "E":
        xZ=xP-xZ
        yZ = yP-yZ if yP > yM else yP+yZ
    actionList=["SPORE",feldDict[sporeZiel[0][0]].organ_id,xZ,yZ," "," "]
    sporeZiel.pop(0)
    return "SPORE",startXY,zielXY," "," "

################
def sucheZug(feldDict,runde,i,required_actions_count,myProtList,oppProtList,moveList,lastAktionDict,sporeZiel,myRootId):
    actionList=[]  # ["GROW","1","14","2","BASIC"]
    direktionFeld={"E":[1,0],"W":[-1,0],"N":[0,-1],"S":[0,1]};toteFelderList=[]
    aktion="GROW";richtung="N";organ="BASIC";anzahlRoots=[]
    myList=[];oppList=[];protList=[];zielDict={};moveDict={}
    for xy, feld in feldDict.items():
        if feld.owner ==1 and not feld.organ_root_id in anzahlRoots:
            anzahlRoots.append(feld.organ_root_id)
        if feld.owner == 1 and feld.organ_root_id == myRootId:
            myList.append(xy)
        if feld.owner == 0:
            oppList.append(xy)
            if feld.typ == "TENTACLE":
                direktion = direktionFeld[feld.organ_dir]
                xD,yD=getXY(xy)
                xyD=setXY(xD+direktion[0],yD+direktion[1])
                if xyD in moveList:
                    toteFelderList.append(xyD)

        if feld.typ in ["A","B","C","D"]:
            if not pruefeNachbar(xy,feldDict,"HARVESTER"):
                protList.append(xy)

    startXY,zielXY,abstand,zielProt,organ,richtung = setGraph(zielDict,moveDict,myList,protList,moveList,feldDict,oppList,toteFelderList)

    if organ == "BASIC" and abstand == 2 and feldDict[zielProt].typ in ["A","B","C","D"] and myProtList[2] > 0 and myProtList[3] > 0:
        organ="HARVESTER";richtung=getRichtung(zielXY,zielProt)       
    
    ## Sporer and Spore
    if len(sporeZiel) > 0 and int(sporeZiel[0][2]) == myRootId:
        aktion,startXY,zielXY,organ,richtung = setzeSpore(zielDict,moveDict,myList,protList,moveList,feldDict,oppList,sporeZiel,myRootId)        
    else:
        if len(anzahlRoots) < 2:
            if myProtList[1] > 1 and myProtList[3] > 2 and organ =="BASIC" and len(sporeZiel) == 0:
                organ, zielXY,richtung = pruefeSporer(startXY, zielXY,richtung,moveDict,myList,protList,moveList,feldDict,oppList,sporeZiel,myRootId)

    if len(zielXY) < 1:
        actionList=['WAIT']
    else:
        x,y=getXY(zielXY)

        if myProtList[0] == 0 and organ =="BASIC":
            if myProtList[1] > 0 and myProtList[2] > 1:
                organ="TENTACLE";richtung=getRichtung(zielXY,zielProt) 
            elif myProtList[1] > 0 and myProtList[3] > 1:
                organ="SPORER";richtung=getRichtung(zielXY,zielProt)
            elif myProtList[2] > 0 and myProtList[3] > 0:
                organ="HARVESTER";richtung=getRichtung(zielXY,zielProt)
            
        actionList=[aktion, str(feldDict[startXY].organ_id), str(x),str(y),organ,richtung]
                
####
    if runde in lastAktionDict:
        tList = lastAktionDict[runde]
        tList.append(copy.deepcopy(actionList))
    else:
        tList = copy.deepcopy(actionList) 
    lastAktionDict[runde] = copy.deepcopy(tList)
    return actionList

#######
#######
#######
startZeit=time.time()
feldDict={};moveList=[];lastAktionDict={};sporeZiel=[];myRootIdList=[]
runde,required_actions_count,myProtList,oppProtList,myRootIdList =initMap(feldDict,moveList,sporeZiel)
#print(feldDict,file=sys.stderr)
for i in range(len(myRootIdList)):
    aktion = sucheZug(feldDict,runde,i,required_actions_count,myProtList,oppProtList,moveList,lastAktionDict,sporeZiel,myRootIdList.pop(0))
    print("{} {} {} {} {} {}".format(aktion[0],aktion[1],aktion[2],aktion[3],aktion[4],aktion[5]))
    print("sporeList={}".format(sporeZiel),file=sys.stderr)
    #print("lastAktionDict={}".format(lastAktionDict),file=sys.stderr)
####
print("Zeit: {}".format(time.time()-startZeit),file=sys.stderr)
