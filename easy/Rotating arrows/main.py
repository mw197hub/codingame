import sys
import math
import copy

mList = [['^', 'v']]
w,h=2,1
x,y=0,0

mList = [['>', 'v', '>'], ['>', '<', 'v'], ['^', '^', '<']]
w,h=3,3
x,y=2,1

mList = [['<', '>', '<', '>', '<'], ['<', '>', '<', '>', '<'], ['<', '>', '<', '>', '<'], ['<', '>', '<', '>', '<'], ['<', '>', '<', '>', '<']]
w,h=5,5
x,y=2,2

mList = [['<', '>', '<', '>', '<', '>'], ['<', '>', '^', '>', '>', '>'], ['^', '^', '<', '^', '<', '>'], ['<', '>', '<', '>', '<', '>'], ['<', 'v', 'v', 'v', 'v', 'v']]
#mList = [['<', '>', '<', '>', '<', '>'], ['<', '>', '^', '>', '^', '>'], ['^', '^', '<', '^', '<', '>'], ['<', '>', '<', '>', '<', '>'], ['<', 'v', 'v', 'v', 'v', 'v']]
w,h=6,5
x,y=2,2

rotationList = {'>':'v','v':'<','<':'^','^':'>'}
moveList = {'>':[0,1],'v':[1,0],'<':[0,-1],'^':[-1,0]}
pList=[];erg=0

for m in mList:
    print(m,file=sys.stderr)
xStart = x;yStart=y
while True:
    if y < 0 or x < 0 or x >= w or y >= h:
        break
    pList.append([y,x])    
    rotation = rotationList[mList[y][x]]
    mList[y][x] = rotation
    move = moveList[mList[y][x]]
    x+=move[1];y+=move[0]
    erg+=1
    #print(mList,file=sys.stderr)
    if xStart == x and yStart == y:
        break
print(pList,file=sys.stderr)
print(erg)