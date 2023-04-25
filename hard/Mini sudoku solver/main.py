#  https://www.codingame.com/ide/puzzle/mini-sudoku-solver

import sys,math

lineList=[['2', '0', '4', '3'], ['0', '0', '2', '0'], ['4', '3', '0', '0'], ['0', '0', '3', '4']]

grid=[]
grid=[[ 0 for y in range(4)] for x in range(4)]
for y in range(4):
    for x in range(4):
        grid[y][x] = int(lineList[y][x])

def check(x,y,n):
    global grid
    for i in range(4):
        if grid[i][y]==n:return False
        if grid[x][i]==n:return False
    a=(x//2)*2
    b=(y//2)*2
    for i in range(2):
        for j in range(2):
            if grid[a+i][b+j]==n:return False
    return True

def zero():
    global grid
    for i in range(4):
        for j in range(4):
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
    for i in range(1,5):
        if check(x,y,i):
            grid[x][y]=i
            if solve():
                return True
            grid[x][y]=0
    return False
solve()
for i in grid:
    print(''.join(map(str,i)))