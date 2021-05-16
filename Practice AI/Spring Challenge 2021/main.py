import sys
import math

def cellAbstand(hexaNummer,key1,key2):
    wert1 = hexaNummer[key1]
    wert2 = hexaNummer[key2]
    erg1 = abs(wert1[0] - wert2[0])  
    erg2 = abs(wert1[1] - wert2[1])
    if erg1 == 0 or erg2 > erg1:
        return erg1 + erg2
    else:
        return erg1 * 2


def berechneAbstand(treeList,cellList,hexaNummer,hexaIndex):
    for cellKey,cell in cellList.items():
        summe = 0
        for treeKey,tree in treeList.items():
            erg = cellAbstand(hexaNummer,cellKey,treeKey)
            if tree.is_mine:
                summe = summe + erg
        cell.abstand = summe

def berechneSchatten(treeList,hexaNummer,hexaIndex,schattenAus,schattenWertList,schattenList,cellList):
    schattenList.clear()
    for cellIndex,cell in cellList.items():
        cell.schatten = 0
    for schattenAus in range(6):
        for pos,tree in treeList.items():
            if tree.is_mine:
                koord = hexaNummer[pos]
                move = schattenWertList[schattenAus]
                for i in range(tree.size):
                    koordNeu = str(koord[0] + move[0] *(1 + i)) + "-" + str(koord[1] + move[1] * (1+i))
                    if koordNeu in hexaIndex:
                        cell = cellList[hexaIndex[koordNeu]]
                        cell.schatten += 1
                        schattenList.add(hexaIndex[koordNeu])
    return schattenList

def setWAIT(actionList):
    print("WAIT")
    return []

def sucheBaumKey(keyList,treeList,cellList,schattenList,day):
    key = -1
    wert = 0
    for keyIndex in keyList:
        cell = cellList[keyIndex]
        anzahl = 0
        for j in cell.neighbors:
            if j >= 0:
                anzahl += 1
        if day > 10:
            if cell.richness > wert:
                key = keyIndex
                wert = cell.richness
        else:
            if anzahl < 6:
                key = keyIndex
                wert = 5
            elif wert == 0:
                key = keyIndex 
    return key

def sucheTree(treeList,suchWert,actionList):
    keyList = []
    for key,tree in treeList.items():
        if tree.size == suchWert and tree.is_mine and not key in actionList:            
            keyList.append(key)
    return keyList

def baumFaellen(myTree,treeList,sun,cellList,actionList,hexaNummer,hexaIndex,day,nutrients):
    ziel = -1
    wert = 0
    if (myTree[3] > 2 and day > 10) or nutrients < 8:
        keyList = sucheTree(treeList,3,actionList)
        if len(keyList) > 0:
            for key in keyList:
                cell = cellList[key]
                if cell.richness == 3:
                    wert = cell.richness
                    ziel = key
            if ziel == -1:
                for key in keyList:
                    cell = cellList[key]
                    if cell.abstand > wert:
                        wert = cell.abstand
                        ziel = key

    return ziel

def ausgabeDay22(treeList,sun,day,actionList):
    if day == 22:
        print("WAIT")
    else:
        treffer = True
        keyList = sucheTree(treeList,3,actionList)
        if len(keyList) > 0 and sun >= 4:
            key = keyList[0]
            print("COMPLETE " + str(key))
            actionList.append(key)
            treffer = False

        if treffer:
            actionList = setWAIT(actionList)

def sucheSchatten(kreuzList,startList,cellList):
    wert = 99
    ziel = -1
    start = -1
    for key,zList in kreuzList.items():
        for i in zList:            
            cell = cellList[i]
            if cell.schatten - cell.richness  < wert:
                wert = cell.abstand - cell.richness
                ziel= i
                start = key


    return start,ziel


def sucheAbstand(kreuzList,startList,cellList):
    wert = 0
    ziel = 0
    start = 0
    for key,zList in kreuzList.items():
        for i in zList:            
            cell = cellList[i]
            if cell.abstand + cell.richness * 4 > wert:
                wert = cell.abstand + cell.richness * 4
                ziel= i
                start = key

    return start,ziel

def sucheRand(kreuzList,startList,cellList):
    wert = 9
    ziel = 0
    start = 0
    for key,zList in kreuzList.items():
        for i in zList:
            cell = cellList[i]
            anzahl = 0
            for j in cell.neighbors:
                if j >= 0:
                    anzahl += 1
            if anzahl < wert:
                wert = anzahl
                ziel = i
                start = key
    return start, ziel

def sucheRich(startList,cellList):
    wert = 0
    ziel = 0
    start = 0
    for key,zList in startList.items():
        for i in zList:
            cell = cellList[i]
            if cell.richness > wert:
                wert = cell.richness
                ziel = i
                start = key
    return start, ziel

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

def nichtImSchatten(startHexa,zielHexa,hexaNummer):
    unterschiedR = startHexa[0] - zielHexa[0]
    unterschiedS = startHexa[1] - zielHexa[1]
    if unterschiedR == 0 or abs(unterschiedR) - abs(unterschiedS) == 0:
        return False
    return True

def sucheUeberkreuz(startList,hexaNummer,hexaIndex,kreuzList):
    for treeIndex in startList:
        stList = set()
        startHexa = hexaNummer[treeIndex]
        urList = startList[treeIndex]
        for zielIndex in urList:
            if nichtImSchatten(startHexa,hexaNummer[zielIndex],hexaNummer):
                stList.add(zielIndex)                
        kreuzList[treeIndex] = stList


def sucheSEED(myTree,treeList,sun,cellList,actionList,hexaNummer,hexaIndex,day):
    seedList = set()
    startList = {}
    kreuzList = {}
    waitSchreiben = True
    for key,tree in treeList.items():
        cell = cellList[key]
        if tree.size > 0 and tree.is_mine and not key in actionList:
            stList = set()
            sucheNachbar(seedList,cell,cellList,tree.size,stList)
            startList[key] = stList
    #print(seedList,file=sys.stderr)
    print(startList,file=sys.stderr)
  #  for key,kyList in startList.items():
  #      for ky in kyList:
  #          print(str(ky) + " abstand: " + str(cellList[ky].abstand),file=sys.stderr)
    sucheUeberkreuz(startList,hexaNummer,hexaIndex,kreuzList)
    print(kreuzList,file=sys.stderr)

    if sun >= myTree[0]:
      #  start, ziel = sucheAbstand(kreuzList,startList,cellList)
      #  start,ziel = sucheRand(kreuzList,startList,cellList)
      #  if day > 6:
      #      start,ziel = sucheRich(startList,cellList)
        start, ziel = sucheSchatten(kreuzList,startList,cellList)
        if start > 0:
            print("SEED " + str(start) + " " +str(ziel))
            actionList.append(ziel)
            sun = sun - myTree[0] - 1
            myTree[0] += 1     
            waitSchreiben = False

    return waitSchreiben



######################################

class Cell:
    def __init__(self, cell_index, richness, neighbors):
        self.cell_index = cell_index
        self.richness = richness
        self.neighbors = neighbors
        self.abstand = 999
        self.schatten = 0
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
priceList = [0,1,3,7]  # + anzahl
treeList = {}
myTree = [0,0,1,0]
schattenAus = 0
schattenList = set()

actionList = [27]
day = 0
schattenAus = day % 6

f = open("C:\\Users\wiedm\Python\codingame\Practice AI\Spring Challenge 2021\input.txt", "r")
for x in f:
    inX = [int(n) for n in x.split(",")]
    cellList[inX[0]] = Cell(inX[0],inX[1],[inX[2], inX[3],inX[4],inX[5],inX[6],inX[7]])


treeList[25] = Tree(25,3,True,False)
treeList[29] = Tree(29,3,True,False)

treeList[20] = Tree(20,2,False,True)
treeList[34] = Tree(34,2,False,True)
#treeList[33] = Tree(33,2,False,True)
#treeList[15] = Tree(15,1,True,False)
#treeList[32] = Tree(32,3,True,False)
#treeList[3] = Tree(3,2,True,False)
myTree = [0,0,2,0]
sun = 4

#berechneAbstand(treeList,cellList,hexaNummer,hexaIndex)
#for cellKey,cell in cellList.items():
#    print(str(cellKey) + " abstand: " + str(cell.abstand),file=sys.stderr)

schattenList = berechneSchatten(treeList,hexaNummer,hexaIndex,schattenAus,schattenWertList,schattenList,cellList)
#print(schattenList,file=sys.stderr)
#for cellIndex,cell in cellList.items():
#    print(str(cellIndex) + " - " + str(cell.schatten),file=sys.stderr)

sucheSEED(myTree,treeList,sun,cellList,actionList,hexaNummer,hexaIndex,day)
#ausgabeDay22(treeList,sun,day,actionList)

# print(baumFaellen(myTree,treeList,sun,cellList,actionList,hexaNummer,hexaIndex,day))

#print(sucheTree(treeList,2,actionList))

#keyList = [8,18]
#print(sucheBaumKey(keyList,treeList,cellList,schattenList,day))




'''
 if day > 21:    
        ausgabeDay22(treeList,sun,day,actionList)
    else:
        if myTree[3] >= 20:
            actionList = setWAIT(actionList)
        else:
            key = baumFaellen(myTree,treeList,sun,cellList,actionList,hexaNummer,hexaIndex,day,nutrients)
            if key >= 0:
                print("COMPLETE " + str(key))
                actionList.append(key)                            
            elif myTree[2] > 0 and sun >= priceList[3] + myTree[3] and len(sucheTree(treeList,2,actionList)) > 0 and nutrients > 6 and day > 6:
                keyList = sucheTree(treeList,2,actionList)
                key = sucheBaumKey(keyList,treeList,cellList,schattenList,day)
                actionList.append(key)
                print("GROW " + str(key))
            elif myTree[1] > 0 and sun >= priceList[2] + myTree[2] and len(sucheTree(treeList,1,actionList)) > 0:
                keyList = sucheTree(treeList,1,actionList)
                key = sucheBaumKey(keyList,treeList,cellList,schattenList,day)
                actionList.append(key)
                print("GROW " + str(key))
            elif myTree[0] > 0 and sun >= priceList[1] + myTree[1] and len(sucheTree(treeList,0,actionList)) > 0:            
                keyList = sucheTree(treeList,0,actionList)
                print(keyList,file=sys.stderr)
                key = sucheBaumKey(keyList,treeList,cellList,schattenList,day)
                print(key,file=sys.stderr)
                actionList.append(key)
                print("GROW " + str(key))

            elif sucheSEED(myTree,treeList,sun,cellList,actionList,hexaNummer,hexaIndex,day):
                actionList = setWAIT(actionList)
                
                '''
