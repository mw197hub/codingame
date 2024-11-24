# https://www.codingame.com/ide/puzzle/what-the-brainfuck

import sys,math,string

def sucheKList(posR,klammerList,wert):
    for kList in klammerList:
        if kList[wert] == posR:
            return kList
    return False






#1
rList='+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+.+.';cList=[];s=1
#2
rList='++++++++++[>+++++++>++++++++++>+++<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.';cList=[];s=4
#3
rList=',>,><[<[>>+>+<<<-]>>>[<<<+>>>-]<<-]>.';cList=[4, 9];s=4

#validTest
rList='+]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+.+.';cList=[];s=1
####

erg=''
cellList=[]
posCell=0;posCList=0
klammerList=[]
for i in range(s):
    cellList.append(0)
pos=-1
for i in range(len(rList)):
    if rList[i] == "[":
        pos+=1
        klammerList.append([i,-1])
    elif rList[i] == "]":
        gefunden=False
        for k in range(len(klammerList)-1,-1,-1):
            kList = klammerList[k]
            if kList[1] == -1:
                kList[1] = i
                gefunden=True
                break
        if not gefunden:
            erg = 'SYNTAX ERROR'
            rList = '+'
            break

print(klammerList,file=sys.stderr)
for kList in klammerList:
    if kList[1] == -1:
        erg = 'SYNTAX ERROR'
        rList = '+'
        break


posR=0;posK=-1
while True:
    wert = rList[posR]
    if wert == '+':
        cellList[posCell]+=1
        if cellList[posCell] > 255:
            erg='INCORRECT VALUE'
            break
    elif wert == '-':
        cellList[posCell]-=1
        if cellList[posCell] < 0:
            erg='INCORRECT VALUE'
            break
    elif wert == '>':
        posCell+=1
        if posCell >= s:
            erg='POINTER OUT OF BOUNDS'
            break
    elif wert == '<':
        posCell-=1
        if posCell < 0:
            erg='POINTER OUT OF BOUNDS'
            break
    elif wert == ',':
        cellList[posCell] = cList[posCList]
        posCList+=1
    elif wert == '.':
        erg += chr(cellList[posCell])
    elif wert == '[':
        kList = sucheKList(posR,klammerList,0)
        if cellList[posCell] == 0:
            posR = kList[1]
    elif wert == ']':
        kList = sucheKList(posR,klammerList,1)
        if cellList[posCell] != 0:
            posR = kList[0]
    posR+=1
    if posR == len(rList):
        break

print(cellList,file=sys.stderr)
print(erg)