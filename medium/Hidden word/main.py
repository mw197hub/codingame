# https://www.codingame.com/ide/puzzle/hidden-word

import sys,math

def setYX(y,x):
    return str(y)+"-"+str(x)

def suche(rowList,y,x,clues,normal,suchList):
    moveList=[[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
    
    if y == 0 and x == 2:
        a=0
    for move in moveList:
        yN=y;xN=x;word=rowList[y][x];searchList=[]
        searchList.append(setYX(y,x))
        for i in range(1,len(clues)):        
            yN+=move[0];xN+=move[1]
            if yN >= 0 and yN < len(rowList) and xN >= 0 and xN < len(rowList):
                word += rowList[yN][xN]
                searchList.append(setYX(yN,xN))
            else:
                break
        if word == clues:
            suchList = searchList[:]
            return True,suchList
    return False,[]



wordList=['BAC', 'BOB']
rowList=['BAC', 'BOB', 'RED']
wordList=['BASSOV', 'CELINE', 'CHASSIGNET', 'CISTE', 'COLATURES', 'COUSAIS', 'EAMES', 'ENJUGUENT', 'ERES', 'ESCROC', 'FAUCHARDS', 'GRAUBUNDEN', 'INSERAIENT', 'MALMENEES', 'MEDIUMNITES', 'NARREES', 'NITRIFIAT', 'ODES', 'REGORGEA', 'SURSITES', 'TUERA', 'VOLLEYBALL']
rowList=['VCENJUGUENTO', 'OCORCSEERRAN', 'SOCHASSIGNET', 'SDRAHCUAFDND', 'AENMALMENEES', 'BSETINMUIDEM', 'VOLLEYBALLTG', 'COLATURESAUM', 'ISEMAEGROGER', 'SSURSITESERE', 'TEGNITRIFIAT', 'ENILECOUSAIS']





trefferList=[]
for word in wordList:
    suchList=[];gefunden=False
    for y in range(len(rowList)):
        for x in range(len(rowList)):
            if rowList[y][x] == word[0]:
                gefunden,suchList = suche(rowList,y,x,word.upper(),True,suchList)
                if gefunden:
                    break
        if gefunden:
            trefferList += suchList[:]
            break
    
erg=""
for y in range(len(rowList)):
    for x in range(len(rowList)):
        if setYX(y,x) in trefferList:
            #print(" ",end="")
            a=0
        else:            
          #  print(rowList[y][x],end="")
            erg+=rowList[y][x]
    #print("")
print(erg)