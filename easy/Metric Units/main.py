import sys
import math


def getWert(wert,reihe):
    m="";w=0.0
    if wert[-2:] in reihe:
        return wert[-2:],float(wert[:-2])
    return wert[-1:],float(wert[:-1])

def berechnen(wert1,wert2,m1,m2,mList,reihe):
    erg = wert1
    while True:
        if m1 == m2:
            break
        wert2 = wert2 * mList[m2]
        pos = 0
        for r in reihe:
            if r == m2:
                break
            pos += 1
        m2 = reihe[pos-1]
    erg += wert2
    return erg


exL = ['10m', '+', '10cm']

mList = {'mm':1000,'cm':10,'dm':10,'m':10,'km':1000}
reihe = ['um','mm','cm','dm','m','km']
#reihe = ['km','m','dm','cm','mm','um']


mass = "";erg = 0.01
m1="";m2="";wert1=0.0;wert2=0.0
m1,wert1 = getWert(exL[0],reihe)
m2,wert2 = getWert(exL[2],reihe)
#print(wert1,file=sys.stderr)
for r in reihe:
    if m1 == r:
        mass = m1
        erg = berechnen(wert1,wert2,m1,m2,mList,reihe)
        break
    if m2 == r:
        mass = m2
        erg = berechnen(wert2,wert1,m2,m1,mList,reihe)
        break


if int(erg) == erg:
    print(str(int(erg))+mass)
else:
    print(str(round(erg,5))+mass)



