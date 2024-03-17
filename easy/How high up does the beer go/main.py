# https://www.codingame.com/ide/puzzle/how-high-up-does-the-beer-go

import sys,math

bR,uR,h,beer=2.5,4.0,15.0,473.0
#bR,uR,h,beer=2,2.1,17,200



start=int(h*10)
erg=9999;save=9999
for i in range(start,1,-1):
    aR = ((uR-bR) * ((i/10)  / h)) + bR
    wert = (1/3)*math.pi*(i/10)*(bR*bR+bR*aR+aR*aR)
    print("{}  =  {}".format(i/10,wert),file=sys.stderr)    
    if abs(wert-beer) < save:
        erg=i/10;save=abs(wert-beer)

print(erg)