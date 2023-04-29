import sys,math,time

def zahlUmschreiben(zahl,trueDict,falseList):
    nZahl="";erg="true"
    for z in zahl:
        if z in falseList:
            return "false" 
        if z in trueDict:
            nZahl+=trueDict[z]
    reversZahl=""
    for i in range(len(zahl)-1,-1,-1):
        reversZahl+= nZahl[i]
    if not reversZahl == zahl:
        erg="false"
    return erg

trueDict={'0':'0','1':'1','2':'2','5':'5','6':'9','8':'8','9':'6'}
falseList=['3','4','7']
nextZahl={'0':'1','1':'2','2':'5','5':'6','6':'8','8':'9','9':'0','3':'5','4':'5','7':'8'}
mittList=['0','1','2','5','8']
zahl = "69"  # true  88
#zahl = "6920158510269" # true  6920160910269
#zahl = "654321" # false  655559
zahl = "314159265359"  ## false   500000000005        
#zahl = "6920158510269"  ## true  6920168910269
#zahl = "12688109960188921"  # false  12688110001188921
#zahl = "123456789"  # false  125000521
#zahl = "88888888"  # true 88896888
#zahl = "9987" # false  100001

start=time.time()
erg="true";nZahl="88"
erg = zahlUmschreiben(zahl,trueDict,falseList)
print(erg)
wertList=list(zahl)
ungerade = False if len(zahl)%2==0 else True
if len(zahl) > 7:
    if erg == "true":
        if ungerade:
            mitte=len(zahl)//2
            if wertList[mitte] in mittList:
                wertList[mitte] = nextZahl[str(mitte)]
            else:
                a=0
    mitte=int(len(zahl)//2) if ungerade else int(len(zahl)//2 -1)
    teilZahl=zahl[:mitte+1]
    if teilZahl[0] in falseList:
        teilZahl = nextZahl[teilZahl[0]] + "00000000000000"[:len(teilZahl)-1]
    teilZahl = int(teilZahl)
    for i in range(100000):
        if zahl[0] in falseList:
            teil1 = teilZahl + i
        else:
            teil1 = teilZahl + i +1
        if len(str(teil1)) > len(str(teilZahl)):
            ungerade = True if ungerade == False else False
        wert=str(teil1)
        pos = len(wert) -2 if ungerade else len(wert) -1
        for z in range(pos,-1,-1):
            if wert[z] in ['6','9']:
                if wert[z] == '6':
                    wert+='9'
                else:
                    wert+='6'
            else:
                wert+=wert[z]
        erg = zahlUmschreiben(str(wert),trueDict,falseList)
        if erg == "true":
            print(str(wert))
            break
else:
    for z in range(int(zahl)+1,int(zahl)+1000000):
        erg = zahlUmschreiben(str(z),trueDict,falseList)
        if erg == "true":
            print(str(z))
            break

print(time.time()-start,file=sys.stderr)

exit(0)

if len(zahl) > 7:
    nWert="";treffer=True
    for i in range(len(zahl)//2+1):
        if zahl[i] in falseList:
            treffer=False
            nWert += nextZahl[zahl[i]]
            for i in range(len(zahl)-len(nWert)-1):
                nWert+="0"
            break
        else:
            nWert+=zahl[i]
    if not treffer:
        zahl=nWert + "00000000000000"[:len(zahl)-len(nWert)]
    if treffer:
        nWert=""
        mitte = len(zahl)//2 -1
        saveWert=""
        for i in range(len(zahl)):
            if i == mitte:
                if zahl[i] == "9":
                    nWert=nWert[:-1]
                    nWert+="10"
                else:
                    nWert+=nextZahl[zahl[i]]
                saveWert=nWert
            elif i > mitte:
                if mitte%2 == 1:
                    if i == mitte +1:
                        if zahl[mitte] == "9":
                            nWert+="0"
                        else:
                            if saveWert[-1] == "9":
                                nWert+="6"
                            else:
                                #nWert+=saveWert[-1]
                                nWert+="0"
                    else:
                        pos = i-1 -mitte
                        if saveWert[pos*-1] == "9":
                            nWert+="6"
                        else:
                            nWert+=saveWert[pos*-1]
                else:
                    pos=i-1 -mitte
                    if saveWert[pos*-1] == "9":
                        nWert+="6"
                    else:
                        nWert+=saveWert[pos*-1]
            else:
                nWert+=zahl[i]
        zahl=nWert[:-1]+"0"
for z in range(int(zahl)+1,int(zahl)+10000000000):
    erg = zahlUmschreiben(str(z),trueDict,falseList)
    if erg == "true":
        print(str(z))
        break

print(time.time()-start,file=sys.stderr)