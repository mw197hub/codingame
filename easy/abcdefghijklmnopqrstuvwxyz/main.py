import sys
import math
import string

n=10
mList=[['v', 'k', 'b', 'j', 'b', 'z', 'm', 'b', 'g', 'b'], ['a', 'b', 'c', 'c', 'c', 'p', 'z', 'o', 'u', 'v'], ['f', 'e', 'd', 'o', 'p', 'w', 'l', 'm', 'c', 'l'], ['g', 'l', 'm', 'n', 'q', 'r', 's', 'z', 'y', 'w'], ['h', 'k', 'r', 'h', 'i', 'u', 't', 'y', 'm', 'j'], ['i', 'j', 'q', 'c', 'm', 'v', 'w', 'x', 'o', 'c'], ['p', 'c', 'v', 'l', 'p', 'q', 'z', 'p', 'h', 'l'], ['h', 's', 'g', 'v', 'o', 'k', 'l', 'c', 'x', 'y'], ['u', 'r', 'd', 'j', 'u', 's', 'm', 'b', 'm', 'z'], ['r', 'c', 'h', 'b', 'c', 'a', 'u', 's', 'n', 'p']]
aList=[[9, 5],[1, 0]]

abcList = string.ascii_lowercase
search = [[1,0],[-1,0],[0,1],[0,-1]]
ergList=[]
for start in aList:
    treffer = False
    ergList=[];ergList.append(start)
    for b in range(1,len(abcList)):
        for s in search:
            if start[0]+s[0] >= 0 and start[0]+s[0] < n and start[1]+s[1] >= 0 and start[1]+s[1] < n:
                if mList[start[0]+s[0]][start[1]+s[1]] == abcList[b]:
                    start = [start[0]+s[0],start[1]+s[1]]
                    ergList.append(start)
                    treffer=True;break
        if not treffer:
            break
    if len(ergList) == 26:
        break
for i in range(n):
    for j in range(n):
        if [i,j] in ergList:
            print(mList[i][j],end="")
        else:
            print("-",end="")
    print("")
