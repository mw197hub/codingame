#  https://www.codingame.com/ide/puzzle/the-helpdesk

import sys,math

def getNummer(eDict,eList,pos,worktime,reihenfolge,lastWert):
    nr = -1
    while True:
        wert=999999;anzahl=0;pause=False
        #pos=0
        for i in range(len(eList)):            
            wList = eDict[pos]
            if wList[6] < wert:
                nr=pos;wert=wList[6];anzahl=1
                if wList[5]:
                    pause=True
            elif wList[6] == wert:
                anzahl+=1
                if wList[5]:
                    pause=True
            pos= 0 if pos == len(eList)-1 else pos+1
        wList = eDict[nr]
        if wList[2] >= worktime:
            if nr == 1:
                a=0
            wList = eDict[nr]
            wList[2] = 0;wList[5]=True;wList[6]+=10
            wList[4]+=1
            reihenfolge+=" ("+str(nr)+")"
        else:
            break

    return nr,reihenfolge

#1    1 4     0 0
worktime=100
eList=[1.0, 1.0]
hList=[40, 16, 12, 8, 4]

#3
#worktime=40
#eList=[0.5, 0.5, 0.5, 2.0, 0.5, 0.5, 0.5, 0.5]
#hList=[180, 180, 180, 10, 180, 180, 180, 180, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

#4   1 2    0 1
worktime=20
eList=[1.0, 2.0]
hList=[30, 40, 10]

#5    4 4 4 7 7 4     3 3 1 4 5 3
#worktime=20
#eList=[1.0, 0.5, 0.75, 1.25, 1.5, 1.0]
#hList=[50, 50, 10, 50, 30, 20, 60, 30, 40, 40, 60, 60, 50, 10, 10, 10, 50, 10, 20, 70, 10, 40, 10, 40, 60, 40, 40, 40, 20, 70]

#6    3 6 8 6 2   2 4 5 4 1
#worktime=20
#eList=[0.5, 0.75, 1.0, 1.25, 0.5]
#hList=[30, 40, 30, 40, 60, 10, 30, 40, 10, 20, 60, 30, 40, 70, 20, 60, 10, 70, 10, 20, 40, 51, 60, 40, 20]

#- When a counter is available, 
# it will instantly start with either helping the first visitor waiting in line,
#  or (if worktime minutes have passed) have a 10 minute break.

eDict = {}
for i in range(len(eList)):
    eDict[i] = [eList[i],0,0,0,0,False,i-1000] # effizienz, worktime gesamt, worktime seit pause, erledigt, pausen, pause-gerade, gesamt

#print(eDict,file=sys.stderr)
nr=0;reihenfolge="";wertNummer=0;vorherWert=0
for h in hList:
    for i in range(len(eList)):
        wList=eDict[i]
        wList[5]=False
    nr,reihenfolge = getNummer(eDict,eList,0,worktime,reihenfolge,wertNummer==len(eList) )
    #nr,reihenfolge = getNummer(eDict,eList,nr,worktime,reihenfolge)
    wList = eDict[nr]
    zeit = h/wList[0]
    reihenfolge+=" "+str(nr)
    vorherWert=wList[6]
    wList[3]+=1
    wList[2]+=zeit
    wList[6] = zeit if wList[6] < 0 else wList[6]+zeit

    wertNummer+=1
    #nr= 0 if nr == len(eList)-1 else nr+1

for i in range(len(eList)):
    wList=eDict[i]
    if wList[5] and not i == nr and vorherWert==wList[6]-10:
        wList[4]-=1



print(reihenfolge,file=sys.stderr)
ausgabe1="";ausgabe2=""
for i in range(len(eList)):
    wList = eDict[i]
    ausgabe1+=str(wList[3])+" "
    ausgabe2+=str(wList[4])+" "
print(ausgabe1[:-1])
print(ausgabe2[:-1])