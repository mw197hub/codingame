#https://www.codingame.com/ide/puzzle/sand-fall

import sys,math,string

def pruefe(outList,s,p,x,w):
    if outList[x][p]==' ':
        outList[x][p]=s
        return True
    else:
        p1=1;p2=-1
        if s in string.ascii_uppercase:
            p1=-1;p2=1
        if p+p1 >= 0 and p+p1 < w and outList[x][p+p1]==' ':
            x1=-1;y1=-1
            for i in range(len(outList)-x):
                if  p+p1*(i+1) >= 0 and  p+p1*(i+1) < w and x+i < len(outList) and outList[x+i][p+p1*(i+1)] == ' ':
                        x1=x+i;y1=p+p1*(i+1)
            outList[x1][y1]=s
            return True

        elif p+p2 >= 0 and p+p2 < w and outList[x][p+p2]==' ':
            x1=-1;y1=-1
            for i in range(len(outList)-x):
                if p+p2*(i+1) >= 0 and p+p2*(i+1) < w and x+i < len(outList) and outList[x+i][p+p2*(i+1)] == ' ' :
                        x1=x+i;y1=p+p2*(i+1)
            outList[x1][y1]=s
            return True
        return False           


####
w=3;h=3;inList=[['n', 1], ['e', 1], ['o', 1], ['A', 1]]
w=4;h=4;inList=[['S', 0], ['A', 0], ['l', 0], ['N', 0], ['o', 0], ['I', 0], ['D', 0], ['v', 0]]
w=7;h=6;inList=[['g', 3], ['G', 3], ['g', 3], ['g', 3], ['G', 3], ['G', 3], ['g', 3], ['g', 3], ['g', 3], ['G', 3], ['G', 3], ['G', 3], ['g', 3], ['G', 3], ['g', 3], ['G', 3]]


####


outList=[]
for x in range(h):
    yList=[]
    for y in range(w):
        yList.append(' ')
    outList.append(yList[:])
#print(outList,file=sys.stderr)

for e in inList:
    s=e[0];p=e[1];x=h-1
    while True:
        if pruefe(outList,s,p,x,w):
            break
        x-=1


ende=""
for out in outList:
    erg="";ende=""
    for o in out:
        erg+=o
        ende+="-"
    print("|"+erg+"|")
print("+"+ende+"+")