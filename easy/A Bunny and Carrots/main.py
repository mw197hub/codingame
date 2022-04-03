import sys
import math
import copy


def ermittleRahmen(gridList,m,n):
    nachbar = [[-1,0],[1,0],[0,-1],[0,1]]
    gList = copy.deepcopy(gridList)
    for j in range(m):
        for i in range(n):
            if gList[j][i] > 0:
                for nachb in nachbar:
                    z = j + nachb[0];s=i+nachb[1]
                    if s >= 0 and z >= 0 and s < n and z < m and gridList[z][s] > 0:
                        gList[j][i] -= 1
    print(gList,file=sys.stderr)
    erg = 0
    for i in range(m):
        erg += sum(gList[i])
    return erg


m,n = 2,2;t = 4;choices = [2, 1, 1, 2]
m,n = 3,3;t = 6;choices = [1, 2, 3, 2, 3, 3]
m,n = 1,20;t =6;choices = [2, 5, 8, 13, 15, 16]


gridList = []
for i in range(m):
    gList = []
    for j in range(n):
        gList.append(4)
    gridList.append(copy.deepcopy(gList))
print(gridList,file=sys.stderr)

for _ in range(t):
    spalte = choices.pop(0) -1
    zeile = 0
    for i in range(m,0,-1):
        if gridList[i-1][spalte] == 4:
            gridList[i-1][spalte] = 0
            zeile = i-1; break
    print(gridList,file=sys.stderr)
    rahmen = ermittleRahmen(gridList,m,n)
    print(rahmen)
