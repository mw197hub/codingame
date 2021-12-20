import sys
import math


rowList = ['1 3 2 1', '1 3 2 1', '1 3 2 1', '1 3 2 1']
#rowList = ['0 1 1 1 1', '0 1 1 1 1', '0 1 1 1 1', '0 1 1 1 1']
rowList = ['43']
rowList = ['0 1 1 2', '0 2 1 1', '0 1 1 1', '1 1 1 1']

ergList = []
for row in rowList:
    zList = row.split(" ")
    white = True
    erg = ""
    
    for z in zList:
        if not z == '0':
            for i in range(int(z)):
                if white:
                    erg += "."
                else:
                    erg += "O"
        if white:
            white = False
        else:
            white = True
    ergList.append(erg)

invalid = False
laenge = 0
for erg in ergList:
    if laenge == 0:
        laenge = len(erg)
    else:
        if not laenge == len(erg):
            invalid = True

if invalid:
    print("INVALID")
else:
    for erg in ergList:
        print(erg)