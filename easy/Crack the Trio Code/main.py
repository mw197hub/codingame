# https://www.codingame.com/ide/puzzle/crack-the-trio-code

import sys,math
import itertools


def enthalten(zahl,zw):
    nZahl=[]
    for z in zahl:
        if z > 0 and z <= zw:
            nZahl.append(z)

    for z in (itertools.combinations_with_replacement(nZahl,3)):
        if sum(z) == zw:
            return True
    for z in (itertools.combinations_with_replacement(nZahl,2)):
      #  print("2: {}".format(z))
        if sum(z) == zw:
            return True
    for z in (itertools.combinations_with_replacement(nZahl,1)):
     #   print("1: {}".format(z))
        if sum(z) == zw:
            return True
    return False

l="3,11,12,102,111,120"   #1
l="1,2,3,4,5,6,7,8,9,10,11,12,13,14" #2
l="9,10,11,12,13,14,15,16,17,18,19" #3
l="33,61,66,83,95" #6#
l="8,16,26,27,42,53,65,69,81,83,88,99" #5





zwList=[int(i) for i in l.split(",")]
wList=[]
for i in range(zwList[-1]+1):
    wList.append(i)
zahlenList=(itertools.combinations_with_replacement(wList,3))


kombiList=[]
for i in range(len(zwList)):
    kombiList.append([])
loesungen=[]
for zahl in zahlenList:
    anzahl=0
    if zahl[0] == 17 and zahl[1] == 33 and zahl[2] == 61:
        a=0
    for i in range(len(zwList)):
        zw = zwList[i]
        if sum(zahl) == zw or enthalten(zahl,zw):
            kombi = kombiList[i]
            kombi.append(zahl)
            anzahl+=1
        a=0
    if anzahl == len(zwList):
        loesungen.append(zahl)

#suche(loesungen,kombiList,0)

print(loesungen,file=sys.stderr)

if len(loesungen) == 0:
    print("none")
elif len(loesungen) > 1:
    print("many")
else:
    erg=""
    for loe in loesungen:
        for lo in loe:
            erg=erg+str(lo)+","
    print(erg[:-1])