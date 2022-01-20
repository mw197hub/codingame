import sys
import math
import string

def wertInZoneList(wert,zoneList,anzahlBuchstaben,abcList,posBlub):
    posBlub = 0
    for key, value in zoneList.items():
        if wert == value:
            return key
    abstand = abs(abcList[wert] - posBlub)
    if abstand > 15:
        abstand = len(zoneList) - abstand
    pos = 99
    for key, value in anzahlBuchstaben.items():
        if value == 0:
            diff = abs(abs(abcList[key] - abcList[wert]) - posBlub)
            if diff > 15:
                diff = len(zoneList) - diff
            if diff < abstand:
                for key2, value2 in zoneList.items():
                    if key == value2:
                        pos = key2
                        abstand = diff
                        break
    return pos

def setzeZoneList(wert,zoneList,posBlub):
    first = 99
    last = 99
    for key, value in zoneList.items():
        if value == "-" and first == 99:
            first = key
        if value == "-":
            last = key
    if abs(first - posBlub) > abs(len(zoneList) - last - posBlub):
        first = last
    return first

def setzeOutput(wert,zoneKey,zoneList,posBlub,output,abcList):
    diff = posBlub - zoneKey
    if abs(diff) > 15:
        if diff > 0:
            diff =  diff - len(zoneList)
        else:
            diff = len(zoneList) + diff
        moveW = ">"
        if diff > 0:
            moveW = "<"
    else:
        moveW = ">"
        if diff > 0:
            moveW = "<"
    #print(str(posBlub) + " = " + wert + " - " + zoneList[zoneKey] + " : " + str(diff),file=sys.stderr)

    for i in range(abs(diff)):
        output = output + moveW
    if not wert == zoneList[zoneKey]:
        if zoneList[zoneKey] == "-":
            addWert = abcList[wert]
        else:
            addWert = abcList[wert] - abcList[zoneList[zoneKey]]
        if addWert < 0:
            moveW = "-"
            if addWert > 13:
                moveW = "+"
                addWert = len(abcList) - addWert
        else:
            moveW = "+"
            if addWert > 13:
                moveW = "-"
                addWert = len(abcList) - addWert
        for i in range(abs(addWert)):
            output = output + moveW
        zoneList[zoneKey] = wert
    
    output = output + "."
    return output


def magicInit(magic_phrase,output):
    abcList = {' ':0}
    anzahlBuchstaben = {}
    posBlub = 0
    zoneList = {}
    for i in range(len(string.ascii_uppercase)):
        abcList[string.ascii_uppercase[i]] = i + 1
    #print(abcList,file=sys.stderr)
    for i in range(30):
        zoneList[i] = "-"
    #zoneList = {0: 'O', 1: 'R', 2: 'F', 3: 'A', 4: 'N', 5: 'E', 6: 'L', 7: 'S', 8: 'M', 9: 'I', 10: 'T', 11: 'C', 12: 'W', 13: 'U', 14: 'P', 15: 'Y', 16: 'H', 17: 'B', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' '}

    for i in range(len(magic_phrase)):
        buchstabe = magic_phrase[i]
        if not buchstabe in anzahlBuchstaben:
            anzahlBuchstaben[buchstabe] = 1
        else:
            anzahlBuchstaben[buchstabe] +=1
    print(anzahlBuchstaben,file=sys.stderr)

    for i in range(len(magic_phrase)):
        wert = magic_phrase[i]
        zoneKey = wertInZoneList(wert,zoneList,anzahlBuchstaben,abcList,posBlub)
        if zoneKey == 99:
            zoneKey = setzeZoneList(wert,zoneList,posBlub)
        anzahlBuchstaben[wert] -= 1
        output = setzeOutput(wert,zoneKey,zoneList,posBlub,output,abcList)
        posBlub = zoneKey
    print(zoneList,file=sys.stderr)
    return output





magic_phrase = "AZ"
magic_phrase = "O OROFARNE LASSEMISTA CARNIMIRIE O ROWAN FAIR UPON YOUR HAIR HOW WHITE THE BLOSSOM LAY"
 #             "O OROFARNE LASSEMISTA CARNIMIRIE O ROWAN FAIR UPON YOUR HAIR HFP P CWS W S BMFIIFT ME "
magic_phrase = "MIMAS"

output = ""
laengeInput = 0
laengeOutput = 0

#output = magicInit(magic_phrase,output)
#print(output)
#laengeOutput += len(output)
#laengeInput += len(magic_phrase)

datei = open("eingabe.txt",'r')
for zeile in datei:
    print(zeile[:-1],file=sys.stderr)
    magic_phrase = zeile
    output = ""
    output = magicInit(magic_phrase[:-1],output)
    print(output)
    laengeOutput += len(output)
    laengeInput += len(magic_phrase)

print("Länge Ergebnis: " + str(laengeInput) + " zu " + str(laengeOutput),file=sys.stderr)




