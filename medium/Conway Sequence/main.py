import sys
import math
import copy

r,l = 1,6


ergList = [r]
zwList = []
for i in range(l-1):
    anzahl=0;vorwert=0
    for wert in ergList:        
        if wert == vorwert or anzahl == 0:
            anzahl+=1
            vorwert = wert
        else:
            zwList.append(anzahl)
            zwList.append(vorwert)
            vorwert = wert;anzahl=1
    zwList.append(anzahl)
    zwList.append(vorwert)

    ergList.clear()
    ergList = copy.deepcopy(zwList)
    zwList.clear()

erg = ""
for e in ergList:
    erg = erg + str(e) + " "
print(erg[:-1])
print(*ergList)  # einfacher