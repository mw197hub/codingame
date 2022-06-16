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

def erzeugeListQuer(w0,h0,w,h):
    feldList = []
    for x in range(w):
        if x >= h:
            break
        feldList.append(str(x)+"-"+str(x))
        feldList.append(str(x)+"-"+str(h-1-x))
    return feldList

def newList(listX,w,h):
    feldList = []
    xList = [];yList=[]
    for feld in listX:
        x,y=feld.split("-")
        xList.append(int(x))
        yList.append(int(y))
    xList = sorted(xList);yList=sorted(yList)
    xAnf=xList[0];xEnd=xList[-1];yAnf=yList[0];yEnd=yList[-1]
    xAnf=xAnf-100;xEnd=xEnd+100;yAnf=yAnf-100;yEnd=yEnd+100
    if xAnf < 0:
        xAnf =0
    if yAnf < 0:
        yAnf = 0
    if xEnd >= w:
        xEnd = w-1
    if yEnd >= h:
        yEnd = h-1
    for x in range(xAnf,xEnd,1):
        for y in range(yAnf,yEnd):
            feldList.append(str(x)+"-"+str(y))
    return feldList

def distance(xp1,yp1,xp2,yp2):
    return (math.sqrt( ((xp1-xp2)**2)+((yp1-yp2)**2) ))


def sucheList(bomb_dir,x0,y0,xAlt,yAlt,w0,h0,w,h,feldList,first):
    x1=x0;y1=y0
    newList={}
    for feld in sorted(feldList):
        xf,yf = feld.split("-")
        if first:
            newList[feld] = int(x0) + int(y0) - (int(xf) + int(yf))
        else:
            dist1=distance(x0,y0,int(xf),int(yf))
            dist2=distance(xAlt,yAlt,int(xf),int(yf))
            if bomb_dir == "SAME" and dist1 == dist2:            
                newList[feld] = dist1
                #newList[feld] = int(x0) + int(y0) - (int(xf) + int(yf))
            if bomb_dir == "WARMER" and dist1 < dist2:
                newList[feld] = dist1
                #newList[feld] = int(x0) + int(y0) - (int(xf) + int(yf))
            if bomb_dir == "COLDER" and dist1 > dist2:
                newList[feld] = dist2
                #newList[feld] = int(x0) + int(y0) - (int(xf) + int(yf))

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
#7zielList.clear();zielList=['402-645']
#3zielList.clear();zielList=['0-59']
zielList.clear();zielList=['1000-2252']

for ziel1 in zielList:
  #3  n=12;runde = 0;phase=0;w,h=1,100;x0,y0=0,3;w0,h0,xAlt,yAlt=0,0,x0,y0;feldList=[];first=True;wMax=w;hMax=h
  #7  n=27;runde=0;phase=0;w,h=1000,1000;x0,y0=501,501;w0,h0,xAlt,yAlt=0,0,x0,y0;feldList=[];first=True;wMax=w;hMax=h
    n=31;runde = 0;phase=0;w,h=8000,8000;x0,y0=3200,2100;w0,h0,xAlt,yAlt=0,0,x0,y0;feldList=[];first=True;wMax=w;hMax=h
    print("Start: " + str(ziel1),file=sys.stderr)
    xZiel,yZiel=ziel1.split("-");xZiel=int(xZiel);yZiel=int(yZiel);listX=[];listY=[]
    listX = erzeugeListQuer(w0,h0,w,h)
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

        if len(listX) < 150 and phase == 0:
            phase = 1;first=True
            if len(listX) == 0:
                feldList = erzeugeList(w0,h0,w,h)
            else:
                feldList = newList(listX,w,h)

        if x0 == xZiel and y0 == yZiel:
            print("erreicht",file=sys.stderr);break
        runde+=1
        if runde > n:
            print("Zeit abgelaufen",file=sys.stderr);fehler=True;break
    if fehler:
        break