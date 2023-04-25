import sys,math


outList=[['8', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '3', '6', '0', '0', '0', '0', '0'], ['0', '7', '0', '0', '9', '0', '2', '0', '0'], ['0', '5', '0', '0', '0', '7', '0', '0', '0'], ['0', '0', '0', '0', '4', '5', '7', '0', '0'], ['0', '0', '0', '1', '0', '0', '0', '3', '0'], ['0', '0', '1', '0', '0', '0', '0', '6', '8'], ['0', '0', '8', '5', '0', '0', '0', '1', '0'], ['0', '9', '0', '0', '0', '0', '4', '0', '0']]
#outList=[['1', '2', '0', '0', '7', '0', '5', '6', '0'], ['5', '0', '7', '9', '3', '2', '0', '8', '0'], ['0', '0', '0', '0', '0', '1', '0', '0', '0'], ['0', '1', '0', '2', '4', '0', '0', '5', '0'], ['3', '0', '8', '0', '0', '0', '4', '0', '2'], ['0', '7', '0', '0', '8', '5', '0', '1', '0'], ['0', '0', '0', '7', '0', '0', '0', '0', '0'], ['0', '8', '0', '4', '2', '3', '7', '0', '1'], ['0', '3', '4', '0', '1', '0', '0', '2', '8']]



grid=[[ 0 for y in range(9)] for x in range(9)]
for y in range(9):
    for x in range(9):
        grid[y][x] = int(outList[y][x])

def check(x,y,n):
    global grid
    for i in range(9):
        if grid[i][y]==n:return False
        if grid[x][i]==n:return False
    a=(x//3)*3
    b=(y//3)*3
    for i in range(3):
        for j in range(3):
            if grid[a+i][b+j]==n:return False
    return True

def zero():
    global grid
    for i in range(9):
        for j in range(9):
            if grid[i][j]==0:
                return j,i
    return None

def solve():
    global grid
    z = zero()
    #print("solve")
    if z == None:
        return True
    y,x=z
    for i in range(1,10):
        if check(x,y,i):
            grid[x][y]=i
            if solve():
                return True
            grid[x][y]=0
    return False
solve()
for i in grid:
    print(''.join(map(str,i)))