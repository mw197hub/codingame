import sys
import math
from collections import namedtuple
#platz davor 1870, jetzt 747 bronze
# silver 1188, 

class Figur:
    def __init__(self, id,type,x,y,shield_life,is_controlled,health,vx,vy,near_base,threat_for,distMyBase,distEmBase,mZiel):
        self.id=id;self.type=type;self.x=x;self.y=y;self.shield_life=shield_life;self.is_controlled=is_controlled
        self.health=health;self.vx=vx;self.vy=vy;self.near_base=near_base;self.threat_for=threat_for;self.distMyBase=distMyBase
        self.distEmBase=distEmBase;self.mZiel=mZiel

def distance(x1,y1,x2,y2):
    return math.sqrt( ((x1-x2)**2)+((y1-y2)**2) )

    

def sucheZiel(m,my_heroes,monsters,opp_heroes,myHealth,myMana,emHealth,emMana,base_x,base_y,emBase_x,emBase_y,runde):
    if base_x == 0:
        befehl = "MOVE";x=base_x;y=base_y;idZiel=0;anzahlWind=0;distMin=0;distMax=9000;zWind=0;zMana=10
        if m == 0:x=11000;y=5600;distMin=8000;distMax=20000
        if m == 1:x=6250;y=2050
        if m == 2:x=2900;y=5300
    else:
        befehl = "MOVE";x=base_x;y=base_y;idZiel=0;anzahlWind=0;distMin=0;distMax=9000;zWind=0;zMana=10

    entfernung=100000;iZiel=99
    for i in range(len(monsters)):
        mon = monsters[i]
        if mon.distMyBase < entfernung and mon.distMyBase > distMin and mon.distMyBase < distMax and mon.mZiel==0:
            entfernung = mon.distMyBase;x=monsters[i].x;y=monsters[i].y;befehl = "MOVE";iZiel=i
        if distance(my_heroes[m].x,my_heroes[m].y,mon.x,mon.y) < 1270 and mon.near_base == 1:
            anzahlWind += 1

    if anzahlWind > zWind and myMana > zMana and m < 2:
        befehl = "SPELL WIND";x=emBase_x;y=emBase_y
    if iZiel < 99:
        monsters[iZiel].mZiel=m+1
        print(str(m) + " : " + str(monsters[iZiel].id) + " - " + str(monsters[iZiel].mZiel),file=sys.stderr)        
    return befehl,x,y,idZiel



TYPE_MONSTER = 0
TYPE_MY_HERO = 1
TYPE_OP_HERO = 2
# base_x: The corner of the map representing your base
base_x, base_y = [int(i) for i in input().split()]
heroes_per_player = int(input())  # Always 3
print("Base: " + str(base_x) + " - " +str(base_y),file=sys.stderr)
emBase_x = 17630;emBase_y=9000
if base_x > 0:
    emBase_x=0;emBase_y=0
runde=0
# game loop
while True:
    myHealth=0;myMana=0;emHealth=0;emMana=0;runde+=1
    for i in range(2):
        emHealth, emMana = [int(j) for j in input().split()]
        if i == 0:
            myHealth = emHealth;myMana=emMana
    monsters = [];my_heroes = [];opp_heroes = []
    entity_count = int(input())  # Amount of heros and monsters you can see
    for i in range(entity_count):
        _id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for = [int(j) for j in input().split()]
        figur = Figur(_id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for,distance(x,y,base_x,base_y),distance(x,y,emBase_x,emBase_y),0)
     
        if _type == TYPE_MONSTER:
            monsters.append(figur)
        elif _type == TYPE_MY_HERO:
            my_heroes.append(figur)
        elif _type == TYPE_OP_HERO:
            opp_heroes.append(figur)



    for i in range(heroes_per_player):
        target = None        
        befehl,x,y,idZiel = sucheZiel(i,my_heroes,monsters,opp_heroes,myHealth,myMana,emHealth,emMana,base_x,base_y,emBase_x,emBase_y,runde) 
        if befehl == "MOVE" or "SPELL WIND" or "SPELL CONTROL":
            print(f'{befehl} {x} {y}')
        else:
            if befehl == "SPELL SHIELD":
                print(f'{befehl} {idZiel}')
            else:
                print('WAIT')
