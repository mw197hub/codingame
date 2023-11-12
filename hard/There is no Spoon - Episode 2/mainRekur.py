# https://www.codingame.com/ide/puzzle/there-is-no-spoon-episode-2

import sys,math,copy,time

def pruefeUeberKreuz(verbindungen,y,x,y1,x1):
    for verb in verbindungen:
        cy1,cx1,cy2,cx2,wert= verb
        #print("{} zu {} # {} zu {}".format(min(cy1,cy2),min(y,y1),max(cy1,cy2),max(y,y1)))
        if min(cy1,cy2) > min(y,y1) and max(cy1,cy2) < max(y,y1):
            if min(cx1,cx2) < min(x,x1) and max(cx1,cx2) > max(x,x1):
                return False
        if min(cx1,cx2) > min(x,x1) and max(cx1,cx2) < max(x,x1):
            if min(cy1,cy2) < min(y,y1) and max(cy1,cy2) > max(y,y1):
                return False
    return True

def pruefeAnzahl(graph,verbindungen,y,x,y1,x1,r):
    wert1=graph[(y,x)];wert2=graph[(y1,x1)]
    bisher1,bisher2=0,0
    for verb in verbindungen:
        cy1,cx1,cy2,cx2,wert=verb
        if y == cy1 and x == cx1 and y1 == cy2 and x2 == cx2:
            return False
        if cy1 == y and cx1 == x:
            bisher1+= wert
        if cy2 == y and cx2 == x:
            bisher1+=wert
        if cy1 == y1 and cx1 == x1:
            bisher2+= wert
        if cy2 == y1 and cx2 == x1:
            bisher2+=wert
    if wert1 >= bisher1+r and wert2 >= bisher2 + r:
        return True
    return False

def endeErreicht(verbindungen,graph):
    pGraph= copy.deepcopy(graph)
    for verb in verbindungen:
        cy1,cx1,cy2,cx2,wert=verb
        pGraph[(cy1,cx1)] -= wert
        pGraph[(cy2,cx2)] -= wert
    for yx in pGraph:
        if not pGraph[yx] == 0:
            if pGraph[yx] < 0:
                print(" da läuft was schief",file=sys.stderr)
                exit(1)
            return False
    
    return True


##############

lineList=[['1', '.', '2'], ['.', '.', '.'], ['.', '.', '1']]   # 1
lineList=[['2', '.'], ['4', '2']]  # 2
lineList=[['1', '.', '3'], ['.', '.', '.'], ['1', '2', '3']]  # 3
lineList=[['1', '4', '.', '3'], ['.', '.', '.', '.'], ['.', '4', '.', '4']]   # 4
#lineList=[['2', '.', '.', '2', '.', '1', '.'], ['.', '3', '.', '.', '5', '.', '3'], ['.', '2', '.', '1', '.', '.', '.'], ['2', '.', '.', '.', '2', '.', '.'], ['.', '1', '.', '.', '.', '.', '2']]  # 6
#lineList=[['3', '.', '.', '2', '.', '2', '.', '.', '1', '.', '.', '.', '.', '3', '.', '.', '.', '.', '.', '.', '.', '.', '4'], ['.', '2', '.', '.', '1', '.', '.', '.', '.', '2', '.', '6', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', '.'], ['.', '.', '3', '.', '.', '6', '.', '.', '.', '.', '3', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '2', '.', '.', '.', '.', '.', '.', '.', '.', '1', '.', '.', '3', '.', '3', '.'], ['.', '.', '1', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '3', '.', '.', '3', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '3', '.', '.', '3', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '3', '.', '.', '.', '8', '.', '.', '.', '.', '.', '8', '.', '.', '.', '.', '.', '.', '.', '.', '.', '3', '.'], ['6', '.', '5', '.', '1', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '1', '.', '.', '3', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', '.', '.', '6', '.', '3', '1', '.', '.', '2', '.'], ['.', '.', '4', '.', '.', '4', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['5', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '7', '.', '.', '.', '7', '.', '.', '.', '3', '.', '3', '.'], ['.', '2', '.', '.', '3', '.', '.', '3', '.', '.', '3', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '2', '.', '.', '2', '.', '.', '.', '1', '.', '6', '.', '.', '.', '3', '.', '.', '.'], ['.', '.', '.', '.', '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '4', '.', '.', '.', '.', '5', '.', '.', '.', '3', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', '.', '3', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '3', '.', '3', '.', '.', '2', '.', '4', '4', '.', '.', '.', '.', '1', '.', '.'], ['3', '.', '.', '.', '1', '.', '3', '.', '2', '.', '3', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '2', '.', '.', '.', '.', '.', '3', '.', '.', '.', '6', '.', '.', '.', '.', '.', '.', '.', '.', '.', '5', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '1', '.', '.', '.', '.', '.', '.'], ['.', '1', '.', '.', '.', '.', '.', '.', '.', '3', '.', '6', '.', '2', '.', '.', '.', '2', '.', '.', '.', '4', '.'], ['5', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '3', '.', '.', '.', '.', '.', '3'], ['4', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '4', '.', '2']]


########

start=time.time()

graph={}
verbindungen=[];gesamtAnzahl=0
moeglicheWege=[]
wege=[[1,0],[-1,0],[0,1],[0,-1]]
for y in range(len(lineList)):
    for x in range(len(lineList[0])):
        if not lineList[y][x] == ".":
            graph[(y,x)] = int(lineList[y][x])
            for weg in wege:
                y1=y;x1=x
                while True:
                    y1+=weg[0];x1+=weg[1]
                    if y1 < 0 or x1 < 0 or y1 >= len(lineList) or x1 >= len(lineList[0]):
                        break
                    if not lineList[y1][x1] == ".":
                        if not (y1,x1,y,x,1) in moeglicheWege:
                            moeglicheWege.append((y,x,y1,x1,1))
                            if int(lineList[y][x]) > 1 and int(lineList[y1][x1]) > 1:
                                moeglicheWege.append((y,x,y1,x1,2))
                        break

print(moeglicheWege,file=sys.stderr)
print(graph,file=sys.stderr)

lifo=[];last=False
while moeglicheWege != []:
    print(moeglicheWege,file=sys.stderr)
    y1,x1,y2,x2,r = moeglicheWege.pop(0)
    
 #   r = remain_number(i,j)
    
    if pruefeUeberKreuz(verbindungen,y1,x1,y2,x2) and pruefeAnzahl(graph,verbindungen,y1,x1,y2,x2,r):
        verbindungen.append((y1,x1,y2,x2,r))
        lifo.append((y1,x1,y2,x2,r))
        last=True
    else:
        moeglicheWege.append((y1,x1,y2,x2,r))        
        if not last:
            verbindungen.pop()
            y1,x1,y2,x2,r = lifo.pop()
            moeglicheWege.append((y1,x1,y2,x2,r))
        last=False
    if endeErreicht(verbindungen,graph):
        break

for verb in verbindungen:
   ## print("{} {} {} {} {}".format(verb[1],verb[0],verb[3],verb[2],verb[4]))
    print("{} {} {} {} {}".format(verb[0],verb[1],verb[2],verb[3],verb[4]))

print("Zeit: {}".format(time.time()-start),file=sys.stderr)