import sys
import math


def distance(p1,p2):
    return int(round(math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) ),0))

# Score points by scanning valuable fish faster than your opponent.
creature_count = int(input());creatureID={}
for i in range(creature_count):
    creature_id, color, _type = [int(j) for j in input().split()]
    creatureID[creature_id] = [color,_type]
print("creatureID={}".format(creatureID),file=sys.stderr)

# game loop
runde=0
while True:
    droneDict={};radarList=[];cDict={}
    myScanList=[];beforeScanList=[]
#
    my_score = int(input())
    foe_score = int(input())
    my_scan_count = int(input())
    for i in range(my_scan_count):
        creature_id = int(input())
        myScanList.append(creature_id)
    foe_scan_count = int(input())
    for i in range(foe_scan_count):
        creature_id = int(input())
    my_drone_count = int(input())
    for i in range(my_drone_count):
        drone_id, drone_x, drone_y, emergency, battery = [int(j) for j in input().split()]
        droneDict[drone_id] = [0,drone_x, drone_y, emergency, battery]
    foe_drone_count = int(input())
    for i in range(foe_drone_count):
        drone_id, drone_x, drone_y, emergency, battery = [int(j) for j in input().split()]
        droneDict[drone_id] = [1,drone_x, drone_y, emergency, battery]
    drone_scan_count = int(input())
    for i in range(drone_scan_count):
        drone_id, creature_id = [int(j) for j in input().split()]
        beforeScanList.append([drone_id, creature_id])
    visible_creature_count = int(input())
    for i in range(visible_creature_count):
        creature_id, creature_x, creature_y, creature_vx, creature_vy = [int(j) for j in input().split()]        
        cDict[creature_id]=[creature_x, creature_y, creature_vx, creature_vy]
    radar_blip_count = int(input())
    for i in range(radar_blip_count):
        inputs = input().split();drone_id = int(inputs[0]);creature_id = int(inputs[1]);radar = inputs[2]
        radarList.append([drone_id,creature_id,radar])
    print("droneDict={};radarList={}".format(droneDict,radarList),file=sys.stderr)
    print("myScanList={};beforeScanList={}".format(myScanList,beforeScanList),file=sys.stderr)
    for i in range(my_drone_count):

        deepDict={0:[2500,5000],1:[5000,7500],2:[7500,9999]}
        zielRadar={"BR":0,"BL":0,"TR":0,"TL":0};light=1;xZiel,yZiel=0,0;puffer=0
        moveDict={"BR":[420,420],"BL":[-420,420],"TR":[420,-420],"TL":[-420,-420]}
        for id,wList in droneDict.items():
            if wList[0] == 0:
                for rList in radarList:
                    if id == rList[0] and not rList[1] in myScanList:          
                        zielRadar[rList[2]] += 1
                move = sorted(zielRadar.items(), key=lambda item: item[1],reverse=True)
                print("move={}".format(move),file=sys.stderr)
                xZiel=wList[1]+moveDict[move[0][0]][0]
                yZiel=wList[2]+moveDict[move[0][0]][1]
                for before in beforeScanList:
                    if before[0] == id:
                        puffer+=1
                if puffer > 3:
                    yZiel=0
        print("MOVE {} {} {}".format(xZiel,yZiel,light))
    runde+=1