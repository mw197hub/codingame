import sys
import math
import time

m = 26
n = 3
barList = [1, 2, 3,4,5,6,7,8]

ergListSumme = []
ergListSumme.append([1,3,4,7,10])
ergListSumme.append([1,3,4,8,10])
ergListSumme.append([1,2,5,8,10])
ergListSumme.append([1,2,5,9,9])
ergListSumme.append([1,1,5,8,10])

erg = ""
ergList = []
ergebnis = []

laenge = 99
zwErg = []
zwWert = 0
zwLaenge = 99
ergL1 = []
ergL2 = []
for ergList in ergListSumme:
    if sum(ergList) > zwWert:
        zwWert = sum(ergList)
for ergList in ergListSumme:
    if sum(ergList) == zwWert:
        ergL1.append(ergList)

for ergList in ergL1:
    if len(ergList) < laenge:
        laenge = len(ergList)
for ergList in ergL1:
    if len(ergList) == laenge:
        ergL2.append(ergList)
ergebnis = ergL2.pop()
for ergList in ergL2:
    kleiner = False
    for e in range(0,len(ergebnis)):
        if ergebnis[e] < ergList[e]:
            break
        if ergebnis[e] > ergList[e]:
            kleiner = True
            break
    if kleiner:
        ergebnis = ergList[:]



print(sum(ergebnis),file=sys.stderr)
for e in ergebnis:
    erg = erg + " " + str(e)
print(str(erg[1:]))