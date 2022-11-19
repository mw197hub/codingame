#  https://www.codingame.com/ide/puzzle/buzzle

import sys,math

BS="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def to_base(n, b): 
    return "0" if not n else to_base(n//b, b).lstrip("0") + BS[n%b]
def to_int(s,b):
    n = 0
    for i in range(len(s)):
        p = BS.find(s[-(i+1)])
        if i > 0:
            n = n + (p*b**(i))
        else:
            n = p
    return n

def level1(wert,k,n):
    iWert = int(BS.find(wert[-1]))
    if iWert == k:
        return True    
    iWert = to_int(wert,n)
    if iWert % k == 0:
        return True
    return False

def level2(wert,k,n):
    betrag = str(wert)
    while len(betrag) > 1:
        quer =0
        for i in range(len(betrag)):
            quer+= int(BS.find(betrag[i]))
        betrag = to_base(int(quer),n)
        e = level1(betrag,k,n)
        if e:
            return True
    return False


n,a,b=10,107,114
kList=[7]

n,a,b=10,34,40
kList=[7]

n,a,b=10,572,588
kList=[5,9]

n,a,b=18,1031,1037
kList=[11,17]

n,a,b=12,94,96
kList=[7,11]

for wert in range(a,b+1):    
    erg = False
    for k in kList:
        nWert = to_base(wert,n)
        erg = level1(nWert,k,n)
        if erg:
            break
        erg = level2(nWert,k,n)
        if erg:
            break
    if erg:
        print("Buzzle")
    else:
        print(wert)

#print(to_base(1148,18))
#print(to_int('39E',18))
#print("abcd"[-2:])