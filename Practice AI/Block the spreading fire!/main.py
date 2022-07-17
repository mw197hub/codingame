import sys
import math

def spreading(fireList,i,j,fire):
    spreadList=[[1,0],[-1,0],[0,1],[0,-1]]
    for wert in spreadList:
        iN = i + wert[0];jN=j+wert[1]
        if fireList[iN][jN] == -1:
            fire+=1;fireList[iN][jN] = 1
    return fire


def fireEntwicklung(fireList,width, height,tree_treatment_duration, tree_fire_duration,house_treatment_duration, house_fire_duration,gridList,cooldown,house):
    fire=0;cooldown+=1
    if (cooldown == tree_treatment_duration and not house) or (house and cooldown == house_treatment_duration):
        cooldown = 0
    for i in range(height):
        for j in range(width):
            if fireList[i][j] >= 0:
                fireList[i][j] += 1
                if gridList[i][j] == "X":
                    if fireList[i][j] == house_fire_duration:
                        fireList[i][j] = -3
                        fire = spreading(fireList,i,j,fire)
                else:
                    if fireList[i][j] == tree_fire_duration:
                        fireList[i][j] = -3
                        fire = spreading(fireList,i,j,fire)

    return fire,cooldown

def startFire(gridList,fire_start_x, fire_start_y,width, height):
    fireList=[[0 for i in range(width)] for i in range(height)]
    for i in range(height):
        for j in range(width):
            if gridList[i][j] == "." or "X":
                fireList[i][j] = -1
            if gridList[i][j] == "#":
                fireList[i][j] = -2
    fireList[fire_start_x][fire_start_y] = 0
    return fireList

def getLine(fire_start_x, fire_start_y,width, height,abstand):
    pos = fire_start_x if fire_start_x < fire_start_y else fire_start_y

    return pos

def setErgList(tree_treatment_duration, tree_fire_duration,house_treatment_duration, house_fire_duration,gridList,fireList,fire_start_x, fire_start_y,width, height):
    ergList = [];verhaeltnis=tree_fire_duration/tree_treatment_duration;spreadList=[[1,0],[-1,0],[0,1],[0,-1]]
    if verhaeltnis >= 4:
        for wert in spreadList:
            ergList.append([fire_start_x+wert[0],fire_start_y+wert[1]])
        return ergList
    abstand = int( math.sqrt(width*height)/(verhaeltnis*2))  # ermittelt den Abstand zum Feuer
    holzList={}
    line = getLine(fire_start_x, fire_start_y,width, height,abstand)
    return ergList

tree_treatment_duration, tree_fire_duration, tree_value = 2,4,100
house_treatment_duration, house_fire_duration, house_value = 2,4,3700
width, height = 10,10
fire_start_x, fire_start_y = 3,2
gridList = ['##########', '#........#', '#........#', '#........#', '#........#', '#.....X..#', '#........#', '#........#', '#........#', '##########']

fireList = startFire(gridList,fire_start_x, fire_start_y,width, height)
runde=0;cooldown=0;house=False
ergList = setErgList(tree_treatment_duration, tree_fire_duration,house_treatment_duration, house_fire_duration,gridList,fireList,fire_start_x, fire_start_y,width, height)
while True:

    
    if cooldown == 0:
        if len(ergList) > 0:
            erg = ergList.pop()
            print(str(erg[0])+" "+str(erg[1]))
            house=False
            if gridList[erg[0]][erg[1]] == "X":
                house=True
            fireList[erg[0]][erg[1]] = -2
    fire,cooldown=fireEntwicklung(fireList,width, height,tree_treatment_duration, tree_fire_duration,house_treatment_duration, house_fire_duration,gridList,cooldown,house)
    runde+=1
    if runde > 50:
        break

for line in fireList:
    print(line,file=sys.stderr)