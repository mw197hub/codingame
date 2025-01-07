import sys,math,copy

def initMap(feldDict,moveList):
    runde=0;required_actions_count=0;myProtList=[];oppProtList=[]
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
                else:
                    zList = zeile.split(" ")
                    owner=zList[0].split(":");owner=int(owner[1])
                    xy=zList[1].split(":");x,y=getXY(xy[1])
                    typ=zList[2].split(":");typ=typ[1]
                    organ_id=zList[3].split(":");organ_id=int(organ_id[1])
                    organ_dir=zList[4].split(":");organ_dir=organ_dir[1]
                    organ_parent_id=zList[5].split(":");organ_parent_id=int(organ_parent_id[1])
                    organ_root_id=zList[6].split(":");organ_root_id=int(organ_root_id[1])
                    feldDict[setXY(x,y)]  = Feld(x,y,typ,owner,organ_id,organ_dir,organ_parent_id,organ_root_id)
    eingabe.close()

    return runde,required_actions_count,myProtList,oppProtList
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
        return "N"
    if yN < y:
        return "S"
    return richtung
def pruefeNachbar(xy,feldDict,sTyp):
    x,y=getXY(xy)
    for xyN in [setXY(x+1,y),setXY(x-1,y),setXY(x,y+1),setXY(x,y-1)]:
        if xyN in feldDict:
            if feldDict[xyN].typ == sTyp and feldDict[xyN].owner == 1:
                return True
    return False
def bfs_shortest_path(graph, start, goal):
    explored = []
    queue = [[start]] 
    if start == goal:
        return [] # start ist ziel
    while queue:
        path = queue.pop(0)
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
    return "So sorry, but a connecting path doesn't exist :("
def setGraph(zielDict,moveDict,myList,protList,moveList,feldDict,oppList):
    graph={};removeList=[]
    for xy in moveList:
        if xy in feldDict:
            feld = feldDict[xy]
            if  feld.typ == "A":
                if pruefeNachbar(xy,feldDict,"HARVESTER"):
                    removeList.append(xy)
    for remove in removeList:
        moveList.remove(remove)
    for xy in moveList:
        mList=[]
        x,y=getXY(xy)
        if setXY(x+1,y) in moveList:
            mList.append(setXY(x+1,y))
        if setXY(x-1,y) in moveList:
            mList.append(setXY(x-1,y))
        if setXY(x,y+1) in moveList:
            mList.append(setXY(x,y+1))
        if setXY(x,y-1) in moveList:
            mList.append(setXY(x,y-1))
        if len(mList) > 0:
            graph[xy]=mList[:]
        #print(graph,file=sys.stderr)
    laenge=100;ziel="";start="";weg=[];moveXY=""
    if len(protList) > 0:                
        for my in myList:
            zDict={}
            for prot in protList:
                erg = bfs_shortest_path(graph, my, prot)
                zDict[prot] = erg[:]
                if len(erg)-1 < laenge and laenge > 1 and not erg[1] in feldDict:
                    laenge=len(erg)-1;ziel=prot;start=my;weg=erg[:]
            moveDict[my] = copy.deepcopy(zDict)
        for prot in protList:
            zDict={}
            for my in myList:
                erg = bfs_shortest_path(graph, prot, my)
                zDict[my] =len(erg)-1
            zielDict[prot] = copy.deepcopy(zDict)
        moveXY=weg[1]
    else:
        for my in myList:
            if len(graph[my]) > 0:
                for gr in graph[my]:
                    if gr not in feldDict:
                        start=my;moveXY=gr;ziel=gr

    return start,moveXY,laenge,ziel

def sucheZug(feldDict,runde,i,required_actions_count,myProtList,oppProtList,moveList):
    actionList=[]  # ["GROW","1","14","2","BASIC"]
    aktion="GROW";richtung="N";organ="BASIC"
    myList=[];oppList=[];protList=[];zielDict={};moveDict={}
    for xy, feld in feldDict.items():
        if feld.owner == 1:
            myList.append(xy)
        if feld.owner == 0:
            oppList.append(xy)
        if feld.typ == 'A':
            if not pruefeNachbar(xy,feldDict,"HARVESTER"):
                protList.append(xy)
    startXY,zielXY,abstand,zielProt = setGraph(zielDict,moveDict,myList,protList,moveList,feldDict,oppList)
    if abstand == 2 and feldDict[zielProt].typ == "A":
        organ="HARVESTER"
        richtung=getRichtung(zielXY,zielProt)
    

    x,y=getXY(zielXY)
    actionList=[aktion, str(feldDict[startXY].organ_id), str(x),str(y),organ,richtung]
    return actionList

####
feldDict={};moveList=[]
runde,required_actions_count,myProtList,oppProtList =initMap(feldDict,moveList)
#print(feldDict,file=sys.stderr)
for i in range(1):
    aktion = sucheZug(feldDict,runde,i,required_actions_count,myProtList,oppProtList,moveList)
    print("{} {} {} {} {} {}".format(aktion[0],aktion[1],aktion[2],aktion[3],aktion[4],aktion[5]))
####

