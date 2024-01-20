# https://www.codingame.com/training/easy/anagram-to-break-the-code

import sys,math

def anhaengen(zahl,satzList):
    w = str(zahl)
    satzList.append(w[-1])

def sucheAna(word,satzList):
    for sa in satzList:
        if not sa == word:
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

######

word="god";satz="My dog scared them away"
word="baker";satz="I need a break now !"
word="flow";satz="In the silence of the night,a lone wolf howled."
word="cheater";satz="The teacher told us a funny story. He is the best teacher, even though he has the least experience. Our teacher looks very young."


word="cautioned";satz="educbtiom deucatiox education cautionea!!! gogogonow."
word="mastering";satz="mastering streaming is very important for teenagers"

######

markList=[":",".",",","?","!"]
word=word.lower()
satzN=""
for mark in markList:
    satz = satz.replace(mark," ")
for s in satz:
    if not s in markList:
        satzN+=s.lower()
satzN=satzN.strip()    
satzL=satzN.split(" ")
satzList=[]
for s in satzL:
    if not s == "":
        satzList.append(s)



anagram=sucheAna(word,satzList)

if len(anagram) == 0:
    print("IMPOSSIBLE")
else:
    codeList=[]
    
    pos=-1;vorher,nachher=0,0
    for i in range(len(satzList)):
        if anagram == satzList[i] and pos == -1:
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