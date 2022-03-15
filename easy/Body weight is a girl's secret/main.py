import sys
import math


def bildeWert(e):
    testList = [0,0,0,0,0,0,0,0,0,0]
    testList[0] = e[0] + e[1];testList[1] = e[0] + e[2];testList[2] = e[0] + e[3]
    testList[3] = e[0] + e[4];testList[4] = e[3] + e[4];testList[5] = e[1] + e[2]
    testList[6] = e[1] + e[3];testList[7] = e[1] + e[4];testList[8] = e[2] + e[3]
    testList[9] = e[2] + e[4]
    return testList

inputList = [96, 97, 103, 108, 114, 115, 121, 127, 128, 139]
#ergList = [45, 51, 52, 63, 76]
ergList = [0,0,0,0,0]
ergebnis= ""
mittelwert = int(sum(inputList) / 4)
ergList[2] = mittelwert  - inputList[0] - inputList[-1]
anfang = inputList[0] - (ergList[2] -1)
ende = inputList[-1] - (ergList[2] +1)

while True:
    treffer = False
    while inputList[-1]-ende < ende:
        ergList=[anfang,inputList[0]-anfang,ergList[2],inputList[-1]-ende,ende]
        print(ergList,file=sys.stderr)
        if sorted(bildeWert(ergList)) == inputList and sum(ergList) == mittelwert:
            treffer = True; break
        ende -=1
    if treffer:
        break
    anfang +=1
    ende = inputList[-1] - (ergList[2] +1)

for erg in sorted(ergList):
    ergebnis = ergebnis + str(erg)+" "
print(ergebnis[:-1])


