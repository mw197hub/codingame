# https://www.codingame.com/ide/puzzle/pachinko-jackpot

import sys,math,copy,itertools



height=5;iList=['0', '12', '012', '0120', '12012'];pList=[900, 600, 300, 500, 700, 800]
#height=5;iList=['1', '00', '000', '0000', '00000'];pList=[900, 600, 300, 500, 700, 800]

datei = open('C:\\Users\\marku\\Python\\codingame\\easy\\Pachinko Jackpot\\input.txt','r')
i=0
iList.clear();pList.clear()
for zeile in datei:
    if i == 0:
        height=int(zeile)
    else:
        if i <= height:
            iList.append(zeile[:-1])
        else:
            pList.append(int(zeile[:-1]))
    i+=1        
##
height=5;iList=['0', '12', '012', '0120', '12012'];pList=[900, 600, 300, 500, 700, 800]


###
erg=0
#print(gList,file=sys.stderr)
graph={'0':int(iList[0])}
for x in range(1,len(iList)):    
    zDict={}
    for id,wert in graph.items():
        pos = id[-1]
        for i in range(2):
            idN = id+str(i+int(pos))
            zDict[idN] = wert+int(iList[x][int(pos)+i])
    graph.clear()
    graph = copy.deepcopy(zDict)
#print(graph,file=sys.stderr)
#print(len(graph))
for id,wert in graph.items():
    pos = id[-1]
    ber1 = pList[int(pos)] * wert
    ber2 = pList[int(pos)+1] * wert
  #  print(ber)
    if ber1 > erg:
        erg = ber1
    if ber2 > erg:
        erg = ber2
print(erg)


###
datei.close()


zahlen=[]
#for i in range(height):
#    zahlen.append(i)
#print(zahlen)
#perm = itertools.permutations(zahlen)
#for i in list(perm):
#    print(i)


#height = int(input())

best = [];i=0
for row in range(height):
    increments = [int(each) for each in iList[i]]
    print(increments,file=sys.stderr)
    #assert len(increments) == row + 1
    skew = zip(best + [0], [0] + best, increments)
    best = [max(left, right) + each for left, right, each in skew]

    i+=1

#prizes = [pList for _ in range(height + 1)]
prizes = pList[:]
skew = zip(best + [0], [0] + best, prizes)
jackpot = max(max(left, right) * prize for left, right, prize in skew)

print(jackpot)