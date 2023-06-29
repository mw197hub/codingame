#  https://www.codingame.com/ide/puzzle/the-helpdesk

import sys,math

def getWert(zwDict):
    ausgabe=""
    for nr in sorted(zwDict):
        wert = zwDict[nr]
        ausgabe+=str(wert)+" "
    return ausgabe


#3  1 1 1 21 1 1 1 1   0 0 0 2 0 0 0 0
worktime=40
eList=[0.5, 0.5, 0.5, 2.0, 0.5, 0.5, 0.5, 0.5]
hList=[180, 180, 180, 10, 180, 180, 180, 180, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

#4   1 2   0 1
worktime=20
eList=[1.0,2.0]
hList=[30,40,10]

#5    4 4 4 7 7 4     3 3 1 4 5 3
worktime=20
eList=[1.0, 0.5, 0.75, 1.25, 1.5, 1.0]
hList=[50, 50, 10, 50, 30, 20, 60, 30, 40, 40, 60, 60, 50, 10, 10, 10, 50, 10, 20, 70, 10, 40, 10, 40, 60, 40, 40, 40, 20, 70]

#6
worktime=20
eList=[0.5, 0.75, 1.0, 1.25, 0.5]
hList=[30, 40, 30, 40, 60, 10, 30, 40, 10, 20, 60, 30, 40, 70, 20, 60, 10, 70, 10, 20, 40, 51, 60, 40, 20]



#- When a counter is available, 
# it will instantly start with either helping the first visitor waiting in line,
#  or (if worktime minutes have passed) have a 10 minute break.


pos1=-1;pos2=-1;bisherPos=-1;nr=0
persDict={};breakDict={};timeDict={};arbeitDict={};bzDict={}
for i in range(len(eList)):
    persDict[i]=0;breakDict[i]=0;timeDict[i]=-100+i;arbeitDict[i]=0
for h in hList:    
    while True:
        newDict = sorted(timeDict.items(), key=lambda kv: kv[1])
        pos1=newDict[0][0];pos2=newDict[1][0]
        print("{}#h: {} pos: {}  {}".format(nr,h,pos1,timeDict),file=sys.stderr) 
        if nr == 24:
            a=0
        if arbeitDict[pos1] >= worktime:
            arbeitDict[pos1]=0
            timeDict[pos1]+=10
            breakDict[pos1]+=1    
    #    else:            
    #        if bisherPos > -1 and timeDict[pos1] == timeDict[bisherPos]:
    #            pos1 = bisherPos
    #        break            
    #    if nr == len(hList) - 1 and timeDict[pos1] == timeDict[pos2]:
    #        break
    #    bisherPos=pos1

        if nr == len(hList) - 1:
            for aPos,tWert in timeDict.items():
                if arbeitDict[aPos] >= worktime and timeDict[aPos] < timeDict[pos1]:
                    arbeitDict[aPos]=0
                    timeDict[aPos]+=10
                    breakDict[aPos]+=1 
        if (timeDict[pos1] <= timeDict[pos2])  or (arbeitDict[pos2]>=worktime and timeDict[pos1] <= timeDict[pos2]+10):
            break
    dauer=h/eList[pos1]
    arbeitDict[pos1]+=dauer
    timeDict[pos1] = dauer if timeDict[pos1] < 0 else timeDict[pos1]+dauer
    persDict[pos1]+=1
    nr+=1

print(getWert(persDict)[:-1])
print(getWert(breakDict)[:-1])
