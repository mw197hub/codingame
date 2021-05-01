import sys
import math
import time
from itertools import combinations

ergM = []
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

def combs(barList):
    if len(barList) == 0:
        return [[]]
    cs = []
    for c in combs(barList[1:]):
        cs += [c, c+[barList[0]]]
    return cs



#m = 1489
#n = 19
#barList = [3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]
# 3 6 10 21 28 45 55 66 78 91 105 120 136 153 171 190 210

#m = 113
#n = 10
#barList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# 5 7 13 17 19 23 29

#m = 46
#n = 7
#barList = [1, 3, 5, 7, 9, 11, 13]
# 1 5 7 9 11 13

m = 7
n = 5
barList = [5, 6, 7, 8, 9]
# 7

#m = 6
#n = 3
#barList = [1, 2, 4]
# 2 4

#m = 1565
#n = 22
#barList = [2, 4, 7, 11, 16, 22, 29, 37, 46, 56, 67, 79, 92, 106, 121, 137, 154, 172, 220, 221, 250, 300]
# 56 106 121 137 154 220 221 250 300

startTime = time.time()

erg = ""
ergList = []
ergListSumme= []
ergebnis = []

for anz in range(1,n+1):
  #  print(str(anz) + " anzahl",file=sys.stderr)
    neuList = []          
    #zahlenErmitteln(anz,barList,m,n,0,ergListSumme,neuList) 
output = combs(barList[:]) 

#output = sum([list(map(list, combinations(barList, i))) for i in range(len(barList) + 1)], [])
for out in output:
    if sum(out) <= m:
        ergListSumme.append(sorted(out[:]))

#for e in ergListSumme:
#    print(e,file=sys.stderr)
print(len(ergListSumme),file=sys.stderr)
laenge = 99
zwErg = []
zwWert = 0
ergL1 = []
ergL2 = []

for ergList in ergListSumme:
    if sum(ergList) > zwWert:
        zwWert = sum(ergList)
for ergList in ergListSumme:
    if sum(ergList) == zwWert:
        ergL1.append(ergList)
#print(ergL1,file=sys.stderr)
for ergList in ergL1:
    if len(ergList) < laenge:
        laenge = len(ergList)
for ergList in ergL1:
    if len(ergList) == laenge:
        ergL2.append(ergList)
#print(ergL2,file=sys.stderr)
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
if len(ergM) > 0:
    ergebnis = ergM

print(sum(ergebnis),file=sys.stderr)
for e in ergebnis:
    erg = erg + " " + str(e)
print(str(erg[1:]))

print('{:5.3f}s'.format(time.time()-startTime))