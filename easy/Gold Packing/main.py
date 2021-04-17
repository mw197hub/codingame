import sys
import math
import time

def zahlenErmitteln(anz,barList,m,n,start,ergListSumme,neuList):
  #  print(str(neuList),file=sys.stderr)
    for i in range(start,n):
        neuList.append(barList[i])   
        if len(neuList) < anz:
            zahlenErmitteln(anz,barList,m,n,i+1,ergListSumme,neuList) 
        else:
            if sum(neuList) <= m:
                ergListSumme.append(neuList[:])
        neuList.pop()

m = 1489
n = 19
# 3 6 10 21 28 45 55 66 78 91 105 120 136 153 171 190 210
barList = [3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]

#m = 6
#n = 3
#barList = [1, 2, 4]

startTime = time.time()

erg = ""
ergList = []
ergListSumme= []
ergebnis = []

for anz in range(1,n+1):
  #  print(str(anz) + " anzahl",file=sys.stderr)
    neuList = []          
    zahlenErmitteln(anz,barList,m,n,0,ergListSumme,neuList) 

laenge = 99
zwErg = []
zwWert = 99999
zwLaenge = 99
#print(ergListSumme,file=sys.stderr)
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

print('{:5.3f}s'.format(time.time()-startTime))