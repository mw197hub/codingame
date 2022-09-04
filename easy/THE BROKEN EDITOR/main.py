from re import T
import sys
import math

typed_keys = "echo \"Hello World!\";"
typed_keys = "<<SELECT * FROM users WHERE age >= 18>>;"
typed_keys = "print $_=~/[0-9a-z]/i;"
typed_keys = "x--?i--:y-D"

outList = [' ' for i in range(len(typed_keys))]

pos = 0;anzahl=0
for i in range(len(typed_keys)):
    if typed_keys[i] == "<":
        pos -= 1
        if pos < 0:
            pos = 0
    elif typed_keys[i] == ">":
        if pos < anzahl:
            pos += 1
    elif typed_keys[i] == "-":
        if pos > 0:
            pos-=1
            outList.pop(pos);anzahl-=1
    else:
        outList.insert(pos,typed_keys[i])
        pos+=1;anzahl+=1
erg = ""
for i in range(anzahl):
    erg = erg + outList[i]
print(erg)