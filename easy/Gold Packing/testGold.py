import sys
import math
import time

m = 20
n = 3
barList = [1, 2, 3,4,5,6,7,8]

ergListSumme = []
ergListSumme.append([1,3,4,8])
ergListSumme.append([1,2,5,8])
ergListSumme.append([1,1,5,9])

erg = ""
ergList = []
ergebnis = []

laenge = 99
zwErg = []
zwWert = 99999
zwLaenge = 99

for ergList in ergListSumme:
    if sum(ergList) == m:
        if len(ergList) < laenge:
            ergebnis = ergList[:]
            laenge = len(ergList)
        elif len(ergList) == laenge:
            kleiner = False
            for b in range(0,len(ergList)):
                if ergList[b] > ergebnis[b]:                     
                    break
                if ergList[b] < ergebnis[b]:        
                    kleiner = True
                    break
            if kleiner:
                ergebnis = ergList[:]
                laenge = len(ergList)
    else:
        if m - sum(ergList) < zwWert:
            zwWert = m - sum(ergList)
            zwErg = ergList[:]
        elif m - sum(ergList) == zwWert:                        
            if len(ergList) < zwLaenge:
                zwLaenge = len(ergList)
                zwErg = ergList[:]
            elif len(ergList) == zwLaenge:
                kleiner = False
                for b in range(0,len(ergList)):
                    if ergList[b] > zwErg[b]:                     
                        break
                    if ergList[b] < zwErg[b]:        
                        kleiner = True
                        break
                if kleiner:
                    zwErg = ergList[:]
                    zwLaenge = len(ergList)

if len(ergebnis) == 0:
    ergebnis = zwErg[:]

print(sum(ergebnis),file=sys.stderr)
for e in ergebnis:
    erg = erg + " " + str(e)
print(str(erg[1:]))