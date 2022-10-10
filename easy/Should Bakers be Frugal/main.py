import sys
import math

def getCookies(sideN,rad):
    if rad*2 > sideN:
        return 0,0
    anzahl = (int(sideN / (rad*2)) **2)
    cookie = (rad**2) * math.pi
    return anzahl,(sideN * sideN - (  cookie * anzahl))

side,diameter=3,1 #1 = 2
side,diameter=12,3 #2 = 4
side,diameter=12,6 #3 = 0
side,diameter=12,5 #4 = 3

#anzahlWaste = (int(side / diameter) **2)
#cookie = ((diameter/2)**2) * math.pi
#restTeig = side * side - (  cookie * anzahlWaste)
anzahlWaste,restTeig = getCookies(side,diameter/2)
erg = 0
while True:
    anzahl,restTeig = getCookies(math.sqrt(restTeig),diameter/2)
    erg += anzahl
    if anzahl == 0:
        break

print(int(erg))