import sys
import math
from collections import OrderedDict


def up(e,ergL,leer,pos):
    line = ergL[e]
    line = line + leer[:pos-len(line)] + "/"
    ergL[e] = line
    return pos + 1

def down(e,ergL,leer,pos):
    line = ergL[e]
    line = line + leer[:pos-len(line)] + "\\"
    ergL[e] = line
    return pos + 1

heightL = [1, 2, 1]
heightL = [3, 7, 2, 9]
heightL = [2, 4, -2, 3] 
heightL = [2, 7, -2, -2, -3]

start=0
if min(heightL) < 0:
    start = abs(min(heightL)) + 1
    for i in range(len(heightL)):
        heightL[i] += start
print(heightL,file=sys.stderr)

maxH = max(heightL) if max(heightL) > 0 else 0
minH = min(heightL) if min(heightL) < 0 else 0
ergL = {}
leer = "                                                                                                   "
for i in range(minH,maxH,1):
    ergL[i] = ""
pos = 0;ebene=start
for h in heightL:
    if h > ebene:
        for e in range(ebene,h,1):
            pos = up(e,ergL,leer,pos)
        pos = down(e,ergL,leer,pos)
        ebene = h -1
    else:
        for e in range(ebene-1,h-2,-1):
            pos = down(e,ergL,leer,pos)
        ebene = h -1
        for e in range(ebene,h,1):
            pos = up(e,ergL,leer,pos)
        pos = down(e,ergL,leer,pos)
        ebene = h -1
print(ergL,file=sys.stderr)

if ebene > start:
    for e in range(ebene-1,start-1,-1):
        pos = down(e,ergL,leer,pos)
        ebene = ebene -1
elif ebene < start:
    for e in range(ebene,start,1):
        pos = up(e,ergL,leer,pos)
        ebene = ebene +1
    

for e,line in reversed(sorted(ergL.items())):
    print(line)




