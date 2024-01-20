# https://www.codingame.com/training/easy/anagram-to-break-the-code

import sys,math

def anhaengen(zahl,satzList):
    w = str(zahl)
    satzList.append(w[-1])

def sucheAna(word,satzList):
    for sa in satzList:
        wList=list(word)
        posList=[];treffer=True
        for i in range(len(sa)):
            if sa[i] in wList:
                wList.remove(sa[i])
            else:
                treffer=False
        if treffer and len(wList) == 0:
            return sa
    return ""


word="god";satz="My dog scared them away"
word="baker";satz="I need a break now !"


word=word.lower()
satzN=""
for s in satz:
    if not s in [":",".",",","?","!"]:
        satzN+=s.lower()
satzN=satzN.strip()    
satzList=satzN.split(" ")
anagram=sucheAna(word,satzList)

if len(anagram) == 0:
    print("IMPOSSIBLE")
else:
    codeList=[]
    
    pos=-1;vorher,nachher=0,0
    for i in range(len(satzList)):
        if anagram == satzList[i]:
            pos=i
        else:
            if pos > -1:
                nachher+=len(satzList[i])
            else:
                vorher+=len(satzList[i])
    anhaengen(pos,codeList)
    anhaengen(len(satzList)-1-pos,codeList)
    anhaengen(vorher,codeList)
    anhaengen(nachher,codeList)

    #print(codeList,file=sys.stderr)
    erg=""
    for code in codeList:
        erg+=code+"."
    print(erg[:-1])