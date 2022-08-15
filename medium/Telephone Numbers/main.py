import sys
import math

def suche(wert,dict,anzahl):    
    if len(wert) == 0:
        return dict,anzahl

    t = wert[0]    
    if len(wert) > 1:
        wert=wert[1:]
    else:
        wert = ""
    if t in dict:
        dict[t],anzahl = suche(wert,dict[t],anzahl)
    else:
        anzahl +=1
        dict[t],anzahl = suche(wert,{},anzahl)
    return dict,anzahl

teleList = ['0467123456']  #1
teleList = ['0123456789', '1123456789']  #2
teleList = ['0123', '01']

anzahl = 0
ergDict = {}
for tele in teleList:
    if tele[0] in ergDict:
        ergDict[tele[0]],anzahl = suche(tele[1:],ergDict[tele[0]],anzahl)
    else:
        anzahl +=1
        ergDict[tele[0]],anzahl = suche(tele[1:],{},anzahl)


print(ergDict)
print(str(anzahl))