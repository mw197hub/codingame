# https://www.codingame.com/ide/puzzle/mandelbrot-set-approximation

import sys,math,cmath

def pruefen(c):
    z=0
    for i in range(10):
        z = z**2 +c
    if abs(z) <= 1:
        return "*"
    return " "


n=7
n=13
#n=19
#n=25


ny=n
nx=3*(n-1)/2+1
dy=2.0/(ny-1)
dx=3.0/(nx-1)
#print("dx: {}  dy: {}".format(dx,dy),file=sys.stderr)
xList,yList=[],[]
start=-2
while True:
    xList.append(start)
    start+=dx
    start = round(start,9)
    if round(start,6) > 1:
        print(start)
        break
print((xList),file=sys.stderr)
start=1
while True:
    yList.append(start)
    start-=dy
    start = round(start,9)
    if start < -1:
        break
#print(yList)

for y in yList:
    for x in xList:
        print(pruefen(complex(x,y)),end="")
    print("")



