# https://www.codingame.com/ide/puzzle/micro-assembly

import sys,math

a=1;b=2;c=3;d=-4
instructionList=['MOV b 3', 'MOV c a']

a=2;b=3;c=4;d=5
instructionList=['ADD a b 1', 'ADD b 2 7', 'ADD c a b']

a=14;b=2;c=21;d=9
instructionList=['SUB a a a', 'SUB d 12 a', 'SUB b 15 3']

#a=3;b=5;c=7;d=9
#instructionList=['SUB b b 1', 'JNE 0 b 0']

a=1;b=3;c=3;d=7
instructionList=['MOV a 10', 'MOV b 5', 'MOV c b', 'SUB c c 1', 'ADD a a c', 'JNE 3 c 0', 'SUB b b 1', 'JNE 2 b c', 'SUB d 0 d']


#####

abcDict={'a':a,'b':b,'c':c,'d':d}
pos = 0
while True:
    instruction = instructionList[pos]
    insList=instruction.split(" ")
    if insList[0] == "MOV":
        wert=insList[2]
        if insList[2] in abcDict:
            wert=abcDict[insList[2]]
        else:
            wert = int(wert)
        abcDict[insList[1]] = wert
    elif insList[0] == "JNE":
        wert2=insList[3]
        if insList[3] in abcDict:
            wert2=abcDict[insList[3]]
        else:
            wert2 = int(wert2)
        if abcDict[insList[2]] != wert2:
            pos = int(insList[1]) -1

    elif insList[0] == "ADD" or insList[0] == "SUB":
        wert1=insList[2]
        if insList[2] in abcDict:
            wert1=abcDict[insList[2]]
        else:
            wert1 = int(wert1)
        wert2=insList[3]
        if insList[3] in abcDict:
            wert2=abcDict[insList[3]]
        else:
            wert2 = int(wert2)
        if insList[0] == "ADD":
            abcDict[insList[1]]= wert1 + wert2
        else:
            abcDict[insList[1]]= wert1 - wert2
    pos+=1
    if pos == len(instructionList):
        break


print(str(abcDict['a'])+' '+str(abcDict['b'])+' '+str(abcDict['c'])+' '+str(abcDict['d']))
