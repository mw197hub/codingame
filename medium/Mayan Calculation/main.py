import sys
import math

def getErg(erg,l,zahlDict):
    out = int(erg / 20)
    if out > 20:
        out = getErg(out,l,zahlDict)        
    s = zahlDict[out]        
    for i in range(h):
        print(s[i*l:i*l+l])
    return erg % 20

def getWert(nWert,h,l,zahlDict):
    wert = 0
    durchLauf = int(len(nWert)/l/h) -1
    for i in range(int(len(nWert)/l/h)):
        n = nWert[i*l*h:i*l*h+l*h]
        for zahl,wort in zahlDict.items():
            if wort == n:
                if durchLauf == 0:
                    wert += zahl
                else:
                    wert += zahl * 20** durchLauf
                break
        durchLauf -= 1
    return wert

l,h=4,4 #1
nList=['.oo.o...oo..ooo.oooo....o...oo..ooo.oooo....o...oo..ooo.oooo....o...oo..ooo.oooo', 'o..o................____________________________________________________________', '.oo.....................................________________________________________', '............................................................____________________']
n1="o..............."
n2="o..............."
operation="+"

l,h=4,4 #5
nList=['.oo.o...oo..ooo.oooo....o...oo..ooo.oooo....o...oo..ooo.oooo....o...oo..ooo.oooo', 'o..o................____________________________________________________________', '.oo.....................................________________________________________', '............................................................____________________']
n1="o...____........ooo............."
n2="oo..____........"
operation="-"

zahlDict = {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: '', 15: '', 16: '', 17: '', 18: '', 19: ''}
for n in nList:
    for i in range(20):
        zahlDict[i] += n[i*l:i*l+l]
wert1 = getWert(n1,h,l,zahlDict)
wert2 = getWert(n2,h,l,zahlDict) 
erg = eval(str(wert1)+" " + operation +" "+ str(wert2))
print(str(wert1) + " " + operation + " " + str(wert2) + " = "+str(erg),file=sys.stderr)

if erg > 20:
    erg = getErg(erg,l,zahlDict)
    s = zahlDict[erg]    
    for i in range(h):
        print(s[i*l:i*l+l])
else:
    s = zahlDict[erg]    
    for i in range(h):
        print(s[i*l:i*l+l])
    
    
        

