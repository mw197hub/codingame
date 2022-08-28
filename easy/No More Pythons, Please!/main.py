import sys
import math
sys.setrecursionlimit(15000)

def bewegen(start,mapList,moveDict,zl,n,m,bisherList,zulDict):
    zl+=1;bisherList.append(start)
    print(start,file=sys.stderr)
    for i in range(len(moveDict[mapList[start[0]][start[1]]])):
        mList = moveDict[mapList[start[0]][start[1]]]
        move = mList[i]
        newM = [start[0]+move[0], start[1]+move[1]]
        if newM[0] >= 0 and newM[1] >= 0 and newM[0] < n and newM[1] < m:
            if not newM in bisherList:
                zuList = zulDict[mapList[start[0]][start[1]]]
                if mapList[newM[0]][newM[1]] in zuList[i]:
                    zl = bewegen(newM,mapList,moveDict,zl,n,m,bisherList,zulDict)                    
    return zl

n,m = 7,7
mapList = [['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['<', '-', '-', '-', '-', '-', 'o'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.']]
n,m=5,7  #15 1
mapList=[['*', '-', '-', '-', '-', '-', '*'], ['|', '*', '-', '-', '-', '*', '|'], ['|', '|', '*', '-', '*', '|', '|'], ['|', '|', '|', '.', '|', '|', '|'], ['v', 'o', 'v', '.', 'o', 'v', 'o']]

# *-----*
# |*---*|
# ||*-*||
# |||.|||
# vov.ovo


moveDict = {'o':[[1,0],[-1,0],[0,1],[0,-1]],'-':[[0,1],[0,-1]],'|':[[1,0],[-1,0]],'>':[],'<':[],'v':[],'^':[],'*':[[1,0],[-1,0],[0,1],[0,-1]]}
zulDict = {'o':[['|'],['|'],['-'],['-']],'-':[['-','*','>'],['-','*','<']],'|':[['|','*','v'],['|','*','^']],'>':[],'<':[],'v':[],'^':[],'*':[['v','|'],['^','|'],['>','-'],['<','-']]}

startList = []
laenge=0;anzahl=0

for i in range(n):
    for j in range(m):
        if mapList[i][j] == "o":
            startList.append([i,j])
print(startList,file=sys.stderr)
for start in startList:
    print("start: " + str(start[0])+"-"+str(start[1]),file=sys.stderr)
    bisherList=[]
    zl=bewegen(start,mapList,moveDict,0,n,m,bisherList,zulDict)
    if zl > laenge:
        laenge = zl; anzahl=1
    elif zl == laenge:
        anzahl +=1

print(laenge)
print(anzahl)