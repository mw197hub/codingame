import sys
import math
import copy


aussenList = ["."]
innenList = ["+","|","-"]
grenzList = []
grenzen = []
fuellList = []

def bildeKey(x,y):
    return (str(x)+"-"+str(y))
def loeseKey(key):
    tab = key.split("-")
    return int(tab[0]),int(tab[1])

def schritte(x,y):
    yield x -1,y
    yield x, y -1
    yield x +1,y
    yield x, y +1
    yield x+1,y+1
    yield x-1,y-1
    yield x+1,y-1
    yield x-1,y+1
    return x,y

def fuelle(x1,y1,fuell,grenzList):
    if bildeKey(x1,y1) in grenzList:
        return
    if bildeKey(x1,y1) in fuell:
        return
    fuell.add(bildeKey(x1,y1))
    for x2, y2 in schritte(x1,y1):
        fuelle(x2,y2,fuell,grenzList)
       

def fuellInhalt(grenzList):
    fuell = set()
    keyList = grenzList
    x1,y1 = loeseKey(keyList[0])
    x1 += 1
    y1 += 1

    fuelle(x1,y1,fuell,grenzList)        
    fuellList.append(fuell.copy())
    

def sucheGrenze(feld,feld2,tabList,x,y,wert):
    grenzList.append(bildeKey(x,y))
    for x,y in schritte(x,y):
        if bildeKey(x,y) in tabList:
            if feld[x][y] in innenList:
                tabList.remove(bildeKey(x,y))
                sucheGrenze(feld,feld2,tabList,x,y,feld[x][y])

def grenzenBilden(feld,feld2,tabList,x,y):    
    grenzList.clear()
    tabList.remove(bildeKey(x,y))
    if feld[x][y] in innenList:
        feld2[x][y] = "I"
        sucheGrenze(feld,feld2,tabList,x,y,feld[x][y])
        #print(grenzList)
        grenzen.append(grenzList[:])
    if feld[x][y] in aussenList:
        feld2[x][y] = "A"



feld = [['+', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '+'], ['|', ' ', ' ', ' ', ' ', 'o', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'o', ' ', '|'], ['+', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '+', ' ', ' ', '+', '+'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '+', '+', ' ', '+', '+', '.'], ['.', '.', '.', '.', 'o', '.', '.', '.', '.', '+', '+', ' ', '+', '+', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '+', '+', ' ', '+', '+', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '+', '+', ' ', '+', '+', '.', '.', '.', '.'], ['.', 'o', 'o', '.', '.', '.', '+', '+', 'o', '+', '+', '.', '.', '.', 'o', '.'], ['.', '.', '.', '.', '.', '+', '+', ' ', '+', '+', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '+', '+', ' ', '+', '+', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '+', '+', ' ', '+', '+', '.', '.', '.', '.', 'o', 'o', '.', '.'], ['.', '.', '+', '+', ' ', '+', '+', '.', '.', '.', '.', 'o', '.', '.', '.', '.'], ['.', '+', '+', ' ', '+', '+', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['+', '+', 'o', ' ', '+', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '+'], ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'o', ' ', ' ', ' ', ' ', ' ', ' ', '|'], ['+', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '+']]

feld2 = []
feld2 = copy.deepcopy(feld)
tabList = []

for x in range(16):
    for y in range(16):
        tabList.append(bildeKey(x,y))

erg = 0
for x in range(16):
    for y in range(16):
        if bildeKey(x,y) in tabList:
            grenzenBilden(feld,feld2,tabList,x,y)

for grenzList in grenzen:
    fuellInhalt(grenzList)
#fuellInhalt(grenzen.pop())

#print(fuellList)

for x in range(16):
    for y in range(16):
        if feld[x][y] == "o":
            anzahl = 0
            key = bildeKey(x,y)
            for fuell in fuellList:
                if key in fuell:
                    anzahl += 1
            if anzahl % 2:
                erg = erg + 1    
            
print(erg)


'''
feld.append(['+', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '+'])
feld.append(['|', ' ', ' ', ' ', 'o', ' ', ' ', ' ', ' ', ' ', ' ', 'o', 'o', ' ', ' ', '|'])
feld.append(['|', ' ', '+', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '+', 'o', '|'])
feld.append(['|', ' ', '|', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '|', ' ', '|'])
feld.append(['|', ' ', '|', '.', '+', '-', '-', '-', '-', '-', '-', '+', 'o', '|', 'o', '|'])
feld.append(['|', ' ', '|', '.', '|', ' ', ' ', ' ', ' ', ' ', ' ', '|', '.', '|', ' ', '|'])
feld.append(['|', ' ', '|', 'o', '|', ' ', '+', '-', '-', '+', 'o', '|', '.', '|', ' ', '|'])
feld.append(['|', ' ', '|', '.', '|', ' ', '|', 'o', 'o', '|', 'o', '|', '.', '|', ' ', '|'])
feld.append(['|', ' ', '|', '.', '|', ' ', '+', '-', '-', '+', ' ', '|', '.', '|', ' ', '|'])
feld.append(['|', ' ', '|', '.', '|', ' ', ' ', 'o', 'o', ' ', ' ', '|', '.', '|', ' ', '|'])
feld.append(['|', ' ', '|', '.', '|', 'o', 'o', 'o', 'o', 'o', 'o', '|', '.', '|', ' ', '|'])
feld.append(['|', ' ', '|', '.', '+', '-', '-', '-', '-', '-', '-', '+', 'o', '|', 'o', '|'])
feld.append(['|', 'o', '|', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '|', ' ', '|'])
feld.append(['|', 'o', '+', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '+', ' ', '|'])
feld.append(['|', ' ', ' ', ' ', ' ', ' ', ' ', 'o', ' ', ' ', ' ', 'o', ' ', ' ', ' ', '|'])
feld.append(['+', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '+'])
'''