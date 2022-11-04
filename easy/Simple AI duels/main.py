import sys
import math

def getRAND(x):
    erg = (137 * x + 187) % 256
    b = str(bin(erg))[2:]
    anz = b.count("1")
    act = "C" if anz % 2 else "D"
    return erg,act

def player(i,list,b1,b2,p1,p2):
    if i == 0:
        for l in list:
            if "START" in l:
                return l[1]
    for l in list:
        if l[0] == "OPP":
            if l[1] == "MAX":
                anz = b2.count(l[2])
                if anz > len(b2)/2:
                    return l[3]
            elif l[1] == "LAST":
                pos = int(l[2]) * -1
                anz = b2[pos:].count(l[3])
                if abs(pos) > len(b2):
                    pos = len(b2)
                if anz > abs(pos)/2:
                    return l[4]
            elif l[1] == "WIN":
                if p2 > p1:
                    return l[2]
            elif b2[int(l[1])] == l[2]:
                return l[3]
        if l[0] == "ME":
            if l[1] == "MAX":
                anz = b1.count(l[2])
                if anz > len(b2)/2:
                    return l[3]
            elif l[1] == "LAST":
                pos = int(l[2]) * -1
                anz = b1[pos:].count(l[3])
                if abs(pos) > len(b1):
                    pos = len(b1)
                if anz > abs(pos)/2:
                    return l[4]
            elif l[1] == "WIN":
                if p1 > p2:
                    return l[2]
            elif b1[int(l[1])] == l[2]:
                return l[3]

    for l in list:
        if l[0] == "*":
            return l[1]

nbturns=100
ai1,ai2='NiceGuy1','NiceGuy2'
list1=[['*', 'C']]
list2=[['*', 'C']]

ai1,ai2='Joker1','Joker2'
list1=[['*', 'RAND']]
list2=[['*', 'RAND']]

rbturns=1000
list1=[['START', 'C'], ['ME', '-1', 'D', 'D'], ['OPP', '-1', 'D', 'D'], ['*', 'C']]
list2=[['*', 'D']]

rbturns=100
list1=[['START', 'C'], ['OPP', 'MAX', 'D', 'D'], ['*', 'C']]
list2=[['START', 'RAND'], ['ME', '-1', 'D', 'C'], ['ME', '-1', 'C', 'D']]

rbturns=100
list1=[['START', 'C'], ['OPP', 'MAX', 'D', 'D'], ['*', 'C']]
list2=[['START', 'RAND'], ['ME', '-1', 'D', 'C'], ['ME', '-1', 'C', 'D']]

rbturns=100
list1=[['START', 'C'], ['OPP', 'LAST', '3', 'D', 'D'], ['*', 'C']]
list2=[['START', 'RAND'], ['OPP', '-1', 'D', 'C'], ['OPP', '-1', 'C', 'D']]

rbturns=100
list1=[['START', 'C'], ['ME', 'WIN', 'D'], ['*', 'C']]
list2=[['START', 'RAND'], ['ME', '-1', 'D', 'C'], ['ME', '-1', 'C', 'D']]


p1,p2,x=0,0,12
bisher1,bisher2=[],[]
for i in range(nbturns):
    act1 = player(i,list1,bisher1,bisher2,p1,p2)
    act2 = player(i,list2,bisher2,bisher1,p2,p1)

    if act1 == "RAND":
        x,act1 = getRAND(x)
    if act2 == "RAND":
        x,act2 = getRAND(x)

    bisher1.append(act1);bisher2.append(act2)
    if act1 == "C" and act2 == "C":
        p1+=2;p2+=2
    elif act1 == "D" and act2 == "D":
        p1+=1;p2+=1
    elif act1 == "C":
        p1+=0;p2+=3
    else:
        p1+=3;p2+=0

print(str(p1) + " zu "+str(p2),file=sys.stderr)
print(bisher1,file=sys.stderr)
print(bisher2,file=sys.stderr)

if p1 == p2:
    print("DRAW")
elif p1 > p2:
    print(ai1)
else:
    print(ai2)
