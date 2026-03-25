# https://www.codingame.com/ide/puzzle/chocolate-bar-cut

import sys,math


nList=[[1, 3], [3, 1], [2, 2], [2, 5], [2, 4], [3, 4]]


for x,y in nList:
    if x == y:
        print(x)
    else:
        diff = abs(x-y)
        