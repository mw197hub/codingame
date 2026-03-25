# https://www.codingame.com/ide/puzzle/highest-truncated-pyramid

import sys,math

n=1
n=5

ergList=[];start=1
while True:
    testList=[]
    for i in range(start,n+1):
        testList.append(i)
        if sum(testList) >= n:
            break
    if sum(testList) == n:
        ergList=testList[:]
        break
    start+=1

for erg in ergList:
    e=""
    for i in range(erg):
        e+="*"
    print(e)