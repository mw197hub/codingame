# https://www.codingame.com/ide/puzzle/euclids-algorithm

import sys,math

a,b=25,3
#a,b=21,3

aS,bS,restS=a,b,0
while True:
    c=a//b
    rest = a%b
    print("{}={}*{}+{}".format(a,b,c,rest))
    restS=b
    if rest == 0:
        break
    a=b;b=rest
print("GCD({},{})={}".format(aS,bS,restS))