import sys
import math


def suche(feldList,i,j,anzahl,tiefe,n):
    feldList[i][j] = -1
    sucheL=[[1,0],[0,1],[-1,0],[0,-1]]
    for w in sucheL:
        iN=i+w[0];jN=j+w[1]
        if iN >= 0 and iN < n and jN >= 0 and jN < n and feldList[iN][jN] <= h and feldList[iN][jN] > 0:
            if tiefe > feldList[iN][jN]:
                tiefe = feldList[iN][jN]
            anzahl, tiefe= suche(feldList,iN,jN,anzahl+1,tiefe,n)

    return anzahl,tiefe

h = 5; n = 5; feldList = [[8, 9, 9, 8, 7], [8, 2, 3, 2, 7], [6, 4, 5, 4, 8], [9, 8, 4, 2, 7], [7, 8, 9, 6, 5]] #2
#suchList = [[0 for i in range(n)] for i in range(n)]
anzahl=0;tiefe=h+1
erg = 0

for i in range(n):
    for j in range(n):
        if feldList[i][j] <= h and feldList[i][j] > 0:
            anzahlNEW, tiefeNEW= suche(feldList,i,j,1,feldList[i][j],n)
            if anzahlNEW > anzahl or (anzahlNEW == anzahl and tiefeNEW < tiefe):
                tiefe = tiefeNEW;anzahl=anzahlNEW

print(str(tiefe))