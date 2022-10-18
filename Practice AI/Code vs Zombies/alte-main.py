import sys
import math

# Save humans, destroy zombies!

class Mensch():
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.distanzZ = 0
        self.distanzAsh = 0
        self.rundenZ = 0
        self.zuretten = True

class Zombie():
    def __init__(self, id, x, y, nextX, nextY):
        self.id = id
        self.x = x
        self.y = y
        self.nextX = nextX
        self.nextY = nextY
        self.distanzAsh = 0

def distanz(x1,y1,x2,y2):
    return math.sqrt(((x1-x2)**2)+((y1-y2)**2) )

def berechneDistanz(x,y,menschListe,zombieListe):
    for m in menschListe:
        m.distanzAsh = int((distanz(x,y,m.x,m.y) / 1000) - 2)
        nearZ = 99999
        for z in zombieListe:
            near = distanz(m.x,m.y,z.x,z.y)
            if near < nearZ:
                m.distanzZ = near
                m.rundenZ = int(((near + 399 ) / 400) - 1)
                nearZ = near
        if m.rundenZ < m.distanzAsh:
            m.zuretten = False
    for z in zombieListe:
        z.distanzAsh = distanz(x,y,z.nextY,z.nextY)

# game loop
menschListe = []
zombieListe = []
maxX = 16000
maxY = 9000
ashMove = 1000
zombieMove = 400
moveX = 0
moveY = 0
rangeAsh = 2000
runde = 0
while True:
    menschListe *= 0
    zombieListe *= 0
    runde = runde + 1
    x, y = [int(i) for i in input().split()]
    print("ash: " + str(x) + " - " + str(y),file=sys.stderr)
    
    human_count = int(input())    
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
        m = Mensch(human_id,human_x,human_y)
        menschListe.append(m)
        print("mensch: " + str(human_id) + " : " + str(human_x) + " - " + str(human_y),file=sys.stderr)
    zombie_count = int(input())
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
        z = Zombie(zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext)
        zombieListe.append(z)
        print("zombie: " + str(zombie_id) + " : " + str(zombie_x) + " - "+ str(zombie_y),file=sys.stderr)        
    berechneDistanz(x,y,menschListe,zombieListe)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    for m in menschListe:
        print("weg: " + str(m.rundenZ) + " zu " + str(m.distanzAsh) + " = " + str(m.zuretten),file=sys.stderr)
        #if m.rundenZ <= m.distanzAsh:
        if m.zuretten:
            moveX = m.x
            moveY = m.y
            break
    # Your destination coordinates

    print(str(moveX) + " " + str(moveY))
