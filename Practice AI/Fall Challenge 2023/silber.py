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
runde=0;auftauchen=False;moveP=0
saveDict={}
while True:
    droneDict={};radarList=[];cDict={}
    myScanList=[];beforeScanList=[]
    enemyScanList=[];myId=[]
#
    my_score = int(input())
    foe_score = int(input())
    my_scan_count = int(input())
    for i in range(my_scan_count):
        creature_id = int(input());myScanList.append(creature_id)
    foe_scan_count = int(input())
    for i in range(foe_scan_count):
        creature_id = int(input());enemyScanList.append(creature_id)
    my_drone_count = int(input())
    for i in range(my_drone_count):
        drone_id, drone_x, drone_y, emergency, battery = [int(j) for j in input().split()]
        droneDict[drone_id] = [0,drone_x, drone_y, emergency, battery];myId.append(drone_id)
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
    print("myScanList={};beforeScanList={};enemyScanList={}".format(myScanList,beforeScanList,enemyScanList),file=sys.stderr)
    #####
    puffer=0;anzahlFische=0;scList=[]
    for bList in beforeScanList:
        if bList[0] in myId and not bList[1] in scList:
            puffer+=1;scList.append(bList[1])
    if puffer == 0:
      #  if auftauchen:
        moveP=0
        auftauchen=False
    for rList in radarList:
        if rList[0] == 0:
            anzahlFische+=1
    print("puffer={},anzahlFische={},cDict={}".format(puffer,anzahlFische,cDict),file=sys.stderr)
  #  for i in range(my_drone_count):
    for id,wList in droneDict.items():
        xyList=[550, 1120, 1690, 2260, 2830, 3400, 3970, 4480,4990,5490,5999,6569,7139,7709,8279,8849,9419]
        deepDict={0:[2500,5000],1:[5000,7500],2:[7500,9999]}
        zielRadar={"BR":0,"BL":0,"TR":0,"TL":0};light=1;xZiel,yZiel=0,0
        #moveDict={"BR":[420,420],"BL":[-420,420],"TR":[420,-420],"TL":[-420,-420]}
        moveDict={"BR":[10,600],"BL":[-10,600],"TR":[10,-600],"TL":[-10,-600]}
        moveList=[[0,600],[0,600],[420,420],[420,420],[420,420],[-420,420],[-420,420],[420,420],[420,420],[-420,420],[-420,420],[420,420],[420,420],[-420,420],[-420,420],[-420,420],[0,0],[-300,-500],[600,0],[600,0],[420,-420],[400,-300],[400,-300]]
        if wList[0] == 0:        
            for rList in radarList:
                if id == rList[0] and not rList[1] in myScanList:          
                    zielRadar[rList[2]] += 1
            move = sorted(zielRadar.items(), key=lambda item: item[1],reverse=True)
            print("id={}  move={}".format(id,move),file=sys.stderr)
            #xZiel=wList[1]+moveDict[move[0][0]][0]
            #yZiel=wList[2]+moveDict[move[0][0]][1]
            if not auftauchen and len(moveList) > moveP and moveList[moveP][0] == 0 and moveList[moveP][1] == 0:
                print("WAIT {}".format(light))
            else:

                if puffer > 9 or auftauchen or len(moveList) <= moveP:
                    yZiel=450;auftauchen=True
                    xZiel=3000
                    if id == 2 or id == 3:
                        xZiel=7000
                else:
                    xZiel=wList[1]+moveList[moveP][0]
                    yZiel=wList[2]+moveList[moveP][1]
                if runde < 2:
                    light = 0
                print("MOVE {} {} {}".format(xZiel,yZiel,light))
    runde+=1
    moveP+=1