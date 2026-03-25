import sys,math,copy
import heapq,time,os

my_id=0;width=0;height=0
richtungList={'UP':['UP','RIGHT','LEFT'],'DOWN':['DOWN','RIGHT','LEFT'],'LEFT':['DOWN','LEFT','UP'],'RIGHT':['DOWN','UP','RIGHT']}

class GravitySnakeSolver:
    def __init__(self, grid, snake_start, goal, max_reach):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.snake_start = tuple(snake_start)
        self.goal = goal
        self.max_reach = max_reach

    def get_grounded_index(self, body):
        """Findet das erste Segment, das Boden unter sich hat."""
        for i, (y, x) in enumerate(body):
            if y + 1 < self.rows and self.grid[y+1][x] == 1:
                return i
        return None

    def get_neighbors(self, current_body):
        neighbors = []
        hy, hx = current_body[0]

        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ty, tx = hy + dy, hx + dx

            # 1. Basis-Checks
            if not (0 <= ty < self.rows and 0 <= tx < self.cols): continue
            if self.grid[ty][tx] == 1: continue
            if (ty, tx) in current_body[:-1]: continue

            # 2. Bewegung ausführen (Kopf schiebt, Schwanz zieht nach)
            new_body = [(ty, tx)] + list(current_body[:-1])

            # 3. Physik-Simulation (Stabilität vor Sacken)
            while True:
                g_idx = self.get_grounded_index(new_body)
                
                # Absturz wenn kein Halt oder Reichweite überschritten
                if g_idx is None or g_idx > self.max_reach:
                    if any(y + 1 >= self.rows for y, x in new_body): 
                        new_body = None
                        break
                    new_body = [(y + 1, x) for y, x in new_body]
                    continue 

                # Kontrolliertes Sacken des Kopfes
                chy, chx = new_body[0]
                if chy + 1 < self.rows and self.grid[chy+1][chx] == 0:
                    potential = [(chy + 1, chx)] + list(new_body[:-1])
                    p_g_idx = self.get_grounded_index(potential)
                    # Nur sacken, wenn danach noch stabil
                    if p_g_idx is not None and p_g_idx <= self.max_reach:
                        if (chy + 1, chx) in new_body[1:]: break
                        new_body = potential
                        continue 
                break 

            if new_body:
                neighbors.append(tuple(new_body))
        return neighbors

    def solve(self):
        # A* Suche
        pq = [(0, 0, self.snake_start)]
        visited = {self.snake_start: 0}
        came_from = {self.snake_start: None}
        
        while pq:
            _, cost, current_body = heapq.heappop(pq)
            if current_body[0] == self.goal:
                path = []
                while current_body:
                    path.append(current_body)
                    current_body = came_from.get(current_body)
                return path[::-1]

            for next_state in self.get_neighbors(current_body):
                if next_state not in visited or cost + 1 < visited[next_state]:
                    visited[next_state] = cost + 1
                    # Heuristik: Manhattan Distanz des Kopfes zum Ziel
                    h = abs(next_state[0][0] - self.goal[0]) + abs(next_state[0][1] - self.goal[1])
                    heapq.heappush(pq, (cost + 1 + h, cost + 1, next_state))
                    came_from[next_state] = current_body
        return []

def setXY(x,y):
    return str(x)+"#"+str(y)
def getXY(xy):
    hList=xy.split("#")
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
        return "UP"
    return "DOWN"
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
###
###

def initMap(graph,myDict,oppDict,moveList,powerList,snakeDict,feldList,bisherBewegt,zielDict,keinZiel):
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
            hList=wertList[5][8:-2].split("]")
            for h in hList:
                pos=h.find(":");zList=[];aList=h[pos+2:].split(",")
                for a in aList:
                    zList.append(a[2:-1])
                zielDict[int(h[2:pos])]=zList[:]
            hList=wertList[6][8:-2].split("]")
            for h in hList:
                pos=h.find(":");zList=[];aList=h[pos+2:].split(",")
                for a in aList:
                    zList.append(a[2:-1])
                keinZiel[int(h[2:pos])]=zList[:]                
            a=0
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
        if zeile[0:6] == "bisher":
            hList=zeile[12:-3].split("]]")
            for h in hList:
                pos=h.find(":");zList=[];aList=h[pos+2:].split(",")
                i=0
                while True:
                    a=aList[i];b=aList[i+1]
                    if i == len(aList) -2:
                        zList.append([a[3:-1],b[2:-1]])
                    else:
                        zList.append([a[3:-1],b[2:-2]])
                    i+=2
                    if i >= len(aList):
                        break
                bisherBewegt[int(h[2:pos])]=zList[:]
            
    feldList = copy.deepcopy(moveList)                
    for snake,bodyList in snakeDict.items():
        for body in bodyList:
            if body in moveList:
                moveList.remove(body)
    return runde,feldList,rowList
######################################init################
###########################################################
############################################################

def suchePath(graph, start, goal,snakeBody,richtung,moveList):
    explored = [];queue = [[[start],snakeBody]];lauf=0 
    suchList=copy.deepcopy(moveList);suchList.append(start)
    if start == goal:
        return [] # start ist ziel
    while queue:
        path,snBody = queue.pop(0);node = path[-1]
        if node not in explored and node in suchList:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append([new_path,snakeBody])
                if neighbour == goal:
                    return new_path
            explored.append(node)
    return [] # kein Weg zum Ziel

def getDistanz(xyA,xyB):
    x1,y1=getXY(xyA);x2,y2=getXY(xyB)
    return abs(x1-x2)+abs(y1-y2)
def getBodyGestreckt(snakeBody):
    xS,yS=getXY(snakeBody[0])
    for sB in snakeBody[1:]:
        x,y=getXY(sB)
        if not xS == x:
            return False
    return True
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
                    if not setXY(x,y+1) in moveList:
                        startList.append(neighbours)          
            abstand+=1     
            if abstand > 30:
                break
        powerErDict[power] = copy.deepcopy(startList)
    return powerErDict      

def sucheRichtung(snake,start,richtung,graph,powerList,moveList,mRichtungen,snakeLen,snakeBody,bisherList,powerErDict,feldList,zielDict,keinZiel,game_grid):
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

    if not power and len(mrList) > 1:
        if len(bisherList) > 3:
            bList1=bisherList[-1];bList2=bisherList[-2];bList3=bisherList[-3]         
            if bList1[1] == start and bList1[0] in mrList and bList2[1] == start and bList2[0] in mrList and bList3[1] == start and bList3[0] in mrList:
                if bList1[0] == "UP" and not getBodyGestreckt(snakeBody):
                    a=0
                else:
                    mrList.remove(bList1[0])
                    zielList = zielDict[snake]
                    if len(zielList) > 0:
                        z = zielList.pop()
                        #nList=keinZiel[snake];nList.append(z);keinZiel[snake]=nList
                        #keinZiel[snake]=[z]

        powerDist={};bodenList=[]
        for sn in snakeBody:
            xS,yS = getXY(sn)
            if not setXY(xS,yS+1) in feldList:
                bodenList.append(sn)

        for powerXY in powerList:            
            dist=getDistanz(powerXY,start)
            if dist in powerDist:
                pList=powerDist[dist];pList.append(powerXY)
            else:
                powerDist[dist]=[powerXY]
        zaehler=0;lPath=99;ziel=''
        for distPxy,powerL in sorted(powerDist.items()):
            for powerXY in powerL:
                if not powerXY in keinZiel[snake]:
                #    errList= powerErDict[powerXY]
                    distBoden=99
                    for boden in bodenList:
                        dBoden = getDistanz(powerXY,boden)
                        if dBoden < distBoden:
                            distBoden=dBoden
                #   if len(snakeBody) >= distBoden:
                    xZ,yZ=getXY(powerXY);snList=[]
                    for sB in snakeBody:
                        xS,yS=getXY(sB)
                        snList.append((xS,yS))
                    solver = GravitySnakeSolver(game_grid, snList, (xZ,yZ), max_reach=99)
                    pathN = solver.solve()
                #    pathN = suchePath(graph,start,powerXY,snakeBody,richtung,moveList)
                    if len(pathN) > 0 and len(pathN) < lPath:
                        moveR = getRichtung(start,pathN[1])
                        if moveR in mrList:
                            newRichtung=moveR;posSave=pathN[1];power=True;lPath=len(pathN);zaehler=100
                            ziel=powerXY
                    zaehler+=1
            if zaehler > 8:
                break            
            zList=zielDict[snake]
            if not ziel in zList:                                
                zList.append(ziel)
        
    else:
        if len(mrSave) > 0:
            newRichtung = mrSave                
        else:
            if len(mrList) > 0:
                newRichtung=mrList[0]
                xN,yN=getRichtungWerte(newRichtung);x,y=getXY(start)
                xN=x+xN;yN=y+yN;newPos=setXY(xN,yN);posSave=newPos
            else:
                if getDistanz(start,snakeBody[-1]) == 1:
                    newRichtung = getRichtung(start,snakeBody[-1])
    if posSave in moveList:
        moveList.remove(posSave)
    return newRichtung

def bewegung(runde,graph,myDict,oppDict,moveList,powerList,snakeDict,ergList,bisherBewegt,powerErDict,feldList,zielDict,keinZiel,game_grid):
    ergList.clear()

    snakeSort = {k: v for k, v in sorted(snakeDict.items(), key=lambda item: len(item[1]),reverse=True)}
    for snake, bodyList in snakeSort.items():
        if snake in myDict:      
            start=snakeDict[snake][0];richtung=myDict[snake]
            if start in graph:
                newRichtung=sucheRichtung(snake,start,richtung,graph,powerList,moveList,richtungList[richtung],len(snakeDict[snake]),snakeDict[snake],bisherBewegt[snake],powerErDict,feldList,zielDict,keinZiel,game_grid)
                if len(newRichtung) > 0:
                    ergList.append([snake,newRichtung])
                    myDict[snake]=newRichtung
            else:
                if richtung == "UP":
                    x,y=getXY(start)
                    if y < 0:
                        newPos=setXY(x,y-1)
                        if newPos in moveList:
                            ergList.append([snake,"DOWN"])
                            myDict[snake]="DOWN"
                        else:
                            if x > width /2:
                                ergList.append([snake,"LEFT"])
                                myDict[snake]="LEFT"
                            else:
                                ergList.append([snake,"RIGHT"])
                                myDict[snake]="RIGHT"
                    else:
                        if x > 0:
                            newPos=setXY(x-1,y)
                            if newPos in moveList:
                                ergList.append([snake,"LEFT"])
                                myDict[snake]="LEFT"
                        else:
                            newPos=setXY(x+1,y)
                            if newPos in moveList:
                                ergList.append([snake,"RIGHT"])
                                myDict[snake]="RIGHT"
                else:
                    ergList.append([snake,"UP"])
                    myDict[snake]="UP"

            bList=bisherBewegt[snake];bList.append([myDict[snake],start])
            
            


#################
#################
#################

graph={};myDict={};oppDict={};moveList=[];powerList=[];snakeDict={};ergList=[];feldList=[];bisherBewegt={};zielDict={};keinZiel={}
runde,feldList,rowList=initMap(graph,myDict,oppDict,moveList,powerList,snakeDict,feldList,bisherBewegt,zielDict,keinZiel)
game_grid=[]
for row in rowList:
    rList=[]
    for r in row:
        if r == ".":
            rList.append(0)
        else:
            rList.append(1)
    game_grid.append(rList[:])
myDict,oppDict = removeMyOppList(snakeDict,myDict,oppDict)
powerErDict=powerErreichbar(graph,powerList,moveList,snakeDict)
while True:
    bewegung(runde,graph,myDict,oppDict,moveList,powerList,snakeDict,ergList,bisherBewegt,powerErDict,feldList,zielDict,keinZiel,game_grid)
    
    if len(ergList) == 0:
        print("WAIT")
    else:
        ausgabe=""
        for erg in ergList:
            ausgabe+=str(erg[0]) +" "+erg[1]+";"
        print(ausgabe[:-1])

    
    print(runde)
    break