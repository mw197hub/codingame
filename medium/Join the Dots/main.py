# https://www.codingame.com/ide/puzzle/join-the-dots

import sys,math,string

def setzeZeichen(neu,bisher):
    if bisher == "o":
        return "o"
    if bisher == " " or bisher == neu:
        return neu
    if (bisher == "-" and neu == "|") or (neu == "-" and bisher == "|"):
        return "+"
    if (bisher == "\\" and neu == "/") or (neu == "\\" and bisher == "/"):
        return "X"
    if ((bisher == "|" or bisher == "-") and (neu == "/" or neu == "\\")) or ((neu == "|" or neu == "-") and (bisher == "/" or bisher == "\\")):
        return "*"
    return "*"
####

rowList=['1..2', '5...', '....', '4..3'] #1
rowList=['1...4', '.....', '.....', '.....', '3...2'] #3
rowList=['.......1.....6.......', '.....................', '.....................', '4...................3', '.....................', '.....................', '.....................', '.....................', '.....5.........2.....']  #7



####
reihenfolge="123456789"+string.ascii_uppercase
pointDict={}
ausgabeList=[]
for y in range(len(rowList)):
    row=[]
    for x in range(len(rowList[0])):        
        if not rowList[y][x] == ".":
            pointDict[rowList[y][x]]=[x,y]
            row.append("o")
        else:
            row.append(" ")
    ausgabeList.append(row[:])

for i in range(len(reihenfolge)):
    start=reihenfolge[i];ziel="111"
    if i+1 < len(reihenfolge):
        ziel=reihenfolge[i+1]  #ende pruefen?
    if ziel in pointDict:
        start=pointDict[start];ziel=pointDict[ziel]
        xDiff=ziel[0]-start[0];yDiff=ziel[1]-start[1]
        if not abs(xDiff) == 0 and abs(yDiff) == 0:
            for m in range(abs(xDiff)):
                diff = m+1
                if xDiff < 0:
                    diff=diff * -1
                ausgabeList[ziel[1]][start[0]+diff]= setzeZeichen("-",ausgabeList[ziel[1]][start[0]+diff])
        if abs(xDiff) == 0 and not abs(yDiff) == 0:
            for m in range(abs(yDiff)):
                diff = m+1
                if yDiff < 0:
                    diff=diff * -1
                ausgabeList[start[1]+diff][start[0]]= setzeZeichen("|",ausgabeList[start[1]+diff][start[0]])  
        if not abs(xDiff) == 0 and not abs(yDiff) == 0:
            for m in range(abs(yDiff)):
                ydiff = m+1
                if yDiff < 0:
                    ydiff=ydiff * -1
                xdiff = m+1
                if xDiff < 0:
                    xdiff=xdiff * -1
                if (xDiff < 0 and yDiff > 0) or (xDiff > 0 and yDiff < 0):
                    ausgabeList[start[1]+ydiff][start[0]+xdiff]= setzeZeichen("/",ausgabeList[start[1]+ydiff][start[0]+xdiff])
                else:
                    ausgabeList[start[1]+ydiff][start[0]+xdiff]= setzeZeichen("\\",ausgabeList[start[1]+ydiff][start[0]+xdiff])
    else:
        break

for aList in ausgabeList:
    ausgabe=""
    for a in aList:
        ausgabe+=a
    print(ausgabe.rstrip())

