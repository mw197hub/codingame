import sys
import math
from collections import namedtuple
#platz davor 1870, jetzt 747 bronze
# silver 1624, 

def distance(x1,y1,x2,y2):
    return math.sqrt( ((x1-x2)**2)+((y1-y2)**2) )

Entity = namedtuple('Entity', [
    'id', 'type', 'x', 'y', 'shield_life', 'is_controlled', 'health', 'vx', 'vy', 'near_base', 'threat_for','distMyBase','distEmBase'
])

def getGesamtWind(my_heroes,monsters):
    gesamtWind = 0
    for i in range(len(monsters)):
        mon = monsters[i]
        anzahlWind = 0
        for m in range(3):
            if distance(my_heroes[m].x,my_heroes[m].y,mon.x,mon.y) < 1270:
                anzahlWind += 1
        if anzahlWind >= 3:
            gesamtWind=anzahlWind
    print("gesamtWind: " + str(gesamtWind),file=sys.stderr)
    return gesamtWind
    

def sucheZiel2(m,my_heroes,monsters,opp_heroes,myHealth,myMana,emHealth,emMana,base_x,base_y,emBase_x,emBase_y,runde,gesamtWind):
    if base_x == 0:
        befehl = "MOVE";x=base_x;y=base_y;idZiel=0;anzahlWind=0;distMin=0;distMax=18000;zWind=0;zMana=10
        if m == 0:x=6600;y=950
        if m == 1:x=5500;y=3700
        if m == 2:x=2200;y=5300
    else:
        befehl = "MOVE";x=base_x;y=base_y;idZiel=0;anzahlWind=0;distMin=0;distMax=18000;zWind=0;zMana=10

    entfernung=100000
    for i in range(len(monsters)):
        mon = monsters[i]
        if mon.distMyBase < entfernung and mon.distMyBase > distMin and mon.distMyBase < distMax:
            entfernung = mon.distMyBase;x=monsters[i].x;y=monsters[i].y;befehl = "MOVE"
        if distance(my_heroes[m].x,my_heroes[m].y,mon.x,mon.y) < 1270:
            anzahlWind += 1
    
    if runde > 60 and myMana > 40:
        x=11800;y=6065
        print("Wind: " + str(anzahlWind) + "  Dist: " + str(entfernung),file=sys.stderr)
        if gesamtWind >= 3 and distance(my_heroes[m].x,my_heroes[m].y,emBase_x,emBase_y) < 6800:
            befehl = "SPELL WIND";x=emBase_x;y=emBase_y
    return befehl,x,y,idZiel

def sucheZiel(m,my_heroes,monsters,opp_heroes,myHealth,myMana,emHealth,emMana,base_x,base_y,emBase_x,emBase_y,runde,gesamtWind):
    if base_x == 0:
        befehl = "WAIT";x=base_x;y=base_y;idZiel=0;anzahlWind=0;distMin=0;distMax=8000;zWind=0;zMana=10
        if m == 0:
            befehl = "MOVE";x=5400;y=2756;idZiel=0;anzahlWind=0;distMin=4500;distMax=6200;zWind=1;zMana=10
    else:
        befehl = "WAIT";x=base_x;y=base_y;idZiel=0;anzahlWind=0;distMin=0;distMax=8000;zWind=0;zMana=10
        if m == 0:
            befehl = "MOVE";x=12230;y=6244;idZiel=0;anzahlWind=0;distMin=4500;distMax=6200;zWind=1;zMana=10


    entfernung=100000
    for i in range(len(monsters)):
        mon = monsters[i]
        if mon.distMyBase < entfernung and mon.distMyBase > distMin and mon.distMyBase < distMax:
            entfernung = mon.distMyBase;x=monsters[i].x;y=monsters[i].y;befehl = "MOVE"
        if distance(my_heroes[m].x,my_heroes[m].y,mon.x,mon.y) < 1270 and mon.near_base == 1:
            anzahlWind += 1
    if anzahlWind > zWind and myMana > zMana and m < 2:
        befehl = "SPELL WIND";x=emBase_x;y=emBase_y
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
        entity = Entity(
            _id,            # _id: Unique identifier
            _type,          # _type: 0=monster, 1=your hero, 2=opponent hero
            x, y,           # x,y: Position of this entity
            shield_life,    # shield_life: Ignore for this league; Count down until shield spell fades
            is_controlled,  # is_controlled: Ignore for this league; Equals 1 when this entity is under a control spell
            health,         # health: Remaining health of this monster
            vx, vy,         # vx,vy: Trajectory of this monster
            near_base,      # near_base: 0=monster with no target yet, 1=monster targeting a base
            threat_for,      # threat_for: Given this monster's trajectory, is it a threat to 1=your base, 2=your opponent's base, 0=neither
            distance(x,y,base_x,base_y),distance(x,y,emBase_x,emBase_y)
        )        
        if _type == TYPE_MONSTER:
            monsters.append(entity)
        elif _type == TYPE_MY_HERO:
            my_heroes.append(entity)
        elif _type == TYPE_OP_HERO:
            opp_heroes.append(entity)


    gesamtWind = getGesamtWind(my_heroes,monsters)
    for i in range(heroes_per_player):
        target = None        
        befehl,x,y,idZiel = sucheZiel(i,my_heroes,monsters,opp_heroes,myHealth,myMana,emHealth,emMana,base_x,base_y,emBase_x,emBase_y,runde,gesamtWind) 
        if befehl == "MOVE" or "SPELL WIND" or "SPELL CONTROL":
            print(f'{befehl} {x} {y}')
        else:
            if befehl == "SPELL SHIELD":
                print(f'{befehl} {idZiel}')
            else:
                print('WAIT')
