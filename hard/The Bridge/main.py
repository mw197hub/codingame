import sys
import math
import copy

def pruefeEnde(bikeDict,s,laneDict,erg,laengeLane):
    ende = False;move=erg
    if move == "SPEED":
        s+=1
    if move == "SLOW" and s > 0:
        s-=1
    if move == "UP":
        for bike,bPos in bikeDict.items():
            if bPos[2] == 1 and bPos[1] == 0:
                move = "WAIT"
    if move == "DOWN":
        for bike,bPos in bikeDict.items():
            if bPos[2] == 1 and bPos[1] == 3:
                move = "WAIT"
    anz = 0
    for bike,bPos in bikeDict.items():
        if bPos[2] == 1:
            newL = bPos[0]+s if bPos[0]+s < laengeLane else laengeLane -1
            if move == "JUMP":
                if "0" in laneDict[bPos[1]][newL]:
                    bPos[2] = 0
                else:
                    bPos[0] = bPos[0] +s
            elif move == "UP":
                if ("0" in laneDict[bPos[1]][bPos[0]:bPos[0]+s] or "0" in laneDict[bPos[1]-1][bPos[0]:bPos[0]+s]):
                    bPos[2] = 0
                else:
                    bPos[0] = bPos[0] +s;bPos[1] = bPos[1]-1
            elif move == "DOWN":
                if ("0" in laneDict[bPos[1]][bPos[0]:bPos[0]+s] or "0" in laneDict[bPos[1]+1][bPos[0]:bPos[0]+s]):                    
                    bPos[2] = 0
                else:
                    bPos[0] = bPos[0] +s;bPos[1] = bPos[1]+1
            else:
                if "0" in laneDict[bPos[1]][bPos[0]:newL+1]:
                    bPos[2] = 0
                else:
                    bPos[0] = bPos[0] +s
            if bPos[0] >= laengeLane -1:
                bPos[2] = 2
        if bPos[2] == 1:
            anz+=1
    if anz == 0:
        ende = True

    return ende,s,bikeDict

def sucheWeg(bikeDict,s,laneDict,v,laengeLane):
    moveList=["SPEED", "SLOW", "JUMP", "WAIT", "UP", "DOWN"]
    if v >= 3:
        moveList=["JUMP", "WAIT","SLOW","SPEED"]
    else:
        moveList=["JUMP","UP", "DOWN","SLOW","SPEED"]
    ergList=[]
    queue=[]
    for m in moveList:
        tList = [copy.deepcopy(bikeDict),s,m]
       # queue.append(tList)
        queue.insert(0,tList)
    
    while queue:
        path = queue.pop(0)
      #  print(path,file=sys.stderr)
        move = path[-1]
        bDict = path[0]
        speed = path[1]
        ende,speed,bDict = pruefeEnde(bDict,speed,laneDict,move,laengeLane)
        if ende:
            anz = 0
            for nr,bike in bDict.items():
                if bike[2] == 2:
                    anz+=1
            if anz >= v:
                path.append(move)
                return path
            else:
                a=0
        else:
            for move in moveList:
                if move == "SLOW" and speed <= 1:
                    keineAusfuehrung = 0
                else:
                    new_path = list(path)
                    new_path.append(move)
                    new_path[0] = copy.deepcopy(bDict)
                    new_path[1] = speed
                    #queue.append(new_path)
                    queue.insert(0,new_path)

    return ergList



m,v,laengeLane=1,1,30 #1
laneDict={0: ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 1: ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 2: ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '0', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 3: ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']}
bikeDict={0: [0, 2, 1]}
s= 1

m,v,laengeLane=4,4,56 #2
laneDict={0: ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '0', '0', '0', '.', '.', '.', '.', '.', '.', '0', '0', '0', '0', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '0', '0', '0', '0', '0', '0', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 1: ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '0', '0', '0', '.', '.', '.', '.', '.', '.', '0', '0', '0', '0', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '0', '0', '0', '0', '0', '0', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 2: ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '0', '0', '0', '.', '.', '.', '.', '.', '.', '0', '0', '0', '0', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '0', '0', '0', '0', '0', '0', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 3: ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '0', '0', '0', '.', '.', '.', '.', '.', '.', '0', '0', '0', '0', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '0', '0', '0', '0', '0', '0', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']}
bikeDict={0: [0, 0, 1], 1: [0, 1, 1], 2: [0, 2, 1], 3: [0, 3, 1]}
s=1

m,v,laengeLane=4,4,42 #3
laneDict={0: ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '0', '0', '0', '0', '0', '.', '.', '.', '.', '.', '.', '0', '0', '0', '0', '.', '.', '.', '.', '.', '0', '0', '.', '.', '.', '.', '.', '.'], 1: ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '0', '0', '0', '0', '0', '.', '.', '.', '.', '.', '.', '0', '0', '0', '0', '.', '.', '.', '.', '.', '0', '0', '.', '.', '.', '.', '.', '.'], 2: ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '0', '0', '0', '0', '0', '.', '.', '.', '.', '.', '.', '0', '0', '0', '0', '.', '.', '.', '.', '.', '0', '0', '.', '.', '.', '.', '.', '.'], 3: ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '0', '0', '0', '0', '0', '.', '.', '.', '.', '.', '.', '0', '0', '0', '0', '.', '.', '.', '.', '.', '0', '0', '.', '.', '.', '.', '.', '.']}
bikeDict={0: [0, 0, 1], 1: [0, 1, 1], 2: [0, 2, 1], 3: [0, 3, 1]}
s=8

m,v,laengeLane=4,4,36 #4
laneDict={0: ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '0', '0', '.', '.', '0', '0', '.', '.', '0', '0', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 1: ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '0', '0', '.', '.', '0', '0', '.', '.', '0', '0', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 2: ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '0', '0', '.', '.', '0', '0', '.', '.', '0', '0', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 3: ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '0', '0', '.', '.', '0', '0', '.', '.', '0', '0', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']}
bikeDict={0: [0, 0, 1], 1: [0, 1, 1], 2: [0, 2, 1], 3: [0, 3, 1]}
s=1

m,v,laengeLane=4,3,36 #5
laneDict={0: ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '0', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '0', '.', '.', '.', '.', '.', '.', '.', '.'], 1: ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '0', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '0', '.', '.', '.', '.', '.', '.', '.'], 2: ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '0', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '0', '.', '.', '.', '.', '.', '.'], 3: ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '0', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '0', '0', '0', '.', '.', '.', '.', '.', '.']}
bikeDict={0: [0, 0, 1], 1: [0, 1, 1], 2: [0, 2, 1], 3: [0, 3, 1]}
s=6

ergList = sucheWeg(bikeDict,s,laneDict,v,laengeLane)
print(ergList,file=sys.stderr)
for lane in laneDict:
    print(laneDict[lane],file=sys.stderr)


erg = "UP";runde=0
while True:
    #
    erg = ergList.pop(2)
    ende,s,bikeDict = pruefeEnde(bikeDict,s,laneDict,erg,laengeLane)
    print(str(runde) + " runde  " +erg)
    print(bikeDict,file=sys.stderr)
    runde+=1

    #
    outDict = copy.deepcopy(laneDict)
    for bike,bPos in bikeDict.items():
        if bPos[0] > laengeLane-1:
            bPos[0] = laengeLane -1
        if bPos[2] == 1:
            outDict[bPos[1]][bPos[0]] = ">"
        else:
            outDict[bPos[1]][bPos[0]] = "F" if bPos[0] >= laengeLane -1 else "x"
    
    for lane in outDict:
        print(outDict[lane],file=sys.stderr)
    if ende or runde == laengeLane:
        break