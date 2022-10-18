import sys
import math,time
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


def sucheWege(humanList,zombieList):
    ergList = [];time_1 = time.time()
    while time.time() - time_1 < 3:
        a = 0
    return ergList


name = "test1.txt"
datei = open(name,'r')

humanList = {};zombieList={}
runde = 0
while True:
    x, y = [int(i) for i in datei.readline().split()]
    human_count = int(datei.readline())
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in datei.readline().split()]
        humanList[human_id]= [Point(human_x, human_y)]
    zombie_count = int(datei.readline())
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in datei.readline().split()]
        zombieList[zombie_id] = [Point(zombie_x, zombie_y), Point(zombie_xnext, zombie_ynext)]

    ergList = sucheWege(humanList,zombieList)
    for p in ergList:
        print(str(p.x) + " " + str(p.y))
    break