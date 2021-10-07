import sys
import math

def berechnen(x,y,pixelList,weightList,m,n):
    erg = 0
    for i1 in range(m):
        for i2 in range(n):
            erg = erg + weightList[i1][i2] * pixelList[i1+x][i2+y]
    return erg


ergList = []
pixelList = [[100, 200, 100], [200, 100, 200], [50, 100, 50]]
weightList = [[-1, 1], [1, -1]]
r, c = 3,3
m,n = 2,2
range1 = r - m + 1
range2 = c - n + 1

for i1 in range(range1):
    ergString = ""
    for i2 in range(range2):
        ergString = ergString + str(berechnen(i1,i2,pixelList,weightList,m,n)) + " "
    ergList.append(ergString)

for e in ergList:    
    print(e[:-1])