# https://www.codingame.com/ide/puzzle/playing-card-odds

import sys,math,string

def getKarten(teilList,zahl,farbe):
    zList=[];fList=[];eList=[]
    for wort in teilList:
        zList.clear();fList.clear()
        for r in wort:
            if r in zahl:
                zList.append(r)
            else:
                fList.append(r)
        if len(zList) == 0 or len(fList) == 0:
            if len(zList) == 0:
                for z in zahl:
                    for f in fList:
                        wert=z+f
                        if wert not in eList:
                            eList.append(wert)
            else:
                for z in zList:
                    for f in farbe:
                        wert=z+f
                        if wert not in eList:
                            eList.append(wert)
        else:
            for z in zList:
                for f in fList:
                    wert=z+f
                    if wert not in eList:
                        eList.append(wert)
    return eList

#######

removedList=['45C'];soughtList=['7H']
removedList=['45C'];soughtList=['7', 'H']
removedList=['7', 'H'];soughtList=['7H', '7D', 'KH']

#####

cardList=[]
zahl=['2','3','4','5','6','7','8','9','T','J','Q','K','A']
farbe=['C','D','H','S']
for z in zahl:
    for f in farbe:
        wert=z+f
        cardList.append(wert)
print(cardList,file=sys.stderr)

remList = getKarten(removedList,zahl,farbe)
souList = getKarten(soughtList,zahl,farbe)
for r in remList:
    cardList.remove(r)
treffer=0
for s in souList:
    if s in cardList:
        treffer+=1
erg = round((treffer/len(cardList)*100),0)

print("{}%".format(int(erg)))

