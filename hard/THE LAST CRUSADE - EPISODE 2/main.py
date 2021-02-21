import sys
import math

import sys
import math
newPos = {[0,1]:'TOP',[-1,0]:'LEFT', [1,0]:'RIGHT'}

typeList = {0: [0,0], 1: {'TOP':[0,1],'LEFT':[0,1],'RIGHT':[1,0]},
2: {'LEFT':[1,0],'RIGHT':[-1,0]}, 3: {'TOP':[0,1]},
4: {'TOP':[-1,0],'RIGHT':[0,1]}, 5:{'TOP':[1,0],'LEFT':[0,1]},
6:{'LEFT':[1,0],'RIGHT':[-1,0]}, 7: {'TOP':[0,1],'RIGHT':[0,1]}, 
8:{'LEFT':[0,1],'RIGHT':[0,1]}, 9:{'TOP':[0,1],'LEFT':[0,1]},
10:{'TOP':[-1,0]}, 11:{'TOP':[1,0]},
12:{'RIGHT':[0,1]}, 13:{'LEFT':[0,1]} }
rotateList = {2:{'R':3,'L':3}, 3:{'R':2,'L':2},4:{'L':5,'R':0},5:{'R':4,'L':0},
6:{'R':7,'L':9},7:{'R':8,'L':6},8:{'R':7,'L':9},9:{'R':6,'L':8},
10:{'R':0,'L':13},11:{'R':12,'L':0},12:{'R':0,'L':11},13:{'R':10,'L':0}}

feldList = [['0', '-3', '0', '0', '0', '0', '0', '0'], 
            ['0', '11', '3', '3', '2', '3', '12', '0'], 
            ['0', '0', '0', '0', '0', '0', '2', '0'], 
            ['0', '-12', '3', '2', '2', '3', '13', '0']]

w,h = 8,4
ex = 1


while True:
    inputs= ['1', '1', 'TOP']

    xi = int(inputs[0])
    yi = int(inputs[1])
    posi = inputs[2]
    typ = int(feldList[yi][xi])
    richtung = typeList[abs(typ)]
    move = richtung[posi]
    xn = xi + move[0]
    yn = yi + move[1]
    typNew = int(feldList[yn][xn])
    richtungNew = typeList[typNew]
    posNew = newPos[move]
    if posNew in richtungNew:
        print("WAIT")
    else:
        rotate = rotateList[typNew]
        print(rotate,file=sys.stderr)
        if rotate['R'] > 0:
            typC = rotate['R']
            richtungC = typeList[typC]
            if posNew in richtungC:
                feldList[yn][xn] = typC
                print(str(xn) + " " + str(yn) + " RIGHT")
        elif rotate['L'] > 0:
            typC = rotate['L']
            richtungC = typeList[typC]
            if posNew in richtungC:
                feldList[yn][xn] = typC
                print(str(xn) + " " + str(yn) + " LEFT")

    
    print(feldList,file=sys.stderr)
    break