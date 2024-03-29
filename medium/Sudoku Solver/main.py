#  https://www.codingame.com/ide/puzzle/sudoku-solver

import sys,math

def test_cell(s, row, col):
    """
    Given a Sudoku puzzle s, row, and column number, return a list which represents
    the valid numbers that can go in that cell. 0 = possible, 1 = not possible
    """
    used = [0]*10
    used[0] = 1
    block_row = row // 3
    block_col = col // 3

    # Row and Column
    for m in range(9):
        used[s[m][col]] = 1
        used[s[row][m]] = 1

    # Square
    for m in range(3):
        for n in range(3):
            used[s[m + block_row*3][n + block_col*3]] = 1

    return used

def initial_try(s):
    """
    Given a Sudoku puzzle, try to solve the puzzle by iterating through each
    cell and determining the possible numbers in that cell. If only one possible
    number exists, fill it in and continue on until the puzzle is stuck.
    """
    stuck = False

    while not stuck:
        stuck = True
        # Iterate through the Sudoku puzzle
        for row in range(9):
            for col in range(9):
                used = test_cell(s, row, col)
                # More than one possibility
                if used.count(0) != 1:
                    continue

                for m in range(1, 10):
                    # If current cell is empty and there is only one possibility
                    # then fill in the current cell
                    if s[row][col] == 0 and used[m] == 0:
                        s[row][col] = m
                        stuck = False
                        break

def DFS_solve(s, row, col):
    """
    Given a Sudoku puzzle, solve the puzzle by recursively performing DFS
    which tries out the possible solutions and by using backtracking (eliminating
    invalid tries and all the possible cases arising from those tries)
    """
    if row == 8 and col == 8:
        used = test_cell(s, row, col)
        if 0 in used:
            s[row][col] = used.index(0)
        return True

    if col == 9:
        row = row+1
        col = 0

    if s[row][col] == 0:
        used = test_cell(s, row, col)
        for i in range(1, 10):
            if used[i] == 0:
                s[row][col] = i
                if DFS_solve(s, row, col+1):
                    return True

        # Reached here? Then we tried 1-9 without success
        s[row][col] = 0
        return False

    return DFS_solve(s, row, col+1)         

lineList=[['1', '2', '0', '0', '7', '0', '5', '6', '0'], ['5', '0', '7', '9', '3', '2', '0', '8', '0'], ['0', '0', '0', '0', '0', '1', '0', '0', '0'], ['0', '1', '0', '2', '4', '0', '0', '5', '0'], ['3', '0', '8', '0', '0', '0', '4', '0', '2'], ['0', '7', '0', '0', '8', '5', '0', '1', '0'], ['0', '0', '0', '7', '0', '0', '0', '0', '0'], ['0', '8', '0', '4', '2', '3', '7', '0', '1'], ['0', '3', '4', '0', '1', '0', '0', '2', '8']]
lineList=[['0', '0', '0', '7', '0', '0', '0', '4', '0'], ['0', '2', '0', '8', '0', '1', '9', '0', '0'], ['0', '0', '0', '0', '0', '0', '1', '7', '3'], ['1', '0', '2', '0', '0', '6', '0', '9', '7'], ['6', '0', '0', '0', '9', '0', '0', '0', '1'], ['9', '7', '0', '1', '0', '0', '4', '0', '5'], ['3', '5', '4', '0', '0', '0', '0', '0', '0'], ['0', '0', '8', '6', '0', '4', '0', '3', '0'], ['0', '1', '0', '0', '0', '3', '0', '0', '0']]
lineList=[['0', '0', '6', '0', '0', '0', '0', '5', '0'], ['0', '0', '3', '7', '0', '0', '0', '0', '0'], ['7', '0', '0', '0', '3', '5', '0', '0', '8'], ['0', '0', '0', '0', '7', '0', '0', '1', '2'], ['0', '0', '0', '9', '4', '2', '0', '0', '0'], ['6', '2', '0', '0', '8', '0', '0', '0', '0'], ['9', '0', '0', '1', '2', '0', '0', '0', '3'], ['0', '0', '0', '0', '0', '3', '6', '0', '0'], ['0', '5', '0', '0', '0', '0', '7', '0', '0']]
lineList=[['8', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '3', '6', '0', '0', '0', '0', '0'], ['0', '7', '0', '0', '9', '0', '2', '0', '0'], ['0', '5', '0', '0', '0', '7', '0', '0', '0'], ['0', '0', '0', '0', '4', '5', '7', '0', '0'], ['0', '0', '0', '1', '0', '0', '0', '3', '0'], ['0', '0', '1', '0', '0', '0', '0', '6', '8'], ['0', '0', '8', '5', '0', '0', '0', '1', '0'], ['0', '9', '0', '0', '0', '0', '4', '0', '0']]



outList=[[ 0 for y in range(9)] for x in range(9)]
for y in range(9):
    for x in range(9):
        outList[y][x] = int(lineList[y][x])

initial_try(outList)
for line in outList:
    if 0 in line:
        DFS_solve(outList, 0, 0)
        break

for y in range(9):
    for x in range(9):
        print(outList[y][x],end="")
    print("")

