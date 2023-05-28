# https://www.codingame.com/ide/puzzle/tile-a-floor-differently

import math,sys

#1
quarter_size=3
rowList=['  /', '/b ', 'b  ']
#rowList=['123', '456', '789']


bList=['b','d','p','q']
dList=['d','b','q','p']
pList=['p','q','b','d']
qList=['q','p','d','b']

for y in range(quarter_size*4+3):
    for x in range(quarter_size*4+3):
        if y == 0 or y == quarter_size*4+2 or y == quarter_size*2+1:
            if x == 0 or x == quarter_size*4+2 or x == quarter_size*2+1:
                print("+",end="")
            else:
                print("-",end="")
        else:
            if x == 0 or x == quarter_size*4+2 or x == quarter_size*2+1:
                print("|",end="")
            else:
                if y < quarter_size+1:
                    yWert = int(y -1)  
                elif y < quarter_size*2+1:
                    yWert = int((y-1) ) - quarter_size 
                elif y < quarter_size*3+1:
                    yWert = int((y-2) ) - quarter_size *2
                else:
                    yWert = int((y-2) ) - quarter_size *3


                if x < quarter_size+1:
                    xWert = int(x -1)  
                elif x < quarter_size*2+1:
                    xWert = int((x-1) ) - quarter_size 
                elif x < quarter_size*3+1:
                    xWert = int((x-2) ) - quarter_size *2
                else:
                    xWert = int((x-2) ) - quarter_size *3
               # print("x: {} {}    y: {} {}".format(x,xWert,y,yWert),file=sys.stderr)
                wert = " "
                y1 = y - 1 if quarter_size*2+1 else y - 2
                x1 = x - 1 if quarter_size*2+1 else x - 2
                if (y1 < quarter_size and x1 < quarter_size) or (y1 < quarter_size and x1 >= quarter_size*2 and x1 <= quarter_size * 3) or (y1 >= quarter_size *2 and y1 <= quarter_size *3 and x1 < quarter_size) or (y1 >= quarter_size *2 and y1 <= quarter_size *3 and x1 >= quarter_size*2 and x1 <= quarter_size * 3):
                    wert = rowList[yWert][xWert]
                elif (x1 < quarter_size) or (x1 >= quarter_size*2 and x1 <= quarter_size * 3) or (x1 >= quarter_size*2 and x1 <= quarter_size * 3): #2
                    yWert = quarter_size-1-yWert
                    wert = rowList[yWert][xWert]
                    if wert == bList[0]:
                        wert = bList[2]
                    elif wert == dList[0]:
                        wert = dList[2]
                    elif wert == pList[0]:
                        wert = pList[2]
                    elif wert == qList[0]:
                        wert = qList[2]
                    if wert == "/":
                        wert = "\\" 
                    elif wert == "\\":
                        wert = "/"
                elif (y1 < quarter_size) or  (y1 >= quarter_size *2 and y1 <= quarter_size *3) or (y1 >= quarter_size *2 and y1 <= quarter_size *3): #1
                    xWert = quarter_size-1-xWert
                    wert = rowList[yWert][xWert]
                    if wert == bList[0]:
                        wert = bList[1]
                    elif wert == dList[0]:
                        wert = dList[1]
                    elif wert == pList[0]:
                        wert = pList[1]
                    elif wert == qList[0]:
                        wert = qList[1]
                    if wert == "/":
                        wert = "\\" 
                    elif wert == "\\":
                        wert = "/"
                else:
                    yWert = quarter_size-1-yWert
                    xWert = quarter_size-1-xWert
                    wert = rowList[yWert][xWert]
                    if wert == bList[0]:
                        wert = bList[3]
                    elif wert == dList[0]:
                        wert = dList[3]
                    elif wert == pList[0]:
                        wert = pList[3]
                    elif wert == qList[0]:
                        wert = qList[3]                        
                print(wert,end="")
    print("")