# https://www.codingame.com/ide/puzzle/porcupine-fever

import sys,math



y=3;n=2;porList=[[2, 118, 120], [0, 50, 50]]


for i in range(y):
    anzahl=0
    for j in range(n):
        por = porList.pop(0)
        if por[1] > 0:
            anzahl+=por[1]
        zahl1=por[0]*2
        zahl2=por[1]-zahl1
        zahl3=zahl1+zahl2
        porList.append([zahl1,zahl2,zahl3])

    print(anzahl)
    if anzahl == 0:
        break