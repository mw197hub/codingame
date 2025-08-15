# https://www.codingame.com/ide/puzzle/rocky-pohps-concert-date

import sys,math

def areValidFactors (z1,z2):
    n = z1 * z2
    if n == 0 :
        return False
    div = int (n ** .5)
    while n % div : div -= 1
    return div in (z1, z2)



n=44714648  #1
n=11241130  #2
n=144783    #3
n=200104091 #9

erg="";abstand=99999999
for i in range(1,len(str(n))):
    zahl=str(n)    
    wert=int(zahl[:i])*int(zahl[i:])
    if int(zahl[:i]) > 0 and int(zahl[i:]) > 0:
        wert= str(wert)    
        if len(wert) == 5:
            wert="000"+wert
        if len(wert) == 6:
            wert="00"+wert
        if len(wert) == 7:
            wert="0"+wert
        print("{}  {}  #  {}   diff: {}".format(zahl[:i],zahl[i:],wert,abs(int(zahl[:i]) - int(zahl[i:]))),file=sys.stderr)   
        if int(wert[4:6]) <= 12 and int(wert[4:6]) > 0 and int(wert[6:8]) <= 31 and int(wert[6:8]) > 0:
            if areValidFactors(int(zahl[:i]),int(zahl[i:])):
                erg=wert
   
print("{}-{}-{}".format(erg[0:4],erg[4:6],erg[6:8]))