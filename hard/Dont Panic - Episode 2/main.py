#  https://www.codingame.com/ide/puzzle/don't-panic-episode-2

import sys,math,copy,time
from itertools import permutations
from itertools import combinations

def getAktPos(gList,aktFloor,aktPos,aktDirection,elevatorDict,nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators,zwangEleDict,deathDict):
    aPos,aDirection=aktPos,aktDirection
    for i in range(len(gList)):
        if gList[i] == "ZWANG":
            aPos=zwangEleDict[i]
        if gList[i] == "BLOCK":
            aDirection = "LEFT" if aDirection=="RIGHT" else "RIGHT"
        if gList[i] == "ELEVATOR":
            if i+1 in deathDict:
                lrList = deathDict[i+1]
                pos = lrList[0] if aDirection == "RIGHT" else lrList[1]  
                if aDirection == "LEFT" and aPos < pos:
                    pos = -1
                if aDirection == "RIGHT" and aPos > pos:
                    pos = -1              
                if not pos == -1:
                    pos = pos +1 if aDirection == "RIGHT" else pos -1
                    aPos = pos                   
        if gList[i] == "WAIT" or gList[i] == "BLOCK":
            posList=[]
            if i in zwangEleDict:
                posList=zwangEleDict[i]
            elif i in elevatorDict:
                posList=elevatorDict[i]
            if aDirection == "RIGHT":
                for p in sorted(posList,reverse=False):
                    if p >= aPos:
                        aPos=p;break
            else:
                for p in sorted(posList,reverse=True):
                    if p <= aPos:
                        aPos=p;break

    return aPos,aDirection

def getBlockWait(floor,gList,weg,aktFloor,aktPos,aktDirection,elevatorDict,nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators,zwangEleDict,deathDict):
    posList=[]
    anzElev=0
    for g in gList:
        if g == "ELEVATOR":
            anzElev+=1
    anzFrei=nb_additional_elevators-len(zwangEleDict)-anzElev

    anfang,ende=-1,-1
    if weg == "LEFT":
        anfang,ende=1,width//2 +width//10
    else:
        anfang,ende=width//2 -width//10,width-1

    if floor in zwangEleDict:
        posList=zwangEleDict[floor]
    elif floor in elevatorDict:
        posList=elevatorDict[floor]
    if len(posList) == 0:
        if anzFrei > 0:
            return ["WAIT","BLOCK","ELEVATOR"]
        else:
            return ["WAIT","BLOCK"]


    aPos,aDirection = getAktPos(gList,aktFloor,aktPos,aktDirection,elevatorDict,nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators,zwangEleDict,deathDict)
        
    block=True;diff1,diff2=999,999
    for p in posList:
        if aDirection == "RIGHT":
            if aPos <= p:
                diff1=p-aPos 
                block=False
            else:
                diff2=aPos-p+3
        else:
            if aPos >= p:
                diff1=aPos-p
                block=False
            else:
                diff2=p-aPos+3
    if diff2 < diff1:
        block=True
    if diff1 < 999 and diff2 < 999:
        if anzFrei > 0:
            if diff1 < diff2:
                return ["WAIT","BLOCK","ELEVATOR"]
            else:
                return ["BLOCK","WAIT","ELEVATOR"]
        else:
            return ["WAIT","BLOCK"]
    if diff1 == 999:
        if anzFrei > 0:
            if diff2 > width // 2  and diff2 > 15:
                return ["ELEVATOR"]
            else:
                return ["BLOCK","ELEVATOR"]
        else:
            return ["BLOCK"]
    if diff2 == 999:
        if anzFrei > 0:
            if diff1 > width // 2  and diff1 > 15:
                return ["ELEVATOR"]
            else:
                return ["WAIT","ELEVATOR"]
        else:
            return ["WAIT"]
    if anzFrei > 0:
        return ["WAIT","BLOCK","ELEVATOR"]
    else:
        return ["WAIT","BLOCK"]


def erstelleGraph(aktFloor,aktPos,aktDirection,eList,bList,elevatorDict,nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators,zwangEleDict):
    deathDict=getDeathDict(aktFloor,aktPos,aktDirection,eList,bList,elevatorDict,nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators,zwangEleDict)

    graph={};befhlDict={0:"WAIT",1:"BLOCK",2:"ELEVATOR"}
    gesamtList=[];ergList=[]
    if 0 in elevatorDict:        
        moegliche = getBlockWait(0,[],"start",aktFloor,aktPos,aktDirection,elevatorDict,nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators,zwangEleDict,deathDict)
        for m in moegliche:
            gesamtList.append([m])
    else:
        gesamtList.append(["ELEVATOR"])

    wegRichtung=["LEFT"]  # ["LEFT","RIGHT"]    
    lastLevel = 0 if len(zwangEleDict) > 0 else 1
    for weg in wegRichtung:
        for i in range(1,exit_floor+lastLevel):
            if i in zwangEleDict:
                graph[i] = ["ZWANG"]
                for gList in gesamtList:
                    gList.append("ZWANG")
            elif (not i in elevatorDict and i < exit_floor):
                graph[i] = ["ELEVATOR"]
                for gList in gesamtList:
                    gList.append("ELEVATOR")
            else:
                graph[i]= ["WAIT","BLOCK"]   
                ersatzList=gesamtList[:];gesamtList.clear()
            #  if i in elevatorDict and len(elevatorDict[i] > 1):                
                for gList in ersatzList:
                    moegliche = getBlockWait(i,gList,weg,aktFloor,aktPos,aktDirection,elevatorDict,nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators,zwangEleDict,deathDict)
                    for m in moegliche:
                        gList1=gList[:];gList1.append(m)
                        gesamtList.append(gList1)

    
    print(len(gesamtList),file=sys.stderr)    
    a=0
    #perm = list(combinations(range(8),3))
    #print(len(perm),file=sys.stderr)

    for gList in gesamtList:
        if gList == ['ELEVATOR', 'BLOCK', 'WAIT', 'ELEVATOR', 'ELEVATOR', 'BLOCK', 'WAIT', 'WAIT', 'WAIT', 'BLOCK', 'ZWANG']: #8
        #if combi == ['ELEVATOR', 'WAIT', 'WAIT', 'BLOCK', 'WAIT', 'WAIT', 'BLOCK', 'ELEVATOR', 'WAIT', 'ZWANG', 'ZWANG']: #10
            print(gList)

        eList,bList,runde,fertig = erstelleListen(aktFloor,aktPos,aktDirection,eList,bList,elevatorDict,nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators,zwangEleDict,gList,deathDict)
        if fertig and runde < nb_rounds:
            return eList,bList
        elif fertig:            
            # print("{}: {}".format(runde,combi),file=sys.stderr)
            ergList.append([runde,eList,bList])   
    return [],[]

class clone:
    def __init__(self,runde,floor,pos,direction):
        self.aktiv=True;self.runde=runde;self.direction=direction;self.funktion=0;self.pos=pos;self.floor=floor

def moveClone(cloneList,action,elevatorDict,nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators,blockDict):
    firstClone=True;fertig=False
    for cl in cloneList:
        if cl.aktiv:
            if firstClone and (action == "BLOCK" or action == "ELEVATOR"):
                firstClone=False
             #   print("{},{},{}".format(cl.floor,cl.pos,cl.direction),file=sys.stderr)
                if cl.floor == exit_floor and cl.pos == exit_pos:
                    fertig = True
                else:
                    cl.funktion=1
                    cl.aktiv=False
                    if action == "BLOCK":
                        if cl.floor in blockDict:
                            blockDict[cl.floor].append(cl.pos)
                        else:
                            blockDict[cl.floor] = [cl.pos]
                    else:
                        if cl.floor in elevatorDict:
                            elevatorDict[cl.floor].append(cl.pos)
                        else:
                            elevatorDict[cl.floor] = [cl.pos]
            else:
                if firstClone:
                    firstClone=False
                 #   print("{},{},{}".format(cl.floor,cl.pos,cl.direction),file=sys.stderr)                               
                if cl.floor == exit_floor and cl.pos == exit_pos:
                    fertig = True
                else:
                    rest=True     
                    bList = blockDict[cl.floor] if cl.floor in blockDict else []
                    for b in bList:
                        if b == cl.pos:
                            cl.direction = "LEFT" if cl.direction == "RIGHT" else "RIGHT"   
                            cl.pos = cl.pos + 1 if cl.direction == "RIGHT" else cl.pos -1                            
                            rest=False                    
                    if rest:
                        eList = elevatorDict[cl.floor] if cl.floor in elevatorDict else []
                        for e in eList:
                            if e == cl.pos:
                                cl.floor += 1
                                rest=False
                    if rest:
                        cl.pos = cl.pos + 1 if cl.direction == "RIGHT" else cl.pos -1
                    #    bList = blockDict[cl.floor] if cl.floor in blockDict else []
                    #    for b in bList:
                    #        if b == cl.pos:
                    #            cl.direction = "LEFT" if cl.direction == "RIGHT" else "RIGHT"
                    #            cl.pos = cl.pos + 2 if cl.direction == "RIGHT" else cl.pos -2
                if cl.pos < 0 or cl.pos >= width:
                    cl.aktiv=False
    return fertig

def testLauf(eList,bList,elevatorDict,nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators):
    cloneList=[];blockDict={}
    runde=0;action="WAIT"
    while True:
        if runde == 116:
            a=0

        if runde%3 == 0 and len(cloneList) < nb_total_clones:
            cloneList.append(clone(runde,clone_floor,clone_pos,direction))
        firstFloor=-1;firstPos=0;firstDiction="RIGHT"
        for cl in cloneList:
            if cl.aktiv:
                firstFloor=cl.floor;firstPos=cl.pos;firstDiction=cl.direction
                break        
        if firstFloor == -1 and len(cloneList) == nb_total_clones -1:
            return runde,False
        
        if [firstFloor,firstPos] in eList or [firstFloor,-1] in eList:
            if [firstFloor,firstPos] in eList:
                eList.remove([firstFloor,firstPos])
            else:
                eList.remove([firstFloor,-1])
            action = "ELEVATOR"
        elif [firstFloor,firstPos] in bList or [firstFloor,-1] in bList:
            if [firstFloor,firstPos] in bList:
                bList.remove([firstFloor,firstPos])
            else:
                bList.remove([firstFloor,-1])
            action = "BLOCK"
        else:
            action = "WAIT"

      #  print("{}: {},{},{} => {}".format(runde,firstFloor,firstPos,firstDiction,action),file=sys.stderr)
        if moveClone(cloneList,action,elevatorDict,nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators,blockDict):
            return runde,True
        runde+=1
        if runde+1 > nb_rounds*2:
            return runde,False

def erstelleListen(aktFloor,aktPos,aktDirection,eList,bList,elevatorDict,nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators,zwangEleDict,gList,deathDict):

    eList,bList=[],[]
    for i in range(len(gList)):
        if gList[i] == "ZWANG":
            eList.append([i,zwangEleDict[i]])
            aktPos=zwangEleDict[i]
        if gList[i] == "BLOCK":
            bList.append([i,-1])
            aktDirection = "LEFT" if aktDirection=="RIGHT" else "RIGHT"
        if gList[i] == "ELEVATOR":
            if i+1 in deathDict:
                lrList = deathDict[i+1]
                pos = lrList[0] if aktDirection == "RIGHT" else lrList[1]  
                if aktDirection == "LEFT" and aktPos < pos:
                    pos = -1
                if aktDirection == "RIGHT" and aktPos > pos:
                    pos = -1              
                if not pos == -1:
                    pos = pos +1 if aktDirection == "RIGHT" else pos -1
                    aktPos = pos                   
                eList.append([i,pos])
            else:
                eList.append([i,-1])
        if gList[i] == "WAIT" or gList[i] == "BLOCK":
            posList=[]
            if i in zwangEleDict:
                posList=zwangEleDict[i]
            elif i in elevatorDict:
                posList=elevatorDict[i]
            if aktDirection == "RIGHT":
                for p in sorted(posList,reverse=False):
                    if p >= aktPos:
                        aktPos=p;break
            else:
                for p in sorted(posList,reverse=True):
                    if p <= aktPos:
                        aktPos=p;break


    eSavList=eList[:];bSavList=bList[:]
    runde, fertig = testLauf(eList,bList,copy.deepcopy(elevatorDict),nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators)
    #print("{} - {}".format(runde+1,fertig),file=sys.stderr)
    #print(eSavList,file=sys.stderr)
    #print(bSavList,file=sys.stderr)
    return eSavList,bSavList,runde,fertig


def test2(aktFloor,aktPos,aktDirection,eList,bList,elevatorDict,nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators,zwangEleDict,gList):
    #eList,bList=[],[[0,aktPos]];aktDirection="LEFT"
    eList,bList=[],[]
    for i in range(exit_floor+1):
        if i == 2:
            a=0
        if (not i in elevatorDict and not i in zwangEleDict) and i < exit_floor:
            eList.append([i,-1])
        else:
            if i == exit_floor:
                if aktDirection == "RIGHT":
                    if aktPos > exit_pos:
                        bList.append([i,aktPos])
                        aktDirection = "LEFT" if aktDirection == "RIGHT" else "RIGHT"
                else:
                    if aktPos < exit_pos:
                        bList.append([i,aktPos])
                        aktDirection = "LEFT" if aktDirection == "RIGHT" else "RIGHT"
            else:
                posList=[]
                if i in zwangEleDict:
                    posList=zwangEleDict[i]
                elif i in elevatorDict:
                    posList=elevatorDict[i]
                block=True;diff1,diff2=99,99
                for p in posList:
                    if aktDirection == "RIGHT":
                        if aktPos <= p:
                            diff1=p-aktPos 
                            block=False
                        else:
                            diff2=aktPos-p+3
                    else:
                        if aktPos >= p:
                            diff1=aktPos-p
                            block=False
                        else:
                            diff2=p-aktPos+3
                if diff2 < diff1:
                    block=True
                if block:
                    bList.append([i,aktPos])
                    aktDirection = "LEFT" if aktDirection == "RIGHT" else "RIGHT"
                if aktDirection == "RIGHT":
                    for p in sorted(posList,reverse=False):
                        if p >= aktPos:
                            aktPos=p;break
                else:
                    for p in sorted(posList,reverse=True):
                        if p <= aktPos:
                            aktPos=p;break

    eSavList=eList[:];bSavList=bList[:]
    runde, fertig = testLauf(eList,bList,copy.deepcopy(elevatorDict),nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators)
    print("{} - {}".format(runde+1,fertig),file=sys.stderr)
    
    
    print(eSavList,file=sys.stderr)
    print(bSavList,file=sys.stderr)
    return eSavList,bSavList


def getDeathDict(aktFloor,aktPos,aktDirection,eList,bList,elevatorDict,nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators,zwangEleDict):
    deathDict={}
    if len(zwangEleDict) > 0:
        posL,posR = exit_pos,exit_pos
        for i in range(exit_floor,-1,-1):
            if not i in elevatorDict:
                break
            evList = sorted(elevatorDict[i])
            anfang=-1;ende=-1
            for e in evList:
                if e >= posR:
                    ende=e
                    posR=e;break
            for e in sorted(evList,reverse=True):
                if e <= posL:
                    anfang=e
                    posL=e;break
            if anfang > -1 or ende > -1:
                deathDict[i]=[anfang,ende]
                if anfang == -1:
                    posL = -1
                if ende == -1:
                    posR = 999                
            else:
                break
    return deathDict

##########################
#1
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators=2,13,100,1,11,10,1,0
elevatorDict={}
clone_floor,clone_pos,direction=0,2,"RIGHT"
# 4
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators=6,13,100,5,1,10,2,3
elevatorDict={2: [7], 0: [4], 4: [1]}
clone_floor,clone_pos,direction=0,10,"RIGHT"

#nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators=2,13,100,1,2,10,1,0
#elevatorDict={}
#clone_floor,clone_pos,direction=0,9,"RIGHT"

#nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators=7,13,30,6,7,10,3,3
#elevatorDict={2: [6], 0: [6], 3: [7]}
#clone_floor,clone_pos,direction=0,4,"RIGHT"

#6
#nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators=10,19,47,9,9,41,0,17
#elevatorDict={8: [9], 1: [4, 17], 7: [17, 4], 4: [3, 9], 6: [9, 3], 2: [9, 3], 0: [3, 9], 5: [4, 17], 3: [4, 17]}
#clone_floor,clone_pos,direction=0,6,"RIGHT"
#7
#nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators=10,19,42,9,9,41,1,16
#elevatorDict={8: [9], 1: [4, 17], 7: [17, 4], 4: [3, 9], 6: [9, 3], 2: [9, 3], 0: [3, 9], 5: [4, 17], 3: [17]}
#clone_floor,clone_pos,direction=0,6,"RIGHT"
#8
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators=13,36,67,11,12,41,4,34
elevatorDict={4: [34, 23, 9], 10: [23, 34, 3], 8: [1, 23, 34, 9], 5: [34, 4], 3: [17, 34], 6: [13, 22, 34], 7: [17, 34], 1: [24, 17, 4, 34], 11: [11, 13, 4], 9: [34, 2, 17], 2: [23, 3, 34, 24], 0: [34]}
clone_floor,clone_pos,direction=0,6,"RIGHT"
#9
#nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators=13,69,79,11,39,8,5,30
#elevatorDict={11: [42, 13, 4, 38, 11], 8: [1, 66, 9, 34, 23, 56], 1: [34, 17, 50, 4, 24], 3: [17], 10: [23, 3], 2: [24, 3, 23, 58], 6: [57, 34, 13, 65], 5: [46, 4], 7: [17]}
#clone_floor,clone_pos,direction=0,33,"RIGHT"
#10
#nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators=13,69,109,11,47,100,4,36
#elevatorDict={1: [62, 24, 17, 36, 4, 50], 9: [17, 2], 6: [23, 9, 35, 3], 2: [43, 9, 23, 3, 24, 56], 3: [24, 60, 17, 30], 8: [63, 1, 23, 9], 5: [4], 7: [48], 4: [23, 9], 10: [3, 23, 45], 11: [50, 45, 4]}
#clone_floor,clone_pos,direction=0,6,"RIGHT"



 # "WAIT" "BLOCK" 'ELEVATOR"   = 0,1,2
startZeit=time.time()

freiFloorsList=[];exitBlock=False
zwangEleDict={}
for i in range(exit_floor+1):
    if not i in elevatorDict:
        freiFloorsList.append(i)
    if i == exit_floor and i in elevatorDict:
        evList = sorted(elevatorDict[i])
        if not i-1 in elevatorDict:
            zwangEleDict[i-1] = exit_pos
        else:
            anfang=-1;ende=-1
            for e in evList:
                if e < exit_pos:
                    anfang = e
                if e > exit_pos and ende == -1:
                    ende = e
            exitBlock=True
            for e in elevatorDict[i-1]:
                if e > anfang and e < ende:
                    exitBlock=False
            if exitBlock:
                zwangEleDict[i-1] = exit_pos
if len(zwangEleDict) > 0:
    if not exit_floor -2 in elevatorDict:
        zwangEleDict[i-2] = exit_pos
    else:
        evList = sorted(elevatorDict[i-1])
        anfang=-1;ende=-1
        for e in evList:
            if e < exit_pos:
                anfang = e
            if e > exit_pos and ende == -1:
                ende = e
        exitBlock=True
        for e in elevatorDict[i-2]:
            if e > anfang and e < ende:
                exitBlock=False
        if exitBlock:
            zwangEleDict[i-2] = exit_pos



#rechts oder links
aktFloor,aktPos,aktDirection=clone_floor,clone_pos,direction
#eList,bList=[[0,1]],[[0,5],[1,1]]
eList,bList=[],[]
eList,bList = erstelleGraph(aktFloor,aktPos,aktDirection,eList,bList,copy.deepcopy(elevatorDict),nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators,zwangEleDict)

print(eList,file=sys.stderr)
print(bList,file=sys.stderr)


print(time.time()-startZeit)