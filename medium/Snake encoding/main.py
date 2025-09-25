# https://www.codingame.com/ide/puzzle/snake-encoding

import sys,math

x=1;lineList=['ABC', 'DEF', 'GHI']
x=5;lineList=['ABC', 'DEF', 'GHI']
#x=5;lineList=['I_LOVE_', 'TESTING', 'AMAZING', 'ENCODES', 'NOTYOU?', 'NUM83R5', 'NICE:)!']



for i in range(x):  
    abcDict=[]
    pos=[len(lineList)-1,0]
    abc="";up=True
    for i in range(len(lineList)**2):
        if len(abc) > 0:
            abcDict[lineList[pos[0]][pos[1]]] = abc
        abc=lineList[pos[0]][pos[1]]
        if up:
            xP=pos[0]-1
            if xP < 0:
                pos[0]=0
                pos[1]+=1;up=False
            else:
                pos[0]-=1
        else:
            xP=pos[0]+1
            if xP >= len(lineList):
                pos[0]=len(lineList)-1
                pos[1]+=1;up=True
            else:
                pos[0]+=1
    abcDict[lineList[len(lineList)-1][0]] = abc

for line in lineList:
    print(line)
