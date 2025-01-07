# https://www.codingame.com/ide/puzzle/find-the-winning-strategy

import sys,math,string


def getAnzahlZuege(gameList):
    anzahl=0;fertig=0
    for columen in gameList:
        wert=columen[1] - columen[0] -1
        anzahl+=wert
        if wert == 0:
            fertig +=1
    return anzahl,len(gameList)-fertig

def ungerade(wert):
    if wert %2:
        return True
    return False

def sucheColumn(gameList,move):
    abgleichen=False;maxAbstand=-1;gefundenColumen=-1
    for i in range(len(gameList)):
        columen = gameList[i]
        if columen[1] - columen[0] -1 > maxAbstand:
            gefundenColumen=i;maxAbstand=columen[1] - columen[0] -1
    if gefundenColumen > -1:
        columen = gameList[i]
        return gefundenColumen, columen[0]+move

    for i in range(len(gameList)):
        columen = gameList[i]
        abstand = columen[1] - columen[0] -1
        if abstand > 0:
            if ungerade(move) and not ungerade(abstand):
                return i, columen[0]+move
            if not ungerade(move) and ungerade(abstand):
                return i, columen[0]+move
    return -1,-1

##############################
#1
rows=2;columns=6
gameList=[[1, 5], [0, 5]]
gameList=[[1, 4], [1, 5]]
#2 
#rows=1;columns=30
#gameList=[[0, 29]]
#3
#rows=5;columns=11
#gameList=[[4, 6], [3, 7], [2, 8], [1, 9], [0, 10]]


###############################
# auf gerade Zahl gehen und Spalten gerade offen halten
# alle Columens bei gerader Anzahl auf ungerade, bei ungerade alle auf gerade

while True:
    col=-1;row=-1
    anzahlZuege, offeneColumen = getAnzahlZuege(gameList)
    if offeneColumen == 1:
        for i in range(len(gameList)):
            columen = gameList[i]
            if columen[1] - columen[0] -1 > 0:
                col=i;row=columen[1] -1

    else:
        move = 1
        if ungerade(anzahlZuege) and not ungerade(offeneColumen):
            move = 1
        else:
            move = 2
        col,row = sucheColumn(gameList,move)

    print("{} {}".format(col,row))
    
    


#########
    break