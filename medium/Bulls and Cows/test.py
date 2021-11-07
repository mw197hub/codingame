import sys
import math

#inputList = [['0536','2','2']]
#inputList = [['1234', '4', '0']]
#inputList = [['0473', '2', '2'], ['7403', '0', '4']]
#inputList = [['0123', '1', '0'], ['4567', '0', '0'], ['8901', '1', '0'], ['1110', '3', '0']]
#inputList = [['9073', '2', '0'], ['1248', '2', '0'], ['1043', '0', '0']]
#inputList = [['1111', '0', '0'], ['2222', '1', '0'], ['3333', '0', '0'], ['4444', '0', '0'], ['5555', '0', '0'], ['6666', '0', '0'], ['7777', '2', '0'], ['8888', '1', '0'], ['2778', '0', '4'], ['7287', '2', '2']]
inputList = [['0123', '1', '0'], ['4567', '1', '0'], ['8901', '1', '0'], ['8522', '3', '0'], ['8525', '3', '0']]


n = len(inputList)
lst=[]
for i in range(n):
    guess, bulls, cows = inputList[i][0],inputList[i][1],inputList[i][2]
    bulls = int(bulls)
    cows = int(cows)
    lst+=[[guess,bulls,cows]]
perm = [f'{i:>04}' for i in range(10000)]
for i in perm:
    i = '8528'
    wrong=0
    for j in lst:
        sec = []
        guess = []
        cow,bull=0,0
        for k in range(4):
            if j[0][k]==i[k]: bull+=1
            else: guess+=[j[0][k]]; sec+=[i[k]]
        for k in guess:
            if k in sec:sec.remove(k);cow+=1
        if bull!=j[1] or cow!=j[2]: wrong=1
    if wrong==0: print(i);exit()