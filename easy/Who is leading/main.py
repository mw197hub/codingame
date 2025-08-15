# https://www.codingame.com/ide/puzzle/who-is-leading

import sys,math


teams="A team,Another team";scores_1="8 31 37,32,7,10";scores_2="15 19,17 20,27 29 67,76"  #1



teamList=teams.split(",")
punktList=[0,0];timeList=[0,0]
scoreA=scores_1.split(",");scoreB=scores_2.split(",")
scA=[];scB=[]
for s in scoreA:
    scA.append(list(map(int, s.split())))
for s in scoreB:
    scB.append(list(map(int, s.split())))
for i in range(81):
    for j in range(4):
        if i in scA[j]:
            if j == 0:
                punktList[0]+=5
            elif j == 1:
                punktList[0]+=2
            else:
                punktList[0]+=3
        if i in scB[j]:
            if j == 0:
                punktList[1]+=5
            elif j == 1:
                punktList[1]+=2
            else:
                punktList[1]+=3

    if punktList[0] > punktList[1]:
        timeList[0]+=1
    if punktList[1] > punktList[0]:
        timeList[1]+=1

for i in range(2):
    print("{}: {} {}".format(teamList[i],punktList[i],timeList[i]))