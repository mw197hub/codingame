# https://www.codingame.com/ide/puzzle/zeckendorf-representation-part-i

import sys,math

def searchErg(eList,fDict,num,pos):
    for i in range(pos,0,-1):
        eList.append(fDict[i])
        if sum(eList) == num:
            break
        if sum(eList) < num:
            searchErg(eList,fDict,num,i-2)
        eList.pop()
    return eList


fDict={}
n = 100
num1 = 0
num2 = 1
next_number = num2  
count = 1

while count <= n:
    #print(next_number, end=" ")
    fDict[count] = next_number
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
#print(fDict,file=sys.stderr)


num=64
num=781436


start=100
for i in range(100,1,-1):
    if fDict[i] < num:
        start=i
        break
#print(start,file=sys.stderr)
eList=[]
for i in range(start,0,-1):
    eList.clear()
    eList.append(fDict[i])
    eList=searchErg(eList,fDict,num,i-2)
    if sum(eList) == num:
        outp=""
        for e in sorted(eList,reverse=True):
            outp = outp+str(e)+"+"
        print(outp[:-1])
        break



