#  https://www.codingame.com/ide/puzzle/word-search-for-programmers


# medium: https://www.codingame.com/training/medium/hidden-word

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

rowList=[['I', 'P', 'L', 'U', 'C', 'J', 'M', 'C', 'N', 'Y'], ['A', 'A', 'F', 'I', 'I', 'V', 'A', 'D', 'Z', 'N'], ['T', 'F', 'U', 'U', 'S', 'W', 'G', 'H', 'W', 'E'], ['U', 'B', 'A', 'R', 'T', 'A', 'G', 'D', 'O', 'G'], ['Y', 'S', 'A', 'J', 'I', 'G', 'I', 'U', 'G', 'R'], ['D', 'T', 'E', 'M', 'R', 'F', 'E', 'O', 'K', 'A'], ['H', 'Y', 'T', 'E', 'B', 'K', 'Z', 'C', 'H', 'M'], ['B', 'O', 'M', 'A', 'H', 'A', 'R', 'B', 'A', 'L'], ['W', 'O', 'O', 'Q', 'P', 'U', 'E', 'R', 'N', 'E'], ['H', 'E', 'Z', 'U', 'Y', 'I', 'J', 'H', 'N', 'S']]
cluesList=['Abraham', 'Bart', 'Homer', 'Lisa', 'Maggie', 'Marge', 'Patty', 'Selma']
#cluesList=['LISA']


trefferList=[]
for clues in cluesList:
    suchList=[];gefunden=False
    for y in range(len(rowList)):
        for x in range(len(rowList)):
            if rowList[y][x] == clues[0]:
                gefunden,suchList = suche(rowList,y,x,clues.upper(),True,suchList)
                if gefunden:
                    break
            elif rowList[y][x] == clues[-1]:
                gefunden,suchList = suche(rowList,y,x,clues.upper(),False,suchList)
                if gefunden:
                    break
        if gefunden:
            trefferList += suchList[:]
            break
    
for y in range(len(rowList)):
    for x in range(len(rowList)):
        if setYX(y,x) in trefferList:
            print(rowList[y][x],end="")
        else:
            print(" ",end="")
    print("")