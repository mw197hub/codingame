import sys
import math

girlList=[['G', '.', '.', '.', '.', 'G'], ['.', 'G', '.', '.', 'G', '.'], ['.', '.', 'G', 'G', '.', '.'], ['.', '.', 'G', 'G', '.', '.'], ['.', 'G', '.', '.', 'G', '.'], ['G', '.', '.', '.', '.', 'G']]
h,w=6,6

wertList=[]
for y in range(h):
    for x in range(w):
        if girlList[y][x] == 'G':
            wert= min(x,y) / (x**2+y**2+1)
            wertList.append(wert)
#print(sorted(wertList,reverse=True))
erg=0;summe=0
for wert in sorted(wertList,reverse=False):
    summe = summe + wert - summe * wert
    if summe > 0.4:
        break
    erg+=1
print(erg)