import sys
import math

sonderZeichen = {'bS':'\\', 'sp':' ','sQ':'\'','nl':'nl'}

tList = ['1sp', '1/', '1bS', '1_', '1/', '1bS', 'nl', '1(', '1sp', '1o', '1.', '1o', '1sp', '1)', 'nl', '1sp', '1>', '1sp', '1^', '1sp', '1<', 'nl', '2sp', '3|']


for t in tList:
    anzahl = 0; wert = ""
    #print(t[-2:])
    if t == "nl":
        anzahl = 1;wert="nl"
    elif t[-2:] in sonderZeichen:
        wert = sonderZeichen[t[-2:]]
        anzahl= int(t[:-2])
    else:
        wert = t[-1:]
        anzahl = int(t[:-1])
    for i in range(anzahl):
        if wert == "nl":
            print("")
        else:
            print(wert,end="")