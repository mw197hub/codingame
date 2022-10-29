#  https://www.codingame.com/ide/puzzle/random-walk

import sys,math

def rand(a,b,erg,m):
    return (a*erg+b) %m

a,b,m=8,3,7
ergList=[];erg=0;x,y=0,0;runde=0
while True:
    runde+=1
    erg = rand(a,b,erg,m)
    #print(erg,file=sys.stderr)
    d = erg%4
    if d == 0:
        y-=1
    elif d == 1:
        y+=1
    elif d == 2:
        x-=1
    elif d == 3:
        x+=1
    if x == 0 and y == 0:
        break
 
print(runde)