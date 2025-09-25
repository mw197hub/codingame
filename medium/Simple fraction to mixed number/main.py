# https://www.codingame.com/ide/puzzle/simple-fraction-to-mixed-number

import sys,math

def ggT(a, b):
    """Berechnet den größten gemeinsamen Teiler."""
    while b:
        a, b = b, a % b
    return a


xyList=['42/9', '71/23']
xyList=['-5/20', '-20/-5']
xyList=['0/0', '0/-0', '-0/0', '2/2', '-2/2', '0/-287', '-0/-287', '-6414254/-7344817', '7338165/8696070', '9784128/9994708', '9999999/-9999999', '-9999999/-9999999', '-9999999/9999999']
xyList=['2/2', '4/4']


for i in range(len(xyList)):
    xyL=xyList[i]
    xy=xyL.split("/")
    minus=False
    if xy[0][0] == "-":
        minus=minus ^ True
        wert1=int(xy[0][1:])                
    else:
        wert1=int(xy[0])
    if xy[1][0] == "-":
        minus=minus ^ True
        wert2=int(xy[1][1:])
    else:
        wert2=int(xy[1])    
    ausgabe=""
    if minus:
        ausgabe+="-"
    if wert2 == 0:
        print("DIVISION BY ZERO")
    elif wert1 == 0:
        print("0")
    else:
        if wert1 >= wert2:
            ausgabe+=str(wert1//wert2)
            wert1=wert1 % wert2        
            if wert1 > 0:
                ausgabe+=" "
        if wert1 > 0:
            teiler = ggT(wert1,wert2)
            ausgabe+=str(int(wert1/teiler))+"/"+str(int(wert2/teiler))
        print(ausgabe)
