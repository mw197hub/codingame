#  https://www.codingame.com/ide/puzzle/sudoku-solver

import sys,math

def loesPruef(outList,loesList):
    print("             ",file=sys.stderr)
    for y in range(9):
        for x in range(9):
            if not outList[y][x] == loesList[y][x] and not outList[y][x] == "0":
                print("Fehler {}-{} wert: {} zu {}".format(y,x,loesList[y][x],outList[y][x]),file=sys.stderr)

def klarstellen(ziffer,y,x,optList):
    for i in range(9):
        if ziffer in optList[y][i]:
            optList[y][i].remove(ziffer)
        if ziffer in optList[i][x]:
            optList[i][x].remove(ziffer)
    yS=0;xS=0
    if y > 2:
        yS+=3
    if y > 5:
        yS+=3
    if x > 2:
        xS+=3
    if x > 5:
        xS+=3
    for yN in range(yS,yS+3):
        for xN in range(xS,xS+3):
            if ziffer in optList[yN][xN]:
                optList[yN][xN].remove(ziffer)

def getZeile(y,x,outList,retList):
    tList=[]
    for i in range(9):
        if not outList[y][i] == "0":
            tList.append(outList[y][i])
            if outList[y][i] in retList:
                retList.remove(outList[y][i])
    return tList
def getSpalte(y,x,outList,retList):
    tList=[]
    for i in range(9):
        if not outList[i][x] == "0":
            tList.append(outList[i][x])
            if outList[i][x] in retList:
                retList.remove(outList[i][x])
    return tList
def getFeld(y,x,outList,retList):
   # if y == 3 and x == 5:
   #     print(retList,file=sys.stderr)
    tList=[]
    yS=0;xS=0
    if y > 2:
        yS+=3
    if y > 5:
        yS+=3
    if x > 2:
        xS+=3
    if x > 5:
        xS+=3
    for yN in range(yS,yS+3):
        for xN in range(xS,xS+3):
            if not outList[yN][xN] == "0":
                tList.append(outList[yN][xN])
                if outList[yN][xN] in retList:
                    retList.remove(outList[yN][xN])
    return tList

def ausgabe(outList,runde):
    for y in range(9):
        for x in range(9):
            print(outList[y][x]+"|",end="")
            if x == 2 or x ==5:
                print(" ",end="")
        print("")
        if y == 2 or y == 5:
            print("--------------------") 
    print("## "+str(runde)+" #############")

def zaehlFeld(ziffer,y,x,outList,optList):
 #   if y == 1 and x ==6:
 #      print(optList[y][x],file=sys.stderr)
    anzahl=0
    yS=0;xS=0
    if y > 2:
        yS+=3
    if y > 5:
        yS+=3
    if x > 2:
        xS+=3
    if x > 5:
        xS+=3
    for yN in range(yS,yS+3):
        for xN in range(xS,xS+3):
            if outList[yN][xN] == ziffer:
                return 0
            if ziffer in optList[yN][xN]:
                anzahl+=1
    return anzahl
def zaehlZeile(ziffer,y,x,outList,optList):
    anzahl=0
    for i in range(9):
        if outList[y][i] == ziffer:
                return 0
        if ziffer in optList[y][i]:  
            anzahl+=1
    return anzahl
def zaehlSpalte(ziffer,y,x,outList,optList):
    anzahl=0
    for i in range(9):
        if outList[i][x] == ziffer:
                return 0
        if ziffer in optList[i][x]:  
            anzahl+=1
    return anzahl

def pruefQuer(ziffer,feld,optList,outList):
    felder=[];zifferList=[]
    for y in range(feld[0],feld[0]+3):
        for x in range(feld[1],feld[1]+3):
            if ziffer == outList[y][x]:                
                return
            felder.append([y,x])
            if ziffer in optList[y][x]:
                if not [y,x] in zifferList:
                    zifferList.append([y,x])

    #print(feld,file=sys.stderr)
    for y in range(feld[0],feld[0]+3):   
        yList,xList=[],[]
        intern=True
        for x in range(9):
            oList = optList[y][x]            
            if ziffer in optList[y][x]:
                if not [y,x] in felder:
                    intern=False
                if not [y,x] in yList:
                    yList.append([y,x])
        if intern:
            for x in range(feld[1],feld[1]+3):
                for y in range(9):            
                    if ziffer in optList[y][x]:
                        if not [y,x] in felder:
                            intern=False
                        if not [y,x] in xList:
                            xList.append([y,x])
                if intern:
                    for yL in yList:
                        if yL in xList:
                            outList[yL[0]][yL[1]] = ziffer
                            optList[yL[0]][yL[1]].clear()
                            klarstellen(ziffer,yL[0],yL[1],optList)
                            return

def pruefZweiZiffer(ziffer,feld,optList,outList):
    felder=[];zweiList=[];zahlDict={}
    for zahl in range(1,10):
        ziffer = str(zahl)
        zahlDict[ziffer] = []
        for y in range(feld[0],feld[0]+3):
            for x in range(feld[1],feld[1]+3):
                oList = optList[y][x]
                if ziffer in optList[y][x]:
                    zahlDict[ziffer].append([y,x])
    for zahl,zList in zahlDict.items():
        if len(zList) == 2:
            for zahl2,zList2 in zahlDict.items():
                if not zahl2 == zahl and sorted(zList2) == sorted(zList):
                    for z in zList:
                        optList[z[0]][z[1]].clear()
                        optList[z[0]][z[1]].append(zahl)
                        optList[z[0]][z[1]].append(zahl2)
                    
                    for y in range(feld[0],feld[0]+3):
                        for x in range(feld[1],feld[1]+3):
                            if not [y,x] in zList:
                                if zahl in optList[y][x]:
                                    optList[y][x].remove(zahl)
                                if zahl2 in optList[y][x]:
                                    optList[y][x].remove(zahl2)   
                   # print('{}-{}: {}'.format(8,6,optList[8][6]))            

lineList=[['1', '2', '0', '0', '7', '0', '5', '6', '0'], ['5', '0', '7', '9', '3', '2', '0', '8', '0'], ['0', '0', '0', '0', '0', '1', '0', '0', '0'], ['0', '1', '0', '2', '4', '0', '0', '5', '0'], ['3', '0', '8', '0', '0', '0', '4', '0', '2'], ['0', '7', '0', '0', '8', '5', '0', '1', '0'], ['0', '0', '0', '7', '0', '0', '0', '0', '0'], ['0', '8', '0', '4', '2', '3', '7', '0', '1'], ['0', '3', '4', '0', '1', '0', '0', '2', '8']]
lineList=[['0', '0', '0', '7', '0', '0', '0', '4', '0'], ['0', '2', '0', '8', '0', '1', '9', '0', '0'], ['0', '0', '0', '0', '0', '0', '1', '7', '3'], ['1', '0', '2', '0', '0', '6', '0', '9', '7'], ['6', '0', '0', '0', '9', '0', '0', '0', '1'], ['9', '7', '0', '1', '0', '0', '4', '0', '5'], ['3', '5', '4', '0', '0', '0', '0', '0', '0'], ['0', '0', '8', '6', '0', '4', '0', '3', '0'], ['0', '1', '0', '0', '0', '3', '0', '0', '0']]
lineList=[['0', '0', '6', '0', '0', '0', '0', '5', '0'], ['0', '0', '3', '7', '0', '0', '0', '0', '0'], ['7', '0', '0', '0', '3', '5', '0', '0', '8'], ['0', '0', '0', '0', '7', '0', '0', '1', '2'], ['0', '0', '0', '9', '4', '2', '0', '0', '0'], ['6', '2', '0', '0', '8', '0', '0', '0', '0'], ['9', '0', '0', '1', '2', '0', '0', '0', '3'], ['0', '0', '0', '0', '0', '3', '6', '0', '0'], ['0', '5', '0', '0', '0', '0', '7', '0', '0']]
lineList=[['8', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '3', '6', '0', '0', '0', '0', '0'], ['0', '7', '0', '0', '9', '0', '2', '0', '0'], ['0', '5', '0', '0', '0', '7', '0', '0', '0'], ['0', '0', '0', '0', '4', '5', '7', '0', '0'], ['0', '0', '0', '1', '0', '0', '0', '3', '0'], ['0', '0', '1', '0', '0', '0', '0', '6', '8'], ['0', '0', '8', '5', '0', '0', '0', '1', '0'], ['0', '9', '0', '0', '0', '0', '4', '0', '0']]



#lineList.clear()
#lineList.append(list("000001005"))
#lineList.append(list("000008009"))
#lineList.append(list("000900042"))
#lineList.append(list("080010906"))
#lineList.append(list("000009500"))
#lineList.append(list("905003007"))
#lineList.append(list("000070001"))
#lineList.append(list("500030790"))
#lineList.append(list("762194050"))

loesList=[]
loesList.append(list('812753649'))
loesList.append(list('943682175'))
loesList.append(list('675491283'))
loesList.append(list('154237896'))
loesList.append(list('369845721'))
loesList.append(list('287169534'))
loesList.append(list('521974368'))
loesList.append(list('438526917'))
loesList.append(list('796318452'))

text=""
for line in lineList:
    for l in line:
        text+=l
print(text)


optList=[[ ['1','2','3','4','5','6','7','8','9'] for y in range(9)] for x in range(9)]
outList=lineList[:]
nichtFertig=True;runde=0
feldStart=[[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
while nichtFertig:
    nichtFertig=False
    for y in range(9):
        for x in range(9):
            if not outList[y][x] == "0":
                optList[y][x].clear()                
            else:
                nichtFertig=True
                zeile = getZeile(y,x,outList,optList[y][x])
                spalte = getSpalte(y,x,outList,optList[y][x])
                feld = getFeld(y,x,outList,optList[y][x])
                if len(optList[y][x]) == 1:
                    outList[y][x] = optList[y][x][0]
                    optList[y][x].clear()
                    klarstellen(outList[y][x],y,x,optList)
 #   ausgabe(outList,runde)
    for ziffer in range(1,10):
        for y in range(9):
            for x in range(9):
                if outList[y][x] == "0":
                    anzahl = zaehlFeld(str(ziffer),y,x,outList,optList)
                    if anzahl == 1 and str(ziffer) in optList[y][x]:
                        outList[y][x] = str(ziffer)
                        optList[y][x].clear()
                        klarstellen(outList[y][x],y,x,optList)
                    anzahl = zaehlZeile(str(ziffer),y,x,outList,optList)
                    if anzahl == 1 and str(ziffer) in optList[y][x]:
                        outList[y][x] = str(ziffer)
                        optList[y][x].clear()
                        klarstellen(outList[y][x],y,x,optList)
                    anzahl = zaehlSpalte(str(ziffer),y,x,outList,optList)
                    if anzahl == 1 and str(ziffer) in optList[y][x]:
                        outList[y][x] = str(ziffer)
                        optList[y][x].clear()
                        klarstellen(outList[y][x],y,x,optList)
            # ausschlussverfahren duch merkziffern
            # zahl im kreuzungspunkt finden  4-3 = 3
    for ziffer in range(1,10):
        for feld in feldStart:
            pruefQuer(str(ziffer),feld,optList,outList)
    for feld in feldStart:
        pruefZweiZiffer(str(ziffer),feld,optList,outList)

    loesPruef(outList,loesList)
    ausgabe(outList,runde)
    runde+=1
    if runde > 10:
        break

for y in range(9):
    for x in range(9):
        print(outList[y][x],end="")
    print("")

yxList=[[6,6],[6,7],[7,8],[8,6],[8,8],[5,5],[1,2]]
for yx in yxList:
    print('{}-{}: {}'.format(yx[0],yx[1],optList[yx[0]][yx[1]]),file=sys.stderr)