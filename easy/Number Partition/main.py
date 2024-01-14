# https://www.codingame.com/ide/puzzle/number-partition

import math,sys


def suche(wert,ergList,n,zw):

    if sum(zw) == n:
        ergList.append(zw[:])
    else:
        for i in range(wert,0,-1):
            zw1=zw[:]
            zw1.append(i)
            if sum(zw1) <= n:
                suche(i,ergList,n,zw1)

n=4
ergList=[]
for i in range(n,0,-1):
    suche(i,ergList,n,[i])

for erg in ergList:
    s=""
    for e in erg:
        s= s+str(e)+" "
    print(s[:-1])
