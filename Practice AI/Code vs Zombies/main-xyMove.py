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


class SimpleEquation(Chromosome):
    def __init__(self, ash,humanList,zombieList,moveLen) -> None:
        self.ash=ash;self.punkte=0.0;self.moveLen=moveLen
        self.moveList=[]  
        self.humanList=humanList
        self.zombieList=zombieList      
        x = ash.x;y=ash.y;xSum=0;ySum=0
        for i in range(moveLen):
            newX=randrange(1000);newY=randrange(1000)
            if randrange(2)==0:
                newX=newX*-1
            if randrange(2)==0:
                newY=newY*-1
            x = x + newX;y=y+newY
            if x < 0:
                x=x*-1
            if x >=16000:
                x=15999-(x-15999)
            if y < 0:
                y=y*-1
            if y >=9000:
                y=8999-(y-8999)
            self.moveList.append(Point(x,y))
            xSum+=x;ySum+=y        
        self.fitness()
     #   print(str(xSum/len(self.moveList))+" - " + str(ySum/len(self.moveList)),file=sys.stderr)

    def fitness(self) -> float:         
        fiboList = {0:0,1:1,2:2,3:3,4:5,5:8,6:13,7:21,8:34,9:55,10:89,11:144,12:233,13:377,14:610,15:987,16:1597,17:2584,18:4181,19:6765,20:10946}
        self.punkte=0;zPunkte=0
        zList=copy.deepcopy(self.zombieList)
        hList=copy.deepcopy(self.humanList)
        newAsh = copy.deepcopy(self.ash)
        for move in self.moveList:
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
            newAsh = gehe(newAsh,move,1000)
            
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

            self.punkte=self.punkte+(fiboList[kills]*10)
            self.punkte = self.punkte 
            if anzZombies == 0:
                break
            if anzHuman == 0:
                self.punkte=0;break
        self.punkte = self.punkte + (1 - (zPunkte/1000000))    

        print("    ",end="")        
        print(self.moveList[0],end="")
        print("  -  ",end="")
        print(self.moveList[len(self.moveList)-1],end="")
        print("   Punkte: ",end="")
        print(str(zPunkte),end="   ")
        print(str(self.punkte))
        
        return self.punkte

    @classmethod
    def random_instance(self,ash,humanList,zombieList,moveLen) -> SimpleEquation:
        return SimpleEquation(ash,humanList,zombieList,moveLen)

    def crossover(self, other: SimpleEquation) -> Tuple[SimpleEquation, SimpleEquation]:
        child1: SimpleEquation = copy.deepcopy(self)
        child2: SimpleEquation = copy.deepcopy(other)
        anz = len(child1.moveList) if len(child1.moveList) < len(child2.moveList) else len(child2.moveList)
        xySwitch=False
        for i in range(anz):
            if xySwitch:
                child1.moveList[i].x = other.moveList[i].x
                child2.moveList[i].x = self.moveList[i].x
            else:
                child1.moveList[i].y = other.moveList[i].y
                child2.moveList[i].y = self.moveList[i].y
            xySwitch = not xySwitch
        return child1, child2

    def mutate(self) -> None:
        for _ in range(5):
            pos = randrange(self.moveLen)
            move = self.moveList[pos]
            wert = randrange(250)
            if random() > 0.5: # mutate x
                if random() > 0.5:
                    move.x += wert
                    if move.x > 15999:
                        move.x=15999-(move.x-15999)
                else:
                    move.x -= wert
                    if move.x < 0:
                        move.x=move.x*-1
            else: # otherwise mutate y
                if random() > 0.5:
                    move.y += wert
                    if move.y > 8999:
                        move.y= 8999-(move.y-8999)
                else:
                    move.y -= wert
                    if move.y < 0:
                        move.y = move.y*-1

    def __str__(self) -> str:
        #return f"X: {self.x} Y: {self.y} Fitness: {self.fitness()}"
        erg=str(self.punkte)+ ":  "
        for m in self.moveList:
            erg = erg + str(m.x) + "-" + str(m.y) + ", "
        return erg




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
    



def testWeg(ash,humanList,zombieList):
    p=0;ergL=[]
    initial_population: List[SimpleEquation] = [SimpleEquation.random_instance(ash,humanList,zombieList,12) for _ in range(10)]  
   # print(initial_population[0])  
   # initial_population[0],initial_population[1] = initial_population[0].crossover(initial_population[1])
   # initial_population[0].mutate()
   # initial_population[0].fitness()
   # print(initial_population[0])
   
    ga: GeneticAlgorithm[SimpleEquation] = GeneticAlgorithm(initial_population=initial_population, threshold=(fiboList[len(zombieList)]*10), max_generations = 1, mutation_chance = 0.1, crossover_chance = 0.7)
    result: SimpleEquation = ga.run()
    print(result)

    return p,ergL

def sucheWege(ash,humanList,zombieList):
    graph = erstelleGraph()
    ergDict = {};ergList=[]
    time_1 = time.time()
    #while time.time() - time_1 < 3.01:
    #    p,ergL = testWeg(ash,humanList,zombieList)
    #    ergDict[p] = copy.deepcopy(ergL)
    p,ergL = testWeg(ash,humanList,zombieList)
    ergDict[p] = copy.deepcopy(ergL)

    for p,ergL in sorted(ergDict.items(),reverse=True):
        ergList = ergDict[p]
    return ergList


name= "C:\\Users\\marku\\Python\\codingame\\Practice AI\\Code vs Zombies\\"
name += "test1.txt"
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
        print(ergList,file=sys.stderr)

    break
    p = ergList.pop(0)
    print(str(p.x) + " " + str(p.y))    
    runde+=1