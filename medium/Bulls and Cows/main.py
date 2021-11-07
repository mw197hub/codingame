import sys 
import math

def werteSuchen(wert,zahl):
    bullsZahl, cowsZahl = 0,0
    wertList = [z for z in wert]
    for i in range(4):
        if wert[i] == zahl[i]:
            bullsZahl += 1
    for i in range(4):
        if zahl[i] in wertList:
            wertList.remove(zahl[i])
            cowsZahl += 1
    return bullsZahl, cowsZahl

def isOkay(wert,zahl,bulls,cows):
    zahlList = [z for z in zahl]
    wertList = [z for z in wert]
    # return: 0 = False, 1 = True, 2 = kann nicht
    bullsZahl, cowsZahl = werteSuchen(wert,zahl)
    if cows > 0 and bulls == 0 and not cowsZahl == cows:
        return 0
    if cows == 0 and bulls > 0 and cowsZahl > bulls:
        return 0

    if bulls + cows == 0:
        for w in wert:
            if w in zahl:
                return 0
    if bulls > 0 and cows == 0:
        anzahl = 0
        for i in range(4):
            if wert[i] == zahl[i]:
                anzahl += 1
        if not anzahl == bulls:
            return 0
    if bulls == 0 and cows > 0:
        anzahl = 0
        for i in range(4):
            if wert[i] == zahl[i]:
                return 0
            if wert[i] in zahlList:
                anzahl += 1
                zahlList.remove(wert[i])
        if not anzahl == cows:
            return 0 
    if bulls > 0 and cows > 0:
        anzahlB = 0
        anzahlC = 0
        for i in range(4):
            if wert[i] == zahl[i] and wert[i] in zahlList:
                anzahlB += 1
                zahlList.remove(wert[i])
            elif wert[i] in zahlList:
                anzahlC += 1
                zahlList.remove(wert[i])
        if not anzahlC == cows or not anzahlB == bulls:
            return 0

    return 1

def pruefen(inp,wertDict):
    wertList = []
    zahl, bulls, cows = inp[0], int(inp[1]), int(inp[2])
    
    for i in range(10000):
        wert = nullergaenzen(str(i),4)
        #bullsW, cowsW = bullsCows(zahl,wert)
        okay = True
        for anzahl,wList in wertDict.items():
            for w in wList:
                if anzahl > 2:
                    if wert.count(w) <= anzahl:
                        okay = False
                if anzahl == 0 and wert.count(w) > 0:
                    okay = False
                #elif wert.count(w) > anzahl:
                #    okay = False

        if okay and isOkay(wert,zahl,bulls,cows) == 1:
            wertList.append(wert)
    return wertList

def nullergaenzen(zahl,laenge):
    for _ in range(laenge - len(zahl)):
        zahl = "0" + zahl
    return zahl


#inputList = [['0536','2','2']]
#inputList = [['1234', '4', '0']]
#inputList = [['0473', '2', '2'], ['7403', '0', '4']]
#inputList = [['0123', '1', '0'], ['4567', '0', '0'], ['8901', '1', '0'], ['1110', '3', '0']]
#inputList = [['9073', '2', '0'], ['1248', '2', '0'], ['1043', '0', '0']]
#inputList = [['1111', '0', '0'], ['2222', '1', '0'], ['3333', '0', '0'], ['4444', '0', '0'], ['5555', '0', '0'], ['6666', '0', '0'], ['7777', '2', '0'], ['8888', '1', '0'], ['2778', '0', '4'], ['7287', '2', '2']]
inputList = [['0123', '1', '0'], ['4567', '1', '0'], ['8901', '1', '0'], ['8522', '3', '0'], ['8525', '3', '0']]

b, c = werteSuchen('8520','0123')
print(str(b) + " - " + str(c),file=sys.stderr)

wertDict = {0:[],1:[],2:[],3:[],4:[]}
wertList = []
erg = "kein Treffer"

for inp in inputList:
    zahl, bulls, cows = inp[0], int(inp[1]), int(inp[2])
    anzahl = bulls + cows
    wertL = wertDict[anzahl]
    for z in zahl:
        if not z in wertL:
            if anzahl > 1:
                if zahl.count(z) >= anzahl:
                    wertL.append(z)
            else:
                wertL.append(z)
    wertDict[anzahl] = wertL[:]
#print(wertDict,file=sys.stderr)
for i in range(1,4):
    wertL = wertDict[i]
    for wert in wertL:
        for j in range(i+1,5):
            verL = wertDict[j]
            if wert in verL:
                wertL.remove(wert)
print(wertDict,file=sys.stderr)

for inp in inputList:
    zahl, bulls, cows = inp[0], int(inp[1]), int(inp[2])
    wertList.append(pruefen(inp,wertDict))

#print(wertList,file=sys.stderr)

#print(feldList,file=sys.stderr)
if len(wertList) == 1:
    erg = wertList[0][0]
else:
    ergL = []
    wertL = wertList[0]
    for wert in wertL:
        treffer = True
        for i in range(len(wertList)- 1):
            if not wert in wertList[i+1]:
                treffer = False
        if treffer:
            ergL.append(wert)
    print(ergL,file=sys.stderr)
    if len(ergL) > 100:
        for inp in inputList:
            zahl, bulls, cows = inp[0], int(inp[1]), int(inp[2])
            if bulls + cows == 1:     
                loeL = []       
                for wert in ergL:
                    anzahl = 0
                    for z in zahl:
                        if z in wert and wert.count(z) == 1:
                            anzahl += 1
                    if anzahl > 1:
                        loeL.append(wert)
                for loe in loeL:
                    ergL.remove(loe)
        print(ergL,file=sys.stderr)
    if len(ergL) == 1:
        erg = ergL[0]
print(erg)

