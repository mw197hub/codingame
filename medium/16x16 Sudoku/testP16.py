import sys,math,time

size = 16

def find_line_number(j):
    return set(grid[x][j] for x in range(size))

def find_column_number(i):
    return set(grid[i][y] for y in range(size))
    
def find_block_number(i,j):
    return set(grid[x][y] 
            for x in range((i//4)*4, (i//4)*4 + 4)
            for y in range((j//4)*4, (j//4)*4 + 4))

def remain_number(i,j):
    #numbers = {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16'}
    numbers = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}
    here = find_line_number(j) | find_column_number(i) | find_block_number(i,j)
    return sorted(list(numbers - here),reverse=True)
    
##############################    
#grid = [[s for s in input()] for _ in range(size)]
#1
rowList=[['.', 'L', 'E', 'K', '.', 'G', '.', '.', '.', '.', '.', 'N', 'O', '.', 'C', '.'], ['.', '.', 'M', '.', 'H', '.', 'J', 'O', 'B', 'D', 'G', '.', 'F', 'E', 'N', 'K'], ['J', '.', '.', 'C', '.', 'B', 'A', 'N', '.', 'E', 'K', '.', '.', '.', '.', 'I'], ['.', 'B', 'G', '.', '.', 'K', '.', '.', 'C', '.', 'J', '.', '.', 'D', 'P', 'M'], ['.', 'H', 'A', '.', 'F', 'L', '.', '.', 'K', '.', '.', 'M', '.', 'P', '.', '.'], ['.', '.', '.', 'O', 'A', '.', '.', '.', '.', '.', 'D', '.', 'I', 'K', '.', 'G'], ['.', '.', 'K', 'D', 'J', '.', 'C', 'B', 'F', 'A', 'I', 'G', '.', 'M', 'H', 'L'], ['.', 'M', '.', '.', '.', '.', '.', 'E', 'P', 'J', 'N', 'O', '.', 'A', '.', '.'], ['G', '.', '.', '.', 'I', 'A', '.', 'D', 'E', '.', 'C', 'J', 'P', '.', '.', '.'], ['A', 'K', '.', '.', '.', '.', 'G', 'H', 'N', 'M', '.', '.', 'L', 'I', 'J', '.'], ['.', '.', 'D', 'J', 'O', 'N', '.', '.', 'G', 'L', '.', 'B', 'K', 'H', '.', 'F'], ['.', 'N', '.', '.', '.', 'J', '.', 'K', '.', 'F', '.', '.', '.', 'G', 'A', 'B'], ['D', '.', '.', 'A', '.', '.', 'F', 'J', '.', '.', 'L', 'I', 'M', '.', 'K', '.'], ['E', '.', 'L', 'F', 'C', 'D', 'B', '.', 'O', '.', 'M', '.', 'N', '.', 'I', '.'], ['.', 'J', 'I', '.', '.', '.', '.', 'P', 'D', '.', '.', '.', '.', '.', 'L', '.'], ['.', '.', '.', '.', '.', 'H', '.', 'I', 'J', '.', '.', '.', '.', 'C', 'B', 'A']]
#3
#rowList=[['.', '.', '.', '.', '.', '.', '.', '.', 'B', '.', 'H', 'A', 'L', '.', '.', 'N'], ['.', '.', 'N', '.', '.', '.', '.', '.', 'D', '.', '.', '.', 'O', 'E', 'F', '.'], ['.', '.', 'K', '.', 'A', '.', '.', 'J', '.', '.', 'N', 'O', '.', 'B', '.', 'P'], ['.', '.', '.', 'C', 'L', '.', 'D', '.', '.', 'G', '.', 'E', '.', 'M', '.', 'J'], ['.', '.', '.', 'J', 'H', '.', '.', 'P', '.', '.', '.', '.', '.', '.', '.', 'E'], ['.', 'N', '.', 'K', '.', '.', '.', '.', '.', 'I', '.', '.', 'J', 'G', 'O', 'D'], ['.', 'O', 'M', '.', '.', 'I', 'E', 'C', 'N', 'B', '.', 'G', 'H', '.', '.', '.'], ['H', 'B', '.', '.', '.', 'D', '.', '.', 'P', '.', 'J', '.', 'N', 'F', 'C', 'I'], ['.', 'H', 'A', '.', 'M', 'E', '.', '.', '.', '.', '.', '.', 'K', 'N', '.', 'C'], ['D', '.', '.', 'E', 'N', 'B', '.', 'H', '.', 'P', 'O', 'L', '.', '.', '.', '.'], ['N', 'M', '.', 'B', '.', '.', 'O', '.', 'J', 'K', '.', '.', 'D', '.', '.', '.'], ['.', 'P', 'L', '.', '.', '.', '.', 'D', '.', '.', '.', '.', '.', 'A', '.', 'O'], ['.', 'E', '.', 'H', 'D', 'C', '.', '.', '.', '.', '.', 'F', 'P', 'K', '.', '.'], ['.', 'C', '.', '.', 'E', 'A', 'N', '.', 'O', 'L', '.', 'P', '.', 'I', '.', '.'], ['I', 'A', '.', 'N', 'G', '.', 'P', 'M', '.', '.', 'K', 'D', '.', '.', 'E', '.'], ['.', '.', 'O', '.', 'I', 'H', '.', '.', '.', '.', '.', 'N', 'A', 'C', '.', '.']]


##############################


abcList=['.','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
numList=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
abcDict={'.': 0, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16}
numDict={0: '.', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P'}
#for i in range(17):
#    abcDict[abcList[i]] = numList[i]
#    numDict[numList[i]] = abcList[i]
grid=[]
for row in rowList:
    line=[]
    for r in row:
        line.append(abcDict[r])
    grid.append(line[:])


empty_cells = sorted([(i,j) for i in range(size) for j in range(size) 
                                if grid[i][j] == 0],reverse=True)

sortDict={}
anzDict={}
for e in empty_cells:
    i,j=e[0],e[1]
    here = find_line_number(j) | find_column_number(i) | find_block_number(i,j)
    sortDict[str(i)+"#"+str(j)] = len(here)
    for h in here:
        if h in anzDict:
            hList=anzDict[h]
            hList.append(str(i)+"#"+str(j))
        else:            
            anzDict[h] = [str(i)+"#"+str(j)]

empty_cells.clear()
#for e in sorted(sortDict.items(), key=lambda item: item[1],reverse=False):
#    i,j=e[0].split("#")
#    empty_cells.append((int(i),int(j)))
for e in sorted(anzDict.items(), key=lambda item: len(item[1]),reverse=True):
    for e1 in e[1]:
        i,j=e1.split("#")
        if not (int(i),int(j)) in empty_cells:
            empty_cells.append((int(i),int(j)))

lifo = []
zeit = time.time()
while empty_cells != []:
    i,j = empty_cells.pop()
    r = remain_number(i,j)
    if r != []:
        grid[i][j] = r.pop()
        lifo.append((i,j,r))
    else:
        while r == []:
            empty_cells.append((i,j))
            grid[i][j] = 0
            i,j,r = lifo.pop()
        grid[i][j] = r.pop()
        lifo.append((i,j,r))
   
ergList=[]
for row in grid:
    line=[]
    for r in row:
        line.append(numDict[r])
    ergList.append(line[:])

for y in range(size):
    print("".join([str(ergList[y][x]) for x in range(size)]))


print("Zeit: {}".format(time.time()-zeit),file=sys.stderr)            
