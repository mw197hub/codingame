import sys,math


mapList=[['#', '#', '#', '#', '#', '#'], ['#', '#', '#', '#', '#', '#'], ['#', '#', '#', '#', '#', '#'], ['#', '#', '#', '#', '#', '#'], ['#', '#', '#', '#', '#', '#'], ['*', '*', '*', '*', '*', '*']]
mapList=[['*', '*', '*', '*', '*', '*'], ['#', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '#']]


suchList=[[-2, -2], [-2, -1], [-2, 0], [-2, 1], [-2, 2], [-1, -2], [-1, -1], [-1, 0], [-1, 1], [-1, 2], [0, -2], [0, -1], [0, 0], [0, 1], [0, 2], [1, -2], [1, -1], [1, 0], [1, 1], [1, 2], [2, -2], [2, -1], [2, 0], [2, 1], [2, 2]]
fireList=[];trees=0
for y in range(6):
    for x in range(6):
        if mapList[y][x] == '*':
            fireList.append([y,x])

if len(fireList) == 0:
    print("RELAX")
else:
    for fire in fireList:
        y = fire[0];x=fire[1]
        for yx in suchList:
            yN = y + yx[0];xN=x+yx[1]
            if yN < 0 or yN > 5 or xN < 0 or xN > 5:
                n=0
            else:
                if mapList[yN][xN] == "#":
                    trees+=1
                    mapList[yN][xN] = "f"
    restTrees=0
    for y in range(6):
        for x in range(6):
            if mapList[y][x] == '#':
                restTrees+=1


    if restTrees == 0:
        print("JUST RUN")
    else:
        print(str(trees))
