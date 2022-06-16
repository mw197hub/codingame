import sys
import math
from operator import itemgetter


def getInput(x0,y0,xAlt,yAlt,runde):    
    if runde == 0:
        return "UNKNOWN",0,0
    dist2 = distance(x0,y0,xZiel,yZiel) # neu
    dist1 = distance(xAlt,yAlt,xZiel,yZiel) # alt
    if dist1 == dist2:
        return "SAME",dist1,dist2
    if dist2 < dist1:
        return "WARMER",dist1,dist2
    return "COLDER",dist1,dist2

def distance(xp1,yp1,xp2,yp2):
    return (math.sqrt( ((xp1-xp2)**2)+((yp1-yp2)**2) ))

def sprungZiel(bomb_dir,x0,y0,xAlt,yAlt,w0,h0,w,h,first,wMax,hMax,zLinks,zRechts):
    x1,y1=x0,y0
    if first:   
        if x0 > w/2:
            x1=w - x0 -1
        else:
            x1=w - x0 -1
        return x1,y1,w0,h0,w,h,x0,y0,zLinks,zRechts
    if bomb_dir == "UNKNOWN":   
        if w == 1:
            y1=h-1-yAlt
            return x1,y1,w0,h0,w,h,x0,y0,zLinks,zRechts
        else:
            x1 = w-1-xAlt
            return x1,y1,w0,h0,w,h,x0,y0,zLinks,zRechts

    if bomb_dir == "SAME":
        x1 = int((x0+xAlt)/2);w=x1+1;w0=x1
        return x1,y1,w0,h0,w,h,x0,y0,zLinks,zRechts

    notWert =0
    if bomb_dir == "WARMER":
        if x0 > xAlt:
            #w0=x0-int((x0-xAlt) /2)-1 if xAlt+int((x0-xAlt) /2)-1 > w0 else w0 +1;notWert=1
            w0=x0-int((x0-xAlt) /2)-1 if xAlt+int((x0-xAlt) /2)-1 > w0 else w0 +1;notWert=1;zLinks=zLinks+1;zRechts=0
        else:
            #w=x0+int((xAlt-x0)/2)+1 if xAlt-int((xAlt-x0)/2)+1 < w else w -1;notWert=-1
            w=x0+int((xAlt-x0)/2)+1 if xAlt-int((xAlt-x0)/2)+1 < w else w -1;notWert=-1;zLinks=0;zRechts=zRechts+1

    if bomb_dir == "COLDER":
        if x0 > xAlt:
            #w=x0-int((x0-xAlt) /2)+1  if x0-int((x0-xAlt) /2)+1 < w else w -1;notWert=-1
            w=x0-int((x0-xAlt) /2)+1  if x0-int((x0-xAlt) /2)+1 < w else w -1;notWert=-1;zLinks=zLinks+1;zRechts=0
        else:
            #w0=x0+int((xAlt-x0)/2)-1 if x0+int((xAlt-x0)/2)-1  > w0 else w0 +1;notWert=1
            w0=x0+int((xAlt-x0)/2)-1 if x0+int((xAlt-x0)/2)-1  > w0 else w0 +1;notWert=1;zLinks=0;zRechts=zRechts+1

    mitte = int(w0 + ((w-w0)/2))
    abstand = mitte - x0
    if abstand == 0:
        x1 = mitte + notWert
    else:
        x1 = mitte + abstand 
    if zLinks > 2 or zRechts > 2:
        if zLinks:
            x1 = w;zLinks=0
        else:
            x1 = w0;zRechts=0

        
    if x1 < 0 or x1 >= wMax:
        x1 = mitte

    return x1,y1,w0,h0,w,h,x0,y0,zLinks,zRechts

w,h=1,100
n=12;runde=0
x0,y0=0,98
w0,h0,xAlt,yAlt=0,0,x0,y0
phase=0;first=False;feldList=[]

zielList = [];fehler=False
for i in range(w):
    for j in range(h):
        zielList.append(str(i)+"-"+str(j))
#7zielList.clear();zielList=['402-645']
#3zielList.clear();zielList=['0-59']
zielList.clear();zielList=['0-2']
#6zielList.clear;zielList=['22-26']
#4zielList.clear;zielList=['4-10']


for ziel1 in zielList:
  #3  n=12;runde = 0;phase=0;w,h=1,100;x0,y0=0,98;w0,h0,xAlt,yAlt=0,0,x0,y0;feldList=[];first=True;wMax=w;hMax=h
  #7  n=27;runde=0;phase=0;w,h=1000,1000;x0,y0=501,501;w0,h0,xAlt,yAlt=0,0,x0,y0;feldList=[];first=True;wMax=w;hMax=h
    n=31;runde = 0;phase=0;w,h=8000,8000;x0,y0=3200,2100;w0,h0,xAlt,yAlt=0,0,x0,y0;feldList=[];first=True;wMax=w;hMax=h
  #6  n=16;runde = 0;phase=0;w,h=50,50;x0,y0=17,29;w0,h0,xAlt,yAlt=0,0,x0,y0;feldList=[];first=True;wMax=w;hMax=h #n=16
  #4  n=15;runde = 0;phase=0;w,h=5,16;x0,y0=1,5;w0,h0,xAlt,yAlt=0,0,x0,y0;feldList=[];first=True;wMax=w;hMax=h #n=16

    print("Ziel: " + str(ziel1),file=sys.stderr)
    xZiel,yZiel=ziel1.split("-");xZiel=int(xZiel);yZiel=int(yZiel);first=False;phase=0;zLinks=0;zRechts=0
    while True:
        bomb_dir,dist1,dist2 = getInput(x0,y0,xAlt,yAlt,runde)
        print(bomb_dir+"   alt:"+str(int(dist1))+"   neu:"+str(int(dist2)),file=sys.stderr)
        if phase == 0:
            x0,y0,w0,h0,w,h,xAlt,yAlt,zLinks,zRechts = sprungZiel(bomb_dir,x0,y0,xAlt,yAlt,w0,h0,w,h,first,wMax,hMax,zLinks,zRechts)
        else:
            y0,x0,h0,w0,h,w,yAlt,xAlt,zLinks,zRechts = sprungZiel(bomb_dir,y0,x0,yAlt,xAlt,h0,w0,h,w,first,hMax,wMax,zLinks,zRechts);first=False

        print(str(runde)+": rahmen: "+str(w0)+"-"+str(h0)+ " zu "+str(w)+"-"+str(h)+"  # alt: "+str(xAlt)+"-"+str(yAlt) + "  # neu: "+str(x0)+"-"+str(y0) +"  # phase: "+str(phase),file=sys.stderr,end=" ")
        print(" zL/zR: "+str(zLinks)+" / " + str(zRechts),file=sys.stderr)

        print(str(x0)+" "+str(y0))

        if w - w0 == 1 and phase == 0:
            phase = 1;first=True


        if x0 == xZiel and y0 == yZiel:
            print("erreicht",file=sys.stderr);break
        runde+=1
        if runde > n:
            print("Zeit abgelaufen",file=sys.stderr);fehler=True;break
    if fehler:
        break
