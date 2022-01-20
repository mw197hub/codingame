import sys
import math
import string

def getZoneKey(wert,zoneList,anzahlBuchstaben,abcList,posBlub):
    zoneKey = -1
    zoneWert = 99
    for key, value in zoneList.items():
        diff = 0
        if value == "-":
            diff = abcList[wert]
        else:
            diff = abs(abcList[value] - abcList[wert])
        if diff > 13:
            diff = len(abcList) - diff
        abstand = abs(posBlub - key)
        if abstand > 15:
            abstand = len(zoneList) - abstand
        if abstand + diff < zoneWert:
            zoneKey = key
            zoneWert = abstand + diff
    return zoneKey

def pruefWiederholung(magic_phrase):
    for i in range(len(magic_phrase)-1):
        if not magic_phrase[i] == magic_phrase[i+1]:
            return 0

    return 1


def setPlusMinus(zoneList,zoneKey,wert,abcList):
    oput = ""
    if zoneList[zoneKey] == "-":
            addWert = abcList[wert]
    else:
        addWert = abcList[wert] - abcList[zoneList[zoneKey]]
    if addWert < 0:
        moveW = "-"
        if addWert < -13:
            moveW = "+"
            addWert = len(abcList) + addWert
    else:
        moveW = "+"
        if addWert > 13:
            moveW = "-"
            addWert = len(abcList) - addWert
    for i in range(abs(addWert)):
        oput = oput + moveW
    zoneList[zoneKey] = wert
    return oput

def wertInZoneList(wert,zoneList,anzahlBuchstaben,abcList):
    for key, value in zoneList.items():
        if wert == value:
            return key
    abstand = abcList[wert]
    pos = 99
    for key, value in anzahlBuchstaben.items():
        if value >= 0:
            diff = abs(abcList[key] - abcList[wert])
            if diff < abstand:
                for key2, value2 in zoneList.items():
                    if key == value2:
                        pos = key2
                        abstand = diff
                        break
    return pos
def setzeZoneList(wert,zoneList):
    for key, value in zoneList.items():
        if value == "-":
            return key
    return 99
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
        output = output + setPlusMinus(zoneList,zoneKey,wert,abcList)
        
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

    wiederholung = pruefWiederholung(magic_phrase)
    if wiederholung > 0:
        wert = magic_phrase[0]
        zoneKey = 0
        output = setPlusMinus(zoneList,zoneKey,wert,abcList)
        output = output + ">"
        laengePhrase = len(magic_phrase)
        while laengePhrase > 26:
            output = output + "-[<.>-]"
            laengePhrase -= 26
        if laengePhrase < 10:
            output = output + "<"
            for i in range(laengePhrase):
                output = output + "."
        else:
            for i in range(27 - laengePhrase):
                output = output + "-"
            output = output + "[<.>-]"

    else:
        for i in range(len(magic_phrase)):
            wert = magic_phrase[i]
            #zoneKey = wertInZoneList(wert,zoneList,anzahlBuchstaben,abcList)
            #if zoneKey == 99:
            #    zoneKey = setzeZoneList(wert,zoneList)
            zoneKey = getZoneKey(wert,zoneList,anzahlBuchstaben,abcList,posBlub)
            anzahlBuchstaben[wert] -= 1
            output = setzeOutput(wert,zoneKey,zoneList,posBlub,output,abcList)
            posBlub = zoneKey
    print(zoneList,file=sys.stderr)
    return output





magic_phrase = "AZ"
magic_phrase = "O OROFARNE LASSEMISTA CARNIMIRIE O ROWAN FAIR UPON YOUR HAIR HOW WHITE THE BLOSSOM LAY"
 #             "O OROFARNE LASSEMISTA CARNIMIRIE O ROWAN FAIR UPON YOUR HAIR HFP P CWS W S BMFIIFT ME "
magic_phrase = "MIMAS"
magic_phrase = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
magic_phrase = "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
magic_phrase = "ZAZA"

output = ""
laengeInput = 0
laengeOutput = 0

output = magicInit(magic_phrase,output)
print(output)
laengeOutput += len(output)
laengeInput += len(magic_phrase)

#datei = open("eingabe.txt",'r')
#for zeile in datei:
#    print(zeile[:-1],file=sys.stderr)
#    magic_phrase = zeile
#    output = ""
#    output = magicInit(magic_phrase[:-1],output)
#    print(output)
#    laengeOutput += len(output)
#    laengeInput += len(magic_phrase)

print("Länge Ergebnis: " + str(laengeInput) + " zu " + str(laengeOutput),file=sys.stderr)




