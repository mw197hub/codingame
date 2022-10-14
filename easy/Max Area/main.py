import sys
import math

aList=[1, 8, 6, 2, 5, 4, 8, 3, 7]
wert=0
for i in range(len(aList)):
    anfang=aList[i]
    ende=anfang
    for j in range(len(aList)-1,i,-1):
        mini=min([anfang,aList[j]])
        if (j-i)*mini > wert:
            wert=(j-i)*mini
        

print(wert)