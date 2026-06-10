# https://www.codingame.com/ide/puzzle/pyramid-stacker

import sys,math

n=14;h=3;cubes="ABCDEFGHIJKLMN"  #1
n=12;h=3;cubes="ABCDEFGHIJKL"   #2


pos=0;ausgabeList=[]
for i in range(h,0,-1):
    zwList=[]
    for y in range(i):
        ausgabe=""
        for x in range(i):
            if pos < len(cubes):
                ausgabe+=cubes[pos]+" "
            else:
                if y > 0:
                    ausgabe+=zwList[y-1][x*2:x*2+2]
            pos+=1
        zwList.append(ausgabe)
    ausgabeList.append(ausgabe[:-1])

for i in range(h,0,-1):
    if len(ausgabeList[i-1]) > 0:
        leer = " " *(i-1)
        print(leer + ausgabeList[i-1])
    else:
        print("")