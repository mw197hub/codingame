import sys
import math

playerDict={'Bowser': ['Winner'], 'Mario': ['Winner']}
infoList=['Mario killed Bowser']

for info in infoList:
    info = info.replace(",","")
    iList = info.split(" ")
    pList=playerDict[iList[0]]
    for i in iList[2:]:
        dList=playerDict[i]
        dList[0] = iList[0]
        pList.append(i)
leerZeile=False
for p,kList in sorted(playerDict.items()):
    if leerZeile:
        print("")
    print("Name: "+ p)
    if len(kList) > 1:
        killed = ""
        for k in sorted(kList[1:]):
            killed+=k+", "
        print("Killed: " + killed[:-2])
    else:
        print("Killed: None")
    print("Killer: "+ kList[0])
    leerZeile=True