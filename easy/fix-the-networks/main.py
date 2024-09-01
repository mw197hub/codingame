# https://www.codingame.com/training/easy/fix-the-networks

import math,sys


def get_bin(x,n):
    return format(x, 'b').zfill(n)

def zaehleNull(zList):
    anzahl=0
    ende=False
    for i in range(3,-1,-1):
        wert =get_bin(int(zList[i]),8)
        for j in range(7,-1,-1):
            if wert[j] == "0":
                anzahl=anzahl+1
            else:
                ende=True
                break
        if ende:
            break
    return anzahl



rList=['10.0.0.32/32', '10.0.0.32/30', '10.0.0.32/28', '10.0.0.32/26']


for r in rList:
    tList=r.split("/")
    zList=tList[0].split(".")
    anzahlNullen=zaehleNull(zList)    
    if anzahlNullen >= 32-int(tList[1]):
        moeglichkeiten=2**(32-int(tList[1]))
        print("valid {}".format(moeglichkeiten))
    else:
        moeglichkeiten=2**(anzahlNullen)
        print("invalid {} {}".format(tList[0]+"/"+str(32-anzahlNullen),moeglichkeiten))