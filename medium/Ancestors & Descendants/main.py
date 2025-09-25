# https://www.codingame.com/ide/puzzle/ancestors-descendants

import sys,math

lineList=['a', '.b', '..c', 'd', '.e', '..f', '.g', 'h']
lineList=['Jade', '.Andrew', '..Rose', '.Mark', 'Heidi']
lineList=['a', '.a1', '..a11', '...a111', '...a112', '..a12', '.a2', 'b', '.b1', '..b11', '.b2', '..b21', '...b211', 'c', '.c1', '..c11', '...c111', '....c1111', '.c2']

###
bisher=[];posV=0;ausgabe="";jetzt=[]
for line in lineList:
    pos=0;jetzt.clear()
    ausgabe=""
    for j in bisher:
        ausgabe+=j+" > "
    name=""
    for l in line:
        if l == ".":
            pos+=1
            jetzt.append(bisher.pop(0))
        else:
            name+=l
    jetzt.append(name)            

    if pos <= posV and len(ausgabe) > 3:
        print(ausgabe[:-3])
    posV=pos
    bisher=jetzt[:]
ausgabe=""
for j in jetzt:
        ausgabe+=j+" > "
print(ausgabe[:-3])