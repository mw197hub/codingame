#  https://www.codingame.com/ide/puzzle/number-formatting

import sys,math

numbertext='200,000,000.000.002'
numbertext='xxx,x23,150.120.1xx'
numbertext='xxx,xxx,xx1.xxx.xxx'
numbertext='xxx,xxx,xxx.xxx.xxx'

wert=""
zahl=""
ausgabe=""
anfang,ende=0,0
for i in range(len(numbertext)):
    if numbertext[i].isnumeric():
        if len(wert) == 0:
            anfang=i;ende=i+1
        else:
            ende=i
        wert+=numbertext[i]
        ausgabe+='x'
    else:
        ausgabe+=numbertext[i]
if len(wert) > 0:
    zahl = str((int(wert)/2))
    if int(wert[0]) == 1:
        anfang+=1
    if int(wert[-1])  % 2 == 0:
        ende-=1
    if float(zahl) < 1:
        zahl = zahl[2:]
    ausgabeList=list(ausgabe)
    erg="";pos=0
    for i in range(len(ausgabe)):
        if i >= anfang and i <= ende+1 and ausgabeList[i] == "x":
            erg+=zahl[pos]
            pos+=1 
            if len(zahl) > pos:
                if not zahl[pos].isnumeric():
                    pos+=1
        else:
            erg+=ausgabeList[i]

    print(erg)
else:
    print(numbertext)