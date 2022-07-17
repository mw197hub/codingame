from re import X
import sys
import math
import string

def getWerte():
    i = 0;abcList={};zahlList={}
    for wert in string.ascii_uppercase:
        zahlList[i]=wert
        abcList[wert] = i;i+=1
    return abcList,zahlList

def setWert(i,zahl,f,iList,zahlList):
    wert = int(zahl % f) + iList[i]
    if wert > 25:
        wert = wert -26;iList[i-1] +=1
    erg = zahlList[wert]
    zahl = int(zahl/f)
    return erg,zahl,iList

x = "AB-123-CD";n=5
x = "AA-999-ZZ";n=1
x = "AZ-566-QS";n=100  # AZ-666-QS
#x = "BW-999-GH";n=1
#x = "CG-007-CG";n=10000  # CG-017-CQ
x = "IO-010-OI";n=100000  #IO-110-SE
#x = "ER-963-DF";n=87654321  # JQ-027-XY
x = "AA-998-AA";n=1   # AA-999-AA

abcList,zahlList = getWerte()
print(abcList)
erg ="    "
f = 26;nummer=0

iList = [abcList[x[0]],abcList[x[1]],abcList[x[7]],abcList[x[8]],int(x[3:6])]
zahl = iList[4] + n
if not zahl == 999:
    nummer = zahl % 999;zahl = int(zahl / 999)
else:
    nummer = zahl;zahl = 0
erg3,zahl,iList = setWert(3,zahl,f,iList,zahlList)
erg2,zahl,iList = setWert(2,zahl,f,iList,zahlList)
erg1,zahl,iList = setWert(1,zahl,f,iList,zahlList)
erg0,zahl,iList = setWert(0,zahl,f,iList,zahlList)

nr = "000" + str(nummer)
print(erg0+erg1+"-"+nr[len(nr)-3:]+"-"+erg2+erg3)