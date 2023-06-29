#  https://www.codingame.com/ide/puzzle/the-helpdesk

import sys,math

def getWert(zwDict):
    ausgabe=""
    for nr in sorted(zwDict):
        wert = zwDict[nr]
        ausgabe+=str(wert)+" "
    return ausgabe
def getPos(persDict,timeDict):
    newDict = sorted(timeDict.items(), key=lambda kv: kv[1])
    return newDict[0][0],newDict[1][0]

#3
worktime=40
eList=[0.5, 0.5, 0.5, 2.0, 0.5, 0.5, 0.5, 0.5]
hList=[180, 180, 180, 10, 180, 180, 180, 180, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

#5    4 4 4 7 7 4     3 3 1 4 5 3
worktime=20
eList=[1.0, 0.5, 0.75, 1.25, 1.5, 1.0]
hList=[50, 50, 10, 50, 30, 20, 60, 30, 40, 40, 60, 60, 50, 10, 10, 10, 50, 10, 20, 70, 10, 40, 10, 40, 60, 40, 40, 40, 20, 70]

#6
#worktime=20
#eList=[0.5, 0.75, 1.0, 1.25, 0.5]
#hList=[30, 40, 30, 40, 60, 10, 30, 40, 10, 20, 60, 30, 40, 70, 20, 60, 10, 70, 10, 20, 40, 51, 60, 40, 20]



#- When a counter is available, 
# it will instantly start with either helping the first visitor waiting in line,
#  or (if worktime minutes have passed) have a 10 minute break.


aktPos=-1;nr=0
persDict={};breakDict={};timeDict={};arbeitDict={};bzDict={}
for i in range(len(eList)):
    persDict[i]=0;breakDict[i]=0;timeDict[i]=-100+i;arbeitDict[i]=0;bzDict[i]=False
for h in hList:    
    while True:
        aktPos,secPos=getPos(persDict,timeDict)    
        print("{}#h: {} pos: {} {}".format(nr,h,aktPos,timeDict),file=sys.stderr) 
        if arbeitDict[aktPos] >= worktime:
            breakDict[aktPos]+=1
            bzDict[aktPos]=False
            timeDict[aktPos]+=10   
            arbeitDict[aktPos]=0
            if nr == len(hList) - 1 and timeDict[aktPos] == timeDict[secPos]:
                break
           # if timeDict[aktPos] <= timeDict[secPos] -10:
           #     break
        else:
            break
    dauer=h/eList[aktPos]
    if timeDict[aktPos] < 0:
        timeDict[aktPos]=dauer
    else:
        timeDict[aktPos]+=dauer    
    persDict[aktPos]+=1
    arbeitDict[aktPos]+=dauer
    nr+=1
    
print(getWert(persDict)[:-1])
print(getWert(breakDict)[:-1])
