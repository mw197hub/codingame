# https://www.codingame.com/ide/puzzle/the-l-game-counting-board-states

import sys,math
import numpy as np


height=3;width=3;n=1
height=6;width=6;n=6

#

lblock = np.array([[1,0,0],[1,1,1]], dtype = np.int32)
lblocks = []
for i in range(2):
    for j in range(4):
        lblocks.append(lblock)
        lblock = np.rot90(lblock)
    lblock = lblock[::-1]

# Count the number of L-block configs by brute force.

cnt = 0
board = np.zeros([height,width], dtype = np.int32)
for a in lblocks:
    sza = a.shape
    for y in range(height - sza[0] + 1):
        for x in range(width - sza[1] + 1):
            board[y:y+sza[0], x:x+sza[1]] = a
            for b in lblocks:
                szb = b.shape
                for y2 in range(height - szb[0] +1):
                    for x2 in range(width - szb[1] + 1):
                        tmp = board[y2:y2+szb[0], x2:x2+szb[1]]
                        if np.sum(tmp * b) == 0: cnt += 1
            board[y:y+sza[0],x:x+sza[1]] = 0

# For each L-block config, find the number of stopper configs.
# This is the combination of (h*w-8) taken n at a time.

if n > (height*width - 8):
    cnts = 0
else:
    cnts = 1
    for i in range(height*width - 7 - n, height*width - 7):
        cnts *= i
    for i in range(1, n+1): 
        cnts = cnts // i

print(cnt * cnts)