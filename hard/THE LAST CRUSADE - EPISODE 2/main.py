import sys
import math


def setzeRichtung(move):
    if move[0] == 0:
        return 'TOP'
    elif move[0] < 0:
        return 'RIGHT'
    else:
        return 'LEFT'
def neueRichtung(mAlt,mNew):
    x = mNew[1] - mAlt[1]
    y = mNew[0] - mAlt[0]
    if x != 0:
        return 'TOP'
    if y < 0:
        return 'LEFT'
    return 'RIGHT'


def bildeGraph(feldList):
    felder = []
    for y in range(h):
        for x in range(w):
            if feldList[y][x] != '0':
                felder.append(str(x)+"-"+str(y))
    #print(felder,file=sys.stderr)
    s = [[1,0],[-1,0],[0,1]]
    graph = {}
    for feld in felder:
        tab = []
        wert = feld.split("-")
        x = int(wert[0])
        y = int(wert[1])
        for move in s:
            x1 = x + move[0]
            y1 = y + move[1]
            if str(x1)+"-"+str(y1) in felder:
                tab.append(str(x1)+"-"+str(y1))

        graph[feld] = tab
  #  print(graph,file=sys.stderr)
  #  print(felder,file=sys.stderr)
    return graph, felder



def schritte(x,y,posV,feldList,felder,schrittList,graph,moveList, ziel,mod):
    if posV == "RIGHT":
        posV = "LEFT"
    elif posV == "LEFT":
        posV = "RIGHT"
        
    feld = str(x)+"-"+str(y)
  #  print(feld,file=sys.stderr)
    schrittList.append(feld)
    if feld in ziel:
        moveList.append(schrittList[:])
        return
   # felder.remove(feld)
    if feld in graph:
        mList = graph[feld]
        for mFeld in mList:
            if mFeld not in schrittList:
                x1,y1 = mFeld.split('-')
                posN = neueRichtung([abs(int(x)),abs(int(y))],[abs(int(x1)),abs(int(y1))])
                typ = int(feldList[abs(int(y))][abs(int(x))])
                pRichtung = direktList[abs(typ)]
                if posV in pRichtung and pRichtung[posV] == posN:
                    schritte(x1,y1,posN,feldList,felder,schrittList,graph,moveList,ziel,mod)
                    schrittList.pop()
                else:
          #  print(mNew,file=sys.stderr)
                    gesetzt = False
                    if typ > 0 and mod:
                        rWert = rotateList[abs(typ)]                                    
                        bewegList = []
                        if 'R' in rWert:
                            gesetzt, bewegList = richtungDrehen('R',rWert,posV,posN,direktList,bewegList,typ,[abs(int(y1)),abs(int(x1))])                
                        if 'L' in rWert and not gesetzt:
                            gesetzt, bewegList = richtungDrehen('L',rWert,posV,posN,direktList,bewegList,typ,[abs(int(y1)),abs(int(x1))]) 
                    if gesetzt:
                        schritte(x1,y1,posN,feldList,felder,schrittList,graph,moveList,ziel,mod)
                        schrittList.pop()
                
    else:
        schrittList.clear()
        return

def sucheWeg(inputs,feldList,felder,graph,ziel,mod):
    moveList = []
    xStart = int(inputs[0])
    yStart = int(inputs[1])
    pos = inputs[2]
    if pos == "RIGHT":
        pos = "LEFT"
    elif pos == "LEFT":
        pos = "RIGHT"
    schrittList = []
    schritte(xStart,yStart,pos,feldList,felder,schrittList,graph,moveList,ziel,mod)
    return moveList

def richtungDrehen(art,rWert,posAlt,posNew,direktList,bewegList,typ,mNew):
    gesetzt = False
    typNew = rWert[art]
    if typNew == 0:
        return gesetzt, bewegList
    pRichtung = direktList[abs(typNew)]
    
    if posAlt in pRichtung and pRichtung[posAlt] == posNew:   
        l = [mNew[0],mNew[1],art, typ, typNew]     
        bewegList.append(l)
        gesetzt = True
      #  print(l,file=sys.stderr)
    else:
        rWert = rotateList[abs(typNew)]
        if art in rWert:
            typNew = rWert[art]
            if typNew == 0:
                return gesetzt, bewegList
            pRichtung = direktList[abs(typNew)]
            if posAlt in pRichtung and pRichtung[posAlt] == posNew:
                l2 = [mNew[0],mNew[1],art, typ, typNew]
                bewegList.append(l2)
                bewegList.append(l2)
                gesetzt = True
              #  print(l2,file=sys.stderr)
              #  print(l2,file=sys.stderr)
    return gesetzt, bewegList

def getMoveDaten(m):
    mAlt = m.split("-")
    return [int(mAlt[0]),int(mAlt[1])]
    
def addiereMove(mAlt,move):
    x1 = mAlt[0] + move[0]
    y1 = mAlt[1] + move[1]
    return[x1,y1]

def pruefeWeg(moveL,typeList,rotateList,inputs):
    moeglich = False
    bewegList = []
    mAlt = getMoveDaten(moveL[0])
    posAlt = inputs[2]
    for i in range(1,len(moveL)-1):        
        mNew = getMoveDaten(moveL[i])
        posNew = neueRichtung(mNew,getMoveDaten(moveL[i+1]))

        typ = int(feldList[mNew[1]][mNew[0]])
        richtung = typeList[abs(typ)]

        pRichtung = direktList[abs(typ)]
        if posAlt in pRichtung and pRichtung[posAlt] == posNew:
            okay = 0
        else:
          #  print(mNew,file=sys.stderr)
            if typ < 0:
                return False,[]
            rWert = rotateList[abs(typ)]            
            # links versuchen
            gesetzt = False
            if 'R' in rWert:
                gesetzt, bewegList = richtungDrehen('R',rWert,posAlt,posNew,direktList,bewegList,typ,mNew)                
            # rechts versuchen
            if 'L' in rWert and not gesetzt:
                gesetzt, bewegList = richtungDrehen('L',rWert,posAlt,posNew,direktList,bewegList,typ,mNew) 
            if not gesetzt:
                return False,[]

        if posNew == 'RIGHT':
            posAlt = 'LEFT'
        else:
            if posNew == 'LEFT':
                posAlt = 'RIGHT'
            else:
                posAlt = 'TOP'
        mAlt = mNew[:]        


    return True,bewegList

# top = [0,1], right = [1,0], left = [-1,0]
typeList = {0: [0,0], 1: {'TOP':[0,1],'LEFT':[0,1],'RIGHT':[0,1]},
2: {'LEFT':[1,0],'RIGHT':[-1,0]}, 3: {'TOP':[0,1]},
4: {'TOP':[-1,0],'RIGHT':[0,1]}, 5:{'TOP':[1,0],'LEFT':[0,1]},
6:{'LEFT':[1,0],'RIGHT':[-1,0]}, 7: {'TOP':[0,1],'RIGHT':[0,1]}, 
8:{'LEFT':[0,1],'RIGHT':[0,1]}, 9:{'TOP':[0,1],'LEFT':[0,1]},
10:{'TOP':[-1,0]}, 11:{'TOP':[1,0]},
12:{'RIGHT':[0,1]}, 13:{'LEFT':[0,1]} }

rotateList = {1:{'R':0,'L':0},2:{'R':3,'L':3}, 3:{'R':2,'L':2},4:{'L':5,'R':0},5:{'R':4,'L':0},
6:{'R':7,'L':9},7:{'R':8,'L':6},8:{'R':9,'L':7},9:{'R':6,'L':8},
10:{'R':13,'L':11},11:{'R':12,'L':10},12:{'R':13,'L':11},13:{'R':10,'L':12}}

direktList = {1:{'TOP':'TOP', 'LEFT':'TOP','RIGHT':'TOP'},
2:{'LEFT':'RIGHT','RIGHT':'LEFT'}, 3:{'TOP':'TOP'},
4:{'TOP':'LEFT','RIGHT':'TOP'},5:{'LEFT':'TOP','TOP':'RIGHT'},
6:{'LEFT':'RIGHT','RIGHT':'LEFT'},7:{'TOP':'TOP','RIGHT':'TOP'},
8:{'LEFT':'TOP','RIGHT':'TOP'},9:{'TOP':'TOP','LEFT':'TOP'},
10:{'TOP':'LEFT'},11:{'TOP':'RIGHT'},
12:{'RIGHT':'TOP'},13:{'LEFT':'TOP'}}


'''
feldList = [['0', '0', '-3', '0', '0'], 
            ['0', '0', '4', '8', '11'], 
            ['0', '0', '-3', '2', '10']]
w,h = 5,3
ex = 2
inputs = ['2', '0', 'TOP']
'''
'''
feldList = [['0', '-3', '0', '0', '0', '0', '0', '0'], 
            ['0', '12', '3', '2', '3', '3', '12', '0'],  #['0', '12', '3', '2', '3', '3', '12', '0'], 
            ['0', '0', '0', '0', '0', '0', '2', '0'], 
            ['0', '-12', '3', '2', '2', '3', '13', '0']]
w,h = 8,4
ex = 1
inputs= ['1', '0', 'TOP']
'''
'''
feldList = [['0', '0', '0', '0', '0', '0', '-3', '0', '0', '0', '0', '0', '0'], 
            ['0', '0', '0', '8', '3', '3', '5', '2', '2', '8', '2', '3', '13'],
            ['0', '0', '11', '5', '13', '0', '3', '0', '0', '3', '0', '0', '2'], 
            ['0', '10', '10', '0', '3', '0', '2', '0', '11', '4', '10', '0', '2'], 
            ['0', '3', '0', '0', '2', '0', '2', '0', '2', '0', '3', '0', '3'],
            ['0', '2', '0', '12', '10', '10', '1', '2', '10', '0', '3', '12', '10'],
            ['12', '6', '0', '2', '0', '3', '2', '12', '3', '3', '10', '4', '-13'], 
            ['11', '-1', '2', '-6', '2', '-6', '6', '-6', '2', '3', '2', '-6', '-10']]
w,h = 13,8
ex = 1
inputs = ['6', '0', 'TOP']
'''
'''
feldList = [['-3', '12', '8', '6', '3', '2', '7', '2', '7', '0', '0', '0', '0'], 
            ['11', '5', '13', '0', '0', '0', '3', '0', '3', '0', '0', '0', '0'], 
            ['0', '11', '2', '2', '3', '3', '8', '2', '-9', '2', '3', '13', '0'], 
            ['0', '0', '0', '0', '0', '12', '8', '3', '1', '3', '2', '7', '0'], 
            ['0', '0', '11', '2', '3', '1', '5', '2', '10', '0', '0', '11', '13'], 
            ['0', '0', '3', '0', '0', '6', '8', '0', '0', '0', '0', '0', '2'], 
            ['0', '0', '11', '3', '3', '10', '11', '2', '3', '2', '3', '2', '8'], 
            ['0', '12', '6', '3', '2', '3', '3', '6', '3', '3', '2', '3', '12'], 
            ['0', '11', '4', '2', '3', '2', '2', '11', '12', '13', '13', '13', '0'], 
            ['0', '0', '-3', '12', '7', '8', '13', '13', '4', '5', '4', '10', '0']]
w,h = 13,10
ex = 2
inputs = ['0','0','TOP']
'''
'''
feldList = [['0', '0', '0', '0', '0', '0', '0', '0', '-3', '0'], 
            ['0', '7', '-2', '3', '-2', '3', '-2', '3', '11', '0'],    
            ['0', '-7', '-2', '2', '2', '2', '2', '2', '2', '-2'], 
            ['0', '6', '-2', '2', '2', '2', '2', '2', '2', '-2'], 
            ['0', '-7', '-2', '2', '2', '2', '2', '2', '2', '-2'], 
            ['0', '8', '-2', '2', '2', '2', '2', '2', '2', '-2'], 
            ['0', '-7', '-2', '2', '2', '2', '2', '2', '2', '-2'], 
            ['0', '-3', '0', '0', '0', '0', '0', '0', '0', '0']]
w,h = 10,8
ex = 1
inputs = ['8','0','TOP']
'''

feldList = [['0', '-3', '0', '-3', '0', '-3', '0', '-3', '-3', '0'], 
            ['0', '7', '-2', '2', '-2', '2', '-2', '2', '10', '0'], 
            ['0', '-7', '-2', '-2', '-2', '-2', '3', '-2', '2', '-2'], 
            ['0', '9', '-2', '-2', '-2', '-2', '-2', '2', '-2', '-2'], 
            ['0', '-7', '-2', '-2', '-2', '-2', '2', '-2', '2', '-2'], 
            ['0', '7', '-2', '-2', '-2', '-2', '-2', '2', '-2', '-2'], 
            ['0', '-7', '-2', '-2', '-2', '-2', '2', '-2', '2', '-2'], 
            ['0', '-3', '0', '0', '0', '0', '0', '0', '0', '0']]
w,h = 10,8
ex = 1
inputs = ['8','0','TOP']
#inputs = ['8','1','TOP']


graph, felder = bildeGraph(feldList)
#print(graph,file=sys.stderr)
#print("-----",file=sys.stderr)
ziel = str(ex)+"-"+str(h - 1)
zielL = []
zielL.append(ziel)
moveList = sucheWeg(inputs,feldList,felder,graph,zielL,True)
print("----- mögliche Wege ------",file=sys.stderr)
print(len(moveList),file=sys.stderr)
print(moveList,file=sys.stderr)
print("-----",file=sys.stderr)
wegeList = []
zaehler = 0
ergList = []
ergWeg = []
anzahl = 999
for moveL in sorted(moveList):
    zaehler += 1
    #print(zaehler,file=sys.stderr)
    #print(moveL,file=sys.stderr)
    moeglich,bewegList = pruefeWeg(moveL,typeList,rotateList,inputs)
    if moeglich:
       # print(zaehler,file=sys.stderr)
       # print(moveL,file=sys.stderr)
        wegeList.append(bewegList[:])
        if len(moveL) < anzahl:
            anzahl = len(moveL)
            ergList = bewegList[:]
            ergWeg = moveL[:]

print(ergList,file=sys.stderr)

richt = {'L':'LEFT','R':'RIGHT'}

print('#### start ###',file=sys.stderr)
runde = 0
richt = {'L':'LEFT','R':'RIGHT'}
while True:
    if runde < len(ergList):
        erg = ergList[runde]
        sum = int(inputs[0]) - erg[0] + int(inputs[1]) - erg[1]

        print(str(erg[0]) + " " + str(erg[1]) + " " + richt[erg[2]])
        feldList[erg[1]][erg[0]] = str(erg[4])
    else:
        print("WAIT")

    if runde > 2:
        break
    runde += 1


rocks = ['5','5','RIGHT']
moveList = sucheWeg(rocks,feldList,felder,graph,ergWeg,False)
if len(moveList) > 0:
    moveL = moveList[0]
    saveL = moveL[:]
    if len(moveL) > 2:
        drehF = moveL.pop()    
        while True:
            drehF = getMoveDaten(moveL.pop())
            if int(feldList[drehF[1]][drehF[0]]) > 0:
                print(drehF)
                break
            if len(moveL) == 0:                                
                while saveL:
                    drehF = getMoveDaten(saveL.pop())
                    typF = int(feldList[drehF[1]][drehF[0]])
                    if typF > 0 and typF in [6,7,8,9]:
                        print("doppelDreh",file=sys.stderr)
                break



[['0', '-3', '0', '-3', '0', '-3', '0', '-3', '-3', '0'], 
['0', '7', '-2', '3', '-2', '2', '-2', '3', '11', '0'], 
['0', '-7', '-2', '-2', '-2', '-2', '2', '-2', '2', '-2'], 
['0', '6', '-2', '-2', '-2', '-2', '-2', '2', '-2', '-2'],
 ['0', '-7', '-2', '-2', '-2', '-2', '2', '-2', '2', '-2'],
  ['0', '8', '-2', '-2', '-2', '-2', '-2', '2', '-2', '-2'],
   ['0', '-7', '-2', '-2', '-2', '-2', '2', '-2', '2', '-2'],
    ['0', '-3', '0', '0', '0', '0', '0', '0', '0', '0']]
