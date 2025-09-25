# https://www.codingame.com/ide/puzzle/minimal-number-of-swaps

import sys,math

xList=[1, 0, 1, 0, 1]


anzahlNull=0
for i in range(sum(xList)):
    if xList[i] == 0:
        anzahlNull+=1
print(anzahlNull)