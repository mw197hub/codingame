import sys
import math
from operator import itemgetter

xZiel,yZiel=0,16
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

def erzeugeList(w0,h0,w,h):
    feldList = []
    for x in range(w0,w,1):
        for y in range(h0,h,1):
            feldList.append(str(x)+"-"+str(y))
    return feldList

def distance(xp1,yp1,xp2,yp2):
    return (math.sqrt( ((xp1-xp2)**2)+((yp1-yp2)**2) ))


def sprungX(bomb_dir,x0,y0,xAlt,yAlt,w0,h0,w,h,first):
    x1,y1=x0,y0
    if first:   
        x1 = w-xAlt
        return x1,y1,w0,h0,w,h,x0,y0
    if bomb_dir == "UNKNOWN":   
        if w == 1:
            y1=h-yAlt
            return x1,y1,w0,h0,w,h,x0,y0
        else:
            x1 = w-xAlt
            return x1,y1,w0,h0,w,h,x0,y0

    if bomb_dir == "SAME":
        x1 = int((x0+xAlt)/2);w=x1;w0=x1
        return x1,y1,w0,h0,w,h,x0,y0
    if bomb_dir == "WARMER":      
        mitte=w0+int((w-w0)/2)
        if x0 > xAlt:
            if w0 < xAlt+int((x0-xAlt)/2)-1:
                w0=xAlt+int((x0-xAlt)/2)-1 
            #w0=mitte-1
        else:
            if w > x0+int((xAlt-x0)/2)+1:
                w=x0+int((xAlt-x0)/2)+1
           # w=mitte+1
        mitte=w0+int((w-w0)/2)     
        x1 = mitte - (x0 - mitte)
        return x1,y1,w0,h0,w,h,x0,y0

    if bomb_dir == "COLDER":
        mitte=w0+int((w-w0)/2)
        if x0 > xAlt:
            if w > xAlt+int((x0-xAlt)/2)+1: 
                w=xAlt+int((x0-xAlt)/2)+1 
            #w=mitte+1
        else:
            if w0 < x0+int((xAlt-x0)/2)-1:
                w0=x0+int((xAlt-x0)/2)-1
            #w0=mitte-1
        mitte=w0+int((w-w0)/2)     
        x1 = mitte - (x0 - mitte)
        return x1,y1,w0,h0,w,h,x0,y0

    return x1,y1,w0,h0,w,h,x0,y0


def sucheList(bomb_dir,x0,y0,xAlt,yAlt,w0,h0,w,h,feldList):
    x1=x0;y1=y0
    newList={}
    for feld in sorted(feldList):
        xf,yf = feld.split("-")
        dist1=distance(x0,y0,int(xf),int(yf))
        dist2=distance(xAlt,yAlt,int(xf),int(yf))
        if bomb_dir == "SAME" and dist1 == dist2:            
            newList[feld] = dist1
        if bomb_dir == "WARMER" and dist1 < dist2:
            newList[feld] = dist1
        if bomb_dir == "COLDER" and dist1 > dist2:
            newList[feld] = dist2

    #print(sorted(newList),file=sys.stderr)
    if str(x0)+"-"+str(y0) in newList:
        newList.pop(str(x0)+"-"+str(y0))
    if len(newList) == 1:
        pos = 0
    else:
        pos = int(len(newList) /2)-1
    i = 0
    #pos = len(newList) -1
    newList = sorted(newList.items(), key=itemgetter(1))
    sortList = []
    for feld in newList:
        if i == pos:
            x1,y1 = feld[0].split("-")            
        i+=1;sortList.append(feld[0])

    return int(x1),int(y1),w0,h0,w,h,x0,y0,sortList

w,h=1,100
n=12;runde=0
x0,y0=0,98
w0,h0,xAlt,yAlt=0,0,x0,y0
phase=0;first=False;feldList=[]

zielList = [];fehler=False
for i in range(w):
    for j in range(h):
        zielList.append(str(i)+"-"+str(j))
zielList.clear();zielList=['402-645']
#3zielList.clear();zielList=['0-59']

for ziel1 in zielList:
  #3  n=12;runde = 0;phase=0;w,h=1,100;x0,y0=0,3;w0,h0,xAlt,yAlt=0,0,x0,y0;feldList=[];first=False;wMax=w;hMax=h
    n=27;runde=0;phase=0;w,h=1000,1000;x0,y0=501,501;w0,h0,xAlt,yAlt=0,0,x0,y0;feldList=[];first=False;wMax=w;hMax=h
    print("Start: " + str(ziel1),file=sys.stderr)
    xZiel,yZiel=ziel1.split("-");xZiel=int(xZiel);yZiel=int(yZiel)
    while True:
        bomb_dir,dist1,dist2 = getInput(x0,y0,xAlt,yAlt,runde)

        print(bomb_dir+"   alt:"+str(int(dist1))+"   neu:"+str(int(dist2)),file=sys.stderr)
        if phase == 0:
            x0,y0,w0,h0,w,h,xAlt,yAlt = sprungX(bomb_dir,x0,y0,xAlt,yAlt,w0,h0,w,h,first)
        else:
            if phase == 1:
                y0,x0,h0,w0,h,w,yAlt,xAlt = sprungX(bomb_dir,y0,x0,yAlt,xAlt,h0,w0,h,w,first);first=False
            else:
                x0,y0,w0,h0,w,h,xAlt,yAlt,feldList = sucheList(bomb_dir,x0,y0,xAlt,yAlt,w0,h0,w,h,feldList)    

        print(str(runde)+": rahmen: "+str(w0)+"-"+str(h0)+ " zu "+str(w)+"-"+str(h)+"  # alt: "+str(xAlt)+"-"+str(yAlt) + " feldList: " + str(len(feldList)) +"  phase: "+str(phase)+" # neu: "+str(x0)+"-"+str(y0),file=sys.stderr)

        if x0 >= wMax:
            x0 = wMax-1
        if x0 < 0:
            x0 = 0
        if y0 >= hMax:
            y0 = hMax-1
        if y0 < 0:
            y0 = 0   
        if x0 == xAlt and y0 == yAlt:
            x0 = w if x0 == 0 else 0
            y0 = h if y0 == 0 else 0

        print(str(x0)+" "+str(y0))

        if w - w0 < 80 and phase == 0:
            phase = 1;first=True
        if h - h0 < 80 and phase == 1:
            phase = 2
            feldList = erzeugeList(w0,h0,w,h)

        if x0 == xZiel and y0 == yZiel:
            print("erreicht",file=sys.stderr);break
        runde+=1
        if runde > n:
            print("Zeit abgelaufen",file=sys.stderr);fehler=True;break
    if fehler:
        break