# https://www.codingame.com/ide/puzzle/chocolate-bar-cut

import sys,math

def count_cut_pieces(x, y):
    # Die Formel für die Anzahl der geschnittenen Quadrate
    return x + y - math.gcd(x, y)


nList=[[1, 3], [3, 1], [2, 2], [2, 5], [2, 4], [3, 4]]


for x,y in nList:
    print(count_cut_pieces(x,y))
        