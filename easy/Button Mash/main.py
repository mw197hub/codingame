# https://www.codingame.com/ide/puzzle/button-mash

import sys,math,copy


######

n=59
n=35641

anzahl=0
while n > 0:
    if n //2 == n / 2:
        n = n //2
    else:
        if (n & 3) == 3 and n > 3:           
           n += 1
        else:
           n -= 1
    anzahl+=1
print(anzahl)




