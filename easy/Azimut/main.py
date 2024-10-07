# https://www.codingame.com/ide/puzzle/azimut

import sys,math


start_direction='N';turnList=['RIGHT']   #1
start_direction='N';turnList=['LEFT', 'FORWARD', 'FORWARD', 'RIGHT', 'FORWARD', 'RIGHT']  # 4


comList=['N','NE','E','SE','S','SW','W','NW']
pos=-1

for i in range(8):
    if start_direction == comList[i]:
        pos = i
        break
#print(comList[pos],file=sys.stderr)
moveDict={'RIGHT':1,'LEFT':-1,'BACK':4,'FORWARD':0}

for turn in turnList:
    move = moveDict[turn]
    pos = pos + move
    if pos < 0:
        pos = pos + 8
    if pos > 7:
        pos = pos - 8
print(comList[pos])