import sys
import math


tnList = [20, 20, 40];c = 100
tnList = [40, 40, 40];c=100

ergList = []
if sum(tnList) < c:
    print("IMPOSSIBLE")
else:
    while True:
        mittelWert = int((c-sum(ergList))/len(tnList))
        kleiner=False
        for tn in tnList:
            if tn < mittelWert:
                ergList.append(tn)
                tnList.remove(tn)
                kleiner=True
        if not kleiner:
            rest = int(c - sum(ergList) - len(tnList) *mittelWert)
            anzahlH = 0
            for tn in tnList:                
                if tn > mittelWert:
                    anzahlH +=1
            
            for tn in tnList:
                if rest > 0 and tn > mittelWert:
                    ergList.append(mittelWert+1)
                    rest -=1
                else:
                    ergList.append(mittelWert)                        
        if sum(ergList) == c:
            break

for erg in sorted(ergList):
    print(erg)