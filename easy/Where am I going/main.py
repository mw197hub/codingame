# https://www.codingame.com/ide/puzzle/where-am-i-going

import sys,math

rowList=['###', '..#', '.##']


wegList=[]
for y in range(len(rowList)):
    row = rowList[y]
    wList=[]
    for x in range(len(row)):
        wList.append(row[x])
    wegList.append(wList[:])
print(wegList,file=sys.stderr)

pos=[0,0]
moveDict={0:[[0,1],[1,0],[-1,0]],1:[[1,0],[0,-1],[0,1]],2:[[0,-1],[-1,0],[1,0]],3:[[-1,0],[0,1],[0,-1]]}
richtung = 0

ergebnis=""
bisher=[]
anzahl=1
while True:
    treffer=False
    for i in range(3):
        move = moveDict[richtung][i]
        if pos[0]+move[0] >= 0 and pos[0]+move[0] < len(wegList) and pos[1]+move[1] >= 0 and pos[1]+move[1] < len(wegList[0]):
            if wegList[pos[0]+move[0]][pos[1]+move[1]] == "#":
                treffer = True
                if i == 0:
                    anzahl+=1
                else:
                    ergebnis+=str(anzahl)
                    if i == 1:
                        ergebnis+="R"
                        richtung+=1
                        if richtung > 3:
                            richtung =0
                    else:
                        ergebnis+="L"
                        richtung-=1
                        if richtung < 0:
                            richtung=3                
                    anzahl=1
                pos[0]+=move[0]
                pos[1]+=move[1]
                break
    if not treffer:
        ergebnis+=str(anzahl)
        break

print(ergebnis)
