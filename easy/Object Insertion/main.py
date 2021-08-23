import sys
import math

def suche(z,s,gList,dList,trefferList):
   # print("start: " + str(z) + ", " + str(s) + ": ",file=sys.stderr,end=" ")
    for o in dList:
    #    print(str(o[0]+z) + ", " + str(o[1]+s)+ "  ",file=sys.stderr,end=" ")
        if [o[0]+z,o[1]+s] not in gList:
            return
    #print(" = treffer",file=sys.stderr,end=" ")        
    trefferList.append([z,s])


objektList = ['.*', '**', '.*']
gridList = ['#..#######', '#.##..####', '###..##...', '####.#####', '##.#######', '##......##', '##.....###', '########..']

oList = []
dList = []
gList = []
trefferList = []
for z in range(len(objektList)):
    for s in range(len(objektList[0])):
        if objektList[z][s] == "*":
            oList.append([z,s])
print(oList,file=sys.stderr)
first = True
for o in oList:
    if first:
        first = False
        z,s = o[0],o[1]
    else:
        dList.append([o[0] - z, o[1] -s])
print(dList,file=sys.stderr)
print("#######",file=sys.stderr)
for z in range(len(gridList)):
    for s in range(len(gridList[0])):
        if gridList[z][s] == ".":
            gList.append([z,s])
print(gList,file=sys.stderr)
print("#######",file=sys.stderr)
for z in range(len(gridList)):
    for s in range(len(gridList[0])):
        if gridList[z][s] == ".":
            suche(z,s,gList,dList,trefferList)
         #   print("----",file=sys.stderr)
print(trefferList,file=sys.stderr)



print(len(trefferList))
if len(trefferList) == 1:  
    o = trefferList[0]
    z,s = o[0],o[1]
    gridList[z] = gridList[z][:s] + "*" + gridList[z][s+1:]
    for o in dList:
        gridList[z+o[0]] = gridList[z+o[0]][:s+o[1]] + "*" + gridList[z+o[0]][s+o[1]+1:]
    for grid in gridList:
        print(grid)
