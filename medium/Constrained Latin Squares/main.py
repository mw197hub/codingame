# https://www.codingame.com/ide/puzzle/constrained-latin-squares

import sys,math,time
import itertools

def find_line_number(j,size,grid):
    return set(grid[x][j] for x in range(size))

def find_column_number(i,size,grid):
    return set(grid[i][y] for y in range(size))

def prufe(ergList,laenge,rowList,positions):
    summe=0
    for i in range(1,laenge+1):
        summe+=i

    for y in range(laenge):
        for x in range(laenge):
            if rowList[y][x] > 0:
                if not rowList[y][x] == ergList[y][x]:
                    return 0
    
   # print(ergList,file=sys.stderr)
    a=0

    for y in range(laenge):
        line = find_line_number(y,laenge,ergList)
        if not len(line) == laenge:
            return 0
        column = find_column_number(y,laenge,ergList)
        if not len(column) == laenge:
            return 0
    return 1

def addRow(stufe,wertList,anzahl,laenge,ergList,rowList,positions):
    stufe+=1
    for w in wertList:
        ergList[stufe -1] = w        
        if stufe == laenge:
            erg = prufe(ergList,laenge,rowList,positions)
            anzahl+=erg        
        else:
            anzahl = addRow(stufe,wertList,anzahl,laenge,ergList,rowList,positions)
    stufe-=1
    return anzahl


rowList=[[1, 2, 3], [2, 0, 0], [3, 0, 0]]   # 1
rowList=[[1, 2, 3], [0, 0, 0], [0, 0, 0]]   # 1 Test
#rowList=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] # 2
#rowList=[[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]] # 3

#rowList=[[1, 2, 3, 4, 5, 6, 0, 0], [2, 3, 4, 5, 6, 0, 0, 0], [3, 4, 5, 6, 0, 0, 0, 0], [4, 5, 6, 0, 0, 0, 0, 0], [5, 6, 0, 0, 0, 0, 0, 0], [6, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 8]] # 7

#rowList=[[0, 8, 7, 6, 0, 4, 3, 2, 1], [8, 0, 0, 0, 0, 0, 0, 0, 2], [7, 0, 0, 0, 0, 0, 0, 0, 3], [6, 0, 0, 5, 2, 3, 0, 0, 0], [0, 0, 0, 3, 0, 2, 0, 0, 5], [4, 0, 1, 2, 3, 0, 0, 0, 6], [3, 0, 0, 0, 0, 0, 0, 0, 7], [2, 0, 0, 0, 0, 0, 0, 0, 8], [1, 0, 3, 0, 5, 0, 7, 8, 0]] # 9

zeit = time.time()
erg=0

stufe,anzahl=0,0
wertList=[]
anz=0
werte = (itertools.permutations(range(1,len(rowList)+1),len(rowList)))
for w in werte:
    wertList.append(w)
    anz+=1

positions = list((x) for x in range(1,len(rowList)+1))
ergList= list([] for x in range(len(rowList)))
anzahl = addRow(0,wertList,anzahl,len(rowList),ergList,rowList,positions)

print(anzahl)
print("Zeit: {}".format(time.time()-zeit),file=sys.stderr)    