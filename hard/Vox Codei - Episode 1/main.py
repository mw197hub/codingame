#  https://www.codingame.com/ide/puzzle/vox-codei-episode-1

import sys,time
import math,copy

def ausgabeMap(mList):
    for m in mList:
        print(m,file=sys.stderr)
    print("------------------------------------------------------------",file=sys.stderr)

def setYX(y,x):
    return str(y)+"-"+str(x)
def getYX(yx):
    y,x = yx.split("-")
    return int(y),int(x)
def getExplo(y,x,mapList):
    tList=[]
    for yV in range(-1,-4,-1):
        if y+yV >= 0:
            if mapList[y+yV][x] == "#":
                break
            elif mapList[y+yV][x] == "@":
                tList.append(setYX(y+yV,x))
    for yV in range(1,4):
        if y + yV < len(mapList):
            if mapList[y+yV][x] == "#":
                break
            elif mapList[y+yV][x] == "@":
                tList.append(setYX(y+yV,x)) 
    for xV in range(-1,-4,-1):
        if x + xV >= 0:
            if mapList[y][x+xV] == "#":
                break
            elif mapList[y][x+xV] == "@":
                tList.append(setYX(y,x+xV))
    for xV in range(1,4):
        if x + xV < len(mapList[0]):
            if mapList[y][x+xV] == "#":
                break
            elif mapList[y][x+xV] == "@":
                tList.append(setYX(y,x+xV))    

    return copy.deepcopy(tList)

def erstelleBombList(mpList):
    bomb2List,test2Dict=[],{}
    for y in range(len(mpList)):
        for x in range(len(mpList[0])):
            if mpList[y][x] == "@":
                bomb2List.append(setYX(y,x))
            elif mpList[y][x] == ".":
                testList = getExplo(y,x,mpList)
                if len(testList) > 0:
                    test2Dict[setYX(y,x)] = testList
    return copy.deepcopy(bomb2List),copy.deepcopy(test2Dict)

def sucheErg(yx,startList,mList,bombs,badList):
    fertig = False;ergList=[];ergDict={}
    for i in range(bombs):
        ergList.append(yx)
        ergDict[yx] = copy.deepcopy(startList)
        for s in startList:
            y,x = getYX(s)
            mList[y][x] = "."
        ausgabeMap(mList)
        bList,tDict = erstelleBombList(mList)
        if len(bList) == 0:
            fertig = True
            break
        for w in sorted(tDict, key=lambda k: len(tDict[k]), reverse=True):
            if not w in badList:
                startList = copy.deepcopy(tDict[w])
                yx = w
                break
    return ergList,ergDict,fertig


# bomb 3 gerade in alle 4 Richtungen

mapList=[['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '#', '.', '.', '.', '@', '.', '.', '.', '#', '.', '.', '.'], ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '#', '.', '@', '.', '#', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '#', '.', '#', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '@', '.', '@', '.', '.', '.', '@', '.', '@', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '#', '.', '#', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '#', '.', '@', '.', '#', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.'], ['.', '.', '.', '#', '.', '.', '.', '@', '.', '.', '.', '#', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]
rounds,bombs=15,4  # test11

#mapList=[['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '#', '@', '@', '@', '.', '#', '@', '@', '@', '.', '.'], ['.', '@', '.', '.', '.', '.', '@', '.', '.', '.', '.', '.'], ['.', '@', '.', '.', '.', '.', '@', '.', '.', '.', '.', '.'], ['.', '@', '.', '.', '.', '.', '@', '.', '.', '@', '#', '.'], ['.', '@', '.', '.', '.', '.', '@', '.', '.', '.', '@', '.'], ['.', '.', '@', '@', '@', '.', '.', '@', '@', '@', '#', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]
#rounds,bombs=15,6  # test10

mapList=[['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '#', '#', '.', '.', '.', '.', '#', '#', '.', '.'], ['.', '#', '@', '@', '#', '.', '.', '#', '@', '@', '#', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '#', '@', '@', '#', '.', '.', '#', '@', '@', '#', '.'], ['.', '.', '#', '#', '.', '.', '.', '.', '#', '#', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]
rounds,bombs=15,4   #t test7

mapList=[['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '@', '.'], ['@', '@', '@', '.', '@', '@', '@', '@'], ['.', '.', '.', '.', '.', '.', '@', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.']]
rounds,bombs=10,2


startTime = time.time()
bombList=[];testDict={}
bombList,testDict = erstelleBombList(mapList)
#print('{:5.3f}s'.format(time.time() - startTime,file=sys.stderr))

#print("------- " + str(len(bombList)),file=sys.stderr)
#print(bombList,file=sys.stderr)
#print("------- " + str(len(testDict)),file=sys.stderr)
testList = sorted(testDict, key=lambda k: len(testDict[k]), reverse=True)
print(testDict,file=sys.stderr)

ergList={};badList=[]
for test in sorted(testDict, key=lambda k: len(testDict[k]), reverse=True):    
    ergList,ergDict,fertig = sucheErg(test,testDict[test],copy.deepcopy(mapList),bombs,badList)
    if fertig:
        break
    badList.append(test)
print(ergList)


# fuers Spiel:

'''
while True:
    # rounds: number of rounds left before the end of the game
    # bombs: number of bombs left
    rounds, bombs = [int(i) for i in input().split()]
    print(str(rounds) + "  bombs: " + str(bombs),file=sys.stderr)    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    bombList=[];testDict={}
    if runde == 0:
        bombList,testDict = erstelleBombList(mapList)
        badList=[]
        for test in sorted(testDict, key=lambda k: len(testDict[k]), reverse=True):    
            ergList,ergDict,fertig = sucheErg(test,testDict[test],copy.deepcopy(mapList),bombs,badList)
            if fertig:
                break
            badList.append(test)
        print(ergList,file=sys.stderr)
    
    if len(ergList) > 0:
        setBomb = False
        for i in range(len(ergList)):
            yx = ergList[i]
            y,x = getYX(yx)
            if mapList[y][x] == ".":
                y,x = getYX(ergList.pop(0))
                print(str(x)+" "+str(y))
                remDict[runde+3] = ergDict[yx]
                setBomb = True
                break
        if not setBomb:
            print("WAIT")
    else:
        print("WAIT")
    if runde in remDict:
        remList = remDict[runde]
        for r in remList:
            y,x = getYX(r)
            mapList[y][x] = "."
    runde+=1
'''
