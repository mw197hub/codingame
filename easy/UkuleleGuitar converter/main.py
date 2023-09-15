# https://www.codingame.com/ide/puzzle/ukuleleguitar-converter

import sys,math

def getNotes(gList,max,noteList):
    for zList in gList:
        okt = zList[0]
        b = okt[0];z=int(okt[1])
        pos=-1
        for i in range(len(noteList)):
            if noteList[i] == b:
                pos=i;break
        for i in range(max):
            pos+=1
            if pos == len(noteList):
                z+=1;pos=0
            zList.append(noteList[pos]+str(z))

mode="guitar"
mode="ukulele"
posList=[[2,6]]

gitarList=[["E4"],["B3"],["G3"],["D3"],["A2"],["E2"]]
ukuList=[["A4"],["E4"],["C4"],["G4"]]

noteList=["C","C","D","D","E","F","F","G","G","A","A","B"]

getNotes(gitarList,21,noteList)
getNotes(ukuList,15,noteList)

print(gitarList[4][21])
print(ukuList[2][6])


startList=gitarList
suchList=ukuList
if not mode == "guitar":
    suchList=gitarList
    startList=ukuList
for info in posList:
    first=False
    erg=""
    note=startList[info[0]][info[1]]
    if info[1] == 0:
        if startList[info[0]][1] == note:
            first=True
    else:
        if not startList[info[0]][info[1]-1] == note:
            first=True
    for i1 in range(len(suchList)):
        sL = suchList[i1]
        e1=-1
        for i2 in range(len(sL)):
            if sL[i2] == note:
                e1=i2
                if first:
                    break
        if e1 > -1:
            erg+=str(i1)+"/"+str(e1)+" "


    if len(erg) == 0:
        print("no match")
    else:
        print(erg[:-1])