#  https://www.codingame.com/ide/puzzle/mirrors

import sys,math

n,rList=2,[0.5, 0.5]   # 0.6667
n,rList=1,[0.011263]   # 0.0113
n,rList=3,[0.313178, 0.055436, 0.998542]   # 0.9985
#n,rList=4,[0.756643, 0.845056, 0.439436, 0.863778]   # 0.9401

light=1
erg=0.0

wertList=[]
for i in range(len(rList)):
    wertList.append([0,0])
#erg = light*rList[0]
wertList[0][0] = light
while True:
    for i in range(len(rList)):
        r = rList[i]
        if wertList[i][0] > 0.00001:
            wert1 = (wertList[i][0]*r) # reflektion
            wert2 = wertList[i][0] - wert1  # geht durch
            if i == 0:
                erg += wert1                
            else:
                wertList[i-1][1] += wert1
            if len(rList) > 1 and i < len(rList) -1:
                wertList[i+1][0] += wert2
            wertList[i][0] = 0
    #print(wertList,file=sys.stderr)

    for i in range(len(rList)-1,-1,-1):
        r = rList[i]
        if wertList[i][1] > 0.00001:
            wert1 = (wertList[i][1]*r) # reflektion
            wert2 = wertList[i][1] - wert1 # geht durch
            if i == 0:
                erg += wert2
            else:                
                if i < len(rList)-1:
                    wertList[i-1][1] += wert2
            if len(rList) > 1 and i < len(rList) -1:
                wertList[i+1][0] += wert1     
            wertList[i][1] = 0
    #print(wertList,file=sys.stderr)

    ende=True
    for wert in wertList:
        if wert[0] > 0.00001 or wert[1] > 0.00001:
            ende=False
    if ende:
        break


erg=round(erg,4)
print("{1:1.4f}".format(1,erg))


