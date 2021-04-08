import sys
import math
import numpy

def getWert(lList):
    return int(lList.pop(0)),int(lList.pop(0))

a = "26751891 1 12423842 0 24697032 -1 75825948 0 16058842 -1 5056344 -1 14781040 -1 48256886 0 37330872 1 68962932 1 37555307 1 2970721 0 26201429 1 48967194 -1 17837665 0 74719356 -2 17461041 -2 20765736 0 15044838 1 6518283 -2 10432178 -2 15225674 -2 6160520 0 32060077 0 52545144 0 3848757 -2 91480452 -1 99032044 1 89501141 1 1526814 0"
b = "40312847 1 84841395 -2 43849784 1 3228664 -1 98445257 -1 22318921 0 42672597 0 4577041 0 5240860 -2 31151717 1 30451395 -2 35469153 -2 25313187 -2 40128193 1 15893237 1 6369211 1 3672509 -1 22259551 0 25942846 -2 12180032 1 4202901 0 68816164 1 520373 -2 107835622 1 50661951 -2 67145499 0 88144650 -1 18354443 -1"
aList = a.split(" ")
bList = b.split(" ")
print(aList)
print(bList)
erg = 0
anzahlB, wertB = getWert(bList)
anzahlA, wertA = getWert(aList)
while len(aList) > 0 or len(bList) > 0:
    
    if anzahlB > anzahlA:
       erg = erg + (wertB * wertA * anzahlA) 
       anzahlB = anzahlB - anzahlA
       anzahlA, wertA = getWert(aList)
    else:
        erg = erg + (wertB * wertA * anzahlB) 
        anzahlA = anzahlA - anzahlB
        anzahlB, wertB = getWert(bList)
erg = erg + (wertB * wertA * anzahlA) 
print(erg)


#print(numpy.array(X) @ numpy.array(Y))
#print(numpy.arange(1,1000000000,1))