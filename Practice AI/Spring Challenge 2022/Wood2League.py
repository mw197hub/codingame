import sys
import math
from collections import namedtuple

def distance(x1,y1,x2,y2):
    return math.sqrt( ((x1-x2)**2)+((y1-y2)**2) )

Entity = namedtuple('Entity', [
    'id', 'type', 'x', 'y', 'shield_life', 'is_controlled', 'health', 'vx', 'vy', 'near_base', 'threat_for','distBase'
])

def sucheZiel(my_heroes,monsters):
    ziel = 0;entfernung=100000
    for i in range(len(monsters)):
        mon = monsters[i]
        if mon.distBase < entfernung:
            entfernung = mon.distBase;ziel=i
    return monsters[ziel]


TYPE_MONSTER = 0
TYPE_MY_HERO = 1
TYPE_OP_HERO = 2
# base_x: The corner of the map representing your base
base_x, base_y = [int(i) for i in input().split()]
heroes_per_player = int(input())  # Always 3
print("Base: " + str(base_x) + " - " +str(base_y),file=sys.stderr)
# game loop
while True:
    for i in range(2):
        health, mana = [int(j) for j in input().split()]
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
            distance(x,y,base_x,base_y)
        )
        
        if _type == TYPE_MONSTER:
            monsters.append(entity)
        elif _type == TYPE_MY_HERO:
            my_heroes.append(entity)
        elif _type == TYPE_OP_HERO:
            opp_heroes.append(entity)

    for i in range(heroes_per_player):
        target = None
        if monsters:
            target = sucheZiel(my_heroes,monsters)        
        if target:
            print(f'MOVE {target.x} {target.y}')
        else:
            print('WAIT')
