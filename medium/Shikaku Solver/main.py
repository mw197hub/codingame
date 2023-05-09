# https://www.codingame.com/ide/puzzle/shikaku-solver

import sys,math,string,copy,time
from itertools import permutations

def ausgabeYXList(yxList):
    for xList in yxList:
        for x in xList:
            print(x,end="")
        print("")
    print("--------------------------")

def setYX(y,x):
    return str(y)+"-"+str(x)
def getYX(wert):
    yx = wert.split("-")
    return int(yx[0]),int(yx[1])
def getRechtecke(wert):
    wertList=[]
    testList=(list(permutations(range(1,wert+1), 2)))
    for test in testList:
        if test[0]*test[1] == wert:
            wertList.append(test)
    if math.sqrt(wert) == int(math.sqrt(wert)):
        wertList.append((int(math.sqrt(wert)),int(math.sqrt(wert))))
    return wertList[:]


def suchePunkte(maxX,maxY,y,x,wertDict,punktDict,yxList,punktVerwendet,yxRechtecke):
    optDict={}
    punktList = yxRechtecke[setYX(y,x)]
    for punkt in punktList:
        if not punkt in punktVerwendet:
            wert = punktDict[punkt]
            wList = wertDict[wert]
            yP,xP = getYX(punkt)
        #  optDict[punkt] = []
            absY = abs(y-yP);absX = abs(x-xP)
            #print("yx: {} {}".format(absY,absX),file=sys.stderr)
            for w in wList:            
                if absY < w[0] and absX < w[1] and absY <= maxY and absX <= maxX and y+w[0] <= maxY and x+w[1] <= maxX:
                    leer=True;punkteDa=0
                    for y1 in range(y,y+w[0]):
                        for x1 in range(x,x+w[1]):
                            if not yxList[y1][x1] == " ":
                                leer = False;break
                            if gitterList[y1][x1] > 0:
                                if punkt == setYX(y1,x1):
                                    punkteDa = punkteDa + punktDict[punkt]  
                                else:
                                    punkteDa = -9999;leer=False;break
                        if not leer:
                            break              
                    if leer and punkteDa == punktDict[punkt]:
                        if not punkt in optDict:
                            optDict[punkt] = [w]
                        else:
                            optDict[punkt].append(w)

    #print(optDict,file=sys.stderr)
    return optDict


def zero(abcList,wertDict,punktDict,yxList,maxY,maxX,punktVerwendet,yxRechtecke):
    y,x=0,0
    for y1 in range(maxY):
        for x1 in range(maxX):
            if yxList[y1][x1] == " ":
                #print("{} {}".format(y1,x1),file=sys.stderr)
                optDict = suchePunkte(maxX,maxY,y1,x1,wertDict,punktDict,yxList,punktVerwendet,yxRechtecke)
                if len(optDict) > 0:
                    return y1,x1,optDict
                return -1,-1,{}
    return None,None,{}

def solve(maxX,maxY,gitterList,abcList,wertDict,punktDict,yxList,anzahl,lastABC,punktVerwendet,yxRechtecke):
    anzahl[1]+=1
    y,x,optDict = zero(abcList,wertDict,punktDict,yxList,maxY,maxX,punktVerwendet,yxRechtecke)
    if y == None:
        if anzahl[0] >= 0:
            anzahl.append(copy.deepcopy(yxList))
        anzahl[0]+=1     
        return False
    #lastABC.append(abc)
    a=0
    for punkt,koordList in optDict.items():
        punktVerwendet.append(punkt)
        for koord in koordList:
            abc = abcList.pop(0);leer=True;punkteDa=0
            for y1 in range(y,y+koord[0]):
                for x1 in range(x,x+koord[1]):
                    yxList[y1][x1] = abc
           # ausgabeYXList(yxList)
            if solve(maxX,maxY,gitterList,abcList,wertDict,punktDict,yxList,anzahl,lastABC,punktVerwendet,yxRechtecke):
                return True
            abcList.insert(0,abc)
            for y1 in range(maxY):
                for x1 in range(maxX):
                    if yxList[y1][x1] == abc:
                        yxList[y1][x1] = " "
                a=0
        punktVerwendet.remove(punkt)
    return False

#5    = 16
w,h=30,30
gitterList=[[6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 45, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 6, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 0, 0, 0, 0], [0, 0, 15, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 0, 0, 0, 0, 0, 0, 0, 0, 6, 8, 0, 0, 6, 0, 0, 15, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 308, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 0, 0, 0, 0, 0, 8, 6, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 0, 0, 8, 0, 15, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 16, 0, 0, 0, 0, 0, 0, 6, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 9, 0, 0, 0, 9, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 96, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

#1   = 1
w,h=10,10
gitterList=[[0, 0, 0, 0, 0, 0, 0, 0, 9, 0], [0, 0, 0, 0, 0, 0, 9, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 20, 0, 0, 8, 0, 0, 0, 6, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 6, 0, 0, 6, 0, 0, 0], [10, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 6, 0, 6, 0, 0, 0, 8, 0], [0, 0, 0, 0, 0, 0, 6, 0, 0, 0]]
#2   = 20
#w,h=15,20
#gitterList=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0], [0, 8, 0, 0, 0, 6, 0, 0, 6, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 10, 0, 0, 0, 0, 6, 0, 6, 0, 0, 0, 0], [0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0], [0, 0, 0, 14, 0, 0, 9, 0, 0, 0, 6, 0, 0, 0, 0], [0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 12, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0], [0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 14, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 24], [0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 6, 0, 0], [0, 0, 0, 9, 0, 0, 6, 0, 0, 28, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 15, 0, 6, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
#3    = 
w,h=20,20
gitterList=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 65, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0], [18, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 6, 0, 0, 0, 0, 0, 6], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0], [0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 6, 8, 0, 0, 0], [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 8, 0, 6, 0, 0, 8, 0, 0, 6, 0, 0, 0, 0, 0, 0], [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 6, 0, 0, 0, 8], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 6, 0, 0, 0, 6, 0, 0, 0, 12, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 16, 0, 0, 10, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0], [0, 0, 0, 0, 0, 9, 0, 9, 0, 0, 0, 0, 0, 6, 0, 0, 8, 0, 8, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0], [0, 0, 0, 0, 0, 0, 26, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0]]


startTime=time.time()

yxList=[[ ' ' for x in range(w)] for y in range(h)]
abcList=list(string.ascii_uppercase) + list(string.ascii_lowercase)
wertDict={};punktDict={}
for y in range(len(gitterList)):
    xList = gitterList[y]
    for x in range(len(xList)):
        wert = xList[x]
        if wert > 0 and not wert in wertDict:
            wertDict[wert] = getRechtecke(wert)
        if wert > 0:
            punktDict[setYX(y,x)] = wert
#print(punktDict,file=sys.stderr)

yxRechtecke={}
for y in range(h):
    for x in range(w):
        if x == 9:
            a=0
        for punkt,wert in punktDict.items():
            wList = wertDict[wert]
            yP,xP = getYX(punkt)
        #  optDict[punkt] = []
            absY = abs(y-yP);absX = abs(x-xP)
            #print("yx: {} {}".format(absY,absX),file=sys.stderr)
            for wl in wList:            
                if absY < wl[0] and absX < wl[1] and absY <= h and absX <= w: # and y+wl[0] <= h and x+wl[1] <= w:
                        yxW = setYX(y,x)
                        if not yxW in yxRechtecke:
                            yxRechtecke[yxW] = [punkt]
                        else:
                            if not punkt in yxRechtecke[yxW]:
                                yxRechtecke[yxW].append(punkt)
#print(yxRechtecke,file=sys.stderr)

anzahl=[0,0];lastABC=[];punktVerwendet=[]
solve(w,h,gitterList,abcList,wertDict,punktDict,yxList,anzahl,lastABC,punktVerwendet,yxRechtecke)

yxString=" ".join(map(str,anzahl[2]))
yxList = anzahl[2]
for i in range(3,len(anzahl)):
    nString=" ".join(map(str,anzahl[i]))
    if nString < yxString:
        yxList = anzahl[i]
        yxString=nString



print(anzahl[0])
for xList in yxList:
    for x in xList:
        print(x,end="")
    print("")
print("Zeit: {}".format(time.time()-startTime),file=sys.stderr)
print(anzahl[1],file=sys.stderr)


exit(0)
yxList = anzahl[2]
print(anzahl[0])
for i in range(2,len(anzahl)):
    yxList = anzahl[i]
    for xList in yxList:
        for x in xList:
            print(x,end="")
        print("")
    print("---------------------")
print("Zeit: {}".format(time.time()-startTime),file=sys.stderr)
print(anzahl[1],file=sys.stderr)