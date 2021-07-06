import sys
import math

def pruefeR(king,posF,pos2):
    sortL = []
    if king[0] == posF[0] and pos2[0] == king[0]:
        sortL.append(king[1])
        sortL.append(posF[1])
        sortL.append(pos2[1])
        sortL.sort()
        if pos2[1] != sortL.pop(1):
            return True
    if king[1] == posF[1] and pos2[1] == king[1]:
        sortL.append(king[0])
        sortL.append(posF[0])
        sortL.append(pos2[0])
        sortL.sort()
        if pos2[0] != sortL.pop(1):
            return True
    return False

def pruefeB(king,posF,pos2):
    x = king[0] - posF[0]
    y = king[1] - posF[1]
    if abs(x) == abs(y):
        if x < 0:
            x = 1
        else:
            x = -1
        if y < 0:
            y = 1
        else:
            y = -1
        x1 = king[0]
        y1 = king[1]
        while True:
            x1 = x1 + x
            y1 = y1 + y
            if x1 < 0 or x1 > 7 or y1 < 0 or y1 > 7:
                break
            if x1 == pos2[0] and y1 == pos2[1]:
                return False
        return True             

    return False

def pruefeN(king,posF,pos2):
    x = king[0] - posF[0]
    y = king[1] - posF[1]
    if abs(x) == 2 and abs(y) == 1:
        return True
    if abs(x) == 1 and abs(y) == 2:
        return True
    return False

def pruefeQ(king,posF,pos2):
    treffer = pruefeR(king,posF,pos2)
    if treffer:
        return treffer
    treffer = pruefeB(king,posF,pos2)

    return treffer

def pruefe(king,f1,pos1,f2,pos2):
    if f1 == "R":
        treffer = pruefeR(king,pos1,pos2)
    if f1 == "N":
        treffer = pruefeN(king,pos1,pos2)
    if f1 == "B":
        treffer = pruefeB(king,pos1,pos2)
    if f1 == "Q":
        treffer = pruefeQ(king,pos1,pos2)
    return treffer

boardList = ['B _ _ _ _ _ _ _', '_ N _ _ _ _ _ _', '_ _ k _ _ _ _ _', '_ _ _ _ _ _ _ _', '_ _ _ _ _ _ _ _', '_ _ _ _ _ _ _ _', '_ _ _ _ _ _ _ _', '_ _ _ _ _ _ _ _']
boardList = ['_ _ _ _ _ _ _ Q', '_ _ _ _ Q _ _ _', '_ _ _ _ _ _ _ _', '_ _ _ _ _ _ _ _', '_ _ _ _ _ _ _ _', '_ _ k _ _ _ _ _', '_ _ _ _ _ _ _ _', '_ _ _ _ _ _ _ _']


#for i in range(8):
#    chess_row = input()

king = []
f1 = ""
f2 = ""
pos1 = []
pos2 = []
for x in range(8):
    zeile1 = boardList[x]
    zeile = zeile1.split(" ")
    for y in range(8):
        z = zeile[y]
        if z != "_" and z != " ":
            if z == "k":
                king.append(x)
                king.append(y)
            else:
                if len(f1) == 0:
                    f1 = z
                    pos1.append(x)
                    pos1.append(y)
                else:
                    f2 = z
                    pos2.append(x)
                    pos2.append(y)
        

print(king,file=sys.stderr)

treffer = False
treffer = pruefe(king,f1,pos1,f2,pos2)
if not treffer:
    treffer = pruefe(king,f2,pos2,f1,pos1)


if treffer:
    print("Check")
else:
    print("No Check")