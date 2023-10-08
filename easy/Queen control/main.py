#

import sys,math


color="white";lineList=[['Q', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.']]

erg=0
richtung=[[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0]]

start=[]
for y in range(8):
    for x in range(8):
        if lineList[y][x] == "Q":
            start=[y,x]
            break
#print(start,file=sys.stderr)
for r in richtung:
    pos=start[:]
    for i in range(7):
        pos[0] += r[0]
        pos[1] += r[1]
        if pos[0] < 0 or pos[0] > 7 or pos[1] < 0 or pos[1] > 7:
            break
        if not lineList[pos[0]][pos[1]] == ".":
            if not lineList[pos[0]][pos[1]] == color[0]:
                erg+=1
            break
        erg+=1


print(erg)
