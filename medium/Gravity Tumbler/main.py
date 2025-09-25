# https://www.codingame.com/ide/puzzle/gravity-tumbler

import sys,math

count=2;lineList=['.................', '.................', '...##...###..#...', '.####..#####.###.', '#################']
count=1;lineList=['.................', '.................', '...##...###..#...', '.####..#####.###.', '#################']


for runde in range(count):
    lineDict={}
    for i in range(len(lineList[0])):
        anzahl=0
        for j in range(len(lineList)):
            if lineList[j][i]=="#":
                anzahl+=1
        lineDict[i]=anzahl
    print(lineDict,file=sys.stderr)
    anzDict={}    
    for lD,wert in lineDict.items():
        for i in range(wert):
            if i in anzDict:
                anzDict[i]+=1
            else:
                anzDict[i]=1
    print(anzDict,file=sys.stderr)
    newList=[]
    for i in range(len(lineList[0])):    
        line=""
        for j in range(len(lineList)):                        
            if len(lineList)-j-1 in anzDict and anzDict[len(lineList)-j-1] >= len(lineList[0])-i:
                line+="#"
            else:
                line+="."
        newList.append(line)
    lineList=newList[:]


lineDict={}
for i in range(len(lineList[0])):
    anzahl=0
    for j in range(len(lineList)):
        if lineList[j][i]=="#":
            anzahl+=1
    lineDict[i]=anzahl
for j in range(len(lineList)):
    ausgabe=""    
    for i in range(len(lineList[0])):
        zeile=len(lineList)-j
        if lineDict[i] >= zeile:
            ausgabe+="#"
        else:
            ausgabe+="."
    print(ausgabe)