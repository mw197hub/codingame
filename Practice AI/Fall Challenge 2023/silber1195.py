# https://www.codingame.com/ide/challenge/fall-challenge-2023
import sys,time
import math,random,copy

def initMap(name,droneDict,fischDict,myScanList,enemyScanList,beforeScanList):
    pfad='C:\\Users\\marku\\Python\\codingame\\Practice AI\\Fall Challenge 2023\\'+name+'.txt'
    print(pfad)
    puffer,anzahlFische,anzahlMonster,runde=0,0,0,0
    eingabe = open(pfad,'r')
    for zeile in eingabe:
        if zeile[0:6] == "puffer":
            iList=zeile.split(";")
            puffer = int(iList[0][iList[0].find("=")+1:])
            anzahlFische = int(iList[1][iList[1].find("=")+1:])
            anzahlMonster = int(iList[2][iList[2].find("=")+1:])
            runde = int(iList[3][iList[3].find("=")+1:])
        if zeile[0:5] == "drone":
            posR = zeile.find("radar")
            iList = zeile[:posR].split(" ")
            id = int(iList[0][iList[0].find(":")+1:])
            droneDict[id] = Drone(id)
            droneDict[id].id = int(iList[1][iList[1].find(":")+1:])
            droneDict[id].x  = int(iList[2][iList[2].find(":")+1:])
            droneDict[id].y  = int(iList[3][iList[3].find(":")+1:])
            droneDict[id].emergency  = int(iList[4][iList[4].find(":")+1:])
            droneDict[id].battery  = int(iList[5][iList[5].find(":")+1:])
            posP = zeile.find("puffer")+7
            puffer = zeile[posP+1:posR-2]
            iList = puffer.split(",")
            for il in iList:
                if len(il) > 0:
                    droneDict[id].pufferList.append(int(il.lstrip()))
            radar=zeile[posR+7:-2]
            iList = radar.split("]")
            for il in iList:
                il = il.replace(",","")
                il = il.replace("[","")
                ili = il.lstrip().split(" ")
                if len(ili) > 1:
                    droneDict[id].radarList.append([int(ili[0]),ili[1][1:-1]])
           # print(droneDict[id])

        if zeile[0:5] == "fisch":
            iList = zeile.split(" ")
            id = int(iList[0][iList[0].find(":")+1:])
            color = int(iList[1][iList[1].find(":")+1:])
            typ = int(iList[2][iList[2].find(":")+1:])
            fischDict[id] = Fisch(id,color,typ)
            fischDict[id].runde = int(iList[3][iList[3].find(":")+1:])
            fischDict[id].x = int(iList[4][iList[4].find(":")+1:])
            fischDict[id].y = int(iList[5][iList[5].find(":")+1:])
            fischDict[id].moveX = int(iList[6][iList[6].find(":")+1:])
            fischDict[id].moveY = int(iList[7][iList[7].find(":")+1:])
          #  print(fischDict[id])

        if zeile[0:5] == "mySca":
            iList = zeile.split(";")
            werte = iList[0][iList[0].find("=")+1:]
            oList = werte[1:-1].split(",")
            for il in oList:
                if len(il) > 0:
                    myScanList.append(int(il.lstrip()))
            werte = iList[1][iList[1].find("=")+1:]
            oList = werte[1:-1].split(",")
            for il in oList:
                if len(il) > 0:
                    enemyScanList.append(int(il.lstrip()))
            werte = iList[2][iList[2].find("=")+1:]
            oList = werte[1:-2].split("]")
            for il in oList:
                il = il.replace(",","")
                il = il.replace("[","")
                ili = il.lstrip().split(" ")
                if len(ili) > 1:
                    beforeScanList.append([int(ili[0]),int(ili[1])])

    return puffer,anzahlFische,anzahlMonster,runde
#####


#######################
# creatureID  [color,type]
# droneDict   [my/enemy,drone_x, drone_y, emergency, battery]
# radarList   [drone_id,creature_id,radar]
# scan0=800, scan1=2000, move=600, sink=300

class Fisch:
    def __init__(self,id,color,typ):
        self.id=id;self.color=color;self.typ=typ;self.x=-1;self.y=-1;self.moveX=-1;self.moveY=-1
        self.my=False;self.enemy=False;self.runde=-1;self.position={}
    def __str__(self) -> str:
        return ("id:{} color:{} type:{} runde:{} x:{} y:{} moveX:{} moveY:{}".format(self.id,self.color,self.typ,self.runde,self.x,self.y,self.moveX,self.moveY))

class Drone:
    def __init__(self,nr):
        self.nr=nr;self.id=-1;self.x=-1;self.y=-1;self.emergency=-1;self.battery=-1;self.ziel=[];self.ausweichen=[]
        self.auftauchen=False;self.light=0;self.radarList=[];self.pufferList=[];self.moveX=0;self.moveY=0
    def __str__(self) -> str:
        return ("id:{} my:{} x:{} y:{} em:{} bat:{} puffer:{} radar:{}".format(self.nr,self.id,self.x,self.y,self.emergency,self.battery,self.pufferList,self.radarList))

########################

def inRange(d1,u2,m1,m2):
    if (d1[0] - u2[0]) * (d1[0] - u2[0]) + (d1[1] - u2[1]) * (d1[1] - u2[1]) <= 500 * 500:
        return True
    if m1==[0,0] and m2==[0,0]:
        return False
    x= u2[0];y=u2[1];ux=d1[0];uy=d1[1]
    x2=x-ux;y2=y-uy;r2=500
    vx2=m2[0]-m1[0];vy2=m2[1]-m1[1]
    a=vx2*vx2+vy2*vy2
    if a <= 0.0:
        return False
    b=2.0*(x2*vx2+y2*vy2)
    c=x2*x2+y2*y2-r2*r2
    delta=b*b-4.0*a*c
    if delta < 0.0:
        return False
    t=(-b - math.sqrt(delta))/(2.0*a)
    if t <= 0.0:
        return False
    if t > 1.0:
        return False
    return True

def distance(p1,p2):
    return int(round(math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) ),0))

def setXyMove(drone):    
    dist = distance([drone.x,drone.y],[drone.ziel[0],drone.ziel[1]])
    if dist < 600:
        return drone.ziel[0]-drone.x,drone.ziel[1]-drone.y
    diffX=drone.ziel[0]-drone.x;diffY=drone.ziel[1]-drone.y
    verhaeltnis= dist/600
    return int(diffX / verhaeltnis),int(diffY / verhaeltnis)

def setzeZonen(droneDict,fischDict,runde):
    for id,fisch in fischDict.items():
        zone=[]
        for nr,drone in droneDict.items():
            if drone.id == 0:
                for radar in drone.radarList:
                    if id == radar[0]:
                        zone.append(radar[1])
        fisch.position[runde]=zone[:]
        #print("id:{}   zone:{}".format(id,fisch.position[runde]),file=sys.stderr)

def setzeTyps(droneDict,fischDict,myScanList,enemyScanList,beforeScanList):
    typDict={0:[0,0,0,0,0],1:[0,0,0,0,0],2:[0,0,0,0,0]};fehlFischList=[]
    # type: [ anzahlVorhanden, myScan, myPuffer, enemyScan, enemyPuffer ]
    fList=[];fangbarList=[];suchFischList=[]
    for id,drone in droneDict.items():
        if drone.id == 0:
            for radar in drone.radarList:
                fList.append(radar[0])
                fisch = fischDict[radar[0]]
                if fisch.typ > -1:
                    typDict[fisch.typ][0]+=1
                    fangbarList.append(fisch.id)
                    suchFischList.append(fisch.id)
            break
    for scan in myScanList:
        typDict[fischDict[scan].typ][1]+=1
        if scan in suchFischList:
            suchFischList.remove(scan)
    for scan in enemyScanList:
        typDict[fischDict[scan].typ][3]+=1
    myL=[];enL=[]
    for id,drone in droneDict.items():
        for pu in drone.pufferList:
            if drone.id == 0:
                if not pu in myL and pu in fangbarList:
                    typDict[fischDict[pu].typ][2]+=1;myL.append(pu)
                if pu in suchFischList:
                    suchFischList.remove(pu)
            else:
                if not pu in enL and pu in fangbarList:
                    typDict[fischDict[pu].typ][4]+=1;enL.append(pu)

    for id in fischDict:
        if not id in fList:
            fehlFischList.append(id)
    print("{}    suchFisch:{}".format(typDict,suchFischList),file=sys.stderr)
    return typDict,fehlFischList,suchFischList

def fischDrone(fischList,drone):
    dList=[];problem=False
    for fisch in fischList:
        d = (distance([drone[0],drone[1]],[fisch[0],fisch[1]]))        
        if d <= 540:
            problem=True
        else:
            dList.append(d)
    return dList,problem

def testeList600(drone,list600,fischList):
    ergList=[];moveX,moveY,maxD,minD=0,0,0,9999
    minX,minY=0,0
    for fisch in fischList:
        for i in range(len(list600)):
            mov = list600[i]
            movList=[]
            movList.append(mov)
            movList.append([mov[0]*-1,mov[1]])
            movList.append([mov[0],mov[1]*-1])
            movList.append([mov[0]*-1,mov[1]*-1])
            for move in movList:
                if not inRange([drone.x,drone.y],[fisch[0],fisch[1]],[move[0],move[1]],[fisch[2],fisch[3]]):
                    d = (distance([drone.x+move[0],drone.y+move[1]],[fisch[0]+fisch[2],fisch[1]+fisch[3]]))     
                    if d > 800:  
                        ergList.append([move,d])
                        dMin = abs((distance([move[0],move[1]],[drone.moveX,drone.moveY])))
                        if dMin < minD:
                            minX,minY=move[0],move[1];minD=dMin
                    if d > maxD:
                        moveX,moveY=move[0],move[1]
    if minX != 0 and minY != 0:
        return ergList,minX,minY
    return ergList,moveX,moveY

def ausweichen(runde,drone,droneDict,fischDict,xyList,deepDict,moveDict,moveList,list600,list540,auftauchen):
    fischList=[];ausweichen=False   # fischList  fX,fY,mfX,mfY
    for id,fisch in fischDict.items():
        if fisch.typ == -1 and fisch.runde == runde:
            if inRange([drone.x,drone.y],[fisch.x,fisch.y],[drone.moveX,drone.moveY],[fisch.moveX,fisch.moveY]):
                ausweichen=True
                fischList.append([fisch.x,fisch.y,fisch.moveX,fisch.moveY])
    if ausweichen:
        drone.light=0
        drone.ausweichen=[runde,fischList[0][0]+fischList[0][2],fischList[0][1]+fischList[0][3]]
        if len(fischList) == 1:
            testList,drone.moveX,drone.moveY=testeList600(drone,list600,fischList)
            #print(testList,file=sys.stderr)
            if len(testList) == 0:
                dFisch=distance([0,0],[fischList[0][2],fischList[0][3]])+1
                verh=600/dFisch
                drone.moveX = int(fischList[0][2]*verh)
                drone.moveY = int(fischList[0][3]*verh)
        else:
            drone.moveX=0;drone.moveY=-600
    else:
        if len(drone.ausweichen) > 0 and runde -1 == drone.ausweichen[0]:
            drone.light=0
            d1 = distance([drone.ausweichen[1],drone.ausweichen[2]],[420,-420])
            d2 = distance([drone.ausweichen[1],drone.ausweichen[2]],[-420,-420])
            if auftauchen:
                d1 = distance([drone.ausweichen[1],drone.ausweichen[2]],[420,420])
                d2 = distance([drone.ausweichen[1],drone.ausweichen[2]],[-420,420])
            
           #if d1 > d2:
           #     drone.moveX,drone.moveY=420,-420
           # else:
           #     drone.moveX,drone.moveY=-420,-420
           # print("vorbei schwimmen",file=sys.stderr)

    return ausweichen

def moveDrone(drone,runde,droneDict,fischDict,myScanList,enemyScanList,beforeScanList,puffer,anzahlFische,xyList,deepDict,moveDict,moveList,list600,list540,typDict,fehlFischList,startPosition,moveTypDict,suchFischList):
    optDeep={0:[3000,4400,3750],1:[5500,6250,6250],2:[9500,8100,8750]} # ohne Licht, mit Licht, Mitte
    xyList=[550, 1120, 1690, 2260, 2830, 3400, 3970, 4480,4990,5490,5999,6569,7139,7709,8279,8849,9419]

    # type 0 suchen
    if typDict[0][1] + typDict[0][2] < typDict[0][0] and len(moveTypDict[0]) > 0:
        if len(drone.ziel) > 0 and distance([drone.x,drone.y],[drone.ziel[0],drone.ziel[1]]) < 100:
            drone.ziel.clear();drone.light=1
        if drone.x < 5000 and len(drone.ziel) == 0:
            drone.ziel = moveTypDict[0].pop(0)
        if drone.x > 5000 and len(drone.ziel) == 0:
            drone.ziel = moveTypDict[0].pop()
        drone.moveX,drone.moveY = setXyMove(drone)
        if drone.y+drone.moveY > 2600:
            drone.light=1

    # type 1 + 2 suchen
    else:        
        andereDrone=None
        for aId,aDrone in droneDict.items():
            if aDrone.id == 0 and not aDrone.nr == drone.nr:
                andereDrone=aDrone
        monsterPos={};fischPos={}
        for radar in drone.radarList:
            if fischDict[radar[0]].typ == -1:
                 monsterPos[radar[1]] =  monsterPos[radar[1]] + 1 if radar[1] in monsterPos else 1
            else:
                if radar[0] in suchFischList:
                    fischPos[radar[1]] = fischPos[radar[1]]+ 1 if radar[1] in fischPos else 1

        zielFische=[]
        for radar in drone.radarList:
            if fischDict[radar[0]].typ > -1:
                if radar[0] in suchFischList:
                    if not radar[1] in monsterPos:
                        zielFische.append(radar[:])

        if len(zielFische) > 0:
            drone.light = 1;zFisch=None
            if drone.nr < andereDrone.nr:                
                zFisch = zielFische.pop(0)
            else:
                zFisch = zielFische.pop()
        
            drone.moveX = moveDict[zFisch[1]][0]
            drone.moveY = moveDict[zFisch[1]][1]
        else:
            drone.light=0
            moveP = sorted(fischPos.items(), key=lambda item: item[1],reverse=True)
            drone.moveX = moveDict[moveP[0][0]][0]
            drone.moveY = moveDict[moveP[0][0]][1]

##########

def aktionFestlegen(runde,droneDict,fischDict,myScanList,enemyScanList,beforeScanList,puffer,anzahlFische,xyBisherList,deepDict,moveDict,moveList,list600,list540,startPosition,moveTypDict):
    aktionList=[];auftauchen=0
    typDict,fehlFischList,suchFischList=setzeTyps(droneDict,fischDict,myScanList,enemyScanList,beforeScanList)
    setzeZonen(droneDict,fischDict,runde)
    #if (typDict[0][0] == typDict[0][2]+typDict[0][1] and typDict[0][1] < typDict[0][0]) or (typDict[1][0] == typDict[1][2]+typDict[1][1] and typDict[2][0] == typDict[2][2]+typDict[2][1] and typDict[1][1] < typDict[1][0] and typDict[2][1] < typDict[2][0]):        
    #    auftauchen=1 if typDict[0][2] == 4 else 2
    if  typDict[0][0] +  typDict[1][0] + typDict[2][0] <= typDict[0][1] + typDict[0][2] + typDict[1][1] + typDict[1][2] + typDict[2][1] + typDict[2][2]:
        auftauchen =2
    for id,drone in droneDict.items():        
        zielRadar={"BR":0,"BL":0,"TR":0,"TL":0};xZiel,yZiel=0,0

        if drone.id == 0:      
            if auftauchen > 0:
                drone.moveX=0
                drone.moveY=-600 if drone.y - 600 > 499 else (drone.y - 499) * -1
                drone.light=0 if auftauchen == 1 else 0
            else:
                moveDrone(drone,runde,droneDict,fischDict,myScanList,enemyScanList,beforeScanList,puffer,anzahlFische,xyBisherList,deepDict,moveDict,moveList,list600,list540,typDict,fehlFischList,startPosition,moveTypDict,suchFischList)
                

            problem=ausweichen(runde,drone,droneDict,fischDict,xyBisherList,deepDict,moveDict,moveList,list600,list540,auftauchen)
            if problem:
                drone.light=0

            if drone.moveX == 0 and drone.moveY <= 300 and drone.moveY >= 0:
                aktionList.append([drone.light,"my"])  # WAIT
            else:
                aktionList.append([drone.x+drone.moveX,drone.y+drone.moveY,drone.light,"xy:"+str(drone.moveX)+"#"+str(drone.moveY)])  # MOVE
    return aktionList


######################################################################################
xyBisherList=[]
deepDict={0:[2500,5000],1:[5000,7500],2:[7500,9999]}
moveDict={"BR":[420,420],"BL":[-420,420],"TR":[420,-420],"TL":[-420,-420]}
#moveDict={"BR":[10,600],"BL":[-10,600],"TR":[10,-600],"TL":[-10,-600]}
moveList=[[0,600],[0,600],[420,420],[420,420],[420,420],[-420,420],[-420,420],[420,420],[420,420],[-420,420],[-420,420],[420,420],[420,420],[-420,420],[-420,420],[-420,420],[0,0],[-300,-500],[600,0],[600,0],[420,-420],[400,-300],[400,-300]]
list600=[[0, 600], [43, 598], [65, 596], [95, 592], [122, 587],  [144, 582],  [163, 577],  [183, 571],  [204, 564], [222, 557],  [241, 549],  [263, 539], [283, 529], [303, 518],[324, 505], [343, 492], [363, 478], [383, 462], [403, 444], [423, 425], [443, 404], [463, 381], [483, 356], [503, 327], [523, 294], [543, 255], [563, 206], [583, 140], [600, 0]]
list540=[[0, 540], [24, 539], [41, 538], [52, 537], [62, 536], [70, 535], [77, 534], [84, 533], [90, 532], [96, 531], [101, 530], [106, 529], [107, 529], [111, 528], [116, 527], [120, 526], [121, 526], [125, 525], [129, 524], [133, 523], [137, 522], [141, 521], [144, 520], [148, 519], [151, 518], [155, 517], [158, 516], [161, 515], [164, 514], [165, 514], [168, 513], [171, 512], [174, 511], [176, 510], [177, 510], [179, 509], [182, 508], [185, 507], [188, 506], [190, 505], [191, 505], [193, 504], [196, 503], [198, 502], [201, 501], [203, 500], [206, 499], [208, 498], [210, 497], [211, 497], [213, 496], [215, 495], [217, 494], [218, 494], [220, 493], [222, 492], [224, 491], [226, 490], [228, 489], [229, 489], [231, 488], [233, 487], [235, 486], [237, 485], [239, 484], [241, 483], [243, 482], [245, 481], [247, 480], [249, 479], [251, 478], [253, 477], [254, 476], [255, 476], [256, 475], [257, 475], [258, 474], [260, 473], [262, 472], [264, 471], [265, 470], [266, 470], [267, 469], [269, 468], [271, 467], [272, 466], [273, 466], [274, 465], [276, 464], [277, 463], [278, 463], [279, 462], [281, 461], [282, 460], [283, 460], [284, 459], [286, 458], [287, 457], [288, 457], [289, 456], [290, 455], [291, 455], [292, 454], [294, 453], [295, 452], [297, 451], [298, 450], [300, 449], [301, 448], [303, 447], [304, 446], [306, 445], [307, 444], [308, 443], [309, 443], [310, 442], [311, 441], [312, 441], [313, 440], [314, 439], [315, 438], [316, 438], [317, 437], [318, 436], [319, 436], [320, 435], [321, 434], [322, 433], [323, 433], [324, 432], [325, 431], [326, 430], [327, 430], [328, 429], [329, 428], [330, 427], [331, 427], [332, 426], [333, 425], [334, 424], [335, 423], [336, 423], [337, 422], [338, 421], [339, 420], [340, 419], [341, 419], [342, 418], [343, 417], [344, 416], [345, 415], [346, 414], [347, 414], [348, 413], [349, 412], [350, 411], [351, 410], [352, 409], [353, 408], [354, 408], [355, 407], [356, 406], [357, 405], [358, 404], [359, 403], [360, 402], [361, 401], [362, 401], [363, 400], [364, 399], [365, 398], [366, 397], [367, 396], [368, 395], [369, 394], [370, 393], [371, 392], [372, 391], [373, 390], [374, 389], [375, 388], [376, 387], [377, 386], [378, 385], [379, 384], [380, 383], [381, 382], [382, 381], [383, 380], [384, 379], [385, 378], [386, 377], [387, 376], [388, 375], [389, 374], [390, 373], [391, 372], [392, 371], [393, 370], [394, 369], [395, 368], [396, 367], [397, 366], [398, 365], [399, 364], [400, 363], [401, 361], [402, 360], [403, 359], [404, 358], [405, 357], [406, 356], [407, 355], [408, 353], [409, 352], [410, 351], [411, 350], [412, 349], [413, 348], [414, 346], [415, 345], [416, 344], [417, 343], [418, 342], [419, 340], [420, 339], [421, 338], [422, 337], [423, 335], [424, 334], [425, 333], [426, 332], [427, 330], [428, 329], [429, 328], [430, 326], [431, 325], [432, 324], [433, 322], [434, 321], [435, 320], [436, 318], [437, 317], [438, 315], [439, 314], [440, 313], [441, 311], [442, 310], [443, 308], [444, 307], [445, 306], [446, 304], [447, 303], [448, 301], [449, 300], [450, 298], [451, 297], [452, 295], [453, 294], [454, 292], [455, 290], [456, 289], [457, 287], [458, 286], [459, 284], [460, 282], [461, 281], [462, 279], [463, 277], [464, 276], [465, 274], [466, 272], [467, 271], [468, 269], [469, 267], [470, 265], [471, 264], [472, 262], [473, 260], [474, 258], [475, 256], [476, 254], [477, 253], [478, 251], [479, 249], [480, 247], [481, 245], [482, 243], [483, 241], [484, 239], [485, 237], [486, 235], [487, 233], [488, 231], [489, 228], [490, 226], [491, 224], [492, 222], [493, 220], [494, 217], [495, 215], [496, 213], [497, 210], [498, 208], [499, 206], [500, 203], [501, 201], [502, 198], [503, 196], [504, 193], [505, 190], [506, 188], [507, 185], [508, 182], [509, 179], [510, 176], [511, 174], [512, 171], [513, 168], [514, 164], [515, 161], [516, 158], [517, 155], [518, 151], [519, 148], [520, 144], [521, 141], [522, 137], [523, 133], [524, 129], [525, 125], [526, 120], [527, 116], [528, 111], [529, 106], [530, 101], [531, 96], [532, 90], [533, 84], [534, 77], [535, 70], [536, 62], [537, 52], [538, 41], [539, 24], [540, 0]]
moveTypDict={0:[[1400,3700],[2000,3700],[2600,3700],[3200,3700],[3800,3700],
                [8800,3700],[8200,3700],[7600,3700],[7000,3700],[6400,3700]],
                1:[],2:[]}
######################################################################################
droneDict={};fischDict={};myScanList=[];enemyScanList=[];beforeScanList=[]
puffer,anzahlFische,anzahlMonster,runde=initMap("input",droneDict,fischDict,myScanList,enemyScanList,beforeScanList)

######################
######################
debug=True;startPosition="links"
#runde=1

while True:
    aktionList=aktionFestlegen(runde,droneDict,fischDict,myScanList,enemyScanList,beforeScanList,puffer,anzahlFische,xyBisherList,deepDict,moveDict,moveList,list600,list540,startPosition,moveTypDict)

    for aktion in aktionList:
        if len(aktion) == 2:
            print("WAIT {} {}".format(aktion[0],aktion[1]))
        else:
            print("MOVE {} {} {} {}".format(aktion[0],aktion[1],aktion[2],aktion[3]))


    runde+=1
    debug=False
    
    break
    if runde >= 15:
        break
    print("----------------------------------- runde:{}".format(runde),file=sys.stderr)
    for id,drone in droneDict.items():
        drone.x+=drone.moveX;drone.moveX=0
        drone.y+=drone.moveY;drone.moveY=0






    #print(distance(f2,dN))
print(distance([7238,9327],[6500,8984]))
print(distance([7238,9327],[6500+260,8984-74]))
print(distance([7238-420,9327-420],[6500+260,8984-74]))