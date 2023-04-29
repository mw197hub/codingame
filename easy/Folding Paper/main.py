import sys,math,copy

def setAktion(aktion,wert,sideWerte):
    if aktion[0] == "=":
        return 1
    if aktion[0] == "+":
        return wert + sideWerte[aktion[1]]
    return wert *2


order='UL'
side="D"
order="DRUL"
side="D"


sideDict={'R':['=1','+R','*2','*2'],'L':['+L','=1','*2','*2'],'U':['*2','*2','=1','+U'],'D':['*2','*2','+D','=1']}  # R L U D
sideWerte={'R':1,'L':1,'U':1,'D':1}
orderList=['R','L','U','D']


for o in order:
    aktionList = sideDict[o]
    sideSave={}
    for i in range(4):
        sideSave[orderList[i]] = setAktion(aktionList[i],sideWerte[orderList[i]],sideWerte)
    sideWerte= copy.deepcopy(sideSave)
    print(sideWerte,file=sys.stderr)
print(sideWerte[side])