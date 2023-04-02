# https://www.codingame.com/ide/puzzle/ascii-art-with-logo-language-part-2
import sys,math

def sucheRP(lineList,twLine):
    if twLine[0:2].upper() == "RP":
        anzahl = int(twLine[3]) if twLine[4] == " " else int(twLine[3:4])
        start = twLine.find("[")
        rLine = twLine[start+1:-1]         
        for _ in range(anzahl):
            lineList.append(rLine)
    else:
        lineList.append(twLine)
        

lineListOri=['setpc +-;RP 2 [Rp 2 [fd 5;rt 90]]']
lineListOri=['RP 2 [setpc Hello];rt 90;fd 5']
lineListOri=['RP 2 [RP 2 [fd 5;rt 90;setpc +];RP 2 [fd 5;rt 90;setpc *]]']
lineListOri=['rt 90;RP 4 [fd 3;lt 90;rp 2 [fd 3;rt 90];fd 3;lt 90;fd 3;rt 90]']
#lineListOri=['rt 90;RP 4 [fd 5;rt 90]']
lineListOri=['cs .', 'rp 2 [rt 45];RP 4 [fd 3;rp 2 [lt 45];rp 2 [fd 3;rp 2 [rt 45]];fd 3;rp 2 [lt 45];fd 3;rp 2 [lt 45]]']



# CS FD RT LT PU PD SETPC RP

lineList=[]=[];aufloesen=True
while aufloesen:
    lineList.clear()
    for line in lineListOri:
        teile = line.split(";")
        startK=0;zeile=""
        for t in teile:
            if startK > 0:
                zeile= zeile + ";" + t
                diff = t.count("[")- t.count("]")
                startK+=diff
                if startK == 0:   
                    sucheRP(lineList,zeile)       
            elif "[" in t:
                if t.count("[") > t.count("]"):
                    startK=t.count("[")- t.count("]")
                    zeile = t
                else:
                    sucheRP(lineList,t)     
            else:
                sucheRP(lineList,t)     
    lineListOri.clear();aufloesen=False
    for line in lineList:
        lineListOri.append(line)
        if "RP" in line.upper():
            aufloesen=True



CS = " "
richtung=0  # 0=[-1,0]  1=[0,1]  2=[1,0]  3=[0,-1]
start=[51,51]
moveDict={0:[-1,0],1:[-1,1],2:[0,1],3:[1,1],4:[1,0],5:[1,-1],6:[0,-1],7:[-1,-1]}
mapList=[[" " for x in range(102)] for y in range(102)]
zeichen="";posZ=0
pen=True;minY,minX,maxY,maxX=150,150,-1,-1
anzahlZ=0
for line in lineList:
    cList = line.split(";")
    for code in cList:
        if code[0:2].upper() == "RT":
            richtung += int(code[3:]) / 45
            if richtung > 7:
                richtung -= 8
        if code[0:2].upper() == "LT":
            richtung -= int(code[3:]) / 45
            if richtung < 0:
                richtung += 8
        if code[0:2].upper() == "PD":
            pen=True
        if code[0:2].upper() == "PU":
            pen=False
        if code[0:5].upper() == "SETPC":
            zeichen = code[6:]
            posZ = 0
        if code[0:2].upper() == "CS":
            CS = code[3]
        if code[0:2].upper() == "FD":    
            if len(zeichen) == 0:
                zeichen = "#"                                
            anzahl = int(code[3:])
            for i in range(anzahl):
                if start[0] < minY:
                    minY = start[0]
                if start[0] > maxY:
                    maxY = start[0]
                if start[1] < minX:
                    minX = start[1]
                if start[1] > maxX:
                    maxX = start[1]
                if pen:
                    if anzahlZ < 20 and anzahlZ > 10:
                        mapList[start[0]][start[1]] = str(anzahlZ)[-1]
                    else:
                        mapList[start[0]][start[1]] = zeichen[posZ]
                        posZ = 0 if posZ == len(zeichen)-1 else posZ+1
                    #anzahlZ+=1
                    
                move = moveDict[abs(richtung)]
                start[0] += move[0];start[1] += move[1]


#print("{}-{}, {}-{}".format(minY,minX,maxY,maxX),file=sys.stderr)
druckList=[];y,x=999,999
for map in mapList[minY:maxY+1]:
    druck=False;zeile=""
    for i in range(minX,maxX+1):
        m = map[i]
        if not m == " ":
            druck=True
            if i < x:
                x = i
        zeile+=m
    if CS == " ":
        zeile = zeile.rstrip().replace(" ",CS)
    else:
        zeile = zeile.replace(" ",CS)
    druckList.append(zeile)

for dr in druckList:
    print(dr)
