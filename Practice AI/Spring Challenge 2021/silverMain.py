import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def berechneSchatten(treeList,hexaNummer,hexaIndex,schattenAus,schattenWertList,schattenList):
    schattenList.clear()
    for pos,tree in treeList.items():
        koord = hexaNummer[pos]
        move = schattenWertList[schattenAus]
        for i in range(tree.size):
            koordNeu = str(koord[0] + move[0] *(1 + i)) + "-" + str(koord[1] + move[1] * (1+i))
            if koordNeu in hexaIndex:
                schattenList.add(hexaIndex[koordNeu])
    return schattenList

def setWAIT(actionList):
    actionList.clear()
    print("WAIT")

def sucheTree(treeList,suchWert,actionList):
    for key,tree in treeList.items():
        if tree.size == suchWert and tree.is_mine and not key in actionList:            
            return key
    return 999

def ausgabeDay22(treeList,sun,day,actionList):
    if day == 22:
        print("WAIT")
    else:
        treffer = True
        for key,tree in treeList.items():        
            if tree.is_mine and not key in actionList:
                key = sucheTree(treeList,3,actionList)
                if key < 999:                
                    if sun >= 4:            
                        print("COMPLETE " + str(key))
                        tree = treeList[key]
                        tree.size = 0
                        actionList.append(key)
                        sun -= 4
                        treffer = False
                        break
        if treffer:
            setWAIT(actionList)



def sucheRich(seedList,cellList):
    wert = 0
    key = 0
    for i in seedList:
        cell = cellList[i]
        if cell.richness > wert:
            wert = cell.richness
            key = i
    return key

def sucheAusgangsbaum(key,treeList,startList):
    treffer = 0
    trefferList = []
    hoehe = 99
    for start,zielList in startList.items():
        if key in zielList:
            trefferList.append(start)
    for start in trefferList:
        tree = treeList[start]
        if tree.size < hoehe and tree.is_mine:
            treffer = start
            hoehe = tree.size
    return treffer

def sucheNachbar(seedList,cell,cellList,size,stList):
    size -= 1
    for i in cell.neighbors:
            if i > 0:
                nCell = cellList[i]                
                if nCell.richness > 0 and not i in treeList:
                    seedList.add(i)
                    stList.add(i)
                if size > 0:
                    sucheNachbar(seedList,nCell,cellList,size,stList)

def sucheSEED(myTree,treeList,sun,cellList,actionList):
    seedList = set()
    startList = {}
    for key,tree in treeList.items():
        cell = cellList[key]
        if tree.size > 0 and tree.is_mine and not key in actionList:
            stList = set()
            sucheNachbar(seedList,cell,cellList,tree.size,stList)
            startList[key] = stList
   # print(seedList,file=sys.stderr)
    print(startList,file=sys.stderr)
    treffer = True
    if sun >= myTree[0] + 1:               
        while (True):
            key = sucheRich(seedList,cellList)
            start = sucheAusgangsbaum(key,treeList,startList)
           # print(str(key) + " - " + str(start),file=sys.stderr)
            if start > 0 and not start in actionList:
                print("SEED " + str(start) + " " +str(key))
                actionList.append(key)
                actionList.append(start)
                sun = sun - myTree[0] - 1
                myTree[0] += 1     
                treffer = False 
                break
            seedList.remove(key)                  

    if treffer:
        setWAIT(actionList)

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

hexaIndex = {'0-3': 25, '0-5': 24, '0-7': 23, '0-9': 22, '1-2': 26, '1-4': 11, '1-6': 10, '1-8': 9, '1-10': 21, '2-1': 27, '2-3': 12, '2-5': 3, '2-7': 2, '2-9': 8, '2-11': 20, '3-0': 28, '3-2': 13, '3-4': 4, '3-6': 0, '3-8': 1, '3-10': 7, '3-12': 19, '4-1': 29, '4-3': 14, '4-5': 5, '4-7': 6, '4-9': 
18, '4-11': 36, '5-2': 30, '5-4': 15, '5-6': 16, '5-8': 17, '5-10': 35, '6-3': 31, '6-5': 32, '6-7': 33, '6-9': 34}

hexaNummer= {25:[0,3],24:[0,5],23:[0,7],22:[0,9],26:[1,2], 11:[1,4],10:[1,6], 9:[1,8],21:[1,10],27:[2,1],12:[2,3],3:[2,5],2:[2,7],8:[2,9],20:[2,11],28:[3,0],13:[3,2],4:[3,4],0:[3,6],1:[3,8],7:[3,10],19:[3,12],
29:[4,1],14:[4,3],5:[4,5],6:[4,7],18:[4,9],36:[4,11],30:[5,2],15:[5,4],16:[5,6],17:[5,8],35:[5,10],31:[6,3],32:[6,5],33:[6,7],34:[6,9]}

schattenWertList = {0:[0,2],1:[-1,1],2:[-1,-1],3:[0,-2],4:[1,-1],5:[1,1]}
#########################################
cellList = {}
treeList = {}
myTree = []
priceList = [0,1,3,7]  # + anzahl
actionList = []
schattenAus = 0
schattenList = set()

number_of_cells = int(input())  # 37
for i in range(number_of_cells):
    # index: 0 is the center cell, the next cells spiral outwards
    # richness: 0 if the cell is unusable, 1-3 for usable cells
    # neigh_0: the index of the neighbouring cell for each direction
    index, richness, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5 = [int(j) for j in input().split()]
   # print(str(index)+","+str(richness)+","+str(neigh_0)+","+str(neigh_1)+","+str(neigh_2)+","+str(neigh_3)+","+str(neigh_4)+","+str(neigh_5),file=sys.stderr)
    cellList[index] = Cell(index,richness,[neigh_0, neigh_1,neigh_2,neigh_3,neigh_4,neigh_5])


# game loop
while True:
    treeList = {}
    schattenList = set()
    myTree = [0,0,0,0]
    day = int(input())  # the game lasts 24 days: 0-23
    nutrients = int(input())  # the base score you gain from the next COMPLETE action
    schattenAus = day % 6
    # sun: your sun points
    # score: your current score
    sun, score = [int(i) for i in input().split()]
    inputs = input().split()
    opp_sun = int(inputs[0])  # opponent's sun points
    opp_score = int(inputs[1])  # opponent's score
    opp_is_waiting = inputs[2] != "0"  # whether your opponent is asleep until the next day
    number_of_trees = int(input())  # the current amount of trees
    for i in range(number_of_trees):
        inputs = input().split()
        cell_index = int(inputs[0])  # location of this tree
        size = int(inputs[1])  # size of this tree: 0-3
        is_mine = inputs[2] != "0"  # 1 if this is your tree
        is_dormant = inputs[3] != "0"  # 1 if this tree is dormant
        treeList[cell_index] = Tree(cell_index,size,is_mine,is_dormant)
        if is_mine:
            myTree[size] += 1
    number_of_possible_moves = int(input())
    for i in range(number_of_possible_moves):
        possible_move = input()

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    print("sun: " + str(sun) + "   Tage: " + str(day) + " nutrients: " + str(nutrients),file=sys.stderr)
    print(myTree,file=sys.stderr)
    print(actionList,file=sys.stderr)

    schattenList = berechneSchatten(treeList,hexaNummer,hexaIndex,schattenAus,schattenWertList,schattenList)
   # print(schattenList,file=sys.stderr)
   
    # GROW cellIdx | SEED sourceIdx targetIdx | COMPLETE cellIdx | WAIT <message>
    if day > 21:    
        ausgabeDay22(treeList,sun,day,actionList)
    else:
        if myTree[3] >= 10:
            setWAIT(actionList)
        else:
            if myTree[2] > 0 and sun >= priceList[3] + myTree[3] and sucheTree(treeList,2,actionList) < 999:
                key = sucheTree(treeList,2,actionList)
                actionList.append(key)
                print("GROW " + str(key))
            elif myTree[1] > 0 and sun >= priceList[2] + myTree[2] and sucheTree(treeList,1,actionList) < 999:
                key = sucheTree(treeList,1,actionList)
                actionList.append(key)
                print("GROW " + str(key))
            elif myTree[0] > 0 and sun >= priceList[1] + myTree[1] and sucheTree(treeList,0,actionList) < 999:            
                key = sucheTree(treeList,0,actionList)
                actionList.append(key)
                print("GROW " + str(key))

            else:
                sucheSEED(myTree,treeList,sun,cellList,actionList)

                



