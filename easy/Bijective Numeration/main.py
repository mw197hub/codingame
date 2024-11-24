# https://www.codingame.com/ide/puzzle/bijective-numeration

import sys,math


deciList=['A', 'A', '12']
deciList=['9A', 'A2', '1A', '12']
deciList=['1', '2', '3', '4']
#deciList=['512', '256', '128', '64', '32', '16', '8', '8']
#deciList=['19', '91']
deciList=['499A', '2A1A', 'AA9', '911']


#####
# a = 10
erg=0
for deci in deciList:
    if "A" in deci:
        wert=0
        for i in range(len(deci)):
            if deci[i] == "A":
                zw = 10
            else:
                zw = int(deci[i])
            faktor= len(deci) - i -1
            multi= 10 ** faktor
            wert+=zw*multi
    else:
        wert=int(deci)
    erg+=wert

while True:    
    eList=list(str(erg))    
    for i in range(len(eList)):
        if eList[i] == "0":
            eList[i] = "A"
            if eList[i-1] == "A":
                eList[i-1] = "9"
            else:
                eList[i-1] = str(int(eList[i-1])-1)
    erg = ''.join(eList)
    if not "0" in erg[1:]:
        break
if erg[0] == "0":
    print(erg[1:])
else:
    print((erg))
