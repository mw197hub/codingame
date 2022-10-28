from __future__ import annotations
import sys
import math,time,copy
from typing import Tuple, List
from chromosome import Chromosome
from genetic_algorithm import GeneticAlgorithm
from random import randrange, random

moveDict={100: [(100, 0), (97, 26), (87, 50), (71, 71), (50, 87), (26, 97), (0, 100), (-26, 97), (-50, 87), (-71, 71), (-87, 50), (-97, 26), (-100, 0), (-97, -26), (-87, -50), (-71, -71), (-50, -87), (-26, -97), (0, -100), (26, -97), (50, -87), (71, -71), (87, -50), (97, -26)], 200: [(200, 0), (193, 52), (173, 100), (141, 141), (100, 173), (52, 193), (0, 200), (-52, 193), (-100, 173), (-141, 141), (-173, 100), (-193, 52), (-200, 0), (-193, -52), (-173, -100), (-141, -141), (-100, -173), (-52, -193), (0, -200), (52, -193), (100, -173), (141, -141), (173, -100), (193, -52)], 300: [(300, 0), (290, 78), (260, 150), (212, 212), (150, 260), (78, 290), (0, 300), (-78, 290), (-150, 260), (-212, 212), (-260, 150), (-290, 78), (-300, 0), (-290, -78), (-260, -150), (-212, -212), (-150, -260), (-78, -290), (0, -300), (78, -290), (150, -260), (212, -212), (260, -150), (290, -78)], 400: [(400, 0), (386, 104), (346, 200), (283, 283), (200, 346), (104, 386), (0, 400), (-104, 386), (-200, 346), (-283, 283), (-346, 200), (-386, 104), (-400, 0), (-386, -104), (-346, -200), (-283, -283), (-200, -346), (-104, -386), (0, -400), (104, -386), (200, -346), (283, -283), (346, -200), (386, -104)], 500: [(500, 0), (483, 129), (433, 250), (354, 354), (250, 433), (129, 483), (0, 500), (-129, 483), (-250, 433), (-354, 354), (-433, 250), (-483, 129), (-500, 0), (-483, -129), (-433, -250), (-354, -354), (-250, -433), (-129, -483), (0, -500), (129, -483), (250, -433), (354, -354), (433, -250), (483, -129)], 600: [(600, 0), (580, 155), (520, 300), (424, 424), (300, 520), (155, 580), (0, 600), (-155, 580), (-300, 520), (-424, 424), (-520, 300), (-580, 155), (-600, 0), (-580, -155), (-520, -300), (-424, -424), (-300, -520), (-155, -580), (0, -600), (155, -580), (300, -520), (424, -424), (520, -300), (580, -155)], 700: [(700, 0), (676, 181), (606, 350), (495, 495), (350, 606), (181, 676), (0, 700), (-181, 676), (-350, 606), (-495, 495), (-606, 350), (-676, 181), (-700, 0), (-676, -181), (-606, -350), (-495, -495), (-350, -606), (-181, -676), (0, -700), (181, -676), (350, -606), (495, -495), (606, -350), (676, -181)], 800: [(800, 0), (773, 207), (693, 400), (566, 566), (400, 693), (207, 773), (0, 800), (-207, 773), (-400, 693), (-566, 566), (-693, 400), (-773, 207), (-800, 0), (-773, -207), (-693, -400), (-566, -566), (-400, -693), (-207, -773), (0, -800), (207, -773), (400, -693), (566, -566), (693, -400), (773, -207)], 900: [(900, 0), (869, 233), (779, 450), (636, 636), (450, 779), (233, 869), (0, 900), (-233, 869), (-450, 779), (-636, 636), (-779, 450), (-869, 233), (-900, 0), (-869, -233), (-779, -450), (-636, -636), (-450, -779), (-233, -869), (0, -900), (233, -869), (450, -779), (636, -636), (779, -450), (869, -233)]}


zone_w,zone_h=16000,9000
zombie_move = 400
ash_move,ash_kill = 1000,2000
fiboList = {1:1,2:2,3:3,4:5,5:8,6:13,7:21,8:34,9:55,10:89,11:144,12:233,13:377,14:610,15:987,16:1597,17:2584,18:4181,19:6765,20:10946}

# Zombies move towards their targets.
# Ash moves towards his target.
# Any zombie within a 2000 unit range around Ash is destroyed.
# Zombies eat any human they share coordinates with

#A zombie is worth the number of humans still alive squared x10, not including Ash.
# If several zombies are destroyed during on the same round, 
# the nth zombie killed's worth is multiplied by the (n+2)th 
# number of the Fibonnacci sequence (1, 2, 3, 5, 8, and so on). 
# As a consequence, you should kill the maximum amount of zombies during a same turn.

class Point():
    x,y = 0,0
    def __init__(self, x=0, y=0):self.x = x; self.y = y
    def __repr__(self) -> str:return (str(self.x) + " # " + str(self.y))

def distance(p1,p2):
    return math.sqrt( ((p1.x-p2.x)**2)+((p1.y-p2.y)**2) )

def gehe(p1,p2,move):
    dist = distance(p1,p2)
    if dist <= move:
        return p2
    p1.x = p1.x + int((p2.x - p1.x) / dist * move)
    p1.y = p1.y + int((p2.y - p1.y) / dist * move)
    return p1



def fitness(ash,zombieList,humanList,moveList) -> float:         
    fiboList = {0:0,1:1,2:2,3:3,4:5,5:8,6:13,7:21,8:34,9:55,10:89,11:144,12:233,13:377,14:610,15:987,16:1597,17:2584,18:4181,19:6765,20:10946}
    punkte=0;zPunkte=0;hPunkte=0
    zList=copy.deepcopy(zombieList)
    hList=copy.deepcopy(humanList)
    newAsh = copy.deepcopy(ash)
    for move in moveList:
        anzZombies=0;anzHuman=0
        for idZ,zombie in zList.items():
            if zombie[2] == 1:
                dist=16000;zielP=Point(0,0)
                for idH,human in hList.items():
                    if human[1] == 1:
                        nD = distance(zombie[0],human[0])
                        if nD < dist:
                            dist=nD;zielP=copy.deepcopy(human[0])
                zombie[0] = copy.deepcopy(gehe(zombie[0],zielP,400))

        nacher = Point(newAsh.x+move.x,newAsh.y+move.y)
        newAsh = gehe(newAsh,nacher,1000)
            
        kills=0
        for idZ,zombie in zList.items():                
            if zombie[2] == 1:
                anzZombies+=1
                distZ = distance(newAsh,zombie[0])
                #   print(distZ)
                zPunkte += distZ
                if distZ <= 2000:
                    zombie[2] = 0;kills+=1
                    anzZombies-=1                    
                else:
                    for idH,human in hList.items():
                        if human[1] == 1:
                            anzHuman+=1
                            nD = distance(zombie[0],human[0])
                            if nD <= 400:
                                human[1]=0;anzHuman-=1
        anzH=0
        for idH,human in hList.items():
            if human[1] == 1:
                anzH+=1

        punkte=punkte+(fiboList[kills*anzH**2]*10)
        punkte = punkte 
        if anzZombies == 0:
            break
        if anzHuman == 0:
            punkte=0;break
    anzH=0
    for idH,human in hList.items():
        if human[1] == 1:
            anzH+=1


     #   print("    ",end="")        
     #   print(self.moveList[0],end="")
     #   print("  -  ",end="")
     #   print(self.moveList[len(self.moveList)-1],end="")
     #   print("   Punkte: ",end="")
     #   print(str(zPunkte),end="   ")
     #   print(str(self.punkte))
        
    return punkte

def setYX(y,x):
    return str(y)+"-"+str(x)

def erstelleGraph():
    ran=1000
    graph={}
    for y in range(ran,9000,ran):
        for x in range(ran,16000,ran):
            graph[setYX(y,x)]="."
   # print(graph)
    return graph
    

def zombieAsh(startP,zielP,ash,dauer):
    posZ=copy.deepcopy(startP)
    for i in range(int(dauer)+1):
        posZ = gehe(posZ,zielP,400)
        dist = distance(ash,posZ)
       # print(dist,file=sys.stderr)
        if dist - ((i+1) *1000) < 2000:
            return posZ,i+1
    return Point(-1,-1),-1


def erstelleWege(ash,humanList,zombieList):
    ergL=[]
    graph = erstelleGraph()
    zielHuman=Point(0,0);distA=-9999
    for zId,zombie in zombieList.items():
        dist=25000;zielP=0
        for hId,human in humanList.items():
            dist2 = distance(zombie[0],human[0])
            if dist2 < dist:
                dist = dist2; zielP=human[0]
        zombie.append(zielP)
        zombie.append(int((dist/400)+0.99))
        ashZiel,ashWann = zombieAsh(zombie[0],zielP,ash,dist/400)
        zombie.append(ashZiel)
        zombie.append(ashWann)
        diffAsh = ashWann - int((dist/400)+0.99)
        if diffAsh > distA and diffAsh <= 0 and not ashZiel.x == -1:
            distA=diffAsh;zielHuman = copy.deepcopy(ashZiel)

        print(zombie,file=sys.stderr)
    print(zielHuman,file=sys.stderr)
    nextHuman=Point(0,0);dist=25000
    for hId,human in humanList.items():
        dist2 = distance(zielHuman,human[0])
        if dist2 < dist and dist2 > 2000:
            dist = dist2; nextHuman=human[0]            
   # print(dist,file=sys.stderr)
   # print(nextHuman,file=sys.stderr)
    ergP = zielHuman
    if distA < 0:
        factor = 1800 / dist  # 2000 klappt nicht
        x = zielHuman.x + int((nextHuman.x - zielHuman.x ) * factor)
        y = zielHuman.y + int((nextHuman.y - zielHuman.y) * factor)
        ergP = Point(x,y)
    
    print(ergP,file=sys.stderr)
    ergL.append(ergP)
    return ergL

def sucheWege(ash,humanList,zombieList):
    punkte=0
    ergL=[];moveList=[]
    time_1 = time.time()
    ergL = erstelleWege(ash,humanList,zombieList)
    #while time.time() - time_1 < 3.01:
    #    mList=ergL.pop(0)
    #    p2 = fitness(ash,zombieList,humanList,mList)
    #    if p2 > punkte:
    #        punkte=p2;moveList = copy.deepcopy(mList)
    
   ## p2 = fitness(ash,zombieList,humanList,ergL.pop(0))
        
    return ergL


name= "C:\\Users\\marku\\Python\\codingame\\Practice AI\\Code vs Zombies\\"
name += "test13a.txt"
datei = open(name,'r')

humanList = {};zombieList={};ergList=[]
runde = 0
while True:
    if runde == 0:
        x, y = [int(i) for i in datei.readline().split()]
        human_count = int(datei.readline())
        for i in range(human_count):
            human_id, human_x, human_y = [int(j) for j in datei.readline().split()]
            humanList[human_id]= [Point(human_x, human_y),1]
        zombie_count = int(datei.readline())
        for i in range(zombie_count):
            zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in datei.readline().split()]
            zombieList[zombie_id] = [Point(zombie_x, zombie_y), Point(zombie_xnext, zombie_ynext),1]

        ergList = sucheWege(Point(x,y),humanList,zombieList)

        ash=Point(x,y)
     #   print(ash,end="   ")
        for move in ergList:
            ash.x+=move.x;ash.y+=move.y
     #       print(ash,end="   ")
     #   print("")

    break
    p = ergList.pop(0)
    print(str(p.x) + " " + str(p.y))    
    runde+=1