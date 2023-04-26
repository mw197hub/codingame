#  https://www.codingame.com/ide/puzzle/killer-sudoku-solver

import sys,math,time,copy
from itertools import permutations



def setYX(y,x):
    return str(y)+"-"+str(x)
def getYX(yx):
    y,x =yx.split("-")
    return int(y),int(x)

def check(y,x,n,outList,abcList,abcDict,cagesDict,wertDict):
    for i in range(9):
        if outList[y][i]==n:return False
        if outList[i][x]==n:return False
    a=(y//3)*3
    b=(x//3)*3
    for i in range(3):
        for j in range(3):
            if outList[a+i][b+j]==n:return False
    abc = abcList[y][x]
    wert = cagesDict[abc]
    abcL = abcDict[abc]
    summe=0;anzNull=0
    for yx in abcL:
        summe+=outList[yx[0]][yx[1]]
    if summe+n> wert:
        return False

    return True

def zero(outList,abcList,abcDict,cagesDict,wertDict):
    #for abcL in sorted(abcDict.items(), key=lambda item:len(item[1])):
    #    for ab in abcL[1]:
    #        if outList[ab[0]][ab[1]]==0:
    #            return ab[0],ab[1]
   #     print(abc,file=sys.stderr)
    for i in range(9):
        for j in range(9):
            if outList[i][j]==0:
                return i,j
    return None

def solve(outList,abcList,abcDict,cagesDict,wertDict,ausgList):
    z = zero(outList,abcList,abcDict,cagesDict,wertDict)
    #print("solve")
    if z == None:
        return True
    y,x=z
    abc = abcList[y][x]

    wertList = wertDict[abc]
    for wL in wertList:
        okay=True
        abcL = abcDict[abc]
        for i in range(len(wL)):
            w = wL[i];ab=abcL[i]
            if outList[ab[0]][ab[1]] == 0:                
                rueck = check(ab[0],ab[1],w,outList,abcList,abcDict,cagesDict,wertDict)
                if not rueck:
                    okay = False;break
            else:
                if not outList[ab[0]][ab[1]] == w:
                    okay = False;break
        if okay:
            for i in range(len(wL)):
                w = wL[i];ab=abcL[i]
                outList[ab[0]][ab[1]]=w
            if solve(outList,abcList,abcDict,cagesDict,wertDict,ausgList):
                return True
            for i in range(len(wL)):
                ab=abcL[i]
                if ausgList[ab[0]][ab[1]] == 0:
                    outList[ab[0]][ab[1]]=0    

    return False

#easy
zahlList=[['5', '6', '.', '.', '1', '.', '.', '2', '.'], ['.', '.', '7', '2', '.', '.', '6', '8', '.'], ['.', '.', '2', '.', '8', '7', '.', '1', '5'], ['.', '.', '.', '.', '.', '.', '3', '.', '9'], ['.', '7', '.', '.', '.', '.', '2', '.', '.'], ['9', '.', '6', '3', '4', '.', '8', '.', '.'], ['2', '.', '9', '.', '.', '8', '.', '.', '.'], ['.', '.', '4', '1', '.', '2', '.', '.', '.'], ['.', '8', '.', '4', '.', '.', '.', '3', '.']]
abcList=[['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'e'], ['a', 'f', 'g', 'h', 'h', 'i', 'i', 'd', 'e'], ['j', 'f', 'g', 'g', 'k', 'l', 'm', 'm', 'e'], ['j', 'j', 'g', 'n', 'k', 'l', 'o', 'p', 'p'], ['q', 'q', 'g', 'n', 'o', 'o', 'o', 'r', 'r'], ['s', 't', 'u', 'u', 'v', 'w', 'w', 'x', 'x'], ['s', 't', 'u', 'u', 'v', 'v', 'w', 'y', 'z'], ['s', 'A', 'u', 'u', 'B', 'y', 'y', 'y', 'z'], ['C', 'A', 'D', 'D', 'B', 'E', 'E', 'F', 'F']]
cages='a=12 b=17 c=4 d=14 e=15 f=13 g=19 h=7 i=10 j=16 k=10 l=13 m=10 n=15 o=15 p=13 q=11 r=11 s=18 t=3 u=28 v=15 w=20 x=8 y=22 z=12 A=11 B=13 C=6 D=9 E=10 F=5'
# hard
zahlList=[['.', '.', '.', '.', '.', '.', '.', '.', '1'], ['.', '.', '.', '.', '5', '.', '.', '.', '.'], ['.', '.', '.', '3', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '9', '.'], ['.', '.', '6', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '9', '.', '7', '.', '.'], ['.', '.', '.', '.', '.', '3', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '8', '.', '.', '5', '.', '.', '.']]
abcList=[['a', 'b', 'b', 'c', 'd', 'd', 'd', 'e', 'f'], ['a', 'g', 'c', 'c', 'c', 'h', 'f', 'f', 'f'], ['i', 'j', 'j', 'j', 'h', 'h', 'k', 'k', 'l'], ['i', 'j', 'm', 'm', 'n', 'n', 'o', 'k', 'p'], ['q', 'r', 'r', 's', 't', 't', 'u', 'v', 'v'], ['q', 'w', 'x', 's', 'y', 'u', 'u', 'z', 'A'], ['q', 'w', 'x', 'x', 'y', 'B', 'B', 'C', 'A'], ['q', 'D', 'x', 'E', 'E', 'B', 'B', 'C', 'C'], ['D', 'D', 'F', 'F', 'F', 'B', 'G', 'H', 'H']]
cages='a=14 b=9 c=17 d=22 e=3 f=20 g=3 h=9 i=6 j=21 k=19 l=7 m=9 n=11 o=4 p=6 q=16 r=15 s=11 t=11 u=10 v=9 w=9 x=20 y=16 z=5 A=5 B=22 C=19 D=17 E=11 F=15 G=3 H=11'
#expert
zahlList=[['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.']]
abcList=[['a', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd'], ['a', 'a', 'b', 'e', 'f', 'g', 'h', 'i', 'i'], ['j', 'k', 'k', 'e', 'f', 'g', 'h', 'i', 'l'], ['j', 'm', 'n', 'n', 'n', 'o', 'o', 'i', 'l'], ['m', 'm', 'm', 'p', 'p', 'q', 'q', 'r', 'l'], ['s', 't', 't', 'p', 'u', 'u', 'q', 'r', 'r'], ['s', 'v', 'w', 'w', 'w', 'x', 'x', 'x', 'y'], ['z', 'v', 'v', 'A', 'B', 'B', 'C', 'C', 'y'], ['z', 'D', 'D', 'A', 'A', 'E', 'E', 'F', 'F']]
cages='a=7 b=23 c=13 d=13 e=5 f=10 g=17 h=11 i=28 j=12 k=8 l=16 m=20 n=9 o=11 p=22 q=14 r=8 s=15 t=13 u=4 v=17 w=11 x=16 y=8 z=4 A=19 B=10 C=7 D=13 E=15 F=6'


startZeit=time.time()
cagesDict={};abcDict={};wertDict={}
for cage in cages.split(" "):
    abc,wert = cage.split("=")
    cagesDict[abc]=int(wert)
    abcDict[abc]=[]
outList=[[ 0 for y in range(9)] for x in range(9)]
for y in range(9):
    for x in range(9):
        if zahlList[y][x] == ".":
            outList[y][x] = 0
        else:
            outList[y][x] = int(zahlList[y][x])
        abc = abcList[y][x]
        abcDict[abc].append([y,x])

#print(abcDict,file=sys.stderr)
for abc,abcL in abcDict.items():
    if len(abcL) == 1:
        ab = abcL[0]
        outList[ab[0]][ab[1]] = cagesDict[abc]
    if cagesDict[abc] == len(abcL):
        for ab in abcL:
            outList[ab[0]][ab[1]] = 1
    if cagesDict[abc] == len(abcL) * 9:
        for ab in abcL:
            outList[ab[0]][ab[1]] = 9

    wert=cagesDict[abc]
    wList=[]
    perList= (list(permutations(range(1,10), len(abcL))))
    for per in perList:
        if sum(per) == wert and max(per) <= 9:
            wList.append(per)
    wertDict[abc] = wList[:]

    #print("{}  {} ".format(abc,len(wList)),file=sys.stderr)



solve(outList,abcList,abcDict,cagesDict,wertDict,copy.deepcopy(outList))

for y in range(9):
    for x in range(9):
        print(outList[y][x],end="")
    print("")

print(time.time()-startZeit,file=sys.stderr)
