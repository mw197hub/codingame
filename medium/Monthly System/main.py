# https://www.codingame.com/ide/puzzle/monthly-system

import sys,math

def to_base(number, base):
    """Converts a non-negative number to a list of digits in the given base.

    The base must be an integer greater than or equal to 2 and the first digit
    in the list of digits is the most significant one.
    """
    if not number:
        return [0]

    digits = []
    while number:
        digits.append(number % base)
        number //= base
    return list(reversed(digits))
##


mList=['FebSepDec', 'JunMarJan']

##
monDict={"Jan":0,"Feb":1,"Mar":2,"Apr":3,"May":4,"Jun":5,"Jul":6,"Aug":7,"Sep":8,"Oct":9,"Nov":10,"Dec":11}
base12={"10":"A","11":"B"}
erg=0
for m in mList:
    zahl=""
    for i in range(len(m)//3):
       # print(m[i*3:(i*3)+3])
        wert=str(monDict[m[i*3:(i*3)+3]])
        if wert in base12:
            wert=base12[wert]
        zahl+=wert
   # print(zahl)
    erg+=int(zahl,base=12)
eList=(to_base(erg,12))
ausgabe=""
for e in eList:
    for mon,wert in monDict.items():
        if wert == e:
            ausgabe+=mon
print(ausgabe)


