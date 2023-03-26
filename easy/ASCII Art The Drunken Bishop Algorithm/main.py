# https://www.codingame.com/ide/puzzle/ascii-art-the-drunken-bishop-algorithm
import sys,math

hexaDict={'0':['00','00'],'1':['01','00'],'2':['10','00'],'3':['11','00'],'4':['00','01'],'5':['01','01'],'6':['10','01'],'7':['11','01'],'8':['00','10'],'9':['01','10'],'a':['10','10'],'b':['11','10'],'c':['00','11'],'d':['01','11'],'e':['10','11'],'f':['11','11']}
moveDict={'00':[-1,-1],'01':[-1,1],'10':[1,-1],'11':[1,1]}
moveList=[[0 for x in range(17)] for y in range(9)]
ueberschrit="---[CODINGAME]---"
start=[4,8]
printDict={0:' ',1:'.',2:'o',3:'+',4:'=',5:'*',6:'B',7:'O',8:'X',9:'@',10:'%',11:'&',12:'#',13:'/',14:'^'}


fingerprint="fc:94:b0:c1:e5:b0:98:7c:58:43:99:76:97:ee:9f:b7"
fingerprint="00:00:00:00:00:00:00:00:ff:ff:ff:ff:ff:ff:ff:ff"

fingerList = fingerprint.split(':')

for finger in fingerList:
    for i in range(1,-1,-1):
        hexa = hexaDict[finger[i]]
        for h in hexa:
            move = moveDict[h]
            if (move[0] > 0 and start[0] < 8) or (move[0]< 0 and start[0] > 0):
                start[0] = start[0]+move[0]
            if (move[1] > 0 and start[1] < 16) or (move[1]< 0 and start[1] > 0):
                start[1] = start[1]+move[1]
            moveList[start[0]][start[1]] +=1
            if moveList[start[0]][start[1]] > 14:
                moveList[start[0]][start[1]] -= 15

moveList[4][8]="S"
moveList[start[0]][start[1]]="E"
for y in range(11):
    for x in range(19):
        if (y == 0 or y == 10) and (x == 0 or x == 18):
            print("+",end="")
        elif y == 0 or y == 10:
            if y == 0:
                print(ueberschrit[x-1],end="")
            else:
                print("-",end="")
        elif x == 0 or x == 18:
            print("|",end="")
        else:
            if moveList[y-1][x-1] in printDict:
                zeichen = printDict[moveList[y-1][x-1]]
            else:
                zeichen = moveList[y-1][x-1]
            print(zeichen,end="")
    print("")

