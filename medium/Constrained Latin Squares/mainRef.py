import sys,math,time
import copy

def ausgabe(rowList):
    for row in rowList:
        print(row,file=sys.stderr)
    print("--------------------",file=sys.stderr)



def find_line_number(j,rowList):
 #   print(set(rowList[j][x] for x in range(len(rowList))))
    return set(rowList[j][x] for x in range(len(rowList)))

def find_column_number(i,rowList):
  #  print(set(rowList[y][i] for y in range(len(rowList))))
    return set(rowList[y][i] for y in range(len(rowList)))
    

def remain_number(i,j,rowList,numbers):
    here = find_line_number(j,rowList) | find_column_number(i,rowList) 
    return sorted(list(numbers - here),reverse=True)

def fuelleCell(pos,rowList,numbers,empty_cells,anzahl):
    i,j = empty_cells[pos]
    rW = remain_number(i,j,rowList,numbers)
    for r in rW:
        rowList[i][j] = r
        if pos == len(empty_cells) -1:
            anzahl+=1
        else:            
            anzahl = fuelleCell(pos+1,rowList,numbers,empty_cells,anzahl)
    rowList[i][j] = 0
    pos-=1
    return anzahl


rowList=[[1, 2, 3], [2, 0, 0], [3, 0, 0]]   # 1
rowList=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]   # 1 Test
rowList=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] # 2
rowList=[[1, 2, 3, 4], [4, 3, 2, 1], [0, 0, 0, 0], [0, 0, 0, 0]] # 2
rowList=[[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]] # 3
rowList=[[1, 2, 3, 4, 5], [5, 4, 2, 3, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]] # 3
rowList=[[2, 0, 0, 0, 0, 0, 7], [0, 4, 0, 3, 0, 0, 0], [0, 0, 3, 0, 0, 0, 0], [0, 0, 0, 6, 0, 0, 4], [1, 5, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2, 0], [0, 1, 0, 0, 0, 7, 0]] # 6  - 14388


#rowList=[[1, 2, 3, 4, 5, 6, 0, 0], [2, 3, 4, 5, 6, 0, 0, 0], [3, 4, 5, 6, 0, 0, 0, 0], [4, 5, 6, 0, 0, 0, 0, 0], [5, 6, 0, 0, 0, 0, 0, 0], [6, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 8]] # 7
#rowList=[[0, 8, 7, 6, 0, 4, 3, 2, 1], [8, 0, 0, 0, 0, 0, 0, 0, 2], [7, 0, 0, 0, 0, 0, 0, 0, 3], [6, 0, 0, 5, 2, 3, 0, 0, 0], [0, 0, 0, 3, 0, 2, 0, 0, 5], [4, 0, 1, 2, 3, 0, 0, 0, 6], [3, 0, 0, 0, 0, 0, 0, 0, 7], [2, 0, 0, 0, 0, 0, 0, 0, 8], [1, 0, 3, 0, 5, 0, 7, 8, 0]] # 9

zeit = time.time()
empty_cells = sorted([(i,j) for i in range(len(rowList)) for j in range(len(rowList)) 
                                if rowList[i][j] == 0],reverse=True)
#print(empty_cells,file=sys.stderr)


numbers = set(x for x in range(1,len(rowList)+1))
anzahl=0
#anzahl = fuelleCell(0,rowList,numbers,empty_cells,anzahl)
bisherList=[]
bisherList.append(rowList[:])
for i1 in range(len(empty_cells)):
    j,i=empty_cells[i1]
    tList=[]
    for bisher in bisherList:
        here = find_line_number(j,bisher) | find_column_number(i,bisher)
        rList = (numbers - here)
        for r in rList:
            bisher[j][i] = r
            tList.append(copy.deepcopy(bisher))
    bisherList = tList[:]

    #print(bisherList,file=sys.stderr)

print(len(bisherList))
 
#print(anzahl)

print("Zeit: {}".format(time.time()-zeit),file=sys.stderr)    

