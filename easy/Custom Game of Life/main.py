import sys
import math
import copy

def wertEr(y,x,gridList,h,w):
    if y < 0 or x < 0 or y >= h or x >= w:
        return 0
    if gridList[y][x] == 'O':
        return 1
    return 0

def zaehle(y,x,gridList,h,w):
    anzahl = 0
    anzahl += wertEr(y-1,x,gridList,h,w)
    anzahl += wertEr(y-1,x-1,gridList,h,w)
    anzahl += wertEr(y-1,x+1,gridList,h,w)
    anzahl += wertEr(y,x-1,gridList,h,w)
    anzahl += wertEr(y,x+1,gridList,h,w)
    anzahl += wertEr(y+1,x,gridList,h,w)
    anzahl += wertEr(y+1,x-1,gridList,h,w)
    anzahl += wertEr(y+1,x+1,gridList,h,w)
    return anzahl

#h, w, n = 3, 4, 1
#alive = "001100000"
#dead = "000100000"
#gridList = [['.', 'O', 'O', '.'], ['O', '.', '.', 'O'], ['.', 'O', 'O', '.']]

h, w, n = 5, 5, 1
alive = "001100000"
dead = "000100000"
gridList = [['.', '.', '.', '.', '.'], 
            ['.', 'O', 'O', 'O', '.'], 
            ['.', 'O', 'O', 'O', '.'], 
            ['.', 'O', 'O', 'O', '.'], 
            ['.', '.', '.', '.', '.']]


newList = copy.deepcopy(gridList)
for i in range(n):
    for y in range(h):
        for x in range(w):
            anzahlNachbarn = zaehle(y,x,gridList,h,w)
            print(str(y)+ " - " + str(x)+"  = " + str(anzahlNachbarn),file=sys.stderr)
            if gridList[y][x] == 'O':
                if alive[anzahlNachbarn] == '1':
                    newList[y][x] = 'O'
                else:
                    newList[y][x] = '.'
            else:
                if dead[anzahlNachbarn] == "1":
                    newList[y][x] = 'O'
                else:
                    newList[y][x] = '.'
    gridList = copy.deepcopy(newList)

for newL in gridList:
    zeile = ""
    for b in newL:
        zeile = zeile + b
    print(zeile)