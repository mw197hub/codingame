import sys
import math
from operator import itemgetter
import random

xZiel,yZiel=0,16
schrittweite = 30
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

def erzeugeStart(w0,h0,w,h):    
    feldList = []
    for x in range(schrittweite,w,schrittweite):
        for y in range(schrittweite,h,schrittweite):
            feldList.append(str(x)+"-"+str(y))
    return feldList

def newList(listX,w,h):
    feldList = []
    xList = [];yList=[]
    for feld in listX:
        x,y=feld.split("-");x=int(x);y=int(y)
        xList.append(x)
        yList.append(y)
        for i in range(-schrittweite,schrittweite,1):
            for j in range(-schrittweite,schrittweite,1):
                if x+i < w and y+j < h:
                    feldList.append(str(x+i)+"-"+str(y+j))
    return feldList

def distance(xp1,yp1,xp2,yp2):
    return (math.sqrt( ((xp1-xp2)**2)+((yp1-yp2)**2) ))


def sucheList(bomb_dir,x0,y0,xAlt,yAlt,w0,h0,w,h,feldList,first):
    x1=x0;y1=y0
    newList={};summX,summY=0,0
    for feld in sorted(feldList):
        xf,yf = feld.split("-")
        if first:
            newList[feld] = int(x0) + int(y0) - (int(xf) + int(yf))
        else:
            dist1=distance(x0,y0,int(xf),int(yf))
            dist2=distance(xAlt,yAlt,int(xf),int(yf))
            if bomb_dir == "SAME" and dist1 == dist2:            
                #newList[feld] = dist1
                newList[feld] = int(x0) + int(y0) - (int(xf) + int(yf));summX=summX+int(xf);summY=summY+int(yf)
            if bomb_dir == "WARMER" and dist1 < dist2:
                #newList[feld] = dist1
                newList[feld] = int(x0) + int(y0) - (int(xf) + int(yf));summX=summX+int(xf);summY=summY+int(yf)
            if bomb_dir == "COLDER" and dist1 > dist2:
                #newList[feld] = dist2   # dist2
                newList[feld] = int(x0) + int(y0) - (int(xf) + int(yf));summX=summX+int(xf);summY=summY+int(yf)
    
    if str(x0)+"-"+str(y0) in newList:
        newList.pop(str(x0)+"-"+str(y0))

    diffX=int(summX/len(feldList));diffY=int(summY/len(feldList))
    
 #   for feld,laenge in newList.items():
 #       print(laenge,file=sys.stderr,end=" ")
 #       print(feld,file=sys.stderr)

    sortList = []
    for feld in newList:       
        sortList.append(feld)
    #x9=random.randint(int(diffX/2)*-1,int(diffX/2))
    #y9=random.randint(int(diffY/2)*-1,int(diffY/2))
    x9=random.randint(0,w)
    y9=random.randint(0,h)
    print("random: " + str(x9)+"  "+str(y9),file=sys.stderr)
    x1=x0+x9
    y1=y0+y9

    if len(feldList) == 1:
        x1,y1=sortList[0].split("-")

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
#7zielList.clear();zielList=['402-645']
#3zielList.clear();zielList=['0-59']
#8zielList.clear();zielList=['1000-2252']
zielList.clear;zielList=['41-42']

for ziel1 in zielList:
  #3  n=12;runde = 0;phase=0;w,h=1,100;x0,y0=0,3;w0,h0,xAlt,yAlt=0,0,x0,y0;feldList=[];first=True;wMax=w;hMax=h
  #7  n=27;runde=0;phase=0;w,h=1000,1000;x0,y0=501,501;w0,h0,xAlt,yAlt=0,0,x0,y0;feldList=[];first=True;wMax=w;hMax=h
  #8  n=31;runde = 0;phase=0;w,h=8000,8000;x0,y0=3200,2100;w0,h0,xAlt,yAlt=0,0,x0,y0;feldList=[];first=True;wMax=w;hMax=h
    n=999;runde = 0;phase=0;w,h=50,50;x0,y0=17,29;w0,h0,xAlt,yAlt=0,0,x0,y0;feldList=[];first=True;wMax=w;hMax=h #n=16


    print("Start: " + str(ziel1),file=sys.stderr)
    xZiel,yZiel=ziel1.split("-");xZiel=int(xZiel);yZiel=int(yZiel);listX=[];listY=[]
    listX = erzeugeStart(w0,h0,w,h)
    if h < schrittweite or w < schrittweite:
        feldList = erzeugeList(w0,h0,w,h);phase=1
    while True:
        bomb_dir,dist1,dist2 = getInput(x0,y0,xAlt,yAlt,runde)
        print(bomb_dir+"   alt:"+str(int(dist1))+"   neu:"+str(int(dist2)),file=sys.stderr)



        laenge=0
        if phase == 0:
            x0,y0,w0,h0,w,h,xAlt,yAlt,listX = sucheList(bomb_dir,x0,y0,xAlt,yAlt,w0,h0,w,h,listX,first);first=False;laenge=len(listX)            
        else:            
            x0,y0,w0,h0,w,h,xAlt,yAlt,feldList = sucheList(bomb_dir,x0,y0,xAlt,yAlt,w0,h0,w,h,feldList,first);first=False;laenge=len(feldList)

        print(str(runde)+": rahmen: "+str(w0)+"-"+str(h0)+ " zu "+str(w)+"-"+str(h)+"  # alt: "+str(xAlt)+"-"+str(yAlt) + " feldList: " + str(laenge) +"  phase: "+str(phase)+" # neu: "+str(x0)+"-"+str(y0),file=sys.stderr)

        if x0 >= wMax:
            x0 = wMax-1
        if x0 < 0:
            x0 = 0
        if y0 >= hMax:
            y0 = hMax-1
        if y0 < 0:
            y0 = 0   
        if x0 == xAlt and y0 == yAlt:
            x0 = w-1 if x0 == 0 else 0
            y0 = h-1 if y0 == 0 else 0

        print(str(x0)+" "+str(y0))

        if len(listX) < 10 and phase == 0:
            phase = 1;first=True
            feldList = newList(listX,w,h)

        if x0 == xZiel and y0 == yZiel:
            print("erreicht",file=sys.stderr);break
        runde+=1
        if runde > n:
            print("Zeit abgelaufen",file=sys.stderr);fehler=True;break
    if fehler:
        break