# https://www.codingame.com/ide/puzzle/ascii-art-with-logo-language
import sys,math

lineList=['RT 90;setpc #;PD;FD 1;PU;FD 1;PD;FD 1']
lineList=['CS .', 'SETPC *', 'FD 5', 'RT 90', 'FD 5', 'RT 90', 'FD 5', 'RT 90', 'FD 5']
#lineList=['RT 90;FD 2;RT 180;FD 1;LT 90;FD 2;PU;FD 1;SETPC *;PD;FD 1;LT 90;FD 1;RT 180;FD 3']
lineList=['setpc *;rt 90', 'fd 2', 'lt 90', 'fd 2', 'rt 90', 'fd 2', 'rt 90', 'fd 2', 'lt 90', 'fd 2', 'lt 90', 'fd 2', 'lt 90', 'fd 2', 'rt 90', 'fd 2', 'rt 90', 'fd 2', 'lt 90', 'fd 2', 'rt 90', 'fd 2', 'lt 90', 'fd 2', 'rt 90', 'fd 2', 'rt 90', 'fd 2', 'lt 90', 'fd 2', 'rt 90', 'fd 2', 'lt 90', 'fd 2', 'rt 90', 'fd 2', 'rt 90', 'fd 2', 'lt 90', 'fd 2', 'lt 90', 'fd 2', 'lt 90', 'fd 2', 'rt 90', 'fd 2', 'rt 90', 'fd 2', 'lt 90', 'fd 2', 'fd 1']
#lineList=['SetPC #;CS .', 'Lt 90;Fd 1', 'Lt 90;Fd 2', 'Lt 90;Fd 3', 'Lt 90;Fd 4', 'Lt 90;Fd 5', 'Lt 90;Fd 6', 'Lt 90;Fd 7', 'Lt 90;Fd 8', 'Lt 90;Fd 9', 'Lt 90;Fd 10', 'Lt 90;Fd 11', 'Lt 90;Fd 12', 'Lt 90;Fd 13', 'Lt 90;Fd 14', 'Lt 90;Fd 15', 'Lt 90;Fd 16', 'Lt 90;Fd 17', 'Lt 90;Fd 18', 'Lt 90;Fd 19', 'Lt 90;Fd 20', 'Lt 90;Fd 21', 'fd 1']

# CS FD RT LT PU PD SETPC

CS = " "
richtung=0  # 0=[-1,0]  1=[0,1]  2=[1,0]  3=[0,-1]
start=[51,51]
moveDict={0:[-1,0],1:[0,1],2:[1,0],3:[0,-1]}
mapList=[[" " for x in range(102)] for y in range(102)]
zeichen="#"
pen=True;minY,minX,maxY,maxX=150,150,-1,-1
anzahlZ=0
for line in lineList:
    cList = line.split(";")
    for code in cList:
        if code[0:2].upper() == "RT":
            richtung += int(code[3:]) / 90
            if richtung > 3:
                richtung -= 4
        if code[0:2].upper() == "LT":
            richtung -= int(code[3:]) / 90
            if richtung < 0:
                richtung += 4
        if code[0:2].upper() == "PD":
            pen=True
        if code[0:2].upper() == "PU":
            pen=False
        if code[0:5].upper() == "SETPC":
            zeichen = code[6]
        if code[0:2].upper() == "CS":
            CS = code[3]
        if code[0:2].upper() == "FD":                                    
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
                        mapList[start[0]][start[1]] = zeichen
                    anzahlZ+=1
                    
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
    
    zeile = zeile.rstrip().replace(" ",CS)
    druckList.append(zeile)

for dr in druckList:
    print(dr)
