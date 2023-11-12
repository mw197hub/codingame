# https://www.codingame.com/ide/puzzle/square-spiral-for-alien-contact

import sys,math,string

def ende(grid,y,x,size):
    treffer=0
    nachbarn=[[1,0],[-1,0],[0,1],[0,-1]]
    for n in nachbarn:
        y1=y+n[0]
        x1=x+n[1]
        if y1 < 0 or x1 < 0 or y1 == size or x1 == size:
            a=0
        else:
            if not grid[y1][x1] == " ":
                treffer+=1

    if treffer > 1:
        return True
    return False



cList=['9', 'topRight', 'clockwise', 'F4', 'G4']
cList=['11', 'topLeft', 'counter-clockwise', 'C15', 'D15']
cList=['19', 'bottomRight', 'clockwise', 'B33', 'D33']
cList=['17', 'bottomRight', 'clockwise', 'M18', 'N17']
cList=['29', 'bottomRight', 'clockwise', 'A2', 'B3']
cList=['51', 'bottomLeft', 'clockwise', 'A100', 'B97']



abcList=list(string.ascii_uppercase)
#print(abcList)
buch1,buch2=0,0
wert1,wert2=int(cList[3][1:]),int(cList[4][1:])
zeichen=cList[3][0]
for i in range(len(abcList)):
    if abcList[i] == cList[3][0]:
        buch1 = i
    if abcList[i] == cList[4][0]:
        buch2 = i
#print("{}  {}".format(wert1,wert2))
pos=buch1
size=int(cList[0])
y,x=0,0;weg=0
yV,xV=0,0
zeroX,zeroY,sizeX,sizeY=0,0,size-1,size-1
if cList[1] == "topLeft":    
    weg=0
    if cList[2] == "clockwise":
        xV=1;zeroY+=2
    else:
        yV=1;zeroX+=2
elif cList[1] == "topRight":
    x=size-1
    weg=1    
    if cList[2] == "clockwise":
        yV=1;sizeX-=2
    else:
        xV=-1;zeroY+=2
elif cList[1] == "bottomRight":
    y=size-1
    x=y
    weg=3
    if cList[2] == "clockwise":
        xV=-1;sizeY-=2
    else:
        yV=-1;sizeX-=2
elif cList[1] == "bottomLeft":
    y=size-1
    weg=2
    if cList[2] == "clockwise":
        yV=-1;zeroX+=2
    else:
        xV=-1;sizeY-=2

anzahl=wert1;posWert=0
veraederung=wert2-wert1
grid=[[" " for y in range(size)] for x in range(size)]
print("y: {}  x: {}  yV: {}  xV: {}".format(y,x,yV,xV),file=sys.stderr)

while True:


    grid[y][x] = zeichen
    x=x+xV;y=y+yV
    if x < zeroX and xV == -1:
        xV=0;x=zeroX;zeroX+=2
        yV = -1 if cList[2] == "clockwise" else 1
        x=x+xV;y=y+yV
    elif y < zeroY and yV == -1:
        yV=0;y=zeroY;zeroY+=2
        xV = 1 if cList[2] == "clockwise" else -1
        x=x+xV;y=y+yV
    elif x > sizeX and xV == 1:
        xV=0;x=sizeX;sizeX-=2
        yV = 1 if cList[2] == "clockwise" else -1
        x=x+xV;y=y+yV
    elif y > sizeY and yV == 1:
        yV=0;y=sizeY;sizeY-=2
        xV = -1 if cList[2] == "clockwise" else 1
        x=x+xV;y=y+yV

    if ende(grid,y,x,size):
        break
    posWert+=1
    if posWert == anzahl:
        anzahl=anzahl+(wert2-wert1)
        posWert=0
        pos= pos + buch2 - buch1
        if pos < 0 or pos > 25:
            break
        zeichen=abcList[pos]
    
    #for y1 in range(size):
    #    print("".join([str(grid[y1][x1]) for x1 in range(size)]))
    #print("------------------------")

if size > 31:
    for y in range(31):
        print("".join([str(grid[y][x]) for x in range(31)]))
else:
    for y in range(size):
        print("".join([str(grid[y][x]) for x in range(size)]))