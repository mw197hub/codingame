#  https://www.codingame.com/ide/puzzle/16x16-sudoku

import sys,math


size = 16
square_size = int(size**.5)
area = size**2

def pos(x, y):
    return y * size + x

def xy(pos):
    return (pos % size, pos//size)  



#1
rowList=[['.', 'L', 'E', 'K', '.', 'G', '.', '.', '.', '.', '.', 'N', 'O', '.', 'C', '.'], ['.', '.', 'M', '.', 'H', '.', 'J', 'O', 'B', 'D', 'G', '.', 'F', 'E', 'N', 'K'], ['J', '.', '.', 'C', '.', 'B', 'A', 'N', '.', 'E', 'K', '.', '.', '.', '.', 'I'], ['.', 'B', 'G', '.', '.', 'K', '.', '.', 'C', '.', 'J', '.', '.', 'D', 'P', 'M'], ['.', 'H', 'A', '.', 'F', 'L', '.', '.', 'K', '.', '.', 'M', '.', 'P', '.', '.'], ['.', '.', '.', 'O', 'A', '.', '.', '.', '.', '.', 'D', '.', 'I', 'K', '.', 'G'], ['.', '.', 'K', 'D', 'J', '.', 'C', 'B', 'F', 'A', 'I', 'G', '.', 'M', 'H', 'L'], ['.', 'M', '.', '.', '.', '.', '.', 'E', 'P', 'J', 'N', 'O', '.', 'A', '.', '.'], ['G', '.', '.', '.', 'I', 'A', '.', 'D', 'E', '.', 'C', 'J', 'P', '.', '.', '.'], ['A', 'K', '.', '.', '.', '.', 'G', 'H', 'N', 'M', '.', '.', 'L', 'I', 'J', '.'], ['.', '.', 'D', 'J', 'O', 'N', '.', '.', 'G', 'L', '.', 'B', 'K', 'H', '.', 'F'], ['.', 'N', '.', '.', '.', 'J', '.', 'K', '.', 'F', '.', '.', '.', 'G', 'A', 'B'], ['D', '.', '.', 'A', '.', '.', 'F', 'J', '.', '.', 'L', 'I', 'M', '.', 'K', '.'], ['E', '.', 'L', 'F', 'C', 'D', 'B', '.', 'O', '.', 'M', '.', 'N', '.', 'I', '.'], ['.', 'J', 'I', '.', '.', '.', '.', 'P', 'D', '.', '.', '.', '.', '.', 'L', '.'], ['.', '.', '.', '.', '.', 'H', '.', 'I', 'J', '.', '.', '.', '.', 'C', 'B', 'A']]

#6
#rowList=[['.', 'C', '.', '.', '.', '.', '.', '.', 'E', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', 'J', '.', '.', 'A', '.', 'B', 'F', 'P', '.', '.', '.', 'K', 'L', 'D'], ['.', '.', 'I', '.', 'D', '.', 'N', 'J', '.', 'A', '.', '.', 'E', 'B', '.', 'G'], ['L', '.', '.', 'A', '.', '.', '.', '.', 'J', '.', '.', 'N', '.', '.', '.', 'O'], ['D', 'H', '.', 'M', 'B', 'J', 'C', 'P', '.', '.', 'F', '.', '.', 'I', 'K', 'A'], ['.', '.', '.', 'L', '.', 'N', 'M', '.', '.', 'O', 'D', '.', '.', '.', '.', 'C'], ['.', '.', 'N', '.', 'I', '.', '.', '.', '.', '.', '.', '.', '.', 'G', '.', '.'], ['B', '.', '.', 'F', '.', '.', 'O', 'G', 'I', 'C', 'P', '.', '.', 'L', 'D', 'M'], ['.', 'G', '.', 'E', '.', '.', '.', 'D', '.', '.', '.', 'I', 'M', '.', 'O', 'K'], ['.', 'A', '.', '.', 'G', '.', 'P', '.', '.', '.', '.', 'F', 'L', 'H', 'C', 'N'], ['.', 'F', '.', '.', '.', '.', 'H', 'O', 'M', '.', 'B', '.', 'G', '.', 'E', '.'], ['M', 'O', 'P', '.', '.', '.', '.', '.', '.', 'G', '.', '.', '.', '.', 'A', '.'], ['.', '.', 'M', 'I', '.', 'B', '.', 'F', '.', 'H', 'O', 'E', 'K', '.', 'G', '.'], ['.', 'B', '.', 'D', 'C', '.', 'E', '.', 'N', '.', 'L', '.', '.', 'F', 'M', '.'], ['G', '.', '.', '.', '.', '.', '.', 'N', 'C', '.', '.', 'P', '.', 'A', '.', 'E'], ['.', 'E', 'F', 'H', '.', '.', '.', 'I', '.', '.', 'G', '.', '.', '.', 'N', '.']]


abcList=['.','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
numList=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

abcDict={}
numDict={}
for i in range(17):
    abcDict[abcList[i]] = numList[i]
    numDict[numList[i]] = abcList[i]

positions = [set() for x in range(area)]
board=[]
for row in rowList:
    for r in row:
        board.append(abcDict[r])

for i in range(area):
    x, y = xy(i)
    for v in range(size):
        positions[i].add(pos(x, v))
        positions[i].add(pos(v, y))
    top_left = pos(square_size * (x//square_size),
                   square_size * (y//square_size))
    for p in [top_left + pos(dx, dy) for dx in range(square_size) for dy in range(square_size)]:
        positions[i].add(p)

###
def get_pos(board, pp):
    seen = {board[i] for i in pp}
    return [x for x in range(1, size+1) if x not in seen]

def solve(board, unknown):
    if len(unknown) == 0:
        return True
    p = unknown[0]
    for m in get_pos(board, positions[p]):
        board[p] = m
        if (solve(board, unknown[1:])):
            return True
    board[p] = 0
    return False




solve(board, [p for p, x in enumerate(board) if x == 0])


ergList=[]
for r in board:
    ergList.append(numDict[r])

for y in range(size):
    print("".join([str(ergList[pos(x, y)]) for x in range(size)]))