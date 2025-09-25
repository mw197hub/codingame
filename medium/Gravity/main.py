# https://www.codingame.com/ide/puzzle/gravity

import sys,math

lineList=['...#...#.#.#...#.', '.#..#...#....#...', '..........#......', '..###...###..##..', '#################']


lineDict={}
for i in range(len(lineList[0])):
    anzahl=0
    for j in range(len(lineList)):
        if lineList[j][i]=="#":
            anzahl+=1
    lineDict[i]=anzahl
print(lineDict,file=sys.stderr)
for j in range(len(lineList)):
    ausgabe=""    
    for i in range(len(lineList[0])):
        zeile=len(lineList)-j
        if lineDict[i] >= zeile:
            ausgabe+="#"
        else:
            ausgabe+="."
    print(ausgabe)