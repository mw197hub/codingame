# https://www.codingame.com/ide/puzzle/shikaku-skill-builder

import sys,math

w,h=3,2;nList=[[0, 0, 0], [0, 4, 0]];pList=['1-1']  #1
w,h=4,3;nList=[[0, 0, 0, 0], [0, 2, 4, 0], [0, 0, 0, 0]];pList=['1-1', '1-2'] #3
w,h=3,2;nList=[[0, 0, 0], [0, 2, 0]];pList=['1-1'] #2
w,h=5,5;nList=[[6, 0, 0, 0, 0], [0, 2, 0, 4, 0], [0, 0, 9, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]];pList=['0-0', '1-1', '1-3', '2-2'] #4

for p in pList:
    rechtecke=[]
    xP,yP=p.split("-");xP=int(xP);yP=int(yP)
    wert=nList[xP][yP]
    for i in range(1,wert+1):
        que = wert // i
        if que * i == wert:
            rechtecke.append([i,int(que)])
    #print(rechtecke,file=sys.stderr)    
    treffer=False;ergList=[]
    for x in range(h):
        for y in range(w):        
           # print("{} - {}".format(x,y))
            for recht in rechtecke:
                xE=x+recht[0]-1;yE=y+recht[1]-1
                if xE < h and yE < w:
                    if xP >=x and yP >= y and xP <= xE and yP <= yE:
                        andereP=False
                        for andere in pList:
                            xA,yA=andere.split("-");xA=int(xA);yA=int(yA)
                            if xA == xP and yA == yP:
                                a=0
                            else:
                                if xA >=x and yA >= y and xA <= xE and yA <= yE:
                                    andereP=True
                        if not andereP:
                            treffer=True
                            #if not treffer:
                                #print("{} {} {}".format(xP,yP,wert));treffer=True
                            #print("{} {} {} {}".format(x,y,recht[1],recht[0]))
                            ergList.append([x,y,recht[1],recht[0]])

    if treffer:
        print("{} {} {}".format(xP,yP,wert));treffer=True
        for erg in sorted(ergList):
            print("{} {} {} {}".format(erg[0],erg[1],erg[2],erg[3]))
        
