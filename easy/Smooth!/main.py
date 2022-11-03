#  https://www.codingame.com/ide/puzzle/smooth

import sys,math

fList=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

restList=[2,3,5]

for f in fList:
    while True:
        if f == 1:
            print("VICTORY")
            break
        else:
            treffer = False
            for r in restList:
                if f % r == 0:
                    f = f / r
                    treffer = True
                    break
            if not treffer:
                print("DEFEAT")
                break