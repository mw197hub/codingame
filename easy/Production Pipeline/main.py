# https://www.codingame.com/ide/puzzle/production-pipeline

import math,sys,copy

def suchePos(ergList,zahl):
    for i in range(len(ergList)):
        if ergList[i] == zahl:
            return i
    return -1

def einsetzen(zahlList,ergList,zahl,pos):
    zahlList.remove(zahl)
    newList=[]
    for i in range(len(ergList)):
      #  if i == pos and zahl > -1:
       #     newList.append(zahl);zahl=-1
        if ergList[i] > zahl and i >= pos and zahl > -1:
            newList.append(zahl);zahl=-1
        newList.append(ergList[i])
    if zahl > -1:
        newList.append(zahl)
    
    return copy.deepcopy(newList)


n=8;iList=['2<5', '3<4', '5<4'] #1
n=20;iList=['5<9', '3<1', '12<8', '6<12', '20<14', '2<5', '15<2']  # 3


zahlList=[]
ergList=[]
erg=""
for i in range(1,n+1):
    zahlList.append(i)

for i in iList:
    print(i,file=sys.stderr)
    iL = i.split("<")
    if iL[0] == iL[1]:
        erg="INVALID";break
    zahl1 = int(iL[0]);zahl2=int(iL[1])    
    pos1 = suchePos(ergList,zahl1)
    pos2 = suchePos(ergList,zahl2)
    if zahl1 in ergList and zahl2 in ergList:
        if pos2 > pos1:
            erg="INVALID";break
        else:
            zahlList.append(zahl2);ergList.remove(zahl2)
            ergList = einsetzen(zahlList,ergList,zahl2,pos1)
    elif pos1 == -1 and pos2 > -1:
        ergList = einsetzen(zahlList,ergList,zahl1,pos2-1)
    elif pos2 == -1 and pos1 > -1:
        ergList = einsetzen(zahlList,ergList,zahl2,pos1+1)
    elif pos1 == -1 and pos2 == -1:
        ergList = einsetzen(zahlList,ergList,zahl1,-1)
        pos1 = suchePos(ergList,zahl1)
        ergList = einsetzen(zahlList,ergList,zahl2,pos1+1)

if len(erg) > 0:
    print("INVALID")
else:
    rangeL = len(zahlList)
    for i in range(rangeL):
        zahl = zahlList[0]
        ergList = einsetzen(zahlList,ergList,zahl,-1)
    for e in ergList:
        erg=erg+str(e)+" "
    print(erg[:-1])