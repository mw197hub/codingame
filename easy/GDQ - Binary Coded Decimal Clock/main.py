import sys,math


def einsetzen(spalte,zahl,wertList):
    treffer="#####"
    #print(zahl,file=sys.stderr)
    wert=str(zahl)
    pos=3
    for i in range(len(wert)-1,0,-1):
        if wert[i] == "b":
            return
        if wert[i] == "1":
            wertList[pos][spalte] = treffer
        pos-=1


eingabe="00:01:02:3"  #1


muster="|_____|_____|_____|_____|_____|_____|"


eing = eingabe.split(":")  # 1:h  2-3:m  4-5:s  6:f
wertList= []
for y in range(4):
    wL=[]
    for x in range(6):
        wL.append("_____")
    wertList.append(wL[:])

einsetzen(0,bin(int(eing[0])),wertList)
einsetzen(1,bin(int(eing[1][0])),wertList)
einsetzen(2,bin(int(eing[1][1])),wertList)
einsetzen(3,bin(int(eing[2][0])),wertList)
einsetzen(4,bin(int(eing[2][1])),wertList)
einsetzen(5,bin(int(eing[3])),wertList)

for wL in wertList:
    ausgabe="|"
    for x in wL:
        ausgabe+=x+"|"
    print(ausgabe)

