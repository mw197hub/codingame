import sys
import math

######################################

class Cell:
    def __init__(self, cell_index, richness, neighbors):
        self.cell_index = cell_index
        self.richness = richness
        self.neighbors = neighbors
class Tree:
    def __init__(self, cell_index, size, is_mine, is_dormant):
        self.cell_index = cell_index
        self.size = size
        self.is_mine = is_mine
        self.is_dormant = is_dormant

#########################################

schattenWertList = {0:[0,2],1:[-1,1],2:[-1,-1],3:[0,-2],4:[1,-1],5:[1,1]}
cellList = {}
priceList = [0,1,3,7]  # + anzahl
treeList = {}
schattenAus = 1
schattenList = set()

hexaNummer= {25:[0,3],24:[0,5],23:[0,7],22:[0,9],
26:[1,2], 11:[1,4],10:[1,6], 9:[1,8],21:[1,10],
27:[2,1],12:[2,3],3:[2,5],2:[2,7],8:[2,9],20:[2,11],
28:[3,0],13:[3,2],4:[3,4],0:[3,6],1:[3,8],7:[3,10],19:[3,12],
29:[4,1],14:[4,3],5:[4,5],6:[4,7],18:[4,9],36:[4,11],
30:[5,2],15:[5,4],16:[5,6],17:[5,8],35:[5,10],
31:[6,3],32:[6,5],33:[6,7],34:[6,9]}

hexaIndex = {'0-3': 25, '0-5': 24, '0-7': 23, '0-9': 22, '1-2': 26, '1-4': 11, '1-6': 10, '1-8': 9, '1-10': 21, '2-1': 27, '2-3': 12, '2-5': 3, '2-7': 2, '2-9': 8, '2-11': 20, '3-0': 28, '3-2': 13, '3-4': 4, '3-6': 0, '3-8': 1, '3-10': 7, '3-12': 19, '4-1': 29, '4-3': 14, '4-5': 5, '4-7': 6, '4-9': 
18, '4-11': 36, '5-2': 30, '5-4': 15, '5-6': 16, '5-8': 17, '5-10': 35, '6-3': 31, '6-5': 32, '6-7': 33, '6-9': 34}

f = open("C:\\Users\wiedm\Python\codingame\Practice AI\Spring Challenge 2021\input.txt", "r")
for x in f:
    inX = [int(n) for n in x.split(",")]
    cellList[inX[0]] = Cell(inX[0],inX[1],[inX[2], inX[3],inX[4],inX[5],inX[6],inX[7]])


#treeList[13] = Tree(13,2,True,False)
#treeList[29] = Tree(29,2,True,False)
#treeList[15] = Tree(15,1,True,False)
#treeList[32] = Tree(32,1,True,False)
#treeList[3] = Tree(3,0,True,False)
treeList[0] = Tree(0,3,True,False)

for pos,tree in treeList.items():
    koord = hexaNummer[pos]
    move = schattenWertList[schattenAus]
    for i in range(tree.size):
        koordNeu = str(koord[0] + move[0] *(1 + i)) + "-" + str(koord[1] + move[1] * (1+i))
        if koordNeu in hexaIndex:
            schattenList.add(hexaIndex[koordNeu])

print(schattenList)
print(6 % 6)