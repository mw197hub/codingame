size = 9

def find_line_number(j):
    return set(grid[x][j] for x in range(size))

def find_column_number(i):
    return set(grid[i][y] for y in range(size))
    
def find_block_number(i,j):
    return set(grid[x][y] 
            for x in range((i//3)*3, (i//3)*3 + 3)
            for y in range((j//3)*3, (j//3)*3 + 3))

def remain_number(i,j):
    numbers = {'1','2','3','4','5','6','7','8','9'}
    here = find_line_number(j) | find_column_number(i) | find_block_number(i,j)
    return sorted(list(numbers - here),reverse=True)
    
    
#grid = [[s for s in input()] for _ in range(size)]
grid=[['1', '2', '0', '0', '7', '0', '5', '6', '0'], ['5', '0', '7', '9', '3', '2', '0', '8', '0'], ['0', '0', '0', '0', '0', '1', '0', '0', '0'], ['0', '1', '0', '2', '4', '0', '0', '5', '0'], ['3', '0', '8', '0', '0', '0', '4', '0', '2'], ['0', '7', '0', '0', '8', '5', '0', '1', '0'], ['0', '0', '0', '7', '0', '0', '0', '0', '0'], ['0', '8', '0', '4', '2', '3', '7', '0', '1'], ['0', '3', '4', '0', '1', '0', '0', '2', '8']]

empty_cells = sorted([(i,j) for i in range(size) for j in range(size) 
                                if grid[i][j] == "0"],reverse=True)


lifo = []

while empty_cells != []:
    i,j = empty_cells.pop()
    r = remain_number(i,j)
    if r != []:
        grid[i][j] = r.pop()
        lifo.append((i,j,r))
    else:
        while r == []:
            empty_cells.append((i,j))
            grid[i][j] = "0"
            i,j,r = lifo.pop()
        grid[i][j] = r.pop()
        lifo.append((i,j,r))
   
 
print(*[''.join(grid[i]) for i in range(size)],sep='\n')
            
