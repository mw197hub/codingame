import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: number of columns.
# h: number of rows.
typeList = {0: [0,0], 1: [0,1], 2: [2,0], 3: [0,1], 4: [2,1], 
5: [2,1], 6: [2,0], 7: [0,1], 8: [0,1],9:[0,1],10:[-1,0],
11:[1,0],12:[0,1],13:[0,1]}
mehrfach =[2,4,5,6]
mehrfachList = {2: {'LEFT':[1,0],'RIGHT':[-1,0]},4: {'TOP':[-1,0],'RIGHT':[0,1]}, 
5:{'TOP':[1,0],'LEFT':[0,1]}, 6:{'LEFT':[1,0],'RIGHT':[-1,0]} }

feldList = [['0', '3', '0'], ['0', '3', '0'], ['0', '3', '0']]
w, h = 3,3
print(str(w) + " - " + str(h),file=sys.stderr)
#for i in range(h):
#    line = input().split(" ")  # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
#    feldList.append(line)
ex = 1  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).
print(feldList,file=sys.stderr)
print(ex,file=sys.stderr)
# game loop
while True:
    inputs = ['1', '0', 'TOP']
    inputs = ['1', '0', 'TOP']
    print(inputs,file=sys.stderr)
    xi = int(inputs[0])
    yi = int(inputs[1])
    pos = inputs[2]
    typ = int(feldList[yi][xi])
    print(typ,file=sys.stderr)
    move = typeList[typ]
    if typ in mehrfach:
        richtung = mehrfachList[typ]
        move = richtung[pos]

    xi = xi + move[0]
    yi = yi + move[1]
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.
    print(str(xi) + " " + str(yi))