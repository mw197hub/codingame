import sys
import math

def nachbarSuche(y,x, yN,xN,w,h):
    y1 = y + yN
    x1 = x + xN
    if x1 < 0 or y1 < 0 or x1 >= w or y1 >= h:
        return
    if feldList[y1][x1] < 99:
        feldList[y1][x1] = feldList[y1][x1] +1

w = 16
h = 9

nachbarList = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
feldList = []
mineList = []
for x in range(h):
    zeile = []
    for y in range(w):
        zeile.append(0)
    feldList.append(zeile)

feldList[5][4] = 99
feldList[5][5] = 99
mineList.append([5,4])
mineList.append([5,5])

print(mineList,file=sys.stderr)

for mine in mineList:
    for nachbar in nachbarList:
        nachbarSuche(mine[0],mine[1],nachbar[0],nachbar[1],w,h)


for z in feldList:
    print(z,file=sys.stderr)