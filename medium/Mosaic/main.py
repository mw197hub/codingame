# https://www.codingame.com/ide/puzzle/mosaic

import sys,math

lineList=['4..', '.7.', '..4']  #1
lineList=['0..', '.5.', '...']  #3
lineList=['.00.', '..3.', '.43.', '....']  #4

##########################################

def setYX(y,x):
    return str(y)+'-'+str(x)
def getYX(yx):
    y,x = yx.split('-')
    return int(y),int(x)
def getMaxWert(y,x,breite):
    wert=0
    for y1 in range(y-1,y+2,1):
        for x1 in range(x-1,x+2,1):
            if y1 < 0 or x1 < 0 or y1 >= breite or x1 >= breite:
                continue
            else:
                wert+=1
    return wert
def nachbarnSetzen(y,x,wert,ausgabeList):
    for y1 in range(y-1,y+2,1):
        for x1 in range(x-1,x+2,1):
            if y1 < 0 or x1 < 0 or y1 >= len(ausgabeList) or x1 >= len(ausgabeList):
                continue
            else:
                if ausgabeList[y1][x1] == 0:
                    ausgabeList[y1][x1] = wert
def pruefenErledigt(feld,ausgabeList,felderDict):
    y,x = getYX(feld)
    anzahl=0;minusWerte=0;nullen=0
    for y1 in range(y-1,y+2,1):
        for x1 in range(x-1,x+2,1):
            if y1 < 0 or x1 < 0 or y1 >= len(ausgabeList) or x1 >= len(ausgabeList):
                continue
            else:
                if ausgabeList[y1][x1] == 1:
                    anzahl+=1
                if ausgabeList[y1][x1] == -1:
                    minusWerte+=1
                if ausgabeList[y1][x1] == 0:
                    nullen+=1
    if int(felderDict[feld][0]) == anzahl:
        return True
    if int(felderDict[feld][0]) == anzahl + (int(felderDict[feld][1]) - minusWerte):
        nachbarnSetzen(y,x,1,ausgabeList)
        return True
    if int(felderDict[feld][0]) == anzahl + nullen:
        nachbarnSetzen(y,x,1,ausgabeList)
        return True
    return False




###
ausgabeList=[] # 0 = offen, 1 = gesetzt, -1 = darf nicht gesetzt werden
felderDict={}
for y in range(len(lineList)):
    line=[]
    for x in range(len(lineList)):
        line.append(0)
    ausgabeList.append(line[:])

for y in range(len(lineList)):
    for x in range(len(lineList)):                
        if not lineList[y][x] == ".":            
            maxWert = getMaxWert(y,x,len(lineList))
            felderDict[setYX(y,x)] = [lineList[y][x],maxWert,0] # anzahl, maxWert, rest
            if int(lineList[y][x]) == 0:
                nachbarnSetzen(y,x,-1,ausgabeList)
                felderDict.pop(setYX(y,x))
            if int(lineList[y][x]) == maxWert:
                nachbarnSetzen(y,x,1,ausgabeList)
                felderDict.pop(setYX(y,x))

print(felderDict,file=sys.stderr)
print(ausgabeList,file=sys.stderr)

while True:
    removeList=[]
    for feld in felderDict:
        if pruefenErledigt(feld,ausgabeList,felderDict):
            removeList.append(feld)
    for remove in removeList:
        y,x = getYX(remove)
        nachbarnSetzen(y,x,-1,ausgabeList)
        felderDict.pop(remove)

    if len(felderDict) == 0:
        break


for y in range(len(ausgabeList)):
    ausgabe=""
    for x in range(len(ausgabeList)):
        if ausgabeList[y][x] == 1:
            ausgabe+="#"
        else:
            ausgabe+="."
    print(ausgabe)


