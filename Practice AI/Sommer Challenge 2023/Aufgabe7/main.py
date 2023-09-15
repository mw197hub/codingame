from json import dumps, loads
from typing import List
import sys

def findAll(text,suche):
    pos=0;tList=[]
    while text[pos:].find(suche) > -1:
        treffer = text[pos:].find(suche)
        pos+=treffer
        tList.append(pos)
        pos+=1
    return tList


def naechst(z,sList):
    for i in range(len(sList)):
        if sList[i] == z:
            return i
    return -1
        

wish_a,wish_b="laser eyes","telepathy"
#wish_a,wish_b="i wish for laser eyes please","i wish for telepathy please"
#wish_a,wish_b="congratulations the wish mixer seems to work well","you really are a master of competitive programming"
wish_a,wish_b="beep","boop"


"telaser epathyes"
"laster lepathyes"
"telepaser ethyes"
"telepathser eyes"

#erg1=mischen(wish_a,wish_b)
#erg2=mischen(wish_b,wish_a)

erg1=""
aList=list(wish_a)
bList=list(wish_b)

a1=aList.pop(0)
b1=bList.pop(0)
while len(aList) > 0 or len(bList) > 0:
    n1=naechst(a1,bList)
    n2=naechst(b1,aList)
    if a1 == b1:
        erg1+=a1;a1,b1="",""
        if len(aList) == 0 or len(bList) == 0:
            break
        a1=aList.pop(0)
        b1=bList.pop(0)
    elif (n1 <= n2 and n1 > -1) or n2 == -1:
        erg1+=b1;b1=""
        if len(bList) == 0:
            break
        b1=bList.pop(0)
    elif n1 > n2 or n1 == -1:
        erg1+=a1;a1=""
        if len(aList) == 0:
            break
        a1=aList.pop(0)

        

if a1 == b1:
    erg1+=a1
while aList:
    erg1+=aList.pop(0)
while bList:
    erg1+=bList.pop(0)
    

print(erg1)