# https://www.codingame.com/ide/puzzle/interstellar

import sys,math

def getFactor(wertI,wertJ,wertK):
    factor=1
     
    wI=0 if len(wertI) < 3 else int(wertI[:-1])
    wJ=0 if len(wertJ) < 3 else int(wertJ[:-1])
    wK=0 if len(wertK) < 3 else int(wertK[:-1])
    if (wI == 0 and wJ == 0) or (wI == 0 and wK == 0) or (wK == 0 and wJ == 0) or (len(wertJ) == 2 or len(wertK) == 2):
        return wertI,wertJ,wertK
    mini=0
    for i in range(1,1000):
        if wI==i or wJ == i or wK == i:
            mini=i;break
    for i in range(mini,1,-1):
        if (wI == 0 or wI % i == 0) and (wJ == 0 or wJ % i == 0) and (wK == 0 or wK % i == 0):
            factor = i;break
    if factor > 1:
        wertI = str(int(wI / factor))+wertI[-1] if len(wertI) > 0 else ""
        wertJ = str(int(wJ / factor))+wertJ[-1] if len(wertJ) > 0 else ""
        if wJ > 0:
            wertJ="+"+wertJ
        wertK = str(int(wK / factor))+wertK[-1] if len(wertK) > 0 else ""
        if wK > 0:
            wertK = "+"+wertK
    return wertI,wertJ,wertK


def setDi(w1,w2,buch):
    if w1 -w2 == 0:
        return ""
    w0 = w1 - w2    
    vorzeichen="+"
    if w0 < 0:
        vorzeichen=""
    if abs(w0) == 1:
        if w0 < 0:
            return "-"+buch
        else:
            return vorzeichen+ buch
    else:
        return vorzeichen+str(w0)+buch

def getWerte(eingabe):
    wert={"i":0,"j":0,"k":0}
    vorzeichen="+"
    w=""
    for i in range(len(eingabe)):
        if eingabe[i] in wert:
            if len(w) > 0:
                we = int(w)
            else:
                we = 1
            if vorzeichen == "-":
                we= we * -1
            wert[eingabe[i]] = we
            w="";vorzeichen="+"
        if eingabe[i] == "-":
            vorzeichen = "-"
        if eingabe[i] in "0123456789":
            w=w+eingabe[i]
    return wert


ship="i+j-k";wormhole="i-j+k"   #1
ship="3i+5j+2k";wormhole="4i+9j+3k"  #2
ship="i+j+k";wormhole="-i-j-k" # 1 vali
#ship="4i+12j-8k";wormhole="4i-6j+4k"  #8
#ship="89k-76i  +76j";wormhole="56i +67j+ 90k"  #4
#ship="5i+6j+7k";wormhole="3i+9j+6k" # 2 Vali
#ship="k";wormhole="j" # 7 vali
#ship="17k-51j";wormhole="34j-17k" # 10 vali

wert1=getWerte(ship)
#print(wert1)
wert2=getWerte(wormhole)
#print(wert2)
#  distance = √((a2 – a1)² + (b2 – b1)² + (c2-c1)²)
#  direction   (a1-a2)i+(b1-b2)j+(c1-c2)k

direction=""
#wertI = setDi(wert2['i'],wert1['i'],'i')


wertI = setDi(wert2['i'],wert1['i'],'i')
wertJ = setDi(wert2['j'],wert1['j'],'j')
wertK = setDi(wert2['k'],wert1['k'],'k')
wertI,wertJ,wertK= getFactor(wertI,wertJ,wertK)

if len(wertI) == 3 and wertI[1] == "1":
    wertI = wertI[0] + wertI[2:]
if len(wertJ) == 3 and wertJ[1] == "1":
    wertJ = wertJ[0] + wertJ[2:]
if len(wertK) == 3 and wertK[1] == "1":
    wertK = wertK[0] + wertK[2:]
direction = wertI+wertJ+wertK

distance = math.sqrt((wert2['i']-wert1['i'])**2 + (wert2['j']-wert1['j'])**2 + (wert2['k']-wert1['k'])**2)

if direction[0] == "+":
    direction=direction[1:]
print("Direction: {}".format(direction))

print("Distance: {}".format(round(distance,2)))