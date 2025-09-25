# https://www.codingame.com/ide/puzzle/ascii-art-glass-stacking

import sys,math

anzahl=6

glas=[" *** "," * * "," * * ","*****"]
anzList=[1,3,6,10,15,21,28,36]

basis=0
for i in range(len(anzList)):
    basis+=1
    if anzList[i] == anzahl or anzahl < anzList[i+1]:
        break

breite=basis*5+(basis-1);anzahl=1
for i in range(basis):
    aktBreite=anzahl*5+(anzahl-1)

    for k in range(4):
        for a in range(int((breite-aktBreite)/2)):
            print(" ",end="")
        for j in range(anzahl):
            print(glas[k],end="")
            if j < anzahl-1:
                print(" ",end="")
        for a in range(int((breite-aktBreite)/2)):
            print(" ",end="")
        print("")
    
    anzahl+=1