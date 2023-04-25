# https://www.codingame.com/ide/puzzle/game-of-life

import sys,math

width,height=3,3
lineList=[['0', '0', '0'], ['1', '1', '1'], ['0', '0', '0']]


outList=lineList[:]
for y in range(height):
    for x in range(width):
        moveList=[[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
        anzahl=0
        for move in moveList:
            yN=y+move[0];xN=x+move[1]
            if yN >= 0 and yN < height and xN >= 0 and xN < width:
                if lineList[yN][xN] == '1':
                    anzahl+=1
        if lineList[y][x] == '1':
            if anzahl < 2 or anzahl > 3:
                print('0',end="")
            else:
                print('1',end="")
        else:
            if anzahl == 3:
                print("1",end="")
            else:
                print('0',end="")
        #print(lineList[y][x],end="")
    print("")
