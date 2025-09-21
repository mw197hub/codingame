# https://www.codingame.com/ide/puzzle/the-fastest

import sys,math

def getWert(wert):
    antwort=""
    for w in wert:
        if w.isnumeric():
            antwort+=w
    return antwort

tList=['10:15:46', '03:59:08', '04:00:08', '03:59:09']

antwort=tList[0]
wert1 = int(getWert(tList[0]))
for i in range(1,len(tList)):
    wert2 = int(getWert(tList[i]))
    if wert2 < wert1:        
        antwort=tList[i]
        wert1=wert2

print(antwort)